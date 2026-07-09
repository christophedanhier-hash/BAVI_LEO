#!/usr/bin/env python3
"""
LEO Serveur Unifié — Wiki BAVI + Dashboard + API
Usage: .venv/bin/uvicorn server:app --host 0.0.0.0 --port 8765
"""
import json, subprocess, os, sys, re, urllib.request, urllib.parse
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

BASE = Path("/opt/data")
BAVI_SITE = BASE / "BAVI_LEO/site"
DASHBOARD_FILE = BASE / "dashboard.html"
CRON_JOBS_FILE = BASE / "profiles/leo-copilot/cron/jobs.json"
N8N_CONFIG_FILE = BASE / "n8n-webhooks.json"
METRICS_FILE = BASE / "metrics/leo-unified.json"
AUTH_TOKEN = "leo-panel-2026"

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
        r = subprocess.run(["/opt/hermes/.venv/bin/hermes", "cron", "run", "--profile", "leo-copilot", job_id],
                          capture_output=True, text=True, timeout=300,
                          env={**os.environ, "HOME": "/opt/data/home"})
        return {"ok": r.returncode == 0, "output": r.stdout[:2000], "error": r.stderr[:500]}
    except Exception as e:
        return {"ok": False, "error": str(e)}

# ── API: Métriques ──
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
@app.get("/api/n8n")
async def api_n8n(request: Request):
    if not check_token(request): raise HTTPException(401)
    return json.loads(N8N_CONFIG_FILE.read_text()) if N8N_CONFIG_FILE.exists() else []

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
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    if not check_token(request): raise HTTPException(401)
    return HTMLResponse(DASHBOARD_FILE.read_text())

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

if BAVI_SITE.exists():
    app.mount("/", StaticFiles(directory=str(BAVI_SITE), html=True), name="wiki")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8765)
