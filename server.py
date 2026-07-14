#!/usr/bin/env python3
"""
LEO Serveur Unifié — Wiki BAVI + Dashboard + API
Usage: .venv/bin/uvicorn server:app --host 0.0.0.0 --port 8765
"""
import json, subprocess, os, sys, re, urllib.request, urllib.parse
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, Response, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import urllib.request

BASE = Path("/home/tofdan/.hermes")
BAVI_SITE = Path("/home/tofdan/Projets_Dev/BAVI_LEO/site-local")
LEO_DASHBOARD_REPO = Path("/home/tofdan/.hermes/leo-dashboard-repo")
CRON_JOBS_FILE = Path("/home/tofdan/.hermes/profiles/leo-copilot/cron/jobs.json")
N8N_CONFIG_FILE = Path("/home/tofdan/.hermes/n8n-webhooks.json")
METRICS_FILE = Path("/home/tofdan/.hermes/metrics/leo-unified.json")
AUTH_TOKEN = "leo-panel-2026"
HA_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0MTIxMDZmOWQ1NWQ0NTFiOThiZjFhMjVhMmJlOTRlZiIsImlhdCI6MTc4MzgzNDc1MCwiZXhwIjoyMDk5MTk0NzUwfQ.CBphayJ3uX6XIT1m5ZOKISOOEfzVgT7IAs8WH9LZhLE"
HA_URL = "http://localhost:8123"
ENERGY_FILE = Path("/home/tofdan/.hermes/metrics/energy.json")
ENERGY_HISTORY_FILE = Path("/home/tofdan/.hermes/metrics/energy_history.json")

# Dashboard builder — génération dynamique
from dashboard_builder import build_html, esc

# Normalisation des noms de modèles
def norm_model(name):
    """Normalise les noms de modèles pour l'affichage."""
    m = (name or "").lower().strip()
    if "deepseek-chat" in m or "deepseek-v4-pro" in m or m == "pro":
        return "DS Pro"
    if "deepseek-v4-flash" in m or "flash" in m:
        return "DS Flash"
    if "gemini" in m:
        return "Gemini"
    if "claude" in m:
        return "Claude"
    if "gpt" in m:
        return "GPT"
    # Tronquer les noms longs
    short = name.split("/")[-1]
    return short[:20]

app = FastAPI(title="LEO Unified Server")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ── Auth helper ──
def check_token(request: Request):
    token = request.query_params.get("token")
    if token == AUTH_TOKEN:
        return True
    auth = request.headers.get("Authorization", "")
    if auth == f"Bearer {AUTH_TOKEN}":
        return True
    return False

# ── API: Crons ──
def list_crons():
    all_jobs, seen_ids = [], set()
    if not CRON_JOBS_FILE.exists():
        return []
    try:
        data = json.loads(CRON_JOBS_FILE.read_text())
        jobs = data if isinstance(data, list) else data.get("jobs", [])
        for j in jobs:
            jid = j.get("id", "")
            if jid and jid not in seen_ids:
                seen_ids.add(jid)
                all_jobs.append(j)
    except Exception:
        pass
    return [{
        "id": j["id"], "name": j.get("name", j["id"][:8]),
        "schedule": j.get("schedule_display", "?"), "enabled": j.get("enabled", False),
        "last_status": j.get("last_status", "?"), "last_run": j.get("last_run_at", "?"),
        "next_run": j.get("next_run_at", "?"), "no_agent": j.get("no_agent", True),
    } for j in all_jobs if "id" in j]

@app.get("/api/crons")
async def api_crons(request: Request):
    if not check_token(request): raise HTTPException(401)
    return list_crons()

@app.post("/api/crons/{job_id}/run")
async def api_cron_run(job_id: str, request: Request):
    if not check_token(request): raise HTTPException(401)
    try:
        # Lancement asynchrone — retour immédiat
        subprocess.Popen(
            ["/home/tofdan/.hermes/venv/bin/hermes", "cron", "run", "--profile", "leo-copilot", job_id],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            env={**os.environ, "HOME": "/home/tofdan"}
        )
        return {"ok": True, "output": f"Cron {job_id} déclenché en arrière-plan"}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@app.post("/api/crons/{job_id}/toggle")
async def api_cron_toggle(job_id: str, request: Request):
    if not check_token(request): raise HTTPException(401)
    HERMES = "/home/tofdan/.hermes/venv/bin/hermes"
    try:
        if not CRON_JOBS_FILE.exists():
            return {"ok": False, "error": "No jobs file"}
        data = json.loads(CRON_JOBS_FILE.read_text())
        jobs = data if isinstance(data, list) else data.get("jobs", [])
        job = next((j for j in jobs if j.get("id") == job_id or j.get("job_id") == job_id), None)
        if not job:
            return {"ok": False, "error": "Job not found"}
        action = "pause" if job.get("enabled", True) else "resume"
        r2 = subprocess.run([HERMES, "cron", action, "--profile", "leo-copilot", job_id],
                           capture_output=True, text=True, timeout=15,
                           env={**os.environ, "HOME": "/home/tofdan"})
        return {"ok": r2.returncode == 0, "action": action, "output": r2.stdout[:500]}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@app.get("/api/crons/{job_id}/history")
async def api_crons_history(job_id: str, request: Request):
    if not check_token(request): raise HTTPException(401)
    # Déduire le nom du script depuis jobs.json
    job = None
    try:
        if not CRON_JOBS_FILE.exists():
            return {"history": []}
        data = json.loads(CRON_JOBS_FILE.read_text())
        jobs = data if isinstance(data, list) else data.get("jobs", [])
        job = next((j for j in jobs if j.get("id") == job_id or j.get("job_id") == job_id), None)
        script_name = ""
        if job:
            script_name = (job.get("script") or "").replace("-wrapper.sh", "").replace(".sh", "").replace(".py", "")
    except:
        script_name = ""
    
    history = []
    status_dir = Path("/home/tofdan/.hermes/cron/output")
    
    # 1. Chercher le .history.jsonl (historique cumulatif)
    if status_dir.exists() and script_name:
        hist_file = status_dir / f"{script_name}.history.jsonl"
        if hist_file.exists():
            try:
                for line in hist_file.read_text().splitlines():
                    if not line.strip():
                        continue
                    d = json.loads(line)
                    history.append({
                        "script": d.get("name", script_name),
                        "timestamp": d.get("timestamp", ""),
                        "exit_code": d.get("exit_code", -1),
                        "duration_sec": d.get("duration_sec", 0),
                        "stderr_lines": d.get("stderr_lines", 0),
                        "stdout_last": d.get("stdout_last", "")[:200]
                    })
                history.sort(key=lambda x: x["timestamp"], reverse=True)
            except:
                pass
    
    # 2. Fallback: .status.json si pas d'historique
    if not history and status_dir.exists():
        for f in sorted(status_dir.glob("*.status.json"), key=lambda x: x.stat().st_mtime, reverse=True):
            try:
                d = json.loads(f.read_text())
                if script_name and script_name not in d.get("name", "") and script_name not in f.stem:
                    continue
                history.append({
                    "script": d.get("name", f.stem),
                    "timestamp": d.get("timestamp", ""),
                    "exit_code": d.get("exit_code", -1),
                    "duration_sec": d.get("duration_sec", 0),
                    "stderr_lines": d.get("stderr_lines", 0),
                    "stdout_last": d.get("stdout_last", "")[:200]
                })
            except:
                pass
    
    # 3. Fallback ultime: last_run du jobs.json
    if not history and job:
        history.append({
            "script": job.get("name", ""),
            "timestamp": job.get("last_run_at", ""),
            "exit_code": 0 if job.get("last_status") == "ok" else 1,
            "duration_sec": 0,
            "stderr_lines": 0,
            "stdout_last": job.get("last_status", "?")
        })
    
    return {"history": history[:50]}

# ── API: Métriques ──
@app.get("/api/machine-kpi")
async def api_machine_kpi(request: Request):
    """KPIs machine pour le dashboard monitoring."""
    kpi_file = Path("/home/tofdan/.hermes/metrics/machine-kpi.json")
    if kpi_file.exists():
        return JSONResponse(json.loads(kpi_file.read_text()))
    return JSONResponse({"error": "no data"}, status_code=404)

@app.get("/api/metrics")
async def api_metrics(request: Request):
    # Public endpoint
    if not METRICS_FILE.exists():
        return {"error": "Metrics file not found"}
    try:
        d = json.loads(METRICS_FILE.read_text())
        b, s, c, i, v, n8, gh, bavi = d.get("budget",{}), d.get("sessions",{}), d.get("crons",{}), d.get("infra",{}), d.get("vaults",{}), d.get("n8n",{}), d.get("github",{}), d.get("bavi",{})
        machines = d.get("infra", {}).get("machines", [])
        return {
            "generated_at": d.get("_meta", {}).get("generated_at", "?"),
            "budget": {"balance": b.get("balance",0), "currency": b.get("currency","$"), "spent_14d": b.get("total_spent_14d",0), "monthly_spent": b.get("monthly_spent",0), "monthly_cap": b.get("monthly_cap","N/A"), "drift": b.get("drift_label","N/A"), "days_remaining": b.get("days_remaining",0)},
            "sessions": {"total": s.get("total",0), "messages_today": s.get("today",{}).get("messages",0), "tokens_today": s.get("today",{}).get("tokens_in",0), "total_tokens_in": s.get("total_tokens_in",0), "total_tokens_out": s.get("total_tokens_out",0), "total_cost": s.get("total_estimated_cost",0), "total_tools": s.get("total_tools",0), "total_api_calls": s.get("total_api_calls",0), "by_source": s.get("by_source",{})},
            "crons": {"total": c.get("total",0), "ok": c.get("status_ok",0), "error": c.get("status_error",0), "pending": c.get("status_pending",0)},
            "infra": {"gateway": i.get("gateway","N/A"), "ollama_models": i.get("ollama",{}).get("models",[]), "n8n_active": n8.get("active_workflows",0), "n8n_total": n8.get("total_workflows",0)},
            "vaults": {"total_notes": v.get("total_notes",0), "total_dailies": v.get("total_dailies",0), "active": v.get("active_vaults",0), "detail": v.get("vaults",{})},
            "models": s.get("by_model",{}), "repos": {"total": gh.get("total_repos",0)},
            "bavi": {"bureaux": bavi.get("bureaux",{}), "voyages": bavi.get("voyages",[])},
            "infra_health": {"cpu": f"{machines[0].get('cpu_load',0)*100:.0f}%", "ram": str(machines[0].get("ram_pct","?"))+"%", "disk": str(machines[0].get("disk_pct","?"))+"%"} if machines else {},
            "bots": d.get("bots",{}).get("bots",[]), "voyages": bavi.get("voyages",{}).get("roadbooks",[]),
            "budget_history": b.get("history",[]), "sessions_daily": s.get("daily",[]), "by_source": s.get("by_source",{}),
        }
    except Exception as e:
        return {"error": str(e)}

# ── API: n8n ──
@app.get("/api/wf")
async def api_workflows(request: Request):
    if not check_token(request): raise HTTPException(401)
    data_file = Path.home() / ".hermes" / "metrics" / "workflows.json"
    if not data_file.exists():
        return {"error": "no data"}
    with open(data_file) as f:
        return json.load(f)

@app.post("/api/wf/{name}/run")
async def api_wf_run(name: str, request: Request):
    if not check_token(request): raise HTTPException(401)
    import subprocess
    scripts_dir = Path.home() / ".hermes" / "scripts"
    # Mapper nom de workflow → script correspondant
    wf_to_script = {
        "gardien-drive": "gardien-drive-wrapper.sh",
        "drive-issue": "drive-issue-wrapper.sh",
        "save-contacts": "save-contacts-wrapper.sh",
        "check-gmail": "check-gmail.py",
    }
    script_name = wf_to_script.get(name, f"{name}.py")
    script_path = scripts_dir / script_name
    if not script_path.exists():
        script_path = scripts_dir / f"{name}-wrapper.sh"
    if not script_path.exists():
        return {"ok": False, "error": f"Script {script_name} introuvable"}
    
    subprocess.Popen(
        ["bash", str(script_path)] if str(script_path).endswith(".sh")
        else ["/home/tofdan/.hermes/venv/bin/python3", str(script_path)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        env={**os.environ, "HOME": "/home/tofdan"}
    )
    return {"ok": True}

@app.post("/api/n8n/save")
async def api_n8n_save(request: Request):
    if not check_token(request): raise HTTPException(401)
    body = await request.json()
    N8N_CONFIG_FILE.write_text(json.dumps(body, indent=2))
    return {"ok": True}

@app.post("/api/n8n/{name}/run")
async def api_n8n_run(name: str, request: Request):
    if not check_token(request): raise HTTPException(401)
    hooks = json.loads(N8N_CONFIG_FILE.read_text()) if N8N_CONFIG_FILE.exists() else []
    url = next((h["url"] for h in hooks if h["name"] == name), None)
    if not url:
        raise HTTPException(404, detail=f"Webhook '{name}' not found")
    try:
        req = urllib.request.Request(url, method="POST", data=b"{}", headers={"Content-Type": "application/json"})
        resp = urllib.request.urlopen(req, timeout=30)
        return {"ok": True, "status": resp.status, "response": resp.read().decode()[:1000]}
    except Exception as e:
        return {"ok": False, "error": str(e)}

# ── Pages ──
MONITORING_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🖥️ Monitoring — LEO</title>
<style>
:root {--bg:#0f172a;--card:#1e293b;--text:#e2e8f0;--dim:#94a3b8;--green:#34d399;--red:#f87171;--yellow:#fbbf24;--blue:#60a5fa;--accent:#818cf8;--border:#334155}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:system-ui,-apple-system,sans-serif;padding:20px;min-height:100vh}
h1{font-size:1.5em;margin-bottom:20px;display:flex;align-items:center;gap:10px}
h1 span{font-size:.6em;color:var(--dim);font-weight:400}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-bottom:20px}
.card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px}
.card h2{font-size:1em;color:var(--dim);margin-bottom:12px;text-transform:uppercase;letter-spacing:.5px}
.kpi{font-size:2em;font-weight:700}
.kpi-label{font-size:.8em;color:var(--dim)}
.row{display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid var(--border)}
.row:last-child{border-bottom:none}
.badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:.75em;font-weight:600}
.badge.up{background:#064e3b;color:var(--green)}
.badge.down{background:#7f1d1d;color:var(--red)}
.badge.warn{background:#78350f;color:var(--yellow)}
.progress-bar{height:8px;border-radius:4px;background:var(--border);margin-top:6px}
.progress-fill{height:100%;border-radius:4px;transition:width .5s}
.bar-green{background:var(--green)}
.bar-yellow{background:var(--yellow)}
.bar-red{background:var(--red)}
.process{font-family:'SF Mono',monospace;font-size:.8em;color:var(--dim);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:400px}
#updated{text-align:right;color:var(--dim);font-size:.75em;margin-top:10px}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
.loading{animation:pulse 1.5s infinite}
</style>
</head>
<body>
<h1>🖥️ Monitoring LEO <span id="uptime">—</span></h1>
<div class="grid" id="kpis">
  <div class="card"><h2>💻 CPU</h2><div class="kpi loading" id="cpu">—</div><div class="kpi-label" id="cpu-load"></div><div class="progress-bar"><div class="progress-fill" id="cpu-bar"></div></div></div>
  <div class="card"><h2>🧠 RAM</h2><div class="kpi loading" id="ram">—</div><div class="kpi-label" id="ram-detail"></div><div class="progress-bar"><div class="progress-fill" id="ram-bar"></div></div></div>
  <div class="card"><h2>💾 Disque</h2><div class="kpi loading" id="disk">—</div><div class="kpi-label" id="disk-detail"></div><div class="progress-bar"><div class="progress-fill" id="disk-bar"></div></div></div>
  <div class="card"><h2>🌡️ Température</h2><div class="kpi loading" id="temp">—</div></div>
  <div class="card"><h2>🐳 Services</h2><div id="services">—</div></div>
  <div class="card"><h2>⏱️ Crons</h2><div class="kpi" id="crons-total">—</div><div class="kpi-label" id="crons-detail"></div></div>
</div>
<div class="card" style="margin-bottom:16px"><h2>📊 Top Processus</h2><div id="processes">—</div></div>
<div class="card"><h2>🌐 Tailscale</h2><div id="tailscale">—</div></div>
<div id="updated">Actualisation toutes les 30s</div>
<script>
async function refresh(){
  try{
    const r=await fetch('/api/machine-kpi');
    const d=await r.json();
    document.getElementById('uptime').textContent=d.uptime||'—';
    // CPU
    const load=d.cpu?d.cpu.load1:'—';
    const cores=d.cpu?d.cpu.cores:'?';
    document.getElementById('cpu').textContent=(load*100).toFixed(0)+'%';
    document.getElementById('cpu').className='kpi';
    document.getElementById('cpu-load').textContent='Load '+load+' | '+cores+' cores';
    const cpuPct=Math.min(load*100/cores*100,100);
    document.getElementById('cpu-bar').style.width=cpuPct+'%';
    document.getElementById('cpu-bar').className='progress-fill '+(cpuPct>80?'bar-red':cpuPct>50?'bar-yellow':'bar-green');
    // RAM
    const ram=d.ram||{};
    const ramUsed=parseFloat(ram.used)||0;
    const ramTotal=parseFloat(ram.total)||1;
    const ramPct=ramUsed/ramTotal*100;
    document.getElementById('ram').textContent=ramPct.toFixed(0)+'%';
    document.getElementById('ram').className='kpi';
    document.getElementById('ram-detail').textContent=ram.used+' / '+ram.total+' (dispo: '+ram.avail+')';
    document.getElementById('ram-bar').style.width=ramPct+'%';
    document.getElementById('ram-bar').className='progress-fill '+(ramPct>85?'bar-red':ramPct>60?'bar-yellow':'bar-green');
    // Disk
    const diskParts=(d.disk||'').split(' ');
    const diskPct=parseInt(diskParts[3])||0;
    document.getElementById('disk').textContent=diskPct+'%';
    document.getElementById('disk').className='kpi';
    document.getElementById('disk-detail').textContent='Utilisé: '+diskParts[1]+' / '+diskParts[0]+' | Libre: '+diskParts[2];
    document.getElementById('disk-bar').style.width=diskPct+'%';
    document.getElementById('disk-bar').className='progress-fill '+(diskPct>85?'bar-red':diskPct>60?'bar-yellow':'bar-green');
    // Temp
    document.getElementById('temp').textContent=(d.cpu?d.cpu.temp:'—')+'°C';
    document.getElementById('temp').className='kpi '+(parseFloat(d.cpu?.temp)>75?'bar-red':'bar-green');
    // Services
    const svc=d.services||{};
    document.getElementById('services').innerHTML=Object.entries(svc).map(([k,v])=>'<div class="row"><span>'+k+'</span><span class="badge '+(v==='UP'?'up':'down')+'">'+v+'</span></div>').join('');
    // Crons
    const cr=d.crons||{};
    document.getElementById('crons-total').textContent=(cr.ok||0)+'/'+(cr.total||0)+' OK';
    document.getElementById('crons-detail').textContent='Erreurs: '+(cr.error||0)+' | En attente: '+(cr.pending||0);
    // Processus
    const procs=(d.top_procs||'').split('\\n').filter(l=>l&&!l.startsWith('USER'));
    document.getElementById('processes').innerHTML=procs.slice(0,8).map(l=>{const p=l.split(/\\s+/);return '<div class="row"><span class="process" title="'+l+'">'+(p[10]||'').split('/').pop()+'</span><span style="color:var(--dim)">'+p[2]+'% CPU | '+p[3]+'% MEM</span></div>'}).join('');
    // Tailscale
    const ts=(d.network||'').split('\\n').filter(l=>l.trim());
    document.getElementById('tailscale').innerHTML=ts.map(l=>{const p=l.split(/\\s+/);const name=p[1]||'?';const status=p[5]||'?';return '<div class="row"><span>'+name+'</span><span class="badge '+(status.includes('offline')?'warn':'up')+'">'+status+'</span></div>'}).join('');
    document.getElementById('updated').textContent='Mis à jour: '+new Date().toLocaleTimeString('fr-BE');
  }catch(e){
    document.getElementById('updated').textContent='Erreur: '+e.message;
  }
}
refresh();
setInterval(refresh,30000);
</script>
</body>
</html>"""

@app.get("/monitoring", response_class=HTMLResponse)
async def monitoring(request: Request):
    """Page monitoring temps réel — LOCAL uniquement."""
    return HTMLResponse(MONITORING_TEMPLATE)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    if not check_token(request): raise HTTPException(401)
    return HTMLResponse(build_html())

# ── Dashboard JS files (served dynamically, no cron needed) ──
LEO_JS_FILES = {
    "monitoring.js": LEO_DASHBOARD_REPO / "monitoring.js",
    "crons.js": LEO_DASHBOARD_REPO / "crons.js",
}

@app.get("/leo/{filename}")
async def leo_static(filename: str):
    if filename not in LEO_JS_FILES:
        raise HTTPException(404)
    from fastapi.responses import Response
    path = LEO_JS_FILES[filename]
    if not path.exists():
        raise HTTPException(404)
    return Response(content=path.read_text(), media_type="text/javascript", headers={"Cache-Control": "no-cache, no-store, must-revalidate"})

# ── API: Recherche full-text ──
@app.get("/api/search")
async def api_search(q: str = ""):
    # Public endpoint
    if not q or len(q) < 2:
        return {"results": []}
    docs_dir = BASE / "BAVI_LEO/docs"
    try:
        r = subprocess.run(
            ["rg", "--no-heading", "--line-number", "--max-count", "3",
             "-i", "--type", "md", q, str(docs_dir)],
            capture_output=True, text=True, timeout=5
        )
        results = []
        seen = set()
        for line in r.stdout.strip().split("\n")[:20]:
            if not line: continue
            parts = line.split(":", 2)
            if len(parts) < 3: continue
            filepath, linenum, content = parts
            rel = filepath.replace(str(docs_dir) + "/", "")
            title = rel.replace(".md", "").replace("/index", "").rsplit("/", 1)[-1]
            url = "/" + rel.replace(".md", "/").replace("/index/", "/")
            if title in seen: continue
            seen.add(title)
            results.append({
                "title": title.replace("-", " ").title(),
                "path": url,
                "snippet": content.strip()[:120],
                "line": int(linenum)
            })
        return {"results": results[:10]}
    except Exception:
        return {"results": []}

# ── API: Wiki Graph ──
@app.get("/api/graph")
async def api_graph(bureau: str = ""):
    docs_dir = BASE / "BAVI_LEO/docs"
    nodes = {}
    links = []
    colors = {"michel":"#a78bfa","sylvia":"#06b6d4","leo":"#818cf8","gerard":"#f97316","virginie":"#ec4899","emile":"#f59e0b","robert":"#3b82f6","sophie":"#22c55e"}
    skip_names = {"index","readme","bureaux","skills","guide-utilisation","analytics","graph","editor","crons","documentation-map","roadbooks"}
    for md_file in docs_dir.rglob("*.md"):
        rel = str(md_file.relative_to(docs_dir))
        parts = rel.replace(".md","").split("/")
        name = parts[-1].replace("-"," ").title()[:40]
        # Déterminer le bureau
        bureau_id = ""
        for i, p in enumerate(parts):
            if p.startswith("bureau-"):
                bureau_id = p.replace("bureau-","")
                break
        # Skip meta pages
        if not bureau_id or parts[-1] in skip_names:
            continue
        nid = rel.replace(".md","").replace(" ","-").lower().replace("/","_")
        is_archived = "/archive/" in rel
        if nid not in nodes:
            color = colors.get(bureau_id,"#64748b")
            # Parse frontmatter for metadata
            meta = {"date":"","version":"","tags":"","statut":""}
            try:
                content = md_file.read_text()
                if content.startswith("---"):
                    end = content.find("---", 3)
                    if end > 0:
                        fm = content[3:end]
                        for line in fm.split("\n"):
                            line = line.strip()
                            if line.startswith("date:"): meta["date"] = line.split(":",1)[1].strip()
                            elif line.startswith("version:"): meta["version"] = line.split(":",1)[1].strip()
                            elif line.startswith("tags:"):
                                tags = line.split(":",1)[1].strip()
                                meta["tags"] = tags.replace("[","").replace("]","").replace('"','').replace("'","")[:60]
                            elif line.startswith("statut:"): meta["statut"] = line.split(":",1)[1].strip()
            except: pass
            nodes[nid] = {"id":nid,"name":name,"bureau":bureau_id,"color":color,"archived":is_archived,**meta}
        nodes[nid]["analyses"] = nodes[nid].get("analyses",0) + 1
        try:
            content = md_file.read_text()
            for match in re.finditer(r'\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]', content):
                raw = match.group(1).strip().lower().replace(' ','-')
                if raw and not raw.startswith('http') and raw != nid and len(links) < 500:
                    links.append({'source':nid,'raw':raw})
            for match in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', content):
                raw = match.group(2).strip()
                if raw.startswith('http'): continue
                raw = re.sub(r'\.md$','',raw)
                raw = re.sub(r'[#?].*$','',raw)
                raw = raw.replace('/','_').replace(' ','-').lower()
                if raw and raw != nid and len(links) < 500:
                    links.append({'source':nid,'raw':raw})
        except: pass
    node_ids = {n["id"] for n in nodes.values()}
    # Resolve raw targets to real node IDs (fuzzy match)
    resolved_links = []
    for l in links:
        raw = l.get("raw","")
        if raw in node_ids: resolved_links.append({"source":l["source"],"target":raw}); continue
        # Try substring match
        for nid in node_ids:
            if raw and raw in nid:
                resolved_links.append({"source":l["source"],"target":nid})
                break
    valid_links = resolved_links
    # Filter by bureau
    if bureau:
        bureau_nodes = {nid for nid,n in nodes.items() if n["bureau"] == bureau}
        nodes = {nid:n for nid,n in nodes.items() if nid in bureau_nodes}
        valid_links = [l for l in valid_links if l["source"] in bureau_nodes and l["target"] in bureau_nodes]
    return {"nodes": list(nodes.values()), "links": valid_links}

# ── API: Éditeur ──
@app.get("/api/editor/load")
async def editor_load(path: str = ""):
    if not path or ".." in path:
        return {"ok": False, "error": "Chemin invalide"}
    fp = BASE / "BAVI_LEO/docs" / path
    if not fp.exists():
        return {"ok": False, "error": "Fichier non trouve"}
    return {"ok": True, "content": fp.read_text()}

@app.post("/api/editor/save")
async def editor_save(request: Request):
    body = await request.json()
    path = body.get("path", "")
    content = body.get("content", "")
    if not path or ".." in path:
        return {"ok": False, "error": "Chemin invalide"}
    fp = BASE / "BAVI_LEO/docs" / path
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(content)
    # Rebuild
    try:
        subprocess.run(["bash", str(BASE / "BAVI_LEO/rebuild-wiki.sh")],
                      capture_output=True, timeout=30)
    except: pass
    return {"ok": True}

# ── Cameras (proxy vers Home Assistant) ──
CAMERAS = [
    {"id": "camera.cloudedge_meari_devant_maison_camera", "name": "📷 Devant Maison"},
    {"id": "camera.cloudedge_meari_arriere_maison_camera", "name": "📷 Arrière Maison"},
    {"id": "camera.cloudedge_meari_tic_camera", "name": "📷 TIC Camera"},
    {"id": "camera.cloudedge_meari_pignon_maison_camera", "name": "📷 Pignon Maison"},
]

@app.get("/cameras")
async def cameras_page(request: Request):
    if not check_token(request): raise HTTPException(401)
    embed = request.query_params.get("embed") == "1"
    
    # Récupérer les états des caméras via HA
    import urllib.request as ur
    cameras_state = {}
    try:
        req = ur.Request(f"{HA_URL}/api/states", headers={"Authorization": f"Bearer {HA_TOKEN}"})
        with ur.urlopen(req, timeout=5) as r:
            states = json.loads(r.read())
            for s in states:
                eid = s["entity_id"]
                if eid.startswith("camera.cloudedge"):
                    cameras_state[eid] = {"state": s["state"], "last": s["last_updated"]}
                elif eid.startswith("binary_sensor.cloudedge") and "awake" in eid:
                    cam_id = eid.replace("binary_sensor.", "camera.").replace("_camera_awake", "_camera")
                    if cam_id not in cameras_state:
                        cameras_state[cam_id] = {}
                    cameras_state[cam_id]["awake"] = s["state"] == "on"
                elif eid.startswith("sensor.cloudedge") and "battery" in eid:
                    cam_id = eid.replace("sensor.", "camera.").replace("_battery", "_camera")
                    if cam_id not in cameras_state:
                        cameras_state[cam_id] = {}
                    cameras_state[cam_id]["battery"] = s["state"]
    except:
        pass
    
    cards = ""
    for cam in CAMERAS:
        cs = cameras_state.get(cam["id"], {})
        battery = cs.get("battery", "?")
        awake = cs.get("awake", False)
        last = cs.get("last", "?")[:19].replace("T", " ")
        
        wake_id = cam["id"].replace("camera.", "button.").replace("_camera", "_wake_camera")
        battery_color = "var(--green)" if battery == "100" else "var(--orange)" if int(battery or 0) > 50 else "var(--red)"
        awake_icon = "🟢" if awake else "💤"
        
        cards += f'''
        <div class="cam-card">
            <div class="cam-name">
                {cam["name"]}
                <span style="float:right;font-size:11px;font-weight:400">
                    <span style="color:{battery_color}">🔋{battery}%</span>
                    <span style="margin-left:8px">{awake_icon}</span>
                </span>
            </div>
            <div class="cam-frame">
                <img id="img-{cam["id"]}" src="/cameras/snapshot/{cam["id"]}" 
                     onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 640 360%22><rect fill=%22%23111%22 width=%22640%22 height=%22360%22/><text fill=%22%23555%22 x=%22320%22 y=%22180%22 text-anchor=%22middle%22 font-size=%2220%22>Chargement…</text></svg>'"
                     style="width:100%;height:100%;object-fit:contain;background:#111">
            </div>
            <div class="cam-actions">
                <button onclick="wakeCam('{cam["id"]}','{wake_id}')" style="background:var(--accent);color:#fff;border:none;border-radius:4px;padding:4px 10px;cursor:pointer;font-size:11px">📡 Wake</button>
                <button onclick="refreshCam('{cam["id"]}')" style="background:var(--green);color:#fff;border:none;border-radius:4px;padding:4px 10px;cursor:pointer;font-size:11px">🔄 Refresh</button>
                <span id="status-{cam["id"]}" style="font-size:10px;color:var(--dim);margin-left:8px">🕐 {last}</span>
            </div>
        </div>'''
    
    head = "" if embed else '''<!DOCTYPE html>
<html lang="fr">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>📷 Caméras LEO</title>'''
    
    css = '''<style>
:root{{--bg:#0d1117;--text:#c9d1d9;--card:#161b22;--border:#30363d;--accent:#1f6feb;--dim:#8b949e;--green:#3fb950;--red:#f85149;--orange:#d29922}}
[data-theme="light"]{{--bg:#f0f2f5;--text:#1a1a2e;--card:#fff;--border:#d1d5db;--accent:#2563eb;--dim:#6b7280;--green:#059669;--red:#dc2626;--orange:#d97706}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,sans-serif;padding:16px}}
h1{font-size:20px;margin-bottom:4px}
.note{color:var(--dim);font-size:11px;margin-bottom:12px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:12px}
.cam-card{background:var(--card);border:2px solid var(--border);border-radius:8px;overflow:hidden}
.cam-name{padding:8px 12px;font-weight:600;font-size:13px;background:#1c2128;border-bottom:2px solid var(--border)}
.cam-frame{aspect-ratio:16/9;overflow:hidden}
.cam-actions{padding:6px 12px;display:flex;align-items:center;background:#1c2128;border-top:2px solid var(--border)}
</style>'''
    
    body_open = "" if embed else f'''{head}
{css}
</head>
<body>'''
    
    body_close = "" if embed else '''</body></html>'''
    
    title = '<h1>📷 Caméras LEO</h1>' if not embed else ''
    
    html = f'''{body_open}
{title}
<div class="note">Caméras batterie — image capturée uniquement sur détection de mouvement. Wake = activation détection.</div>
<div class="grid">{cards}</div>
<script>
//Sync theme
(function(){{var t=localStorage.getItem('leo-theme');if(t)document.documentElement.setAttribute('data-theme',t);}})();
function wakeCam(camId, wakeId) {{
    var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
    var status = document.getElementById('status-'+camId);
    status.textContent = '⏳ Réveil...';
    status.style.color = 'var(--orange)';
    
    fetch('/api/ha/call_service', {{
        method: 'POST',
        headers: {{'Content-Type':'application/json'}},
        body: JSON.stringify({{token:token, domain:'button', service:'press', entity_id:wakeId}})
    }}).then(function() {{
        status.textContent = '✅ En veille détection';
        status.style.color = 'var(--green)';
        setTimeout(function() {{
            var img = document.getElementById('img-'+camId);
            img.src = '/cameras/snapshot/' + camId + '?' + Date.now();
        }}, 2000);
    }}).catch(function() {{
        status.textContent = '❌ Erreur';
    }});
}}

function refreshCam(camId) {{
    var img = document.getElementById('img-'+camId);
    var status = document.getElementById('status-'+camId);
    if (img) {{
        img.src = '/cameras/snapshot/' + camId + '?' + Date.now();
        status.textContent = '🔄 Rafraîchi';
        status.style.color = 'var(--green)';
        setTimeout(function() {{ status.textContent = '🕐 ' + new Date().toLocaleTimeString(); }}, 2000);
    }}
}}

setInterval(function() {{
    document.querySelectorAll('.cam-frame img').forEach(function(img) {{
        img.src = img.src.split('?')[0] + '?' + Date.now();
    }});
}}, 60000);
</script>
{body_close}'''
    return HTMLResponse(html)

@app.get("/cameras/snapshot/{entity_id}")
async def camera_snapshot(entity_id: str, request: Request):
    """Proxy vers Home Assistant pour contourner CORS."""
    from fastapi.responses import Response as FastResponse
    url = f"{HA_URL}/api/camera_proxy/{entity_id}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {HA_TOKEN}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return FastResponse(content=resp.read(), media_type=resp.headers.get("Content-Type", "image/jpeg"))
    except:
        raise HTTPException(502, detail="Caméra inaccessible")

@app.post("/api/ha/call_service")
async def ha_call_service(request: Request):
    """Appelle un service Home Assistant."""
    body = await request.json()
    token = body.get("token", "")
    if token != AUTH_TOKEN:
        raise HTTPException(401)
    
    domain = body.get("domain")
    service = body.get("service")
    entity_id = body.get("entity_id")
    
    url = f"{HA_URL}/api/services/{domain}/{service}"
    data = json.dumps({"entity_id": entity_id}).encode()
    req = urllib.request.Request(url, data=data, 
        headers={"Authorization": f"Bearer {HA_TOKEN}", "Content-Type": "application/json"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return JSONResponse(json.loads(r.read()))
    except Exception as e:
        raise HTTPException(502, detail=str(e))

@app.get("/api/energy")
async def api_energy(request: Request):
    if not check_token(request): raise HTTPException(401)
    if ENERGY_FILE.exists():
        return JSONResponse(json.loads(ENERGY_FILE.read_text()))
    return JSONResponse({"error": "no data"}, status_code=503)

@app.get("/api/energy/history")
async def api_energy_history(request: Request):
    if not check_token(request): raise HTTPException(401)
    if ENERGY_HISTORY_FILE.exists():
        return JSONResponse(json.loads(ENERGY_HISTORY_FILE.read_text()))
    return JSONResponse([], status_code=503)

@app.get("/api/energy/daily")
async def api_energy_daily(request: Request):
    if not check_token(request): raise HTTPException(401)
    daily_file = Path("/home/tofdan/.hermes/metrics/energy_daily.json")
    if daily_file.exists():
        return JSONResponse(json.loads(daily_file.read_text()))
    return JSONResponse([], status_code=503)

@app.get("/api/energy/monthly")
async def api_energy_monthly(request: Request):
    if not check_token(request): raise HTTPException(401)
    monthly_file = Path("/home/tofdan/.hermes/metrics/energy_monthly.json")
    if monthly_file.exists():
        return JSONResponse(json.loads(monthly_file.read_text()))
    return JSONResponse([], status_code=503)

@app.get("/api/energy/telegram")
async def api_energy_telegram(request: Request):
    """Données détaillées DSMR + tableaux."""
    if not check_token(request): raise HTTPException(401)
    import subprocess
    try:
        result = subprocess.run(
            ["/home/tofdan/.hermes/venv/bin/python3", "/home/tofdan/.hermes/scripts/energy-telegram.py"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return JSONResponse(json.loads(result.stdout))
    except:
        pass
    return JSONResponse({"error": "telegram unavailable"}, status_code=503)

@app.get("/energy")
async def energy_page(request: Request):
    if not check_token(request): raise HTTPException(401)
    embed = request.query_params.get("embed") == "1"
    
    snap = {}
    if ENERGY_FILE.exists():
        snap = json.loads(ENERGY_FILE.read_text())
    
    head = "" if embed else '<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>⚡ Énergie LEO</title>'
    chartjs = '<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>'
    
    html = f"""{head}
{chartjs}
<style>
:root{{--bg:#0d1117;--text:#c9d1d9;--card:#161b22;--border:#30363d;--accent:#1f6feb;--dim:#8b949e;--green:#3fb950;--red:#f85149;--orange:#d29922;--purple:#bc8cff;--blue:#58a6ff}}
[data-theme="light"]{{--bg:#f0f2f5;--text:#1a1a2e;--card:#fff;--border:#d1d5db;--accent:#2563eb;--dim:#6b7280;--green:#059669;--red:#dc2626;--orange:#d97706;--purple:#7c3aed;--blue:#2563eb}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,sans-serif;padding:16px}}
h1{{font-size:20px;margin-bottom:16px}}
.kpi-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:16px}}
.kpi-card{{background:var(--card);border:2px solid var(--border);border-radius:8px;padding:14px;text-align:center}}
.kpi-val{{font-size:26px;font-weight:700;margin:4px 0}}
.kpi-lbl{{font-size:11px;color:var(--dim);text-transform:uppercase;letter-spacing:.5px}}
.kpi-sub{{font-size:10px;color:#484f58;margin-top:4px}}
.chart-box{{background:var(--card);border:2px solid var(--border);border-radius:8px;padding:16px;margin-bottom:12px}}
canvas{{max-height:280px}}
.phases{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px}}
.phase{{background:var(--card);border-radius:6px;padding:10px;text-align:center}}
</style>
{"</head><body>" if not embed else ""}
<h1>{'⚡ Énergie — HomeWizard P1' if not embed else ''} <span style="color:var(--dim);font-size:12px;font-weight:400">Fluvius {snap.get('meter','?')}</span></h1>

<div class="kpi-grid">
  <div class="kpi-card"><div class="kpi-val" id="pwr">—</div><div class="kpi-lbl">Puissance</div><div class="kpi-sub" id="pwr-sub"></div></div>
  <div class="kpi-card"><div class="kpi-val" id="net">—</div><div class="kpi-lbl">Bilan Net</div></div>
  <div class="kpi-card"><div class="kpi-val" id="imp">—</div><div class="kpi-lbl">Import Total</div><div class="kpi-sub">kWh</div></div>
  <div class="kpi-card"><div class="kpi-val" id="exp">—</div><div class="kpi-lbl">Export Total</div><div class="kpi-sub">kWh</div></div>
  <div class="kpi-card"><div class="kpi-val" id="peak">—</div><div class="kpi-lbl">Pic Mensuel</div><div class="kpi-sub">W</div></div>
  <div class="kpi-card"><div class="kpi-val" id="volt">—</div><div class="kpi-lbl">Tension</div><div class="kpi-sub">V L1</div></div>
</div>

<div class="chart-box"><canvas id="powerChart"></canvas></div>
<div class="chart-box"><h3 style="margin:0 0 12px;font-size:14px">🔌 Phases</h3><div class="phases" id="phases"></div></div>

<script>
//Sync theme
(function(){{var t=localStorage.getItem('leo-theme');if(t)document.documentElement.setAttribute('data-theme',t);}})();
var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
var powerChart = null;

function loadSnapshot() {{
  fetch('/api/energy?token='+token).then(r=>r.json()).then(d=>{{
    if(d.error) return;
    var pwr = d.power_now_w;
    var color = pwr < 0 ? '#3fb950' : '#f85149';
    ['pwr','net','imp','exp','peak','volt'].forEach(function(id){{ var el=document.getElementById(id); if(!el)return; }});
    document.getElementById('pwr').textContent = Math.abs(pwr)+' W';
    document.getElementById('pwr').style.color = color;
    document.getElementById('pwr-sub') && (document.getElementById('pwr-sub').textContent = pwr < 0 ? '☀️ Injection' : '⚡ Conso');
    document.getElementById('net').textContent = (d.net_kwh>0?'+':'')+d.net_kwh.toFixed(0)+' kWh';
    document.getElementById('net').style.color = d.net_kwh>0?'#3fb950':'#f85149';
    document.getElementById('imp').textContent = d.import_total_kwh.toFixed(0)+' kWh';
    document.getElementById('imp').style.color = '#58a6ff';
    document.getElementById('exp').textContent = d.export_total_kwh.toFixed(0)+' kWh';
    document.getElementById('exp').style.color = '#3fb950';
    document.getElementById('peak').textContent = d.peak_month_w+' W';
    document.getElementById('peak').style.color = '#d29922';
    document.getElementById('volt').textContent = d.voltage_v.toFixed(1)+' V';
    document.getElementById('volt').style.color = '#bc8cff';
    
    var ph = d.phases;
    document.getElementById('phases').innerHTML = ['l1','l2','l3'].map(function(p){{
      var phase = ph[p];
      return '<div class="phase"><div style="font-size:20px;font-weight:700;color:'+(phase.w<0?'#3fb950':'#f85149')+'">'+phase.w+' W</div><div style="font-size:11px">'+phase.v.toFixed(1)+'V · '+phase.a.toFixed(1)+'A</div><div style="font-size:10px;color:var(--dim);margin-top:2px">'+p.toUpperCase()+'</div></div>';
    }}).join('');
  }});
}}

function loadHistory() {{
  fetch('/api/energy/history?token='+token).then(r=>r.json()).then(history=>{{
    if(!history || !history.length) return;
    var labels = history.map(function(p){{return p.ts.substring(11,16)}});
    var values = history.map(function(p){{return Math.abs(p.w)}});
    var colors = history.map(function(p){{return p.w < 0 ? 'rgba(63,185,80,.4)' : 'rgba(248,81,73,.4)'}});
    var borders = history.map(function(p){{return p.w < 0 ? '#3fb950' : '#f85149'}});
    
    if(powerChart) powerChart.destroy();
    var ctx = document.getElementById('powerChart').getContext('2d');
    powerChart = new Chart(ctx, {{
      type: 'bar',
      data: {{ labels: labels, datasets: [{{ label: 'Puissance (W)', data: values, backgroundColor: colors, borderColor: borders, borderWidth: 1, borderRadius: 2 }}] }},
      options: {{ responsive: true, maintainAspectRatio: false,
        plugins: {{ legend: {{display:false}}, title: {{display:true, text:'📈 Puissance — 24h', color:'#8b949e', font:{{size:12}}}} }},
        scales: {{ x: {{ticks:{{color:'#484f58',font:{{size:9}},maxTicksLimit:25}},grid:{{color:'#21262d'}}}}, y: {{ticks:{{color:'#484f58',font:{{size:9}}}},grid:{{color:'#21262d'}}}} }}
      }}
    }});
  }});
}}

loadSnapshot();
loadHistory();
setInterval(loadSnapshot, 30000);
setInterval(loadHistory, 120000);
</script>
{"</body></html>" if not embed else ""}"""
    return HTMLResponse(html)

# ── Wiki Voyages (static files, monté avant BAVI pour priorité) ──
VOYAGES_SITE = Path("/home/tofdan/Projets_Dev/voyages-wiki/site-local")
@app.get("/api/viessmann")
async def api_viessmann(request: Request):
    if not check_token(request): raise HTTPException(401)
    data_file = Path.home() / ".hermes" / "metrics" / "viessmann.json"
    if not data_file.exists():
        return {"error": "no data", "timestamp": None}
    with open(data_file) as f:
        return json.load(f)

@app.get("/viessmann")
async def viessmann_page(request: Request):
    """Page Viessmann — chaudière gaz + solaire."""
    if not check_token(request): raise HTTPException(401)
    embed = request.query_params.get("embed") == "1"
    theme = request.query_params.get("theme", "light")
    
    data_file = Path.home() / ".hermes" / "metrics" / "viessmann.json"
    data = {}
    if data_file.exists():
        try:
            with open(data_file) as f:
                data = json.load(f)
        except:
            pass
    
    cards_html = f"""
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-lbl">🔥 Chaudière</div>
        <div class="kpi-val">{data.get('boiler_temp', '?')}<span style="font-size:16px">°C</span></div>
      </div>
      <div class="kpi-card">
        <div class="kpi-lbl">🌡️ Extérieure</div>
        <div class="kpi-val">{data.get('outside_temp', '?')}<span style="font-size:16px">°C</span></div>
      </div>
      <div class="kpi-card">
        <div class="kpi-lbl">🚿 Eau chaude</div>
        <div class="kpi-val">{data.get('dhw_temp', '?')}<span style="font-size:16px">°C</span></div>
      </div>
      <div class="kpi-card">
        <div class="kpi-lbl">🔧 Brûleur</div>
        <div class="kpi-val">{data.get('burner_modulation', '?')}<span style="font-size:16px">%</span></div>
      </div>
      <div class="kpi-card">
        <div class="kpi-lbl">📐 Circuit 0</div>
        <div class="kpi-val">{data.get('circuit0_supply', '?')}<span style="font-size:16px">°C</span></div>
      </div>
      <div class="kpi-card">
        <div class="kpi-lbl">☀️ Solaire prod</div>
        <div class="kpi-val">{data.get('solar_production', '0')}<span style="font-size:16px">W</span></div>
      </div>
    </div>
    <div class="info-line">
      Mode: <strong>{data.get('circuit0_mode', '?')}</strong> · Programme: <strong>{data.get('circuit0_program', '?')}</strong> · 
      Consigne ECS: <strong>{data.get('dhw_target', '?')}°C</strong> · 
      Solaire total: <strong>{data.get('solar_cumulative', '?')} kWh</strong> · 
      MàJ: <span id="viessmann-updated">{data.get('timestamp', '?')[:19]}</span>
    </div>
    """
    
    html_open = f'<html lang="fr" data-theme="{theme}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>🔥 Viessmann</title>' if not embed else ""
    html_close = "</body></html>" if not embed else ""
    body_tag = '<body>' if not embed else ""
    title_tag = '<h1>🔥 Viessmann — Sombreffe</h1>' if not embed else ''
    
    html = f"""{html_open}
<style>
:root{{--bg:#0d1117;--text:#c9d1d9;--card:#161b22;--border:#30363d;--accent:#1f6feb;--dim:#8b949e;--green:#3fb950;--red:#f85149;--orange:#d29922}}
[data-theme="light"]{{--bg:#f0f2f5;--text:#1a1a2e;--card:#fff;--border:#d1d5db;--accent:#2563eb;--dim:#6b7280;--green:#059669;--red:#dc2626;--orange:#d97706}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,sans-serif;padding:16px}}
h1{{font-size:20px;margin-bottom:16px}}
.kpi-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:16px}}
.kpi-card{{background:var(--card);border:2px solid var(--border);border-radius:8px;padding:14px;text-align:center}}
.kpi-val{{font-size:26px;font-weight:700;margin:4px 0}}
.kpi-lbl{{font-size:11px;color:var(--dim);text-transform:uppercase;letter-spacing:.5px}}
.info-line{{font-size:13px;color:var(--dim);text-align:center;padding:8px;background:var(--card);border-radius:8px;border:2px solid var(--border)}}
</style>
{body_tag}
{title_tag}
{cards_html}
<script>
(function(){{var t=localStorage.getItem('leo-theme');if(t)document.documentElement.setAttribute('data-theme',t);}})();
var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
setInterval(function(){{
  fetch('/api/viessmann?token='+token).then(function(r){{return r.json();}}).then(function(d){{
    if(d.error) return;
    document.querySelectorAll('.kpi-val').forEach(function(el,i){{
      var vals = [d.boiler_temp+'°C', d.outside_temp+'°C', d.dhw_temp+'°C', d.burner_modulation+'%', d.circuit0_supply+'°C', (d.solar_production||0)+'W'];
      if(vals[i]) el.innerHTML = '<span style=\"font-size:26px\">'+vals[i]+'</span>';
    }});
    document.getElementById('viessmann-updated').textContent = (d.timestamp||'').substring(0,19);
  }});
}},30000);
</script>
{html_close}"""
    return HTMLResponse(html)

if VOYAGES_SITE.exists():
    app.mount("/voyages", StaticFiles(directory=str(VOYAGES_SITE), html=True), name="voyages")

if BAVI_SITE.exists():
    app.mount("/", StaticFiles(directory=str(BAVI_SITE), html=True), name="wiki")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8765)
