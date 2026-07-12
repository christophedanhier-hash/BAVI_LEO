#!/usr/bin/env python3
"""Dashboard HTML builder — génère le dashboard à partir de leo-unified.json."""
import json, time
from pathlib import Path
from datetime import datetime, timedelta

METRICS_FILE = Path("/home/tofdan/.hermes/metrics/leo-unified.json")

def esc(t):
    if not t: return ""
    return str(t).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def norm_model(name):
    """Normalise les noms de modèles pour l'affichage."""
    m = (name or "").lower().strip()
    if "deepseek-v4-pro" in m:
        return "DS Pro"
    if "deepseek-chat" in m or "deepseek-v4-flash" in m or "flash" in m:
        return "DS Flash"
    if "gemini" in m:
        return "Gemini"
    if "claude" in m:
        return "Claude"
    if "gpt" in m:
        return "GPT"
    short = (name or "").split("/")[-1]
    return short[:20]

def load_metrics():
    data = json.loads(METRICS_FILE.read_text())
    meta = data.get("_meta", {})
    return {
        "status": meta.get("status", "unknown"),
        "ts": meta.get("generated_at", "?"),
        "sources": meta.get("sources", {}),
        "ok_count": sum(1 for v in meta.get("sources", {}).values() if v.get("status") == "ok"),
        "total_count": len(meta.get("sources", {})),
        "alerts": data.get("alerts", []),
        "s": data.get("sessions", {}) or {},
        "b": data.get("budget", {}) or {},
        "c": data.get("crons", {}) or {},
        "i": data.get("infra", {}) or {},
        "n": data.get("n8n", {}) or {},
        "ba": data.get("bavi", {}) or {},
        "bo": data.get("bots", {}) or {},
        "va": data.get("vaults", {}) or {},
    }

def build_html():
    d = load_metrics()
    s = d["s"]; b = d["b"]; c = d["c"]; i = d["i"]; n = d["n"]
    ba = d["ba"]; bo = d["bo"]; va = d["va"]; alerts = d["alerts"]
    bots_list = bo.get("bots", []) if isinstance(bo, dict) else []
    gw_up = sum(1 for b in bots_list if b.get("online"))
    gw_total = len(bots_list)
    ts = d["ts"]
    
    balance = b.get("balance", 0)
    bgt_color = "#34d399" if balance > 30 else ("#fbbf24" if balance > 15 else "#ef4444")
    days_rem = b.get("days_remaining", 30)
    monthly_spent = b.get("monthly_spent", 0)
    monthly_cap = b.get("monthly_cap", 50)
    
    cr_ok = c.get("status_ok", 0); cr_err = c.get("status_error", 0)
    cr_total = c.get("total", 0)
    
    sess_today = s.get("today", {}).get("sessions", 0)
    sess_total = s.get("total", 0)
    tokens_total = (s.get("total_tokens_in", 0) + s.get("total_tokens_out", 0)) // 1_000_000
    
    daily = s.get("daily", [])
    dmap = {x["date"]: x for x in daily}
    if daily:
        all_dates = sorted(dmap.keys())
        d0 = datetime.strptime(all_dates[0], "%Y-%m-%d")
        d1 = datetime.strptime(all_dates[-1], "%Y-%m-%d")
        delta = (d1 - d0).days
        filled_dates = []
        for day_idx in range(delta + 1):
            dt = d0 + timedelta(days=day_idx)
            ds = dt.strftime("%Y-%m-%d")
            filled_dates.append(dmap.get(ds, {"date": ds, "sessions": 0, "tokens_in": 0, "tokens_out": 0, "messages": 0, "tools": 0}))
    else:
        filled_dates = daily
    js_daily_labels = json.dumps([x["date"][-5:] for x in filled_dates])
    js_daily_sessions = json.dumps([x["sessions"] for x in filled_dates])
    js_daily_tokens = json.dumps([(x.get("tokens_in",0)+x.get("tokens_out",0))//1000 for x in filled_dates])
    
    bh = b.get("history", [])
    js_bh_labels = json.dumps([x["date"][-5:] for x in bh[-30:]])
    js_bh_values = json.dumps([x["balance"] for x in bh[-30:]])
    
    by_model = s.get("by_model", {})
    js_model_labels = json.dumps([norm_model(k) for k in by_model.keys()])
    js_model_sessions = json.dumps([v["sessions"] for v in by_model.values()])
    
    recent = s.get("recent_sessions", [])[:8]
    
    html = f'''<!DOCTYPE html>
<html lang="fr" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LEO Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
<script src="/leo/monitoring.js?v={{version}}"></script>
</script>
<style>
:root {{
  --bg: #0f172a; --card: #1e293b; --border: #334155; --text: #e2e8f0;
  --dim: #64748b; --accent: #a78bfa; --green: #34d399; --yellow: #fbbf24;
  --red: #f87171; --purple: #a78bfa; --header-bg: #1e293b; --hover: #2e1065;
  --shadow: rgba(0,0,0,.3); --th-bg: #0f172a; --th-border: #334155;
  --row-hover: #1e293b; --badge-ok-bg: #0f2a1a; --badge-ok-border: #34d39940;
  --badge-err-bg: #2a0f0f; --badge-err-border: #f8717140;
  --badge-pending-bg: #2a1f0f; --badge-pending-border: #fbbf2440;
  --progress-bg: #334155; --footer-border: #1e293b;
}}
[data-theme="light"] {{
  --bg: #f8fafc; --card: #ffffff; --border: #e2e8f0; --text: #0f172a;
  --dim: #64748b; --accent: #7c3aed; --green: #16a34a; --yellow: #d97706;
  --red: #dc2626; --purple: #7c3aed; --header-bg: #ffffff; --hover: #f1f5f9;
  --shadow: rgba(0,0,0,.08); --th-bg: #f8fafc; --th-border: #e2e8f0;
  --row-hover: #f8fafc; --badge-ok-bg: #dcfce7; --badge-ok-border: #16a34a40;
  --badge-err-bg: #fee2e2; --badge-err-border: #dc262640;
  --badge-pending-bg: #fef3c7; --badge-pending-border: #d9770640;
  --progress-bg: #e2e8f0; --footer-border: #e2e8f0;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);padding:16px;max-width:1500px;margin:0 auto;transition:background .2s,color .2s}}
.header{{display:flex;justify-content:space-between;align-items:center;padding:14px 22px;background:var(--header-bg);border:2px solid var(--border);border-radius:12px;margin-bottom:16px;flex-wrap:wrap;gap:8px;box-shadow:0 1px 4px var(--shadow)}}
.header h1{{font-size:20px}} .header h1 span{{color:var(--accent)}}
.header .sub{{color:var(--dim);font-size:12px}}
.toggle-theme{{background:var(--card);border:2px solid var(--border);border-radius:8px;padding:6px 12px;cursor:pointer;font-size:14px;color:var(--text);transition:.15s}}
.toggle-theme:hover{{border-color:var(--accent)}}
.tabs{{display:flex;gap:4px;margin-bottom:16px;flex-wrap:wrap}}
.tab{{padding:8px 18px;background:var(--card);border:2px solid var(--border);border-radius:8px;cursor:pointer;font-size:13px;font-weight:600;color:var(--dim);transition:.15s}}
.tab:hover{{border-color:var(--accent);color:var(--text);background:var(--hover)}}
.tab.active{{background:var(--accent);border-color:var(--accent);color:#fff;box-shadow:0 0 0 1px var(--accent)}}
.panel{{display:none}} .panel.active{{display:block}}
.kpi-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin-bottom:16px}}
.kpi-card{{background:var(--card);border:2px solid var(--border);border-radius:10px;padding:14px;text-align:center;transition:border-color .15s}}
.kpi-card:hover{{border-color:var(--accent)}}
.kpi-card .icon{{font-size:22px;margin-bottom:4px}}
.kpi-card .val{{font-size:24px;font-weight:700;color:var(--text)}}
.kpi-card .lbl{{font-size:11px;color:var(--dim);margin-top:2px}}
.card{{background:var(--card);border:2px solid var(--border);border-radius:10px;padding:16px;margin-bottom:16px;box-shadow:0 1px 4px var(--shadow)}}
.card h3{{font-size:13px;color:var(--text);text-transform:uppercase;letter-spacing:.3px;margin-bottom:10px;padding-bottom:6px;border-bottom:2px solid var(--border)}}
.grid-2{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}}
@media(max-width:768px){{.grid-2{{grid-template-columns:1fr}}}}
.chart-box canvas{{max-height:220px;width:100%}}
table{{width:100%;border-collapse:collapse;font-size:12px}}
th{{text-align:left;padding:8px 10px;color:var(--dim);font-weight:500;border-bottom:2px solid var(--th-border);background:var(--th-bg);position:sticky;top:0}}
td{{padding:7px 10px;border-bottom:1px solid var(--border);white-space:nowrap}}
tr:hover td{{background:var(--row-hover)}}
.badge{{display:inline-block;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:600;border:1px solid}}
.badge.ok{{background:var(--badge-ok-bg);color:var(--green);border-color:var(--badge-ok-border)}}
.badge.err{{background:var(--badge-err-bg);color:var(--red);border-color:var(--badge-err-border)}}
.badge.pending{{background:var(--badge-pending-bg);color:var(--yellow);border-color:var(--badge-pending-border)}}
.progress{{height:6px;background:var(--progress-bg);border-radius:3px;margin-top:6px;overflow:hidden}}
.progress-bar{{height:100%;border-radius:3px;transition:width .5s}}
.footer{{text-align:center;color:var(--dim);font-size:11px;padding:20px 0;border-top:2px solid var(--footer-border);margin-top:10px}}
a{{color:var(--accent);text-decoration:none}} a:hover{{text-decoration:underline}}
.alert-bar{{background:var(--badge-err-bg);border:2px solid var(--red);border-radius:8px;padding:10px 16px;margin-bottom:14px;display:flex;gap:8px;align-items:center;font-size:13px;box-shadow:0 1px 4px var(--shadow)}}
.alert-bar.warn{{background:var(--badge-pending-bg);border-color:var(--yellow);box-shadow:0 1px 4px var(--shadow)}}
.heal-entry{{padding:5px 8px;font-size:12px;border-bottom:1px solid var(--border);border-radius:4px}}
.heal-entry:last-child{{border:none}}
.heal-entry.fix{{background:var(--badge-ok-bg)}}
.heal-entry.unresolved{{background:var(--badge-err-bg)}}
.repos-grid,.bots-grid,.bureaux-grid{{display:grid;gap:8px}}
.repos-grid{{grid-template-columns:repeat(auto-fill,minmax(240px,1fr))}}
.bureaux-grid{{grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}}
.bots-grid{{grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}}
.repo-card,.bureau-card,.bot-card{{background:var(--card);border:2px solid var(--border);border-radius:8px;padding:10px 12px;font-size:12px;transition:border-color .15s;position:relative}}
.repo-card:hover,.bureau-card:hover,.bot-card:hover{{border-color:var(--accent)}}
.repo-card .name,.bureau-card .name,.bot-card .name{{font-weight:600;font-size:13px;color:var(--text)}}
.repo-card .desc,.bureau-card .desc,.bot-card .desc{{color:var(--dim);font-size:11px;margin-top:2px}}
.mon-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-bottom:16px}}
.mon-card{{background:var(--card);border:2px solid var(--border);border-radius:10px;padding:16px;text-align:center}}
.mon-card h4{{font-size:11px;color:var(--dim);text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px}}
.mon-card canvas{{display:block;margin:0 auto}}
.mon-card .detail{{font-size:10px;color:var(--dim);margin-top:6px}}
.mon-val{{font-size:22px;font-weight:700;margin-top:4px}}
.mon-svc{{display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-bottom:1px solid var(--border);font-size:13px}}
.mon-svc:last-child{{border-bottom:none}}
.badge.up{{background:var(--badge-ok-bg);color:var(--green);border-color:var(--badge-ok-border)}}
.badge.down{{background:var(--badge-err-bg);color:var(--red);border-color:var(--badge-err-border)}}
.gauge-wrap{{position:relative;width:100px;height:100px;margin:0 auto}}
</style>
</head>
<body>

<div class="header">
  <div><h1>🦁 <span>LEO</span> Dashboard</h1><div class="sub">Mise à jour : {esc(ts[:19])}</div></div>
  <div style="display:flex;align-items:center;gap:8px"><span class="badge {'ok' if d['status']=='complete' else 'err'}">{d['status'].upper()}</span> {d['ok_count']}/{d['total_count']} sources <span class="badge {'ok' if gw_up >= gw_total else 'err'}" style="margin-left:4px">{gw_up}/{gw_total} 🛡️</span> <button class="toggle-theme" onclick="toggleTheme()">🌓</button></div>
</div>

{"".join(f'<div class="alert-bar {"warn" if a.get("severity")=="warning" else ""}">{"🔴" if a.get("severity")=="critical" else "🟡"} {esc(a["message"])}</div>' for a in alerts[:3])}

<div class="tabs">
  <div class="tab active" onclick="switchTab(this,'tab-syn')">🏠 Synthèse</div>
  <div class="tab" onclick="switchTab(this,'tab-ana')">📊 Analyse</div>
  <div class="tab" onclick="switchTab(this,'tab-infra')">⚙️ Infra</div>
  <div class="tab" onclick="switchTab(this,'tab-monitoring')">🖥️ Monitoring</div>
  <div class="tab" onclick="switchTab(this,'tab-bavi')">🏛️ BAVI</div>
  <div class="tab" onclick="switchTab(this,'tab-crons-mgmt');loadCrons()">⚙️ Crons</div>
  <div class="tab" onclick="switchTab(this,'tab-cameras');loadCameras()">📷 Caméras</div>
  <div class="tab" onclick="switchTab(this,'tab-energy');loadEnergy()">⚡ Énergie</div>
</div>
<!-- Energy bar -->
<div id="energy-bar" style="display:flex;justify-content:center;align-items:center;gap:16px;padding:8px 16px;background:var(--card);border:2px solid var(--border);border-radius:8px;margin-bottom:8px;font-size:13px;font-weight:600">
  <span id="energy-pwr" style="color:var(--dim)">⚡ Chargement...</span>
  <span id="energy-net" style="color:var(--dim)"></span>
  <span id="energy-imp" style="color:var(--dim);font-size:11px"></span>
  </div>
  <script>
  (function(){{
  var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
  fetch('/api/energy?token='+token).then(function(r){{return r.json()}}).then(function(d){{
    if(d.error) return;
    var pwr = d.power_now_w;
    var color = pwr < 0 ? 'var(--green)' : 'var(--red)';
    document.getElementById('energy-pwr').innerHTML = '⚡ '+Math.abs(pwr)+'W '+(pwr < 0 ? '☀️ Injection' : '🔴 Conso');
    document.getElementById('energy-pwr').style.color = color;
    document.getElementById('energy-net').innerHTML = 'Net: '+(d.net_kwh>0?'+':'')+d.net_kwh.toFixed(0)+' kWh';
    document.getElementById('energy-net').style.color = d.net_kwh > 0 ? 'var(--green)' : 'var(--red)';
    document.getElementById('energy-imp').innerHTML = 'Import: '+d.import_total_kwh.toFixed(0)+' kWh | Export: '+d.export_total_kwh.toFixed(0)+' kWh';
  }}).catch(function(){{}});
  }})();
  </script>

<!-- Synthèse -->
<div id="tab-syn" class="panel active">
<div class="kpi-grid">
  <div class="kpi-card"><div class="icon">💰</div><div class="val" style="color:{bgt_color}">{balance:.2f}</div><div class="lbl">Budget DeepSeek</div></div>
  <div class="kpi-card"><div class="icon">⏱️</div><div class="val" style="color:{'var(--green)' if cr_err==0 else 'var(--red)'}">{cr_ok}/{cr_total}</div><div class="lbl">Crons OK</div></div>
  <div class="kpi-card"><div class="icon">💬</div><div class="val">{sess_today}</div><div class="lbl">Sessions aujourd'hui</div></div>
  <div class="kpi-card"><div class="icon">🧠</div><div class="val">{tokens_total}M</div><div class="lbl">Tokens totaux</div></div>
  <div class="kpi-card"><div class="icon">🌐</div><div class="val" style="color:{'var(--green)' if i.get('gateway')=='running' else 'var(--red)'}">{i.get('gateway','?')}</div><div class="lbl">Gateway</div></div>
  <div class="kpi-card"><div class="icon">📅</div><div class="val">{days_rem}d</div><div class="lbl">Jours budgétaires</div></div>
  <div class="kpi-card"><div class="icon">📓</div><div class="val">{va.get("total_notes",0)}</div><div class="lbl">Notes vaults</div></div>
</div>

<div class="grid-2">
  <div class="card">
    <h3>📈 Crons</h3>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px">
      <div style="background:var(--badge-ok-bg);padding:10px;border-radius:8px;text-align:center;border:1px solid var(--badge-ok-border)"><div style="font-size:18px;font-weight:700;color:var(--green)">{cr_ok}</div><div style="font-size:10px;color:var(--dim)">OK</div></div>
      <div style="background:var(--badge-err-bg);padding:10px;border-radius:8px;text-align:center;border:1px solid var(--badge-err-border)"><div style="font-size:18px;font-weight:700;color:var(--red)">{cr_err}</div><div style="font-size:10px;color:var(--dim)">Erreur</div></div>
      <div style="background:var(--card);padding:10px;border-radius:8px;text-align:center;border:1px solid var(--border)"><div style="font-size:18px;font-weight:700">{cr_total}</div><div style="font-size:10px;color:var(--dim)">Total</div></div>
    </div>
    <div style="margin-top:8px;font-size:12px">{"".join(f'<div style="display:flex;justify-content:space-between;padding:3px 0;border-bottom:1px solid var(--border)"><span>{esc(j["name"])}</span><span class="badge {j["status"]}">{j["status"]}</span></div>' for j in c.get("jobs",[])[:6])}</div>
  </div>
  <div class="card">
    <h3>🕐 Dernières sessions</h3>
    {"".join(f'<div style="display:flex;justify-content:space-between;padding:4px 0;font-size:12px;border-bottom:1px solid var(--border)"><span>{(r.get("title") or r.get("id","")[:12])[:35]}</span><span style="color:var(--dim)">{r.get("source","?")}</span></div>' for r in recent[:6])}
  </div>
</div>

<div class="card">
  <h3>💰 Budget (30 jours)</h3>
  <div style="display:flex;gap:16px;flex-wrap:wrap">
    <div><div class="val" style="font-size:22px;font-weight:700;color:{bgt_color}">${balance:.2f}</div><div class="lbl" style="font-size:11px;color:#8b949e">Restant</div></div>
    <div><div class="val" style="font-size:22px;font-weight:700">${monthly_spent:.2f}</div><div class="lbl" style="font-size:11px;color:#8b949e">Dépensé / mois</div></div>
    <div><div class="val" style="font-size:22px;font-weight:700">{days_rem}d</div><div class="lbl" style="font-size:11px;color:#8b949e">Jours restants</div></div>
  </div>
  <div class="progress"><div class="progress-bar" style="width:{min(100,monthly_spent/monthly_cap*100):.0f}%;background:{bgt_color}"></div></div>
  <canvas id="bhChart" height="60" style="margin-top:8px"></canvas>
</div>

<div class="card">
  <h3>📓 Vaults Obsidian</h3>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:6px">
    {"".join(f'<div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;font-weight:600">{"🦁" if k=="leo" or k=="leo-copilot" else "🏠" if k=="default" else "🎓" if k=="emile" else "🚐"}</div><div style="font-size:14px;font-weight:700">{vv.get("notes",0)}</div><div style="font-size:9px;color:var(--dim)">{"Michel" if k=="leo-copilot" else "Léo" if k=="default" else "Émile" if k=="emile" else k}</div></div>' for k,vv in va.get("vaults",{}).items())}
  </div>
  <div class="sub" style="margin-top:6px;font-size:11px">{va.get("total_dailies",0)} journaux · {va.get("total_notes",0)} notes</div>
</div>
</div>

<!-- Analyse -->
<div id="tab-ana" class="panel">
<div class="kpi-grid">
  <div class="kpi-card"><div class="icon">📝</div><div class="val">{sess_total}</div><div class="lbl">Sessions total</div></div>
  <div class="kpi-card"><div class="icon">🔤</div><div class="val">{(s.get("total_tokens_in",0)/1e6):.1f}M</div><div class="lbl">Tokens In</div></div>
  <div class="kpi-card"><div class="icon">📤</div><div class="val">{(s.get("total_tokens_out",0)/1e6):.1f}M</div><div class="lbl">Tokens Out</div></div>
  <div class="kpi-card"><div class="icon">🔧</div><div class="val">{s.get("total_tools",0):,}</div><div class="lbl">Tool Calls</div></div>
  <div class="kpi-card"><div class="icon">📊</div><div class="val">{s.get("total_api_calls",0):,}</div><div class="lbl">Appels API</div></div>
  <div class="kpi-card"><div class="icon">💲</div><div class="val">${s.get("total_estimated_cost",0):.2f}</div><div class="lbl">Coût estimé</div></div>
</div>

<div class="grid-2">
  <div class="card chart-box"><h3>📊 Sessions / jour</h3><canvas id="sessChart"></canvas></div>
  <div class="card chart-box"><h3>🧠 Tokens / jour (K)</h3><canvas id="tokChart"></canvas></div>
</div>

<div class="card chart-box"><h3>🧠 Modèles</h3><canvas id="modelChart" height="60"></canvas></div>

<div class="card">
  <h3>🔥 Top sessions</h3>
  <table><thead><tr><th>Titre</th><th>Source</th><th>Msg</th><th>Tokens</th><th>Coût</th></tr></thead>
  <tbody>{"".join(f'<tr><td style="max-width:280px;overflow:hidden;text-overflow:ellipsis">{esc((r.get("title") or ("#" + r.get("id","")[:10]))[:45])}</td><td><span class="badge ok">{esc(r.get("source","?"))}</span></td><td>{r.get("messages",0)}</td><td>{(r.get("tokens_in",0)+r.get("tokens_out",0))//1000}k</td><td>${r.get("cost",0):.4f}</td></tr>' for r in recent[:8])}</tbody></table>
</div>
</div>

<!-- Infra -->
<div id="tab-infra" class="panel">
<div class="kpi-grid">
  <div class="kpi-card"><div class="icon">🌐</div><div class="val" style="color:var(--green)">RUN</div><div class="lbl">Gateway</div></div>
  <div class="kpi-card"><div class="icon">🦙</div><div class="val" style="color:var(--green)">OK</div><div class="lbl">Ollama</div></div>
  <div class="kpi-card"><div class="icon">🔧</div><div class="val" style="color:var(--green)">OK</div><div class="lbl">n8n</div></div>
  <div class="kpi-card"><div class="icon">🖥️</div><div class="val">{i.get('machines',[{}])[0].get('cpu_load','?') if i.get('machines') else '?'}</div><div class="lbl">CPU</div></div>
  <div class="kpi-card"><div class="icon">💾</div><div class="val">{i.get('machines',[{}])[0].get('ram_pct','?') if i.get('machines') else '?'}%</div><div class="lbl">RAM</div></div>
  <div class="kpi-card"><div class="icon">💿</div><div class="val">{i.get('machines',[{}])[0].get('disk_pct','?') if i.get('machines') else '?'}%</div><div class="lbl">Disque</div></div>
</div>

<div class="card">
  <h3>⏱️ Crons — {cr_ok} OK · {cr_err} erreur · {cr_total} total</h3>
  <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:10px">
    <span style="background:var(--badge-ok-bg);color:var(--green);padding:2px 10px;border-radius:10px;font-size:11px;font-weight:600;border:1px solid var(--badge-ok-border)">✅ {cr_ok} OK</span>
    <span style="background:var(--badge-err-bg);color:var(--red);padding:2px 10px;border-radius:10px;font-size:11px;font-weight:600;border:1px solid var(--badge-err-border)">❌ {cr_err} erreur</span>
    <span style="background:var(--card);color:var(--dim);padding:2px 10px;border-radius:10px;font-size:11px;font-weight:600;border:1px solid var(--border)">⏸️ {c.get("status_paused",0)} en pause</span>
  </div>
  <table>
    <thead><tr><th></th><th>Cron</th><th>Horaire</th><th>Statut</th></tr></thead>
    <tbody>{"".join(f'<tr><td style="width:14px"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:{j["status"]=="ok" and "var(--green)" or j["status"]=="error" and "var(--red)" or "var(--yellow)"}"></span></td><td style="font-weight:500">{esc(j["name"][:45])}</td><td style="color:var(--dim);font-size:11px">{esc(j.get("schedule_human",""))}</td><td><span class="badge {j["status"]}" style="font-size:10px">{j["status"]}</span></td></tr>' for j in c.get("jobs",[]))}</tbody>
  </table>
</div>
</div>

<!-- Monitoring -->
<div id="tab-monitoring" class="panel">
<div class="mon-grid">
  <div class="mon-card"><h4>💻 CPU</h4><div class="gauge-wrap"><canvas id="mon-cpu-gauge" width="100" height="100"></canvas></div><div class="mon-val" id="mon-cpu-val">—</div><div class="detail" id="mon-cpu-detail">Chargement...</div></div>
  <div class="mon-card"><h4>🧠 RAM</h4><div class="gauge-wrap"><canvas id="mon-ram-gauge" width="100" height="100"></canvas></div><div class="mon-val" id="mon-ram-val">—</div><div class="detail" id="mon-ram-detail">Chargement...</div></div>
  <div class="mon-card"><h4>💾 Disque</h4><div class="gauge-wrap"><canvas id="mon-disk-gauge" width="100" height="100"></canvas></div><div class="mon-val" id="mon-disk-val">—</div><div class="detail" id="mon-disk-detail">Chargement...</div></div>
  <div class="mon-card"><h4>🌡️ Température</h4><div class="mon-val" id="mon-temp-val" style="font-size:36px;margin-top:16px">—</div><div class="detail">CPU Package</div></div>
</div>
<div class="grid-2">
  <div class="card"><h3>🐳 Services</h3><div id="mon-services">Chargement...</div></div>
  <div class="card"><h3>⏱️ État</h3><div id="mon-updated" style="font-size:14px;color:var(--dim)">En attente...</div><div style="margin-top:8px;font-size:12px;color:var(--dim)">Rafraîchissement 10s</div></div>
</div>
<div class="card chart-box" style="height:280px"><h3>📈 Historique (30 points — 5 minutes)</h3><canvas id="mon-history-chart"></canvas></div>
</div>

<!-- Gestion Crons -->
<div id="tab-crons-mgmt" class="panel">
<div class="card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
    <h3 style="margin:0;border:none;padding:0">⏱️ Gestion des Crons</h3>
    <button onclick="loadCrons()" style="background:var(--accent);border:none;color:#fff;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:12px">🔄 Rafraîchir</button>
  </div>
  <table>
    <thead><tr><th></th><th>Nom</th><th>Horaire</th><th>Statut</th><th style="text-align:right">Actions</th></tr></thead>
    <tbody id="crons-mgmt-body"><tr><td colspan="5" style="text-align:center;padding:20px">Chargement...</td></tr></tbody>
  </table>
</div>
</div>

<!-- BAVI -->
<div id="tab-bavi" class="panel">
<div class="bureaux-grid">
{"".join(f'<div class="bureau-card"><div class="name" style="color:{b.get("color","#58a6ff")}">{esc(b.get("name",""))}</div><div class="desc">{esc(b.get("role",""))}</div><div style="font-size:20px;font-weight:700;color:{b.get("color","#58a6ff")};opacity:.4;position:absolute;top:8px;right:12px">{b.get("analyses",0)}</div></div>' for b in ba.get("bureaux",[]))}
</div>

<h3 style="margin:16px 0 8px;font-size:14px;color:#8b949e">🤖 Bots Telegram — Activité par profil</h3>
<div class="bots-grid">
{"".join(f'<div class="bot-card"><div class="name">{esc(bot.get("name",""))} {"🟢" if bot.get("online") else "🔴"}</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;margin-top:6px;font-size:11px"><span style="color:var(--dim)">Sessions</span><span style="text-align:right;font-weight:600">{bot.get("sessions",0)}</span><span style="color:var(--dim)">Messages</span><span style="text-align:right;font-weight:600">{bot.get("messages",0):,}</span><span style="color:var(--dim)">Tokens</span><span style="text-align:right;font-weight:600">{(bot.get("tokens_in",0)+bot.get("tokens_out",0))//1000}k</span><span style="color:var(--dim)">Coût</span><span style="text-align:right;font-weight:600">${bot.get("cost",0):.2f}</span><span style="color:var(--dim)">Modèle</span><span style="text-align:right;font-weight:600;font-size:10px">{norm_model(bot.get("last_model",""))}</span><span style="color:var(--dim)">Dernière</span><span style="text-align:right;font-weight:600;font-size:10px">{(bot.get("last_session","") or "")[:16]}</span></div></div>' for bot in bo.get("bots",[]))}
</div>

<h3 style="margin:16px 0 8px;font-size:14px;color:#8b949e">🗺️ Voyages</h3>
<div class="bots-grid">
{"".join(f'<div class="bot-card"><div class="name">{esc(v.get("name",""))}</div></div>' for v in ba.get("voyages",{}).get("roadbooks",[]))}
</div>

<h3 style="margin:16px 0 8px;font-size:14px;color:#8b949e">📊 Modèles & Coûts</h3>
<div class="card" style="padding:10px">
<table>
<thead><tr><th>Modèle</th><th>Sessions</th><th>Tokens</th><th>Coût</th></tr></thead>
<tbody>{"".join(f'<tr><td>{norm_model(m)}</td><td>{v.get("sessions",0)}</td><td>{(v.get("tokens_in",0)+v.get("tokens_out",0))//1000}k</td><td>{"$"+str(round(v.get("cost",0),4)) if v.get("cost",0)>0 else "-"}</td></tr>' for m,v in sorted(s.get("by_model",{}).items(), key=lambda x:-x[1].get("cost",0)))} <tr style="font-weight:700;border-top:2px solid var(--border)"><td>TOTAL</td><td>{s.get("total",0)}</td><td>{(s.get("total_tokens_in",0)+s.get("total_tokens_out",0))//1000}k</td><td>${s.get("total_estimated_cost",0):.2f}</td></tr></tbody></table>
</div>
</div>

<!-- Caméras -->
<div id="tab-cameras" class="panel" style="padding:0;background:transparent;border:none">
  <div id="cameras-content" style="width:100%;min-height:500px;display:flex;align-items:center;justify-content:center">
    <span style="color:var(--dim)">Cliquez sur l'onglet pour charger...</span>
  </div>
</div>

<!-- Énergie -->
<div id="tab-energy" class="panel" style="padding:0;background:transparent;border:none">
  <div id="energy-content" style="width:100%;min-height:500px;display:flex;align-items:center;justify-content:center">
    <span style="color:var(--dim)">Cliquez sur l'onglet pour charger...</span>
  </div>
</div>

<div class="footer">🦁 LEO Dashboard · Généré dynamiquement</div>

<script>
(function() {{
  function safeChart(id, config) {{
    var el = document.getElementById(id);
    if (!el) return;
    try {{ new Chart(el, config); }} catch(e) {{}}
  }}
  safeChart('bhChart', {{ type:'line', data:{{ labels:{js_bh_labels}, datasets:[{{ label:'Balance', data:{js_bh_values}, borderColor:'#58a6ff', backgroundColor:'rgba(88,166,255,.1)', fill:true, tension:.3, pointRadius:1 }}] }}, options:{{ responsive:true, maintainAspectRatio:true, plugins:{{ legend:{{ display:false }} }}, scales:{{ x:{{ ticks:{{ color:'#484f58', font:{{ size:9 }}, maxTicksLimit:8 }}, grid:{{ color:'#21262d' }} }}, y:{{ ticks:{{ color:'#484f58', font:{{ size:9 }} }}, grid:{{ color:'#21262d' }} }} }} }} }});
  safeChart('sessChart', {{ type:'bar', data:{{ labels:{js_daily_labels}, datasets:[{{ label:'Sessions', data:{js_daily_sessions}, backgroundColor:'rgba(88,166,255,.6)', borderRadius:4 }}] }}, options:{{ responsive:true, maintainAspectRatio:true, plugins:{{ legend:{{ display:false }} }}, scales:{{ x:{{ ticks:{{ color:'#484f58', font:{{ size:9 }}, maxTicksLimit:7 }}, grid:{{ color:'#21262d' }} }}, y:{{ beginAtZero:true, ticks:{{ color:'#484f58', font:{{ size:9 }}, stepSize:1 }}, grid:{{ color:'#21262d' }} }} }} }} }});
  safeChart('tokChart', {{ type:'line', data:{{ labels:{js_daily_labels}, datasets:[{{ label:'Tokens (K)', data:{js_daily_tokens}, borderColor:'#bc8cff', tension:.3, fill:true, backgroundColor:'rgba(188,140,255,.1)' }}] }}, options:{{ responsive:true, maintainAspectRatio:true, plugins:{{ legend:{{ display:false }} }}, scales:{{ x:{{ ticks:{{ color:'#484f58', font:{{ size:9 }}, maxTicksLimit:7 }}, grid:{{ color:'#21262d' }} }}, y:{{ ticks:{{ color:'#484f58', font:{{ size:9 }} }}, grid:{{ color:'#21262d' }} }} }} }} }});
  safeChart('modelChart', {{ type:'doughnut', data:{{ labels:{js_model_labels}, datasets:[{{ data:{js_model_sessions}, backgroundColor:['#58a6ff','#bc8cff','#3fb950','#d29922','#f85149'], borderWidth:0 }}] }}, options:{{ responsive:true, maintainAspectRatio:true, plugins:{{ legend:{{ position:'right', labels:{{ color:'#8b949e', font:{{ size:10 }}, boxWidth:12, padding:6 }} }} }} }} }});
}})();
</script>
</body>
</html>'''
    return html.replace('$0.0000', '-')
