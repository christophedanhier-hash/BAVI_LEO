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
        "n": data.get("wf", {}) or {},
        "ba": data.get("bavi", {}) or {},
        "bo": data.get("bots", {}) or {},
        "va": data.get("vaults", {}) or {},
        "wi": count_wiki_journals(),
    }

def count_wiki_journals():
    """Compte les journaux dans les 5 wikis MkDocs."""
    from pathlib import Path
    wikis = {
        "bavi_journals": Path("/home/tofdan/Projets_Dev/BAVI_LEO/docs"),
        "hermes_journals": Path("/home/tofdan/Projets_Dev/hermes-wiki/docs"),
        "oca_journals": Path("/home/tofdan/Projets_Dev/wiki-oca/docs"),
        "emile_journals": Path("/home/tofdan/Projets_Dev/emile-wiki/docs"),
        "voyages_journals": Path("/home/tofdan/Projets_Dev/voyages-wiki/docs"),
    }
    result = {}
    for key, path in wikis.items():
        result[key] = len(list(path.glob("journal-*.md"))) if path.exists() else 0
    return result

def build_html():
    d = load_metrics()
    s = d["s"]; b = d["b"]; c = d["c"]; i = d["i"]; n = d["n"]
    ba = d["ba"]; bo = d["bo"]; va = d["va"]; wi = d["wi"]; alerts = d["alerts"]
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
    
    by_model_raw = s.get("by_model", {})
    # Fusionner par nom normalisé
    by_model = {}
    for m, v in by_model_raw.items():
        nm = norm_model(m)
        if nm not in by_model:
            by_model[nm] = {"sessions": 0, "tokens_in": 0, "tokens_out": 0, "cost": 0.0}
        by_model[nm]["sessions"] += v.get("sessions", 0)
        by_model[nm]["tokens_in"] += v.get("tokens_in", 0)
        by_model[nm]["tokens_out"] += v.get("tokens_out", 0)
        by_model[nm]["cost"] += v.get("cost", 0.0)
    
    js_model_labels = json.dumps(list(by_model.keys()))
    js_model_sessions = json.dumps([v["sessions"] for v in by_model.values()])
    
    recent = s.get("recent_sessions", [])[:8]
    
    html = f'''<!DOCTYPE html>
<html lang="fr" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LEO Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
<script src="/leo/monitoring.js?v=1784060105"></script>
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
  <div class="tab active" onclick="switchTab(this,'tab-syn')">📊 Synthèse</div>
  <div class="tab" onclick="switchTab(this,'tab-ana')">📈 Analyse</div>
  <div class="tab" onclick="switchTab(this,'tab-crons-mgmt');loadCrons()">🕐 Crons</div>
  <div class="tab" onclick="switchTab(this,'tab-wf');loadWorkflows()">🐍 Workflows</div>
  <div class="tab" onclick="switchTab(this,'tab-monitoring')">🖥️ Monitoring</div>
  <div class="tab" onclick="switchTab(this,'tab-notifications');refreshNotifs()">📋 Notifs</div>
  <div class="tab" onclick="switchTab(this,'tab-cameras')">📷 Caméras</div>
  <div class="tab" onclick="switchTab(this,'tab-energy');loadEnergyDaily()">⚡ Énergie</div>
  <div class="tab" onclick="switchTab(this,'tab-viessmann')">🔥 Viessmann</div>
  <div class="tab" onclick="switchTab(this,'tab-bavi')">🏛️ BAVI</div>
  <div class="tab" onclick="switchTab(this,'tab-audit');loadAudit()">📋 Audit</div>
  <div class="tab" onclick="switchTab(this,'tab-contacts');loadContacts()">📇 Contacts</div>
</div>

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
  <h3>📚 Wikis MkDocs</h3>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:6px">
    <div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;font-weight:600">🦁</div><div style="font-size:14px;font-weight:700">{wi.get("bavi_journals",0)}</div><div style="font-size:9px;color:var(--dim)">BAVI_LEO</div></div>
    <div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;font-weight:600">🤖</div><div style="font-size:14px;font-weight:700">{wi.get("hermes_journals",0)}</div><div style="font-size:9px;color:var(--dim)">Hermes</div></div>
    <div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;font-weight:600">📋</div><div style="font-size:14px;font-weight:700">{wi.get("oca_journals",0)}</div><div style="font-size:9px;color:var(--dim)">OCA</div></div>
    <div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;font-weight:600">🎓</div><div style="font-size:14px;font-weight:700">{wi.get("emile_journals",0)}</div><div style="font-size:9px;color:var(--dim)">Émile</div></div>
    <div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;font-weight:600">✈️</div><div style="font-size:14px;font-weight:700">{wi.get("voyages_journals",0)}</div><div style="font-size:9px;color:var(--dim)">Voyages</div></div>
  </div>
</div>

<div class="card">
  <h3>📓 Vaults Obsidian</h3>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:6px">
        {"".join(f'<div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:8px;text-align:center"><div style="font-size:12px;font-weight:600">{"🦁" if k=="michel" else "🏠" if k=="default" else "🎓" if k=="emile" else "🧭" if k=="sylvia" else "🏛️"}</div><div style="font-size:14px;font-weight:700">{vv.get("dailies",0)}</div><div style="font-size:9px;color:var(--dim)">{"Michel" if k=="michel" else "Léo" if k=="default" else "Émile" if k=="emile" else "Sylvia" if k=="sylvia" else "Robert" if k=="robert" else k}</div></div>' for k,vv in va.get("vaults",{}).items())}
  </div>
  <div class="sub" style="margin-top:6px;font-size:11px">{va.get("total_dailies",0)} journaux · {va.get("total_notes",0)} notes</div>
</div>
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
<script>
(function(){{
  var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
  var _historyChart = null;
  
  function drawGauge(canvasId, value, max, color) {{
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var w = canvas.width, h = canvas.height;
    var cx = w/2, cy = h/2, r = Math.min(w,h)/2 - 8;
    ctx.clearRect(0, 0, w, h);
    ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.strokeStyle='#21262d'; ctx.lineWidth=10; ctx.stroke();
    var angle = (Math.min(value,max)/max) * Math.PI*1.5 - Math.PI*0.75;
    ctx.beginPath(); ctx.arc(cx, cy, r, -Math.PI*0.75, angle); ctx.strokeStyle=color; ctx.lineWidth=10; ctx.lineCap='round'; ctx.stroke();
    ctx.fillStyle='#c9d1d9'; ctx.font='bold 18px -apple-system,sans-serif'; ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.fillText(Math.round(value)+'%', cx, cy);
  }}
  
  function loadMon() {{
    fetch('/api/machine-kpi?token='+token).then(function(r){{return r.json()}}).then(function(d){{
      var cpu = d.cpu || {{}}, ram = d.ram || {{}}, disk = (d.disk||'').split(' ');
      var cpuPct = Math.min((parseFloat(cpu.load1)||0)*100/(cpu.cores||8), 100);
      drawGauge('mon-cpu-gauge', cpuPct, 100, cpuPct>80?'#f85149':cpuPct>50?'#d29922':'#3fb950');
      var el = document.getElementById('mon-cpu-val'); if(el) el.textContent = String(cpu.load1||'?').substring(0,4);
      el = document.getElementById('mon-cpu-detail'); if(el) el.textContent = (cpu.load5||'?')+' / '+(cpu.load15||'?')+' · '+(cpu.cores||8)+' cores '+(cpu.temp||'')+'°C';
      
      var ramUsed = parseFloat((ram.used||'0').replace(',','.').replace(/[^0-9.]/g,''))||0;
      var ramTotal = parseFloat((ram.total||'1').replace(/[^0-9.]/g,''))||1;
      drawGauge('mon-ram-gauge', Math.min(ramUsed/ramTotal*100,100), 100, ramUsed/ramTotal>0.8?'#f85149':ramUsed/ramTotal>0.5?'#d29922':'#3fb950');
      el = document.getElementById('mon-ram-val'); if(el) el.textContent = ram.used||'?';
      el = document.getElementById('mon-ram-detail'); if(el) el.textContent = 'total '+(ram.total||'?')+' · avail '+(ram.avail||'?');
      
      var diskPct = parseFloat(disk[3]||0);
      drawGauge('mon-disk-gauge', diskPct, 100, diskPct>80?'#f85149':diskPct>50?'#d29922':'#3fb950');
      el = document.getElementById('mon-disk-val'); if(el) el.textContent = disk[1]||'?';
      el = document.getElementById('mon-disk-detail'); if(el) el.textContent = 'total '+(disk[0]||'?')+' · libre '+(disk[2]||'?');
      
      el = document.getElementById('mon-temp-val'); if(el) el.textContent = (cpu.temp||'--')+'°C';
      
      var svc = d.services || {{}};
      el = document.getElementById('mon-services');
      if(el) {{
        var h = '';
        Object.keys(svc).forEach(function(n){{ var s=svc[n]; h+='<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid var(--border);font-size:12px"><span>'+n+'</span><span style="color:'+(s==='UP'?'#3fb950':s==='DOWN'?'#f85149':'#d29922')+';font-weight:600">'+s+'</span></div>'; }});
        el.innerHTML = h || '<span style="color:var(--dim)">Aucun</span>';
      }}
      
      el = document.getElementById('mon-updated'); if(el) el.textContent = 'MàJ: '+new Date().toLocaleTimeString('fr-BE');
      
      var hist = d.history || [];
      if(hist.length) {{
        var labels = hist.slice(-30).map(function(p){{return p.ts}});
        var values = hist.slice(-30).map(function(p){{return p.cpu}});
        var ctx = document.getElementById('mon-history-chart');
        if(ctx) {{
          if(_historyChart) _historyChart.destroy();
          _historyChart = new Chart(ctx, {{
            type:'line', data:{{labels:labels,datasets:[{{data:values,borderColor:'#58a6ff',backgroundColor:'rgba(88,166,255,.1)',fill:true,tension:.3,pointRadius:0}}]}},
            options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:false}}}},scales:{{x:{{ticks:{{color:'#484f58',font:{{size:9}},maxTicksLimit:15}},grid:{{color:'#21262d'}}}},y:{{min:0,ticks:{{color:'#484f58',font:{{size:9}}}},grid:{{color:'#21262d'}}}}}}}}
          }});
        }}
      }}
    }}).catch(function(e){{ console.error('monitoring:',e); }});
  }}
  
  // Charger quand l'onglet devient visible
  var origSwitchTab = window.switchTab;
  window.switchTab = function(el, id) {{
    if(origSwitchTab) origSwitchTab(el, id);
    if(id === 'tab-monitoring') {{ loadMon(); setInterval(loadMon, 10000); }}
  }};
  
  // Charger aussi au premier affichage si déjà visible
  if(document.getElementById('tab-monitoring').classList.contains('active')) loadMon();
}})();
</script>

<!-- Gestion Crons -->
<div id="tab-crons-mgmt" class="panel">
<div class="card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
    <div>
      <span id="cr-ok" style="color:var(--green);font-weight:600">0</span> OK ·
      <span id="cr-err" style="color:var(--red);font-weight:600">0</span> Erreurs ·
      <span id="cr-total" style="color:var(--dim)">0</span> jobs
    </div>
    <button onclick="loadCrons()" style="background:var(--accent);border:none;color:#fff;padding:6px 14px;border-radius:6px;cursor:pointer;font-size:12px">🔄 Rafraîchir</button>
  </div>
  <table>
    <thead><tr><th></th><th>Nom</th><th>Horaire</th><th>Statut</th><th>Actions</th></tr></thead>
    <tbody id="crons-mgmt-body"><tr><td colspan="5" style="text-align:center;padding:20px">Chargement...</td></tr></tbody>
  </table>
  <div style="font-size:10px;color:var(--dim);text-align:right;margin-top:4px" id="cr-updated"></div>
</div>
<script>
(function(){{
  var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
  
  function loadCrons() {{
    var tbody = document.getElementById('crons-mgmt-body');
    if (!tbody) return;
    tbody.innerHTML = '<tr><td colspan="5" style="text-align:center;padding:20px">⏳</td></tr>';
    fetch('/api/crons?token='+token).then(function(r){{return r.json()}}).then(function(jobs){{
      var html = '', ok = 0, err = 0;
      jobs.forEach(function(j){{
        var status = j.last_status || 'pending';
        var badge = status === 'ok' ? 'ok' : status === 'error' ? 'err' : 'warn';
        if(status==='ok') ok++; else if(status==='error') err++;
        html += '<tr><td style="width:20px"><span onclick="toggleCron(\\''+j.id+'\\',this)" style="cursor:pointer;font-size:14px" title=\"Activer/Désactiver\">'+(j.enabled?'🟢':'🔴')+'</span></td>'+
          '<td style="max-width:200px;overflow:hidden;text-overflow:ellipsis;font-size:12px" title="'+(j.name||'')+'">'+(j.name||j.id||'?').substring(0,45)+'</td>'+
          '<td style="font-size:10px;color:var(--dim)">'+(j.schedule||'?')+'</td>'+
          '<td><span class="badge '+badge+'">'+status+'</span></td>'+
          '<td style="white-space:nowrap"><button onclick="runCronInline(\\''+j.id+'\\',this)" style="background:var(--accent);color:#fff;border:none;border-radius:4px;padding:2px 8px;cursor:pointer;font-size:10px">▶</button> <button onclick="showCronLog(\\''+j.id+'\\',\\''+(name.replace(/'/g,"\\'"))+'\\')" style="background:var(--card);border:1px solid var(--border);color:var(--dim);border-radius:4px;padding:2px 6px;cursor:pointer;font-size:10px">📋</button></td></tr>';
      }});
      tbody.innerHTML = html;
      document.getElementById('cr-ok').textContent = ok;
      document.getElementById('cr-err').textContent = err;
      document.getElementById('cr-total').textContent = jobs.length;
      document.getElementById('cr-updated').textContent = new Date().toLocaleTimeString('fr-BE');
    }});
  }}
  
  window.loadCrons = loadCrons;
  window.runCronInline = function(id, btn) {{
    btn.textContent = '...'; btn.disabled = true;
    fetch('/api/crons/'+id+'/run?token='+token, {{method:'POST'}}).then(function(r){{return r.json()}}).then(function(){{
      setTimeout(function(){{ loadCrons(); }}, 2000);
    }});
  }};
  
  window.toggleCron = function(id, el) {{
    el.textContent = '⏳';
    fetch('/api/crons/'+id+'/toggle?token='+token, {{method:'POST'}}).then(function(r){{return r.json()}}).then(function(d){{
      el.textContent = d.action === 'resume' ? '🟢' : '🔴';
      setTimeout(function(){{ loadCrons(); }}, 1000);
    }}).catch(function(){{ el.textContent = '❌'; }});
  }};

  window.showCronLog = function(id, name) {{
    var overlay = document.createElement('div');
    overlay.id = 'log-overlay';
    overlay.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.7);z-index:9999;display:flex;align-items:center;justify-content:center';
    overlay.onclick = function(e) {{ if(e.target===overlay) overlay.remove(); }};
    
    var box = document.createElement('div');
    box.style.cssText = 'background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:20px;max-width:750px;max-height:85vh;overflow-y:auto;width:92%;box-shadow:0 8px 32px rgba(0,0,0,.5)';
    box.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">'+
      '<h3 style="margin:0;border:none;padding:0;font-size:15px">📋 '+name+'</h3>'+
      '<span style="font-size:10px;color:var(--dim)">'+id.substring(0,8)+'</span></div>'+
      '<div id="log-content" style="font-size:11px;color:var(--dim)">Chargement...</div>'+
      '<button onclick="document.getElementById(\\'log-overlay\\').remove()" style="margin-top:12px;background:var(--accent);border:none;color:#fff;padding:6px 18px;border-radius:6px;cursor:pointer;font-size:12px">Fermer</button>';
    overlay.appendChild(box);
    document.body.appendChild(overlay);
    
    fetch('/api/crons/logs?token='+token).then(function(r){{return r.json()}}).then(function(data){{
      var jobData = data.jobs[id];
      var entries = (jobData && jobData.entries) ? jobData.entries : [];
      if (!entries.length) {{ document.getElementById('log-content').innerHTML = 'Aucun log'; return; }}
      var html = '<table style="width:100%;font-size:11px"><thead><tr><th style="text-align:left">Heure</th><th style="text-align:left">Statut</th><th style="text-align:left">Résumé</th></tr></thead><tbody>';
      entries.forEach(function(e){{
        var icon = e.status==='error' ? '🔴' : e.status==='warn' ? '🟡' : '🟢';
        var st = e.status==='error' ? 'ERREUR' : e.status==='warn' ? 'AVERT.' : 'OK';
        var stColor = e.status==='error' ? '#f85149' : e.status==='warn' ? '#d29922' : '#3fb950';
        html += '<tr style="border-bottom:1px solid var(--border)">'+
          '<td style="padding:6px 8px;white-space:nowrap;font-weight:600">'+icon+' '+e.ts.substring(11,16)+'</td>'+
          '<td style="padding:6px 8px"><span style="color:'+stColor+';font-weight:600;font-size:10px">'+st+'</span></td>'+
          '<td style="padding:6px 8px;max-width:400px;overflow:hidden;text-overflow:ellipsis">'+(e.summary||'—')+'</td></tr>';
      }});
      html += '</tbody></table>';
      document.getElementById('log-content').innerHTML = html;
    }});
  }};
}}());
</script>
</div>

<!-- BAVI -->
<div id="tab-bavi" class="panel">
<div class="bureaux-grid">
{"".join(f'<div class="bureau-card"><div class="name" style="color:{b.get("color","#58a6ff")}">{esc(b.get("name",""))}</div><div class="desc">{esc(b.get("role",""))}</div><div style="font-size:20px;font-weight:700;color:{b.get("color","#58a6ff")};opacity:.4;position:absolute;top:8px;right:12px">{b.get("analyses",0)}</div></div>' for b in ba.get("bureaux",[]))}
</div>

<h3 style="margin:16px 0 8px;font-size:14px;color:#8b949e">📊 Analytics BAVI</h3>
<div id="analytics-kpi" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:8px;margin-bottom:12px"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
  <div class="card chart-box" style="padding:12px"><h3 style="font-size:11px;color:#8b949e;margin:0 0 8px">📊 Analyses par bureau</h3><canvas id="baviBarChart" height="140"></canvas></div>
  <div class="card chart-box" style="padding:12px"><h3 style="font-size:11px;color:#8b949e;margin:0 0 8px">📈 Sessions / jour (30j)</h3><canvas id="baviSessChart" height="140"></canvas></div>
</div>

<h3 style="margin:16px 0 8px;font-size:14px;color:#8b949e">🔗 Graph des analyses</h3>
<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px" id="graph-filters"></div>
<div id="pack-container" style="background:var(--card);border:1px solid var(--border);border-radius:8px;height:400px;position:relative">
  <div id="pack-msg" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:#8b949e">Chargement...</div>
</div>
<div id="graph-tooltip" style="display:none;position:fixed;background:#1e293b;color:#e2e8f0;border:1px solid #475569;border-radius:6px;padding:6px 10px;font-size:11px;z-index:999;pointer-events:none;max-width:220px;box-shadow:0 4px 12px rgba(0,0,0,.5)"></div>
<div id="pack-info" style="text-align:center;font-size:11px;color:#8b949e;margin-top:4px"></div>
<div style="display:flex;justify-content:center;gap:16px;margin-top:4px;font-size:10px;color:#8b949e">
  <span>🟢 Actif</span><span>⚫ Archivé</span><span>◌ Bureau</span>
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
<tbody>{"".join(f'<tr><td>{m}</td><td>{v.get("sessions",0)}</td><td>{(v.get("tokens_in",0)+v.get("tokens_out",0))//1000}k</td><td>{"$"+str(round(v.get("cost",0),4)) if v.get("cost",0)>0 else "-"}</td></tr>' for m,v in sorted(by_model.items(), key=lambda x:-x[1].get("cost",0)))} <tr style="font-weight:700;border-top:2px solid var(--border)"><td>TOTAL</td><td>{s.get("total",0)}</td><td>{(s.get("total_tokens_in",0)+s.get("total_tokens_out",0))//1000}k</td><td>${s.get("total_estimated_cost",0):.2f}</td></tr></tbody></table>
</div>
</div>

<script src="assets/js/bavi-analytics.js?v=3"></script>

<!-- Audit Contenu -->

<!-- Contacts -->
<div id="tab-contacts" class="panel">
<h2 style="margin:0 0 16px">📇 Contacts</h2>
<div style="display:flex;gap:8px;margin-bottom:12px;align-items:center">
  <input id="contact-search" placeholder="🔍 Filtrer..." style="background:var(--card);border:1px solid var(--border);color:var(--text);padding:6px 12px;border-radius:6px;font-size:13px;width:200px" oninput="filterContacts()">
  <span style="font-size:11px;color:var(--dim)" id="contact-count"></span>
  <span style="flex:1"></span>
  <a href="https://docs.google.com/spreadsheets/d/1MD_gvazC1WbzVBvSwV2QvojKIv69yqlPZSsyIjBC3j4/edit" target="_blank" style="font-size:11px;color:var(--accent)">📊 Ouvrir Sheets</a>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:8px" id="contacts-grid">Chargement...</div>
</div>
<div id="tab-audit" class="panel" style="padding:16px">
  <div id="audit-redac" style="margin-bottom:16px"></div>
  <div id="audit-crons"></div>
</div>

<script>
var _auditLoaded = false;
function loadAudit() {{
  if(_auditLoaded) return;
  _auditLoaded = true;
  var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';

  // Audit rédactionnel
  fetch('/api/audit?token='+token).then(function(r){{return r.json()}}).then(function(d){{
    var issues = d.issues || [];
    var summary = d.summary || {{}};
    var icons = {{duplicate:'🔄', broken_link:'🔗', incoherence:'⚠️', missing_wiki:'❌'}};
    var labels = {{duplicate:'Doublons', broken_link:'Liens cassés', incoherence:'Incohérences', missing_wiki:'Wiki manquant'}};
    
    var s = '<h3 style=\"margin:0 0 8px;padding:0;border:none;font-size:14px\">📝 Audit Rédactionnel</h3>';
    s += '<div style=\"display:flex;gap:12px;margin-bottom:8px;font-size:12px;flex-wrap:wrap\">';
    s += '<span style=\"color:var(--text)\">'+d.total_files+' fichiers · '+d.model+'</span>';
    s += '<span style=\"color:var(--dim);font-size:10px\">'+d.timestamp+'</span>';
    s += '</div>';
    
    var byType = summary.by_type || {{}};
    if(Object.keys(byType).length) {{
      s += '<div style=\"display:flex;gap:10px;margin-bottom:8px;font-size:11px;flex-wrap:wrap\">';
      for(var t in byType) {{
        s += '<span style=\"color:'+(t==='broken_link'?'#f85149':t==='incoherence'?'#d29922':'#8b949e')+'\">'+icons[t]+' '+byType[t]+' '+(labels[t]||t)+'</span>';
      }}
      s += '</div>';
    }}
    
    issues = issues.filter(function(i){{ return i.type && i.msg; }});
    if(issues.length) {{
      issues.forEach(function(i){{
        var bg = i.type==='broken_link' ? 'rgba(248,81,73,.06)' : i.type==='incoherence' ? 'rgba(210,153,34,.06)' : 'var(--card)';
        var border = i.type==='broken_link' ? '#f85149' : i.type==='incoherence' ? '#d29922' : '#8b949e';
        s += '<div style=\"background:'+bg+';border-left:3px solid '+border+';border-radius:6px;padding:6px 10px;margin-bottom:4px;font-size:11px\">';
        s += '<div style=\"font-weight:600\">'+icons[i.type]+' '+(labels[i.type]||i.type)+': '+i.msg+'</div>';
        if(i.locations) s += '<div style=\"font-size:9px;color:var(--dim)\">'+i.locations.join(' | ')+'</div>';
        s += '</div>';
      }});
    }} else {{
      s += '<div style=\"color:var(--green);text-align:center;padding:12px;font-size:12px\">✅ Aucune anomalie</div>';
    }}
    s += '<hr style=\"border-color:var(--border);margin:12px 0\">';
    document.getElementById('audit-redac').innerHTML = s;
  }}).catch(function(){{
    document.getElementById('audit-redac').innerHTML = '<div style=\"color:#f85149\">❌ Audit rédactionnel non disponible</div>';
  }});

  // Audit qualité crons
  fetch('/api/audit/crons?token='+token).then(function(r){{return r.json()}}).then(function(d){{
    var issues = d.issues || [];
    var summary = d.summary || {{}};
    
    var s = '<h3 style=\"margin:0 0 8px;padding:0;border:none;font-size:14px\">🕐 Audit Qualité Crons</h3>';
    s += '<div style=\"display:flex;gap:12px;margin-bottom:8px;font-size:12px;flex-wrap:wrap\">';
    s += '<span style=\"color:var(--text)\">'+d.total_crons+' crons</span>';
    s += '<span style=\"color:var(--green)\">✅ '+summary.ok+'</span>';
    if(summary.errors) s += '<span style=\"color:#f85149\">❌ '+summary.errors+'</span>';
    if(summary.disabled) s += '<span style=\"color:#d29922\">⏸️ '+summary.disabled+'</span>';
    if(summary.pending) s += '<span style=\"color:#8b949e\">⏳ '+summary.pending+'</span>';
    s += '<span style=\"color:var(--dim);font-size:10px\">'+d.timestamp+'</span>';
    s += '</div>';
    
    if(issues.length) {{
      issues.forEach(function(i){{
        var color = i.severity==='error' ? '#f85149' : i.severity==='warning' ? '#d29922' : '#8b949e';
        s += '<div style=\"background:var(--card);border-left:3px solid '+color+';border-radius:6px;padding:6px 10px;margin-bottom:4px;font-size:11px\">';
        s += '<span style=\"font-weight:600;color:'+color+'\">'+i.severity.toUpperCase()+'</span> ';
        s += '<span>'+i.msg+'</span>';
        if(i.detail) s += '<div style=\"font-size:9px;color:var(--dim);margin-top:2px\">'+i.detail+'</div>';
        s += '</div>';
      }});
    }} else {{
      s += '<div style=\"color:var(--green);text-align:center;padding:12px;font-size:12px\">✅ Tous les crons sont sains</div>';
    }}
    document.getElementById('audit-crons').innerHTML = s;
  }}).catch(function(){{
    document.getElementById('audit-crons').innerHTML = '<div style=\"color:var(--dim)\">🕐 Audit crons pas encore disponible</div>';
  }});
}}
</script>

<!-- Notifications Crons -->
<div id="tab-notifications" class="panel" style="padding:16px">
  <div id="notif-list" style="max-height:600px;overflow-y:auto"></div>
  <div style="margin-top:8px;font-size:11px;color:var(--dim);text-align:right" id="notif-updated"></div>
  <script>
  (function(){{
    var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
    var _notifCounter = 0;
    
    function refreshNotifs() {{
      loadNotifications();
      _notifCounter++;
    }}
    
    function loadNotifications() {{
      fetch('/api/crons/logs?token='+token).then(function(r){{return r.json()}}).then(function(data){{
        var h = '';
        var errors = [], warns = [], oks = [];
        var jobIds = Object.keys(data.jobs || {{}}).sort();
        
        jobIds.forEach(function(jid) {{
          var job = data.jobs[jid];
          var entries = job.entries || [];
          var last = entries[0];
          if(!last) return;
          
          var icon = last.status==='error' ? '🔴' : last.status==='warn' ? '🟡' : '🟢';
          var border = last.status==='error' ? '#f85149' : last.status==='warn' ? '#d29922' : '#3fb950';
          var bg = last.status==='error' ? 'rgba(248,81,73,.08)' : last.status==='warn' ? 'rgba(210,153,34,.06)' : 'var(--card)';
          
          var name = job.name || last.title.replace('Cron Job: ','').substring(0,50);
          var time = last.ts.substring(11,16);
          var schedule = job.schedule || '';
          var script = job.script || '';
          var tag = job.no_agent ? '⚙️ script' : '🧠 agent';
          var errorMsg = last.error_msg || '';
          var summary = last.summary || '';
          
          // Grouper par statut
          var card = '<div style="background:'+bg+';border-radius:6px;padding:10px 12px;margin-bottom:6px;font-size:12px;border-left:3px solid '+border+'">';
          // Ligne 1 : icône + nom + heure
          card += '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">';
          card += '<span style="font-weight:600">'+icon+' '+name+'</span>';
          card += '<span style="color:var(--dim);font-size:10px">'+time+'</span>';
          card += '</div>';
          // Ligne 2 : métadonnées
          card += '<div style="font-size:10px;color:var(--dim);margin-bottom:4px;display:flex;gap:8px;flex-wrap:wrap">';
          card += '<span>'+tag+'</span>';
          if(schedule) card += '<span>🕐 '+schedule+'</span>';
          if(script) card += '<span>📄 '+script+'</span>';
          card += '</div>';
          // Erreur / avertissement
          if(errorMsg) {{
            var escapedError = errorMsg.replace(/</g,'&lt;').replace(/>/g,'&gt;');
            card += '<div style="font-size:11px;color:'+(last.status==='error'?'#f85149':'#d29922')+';margin-bottom:4px;padding:4px 6px;background:rgba(248,81,73,.1);border-radius:3px;word-break:break-all">'+escapedError+'</div>';
          }}
          // Résumé
          if(summary) {{
            card += '<div style="color:var(--dim);font-size:11px;max-height:40px;overflow:hidden;line-height:1.3">'+summary.substring(0,200)+'</div>';
          }}
          card += '</div>';
          
          if(last.status==='error') errors.push(card);
          else if(last.status==='warn') warns.push(card);
          else oks.push(card);
        }});
        
        // Assembler : erreurs d'abord, puis warns, puis OKs (max 10)
        h = errors.join('') + warns.join('') + oks.slice(0,15).join('');
        
        // Résumé
        var summary = '<div style="display:flex;gap:12px;margin-bottom:10px;font-size:12px">';
        if(errors.length) summary += '<span style="color:#f85149">🔴 '+errors.length+' erreur(s)</span>';
        if(warns.length) summary += '<span style="color:#d29922">🟡 '+warns.length+' avert.</span>';
        summary += '<span style="color:#3fb950">🟢 '+(oks.length)+' OK</span>';
        summary += '<span style="color:var(--dim);margin-left:auto">'+data.total+' jobs</span>';
        summary += '</div>';
        
        document.getElementById('notif-list').innerHTML = summary + h;
        document.getElementById('notif-updated').textContent = 'MàJ: '+new Date().toLocaleTimeString('fr-BE')+' · refresh #'+_notifCounter;
      }});
    }}
    
    window.loadNotifications = loadNotifications;
    window.refreshNotifs = refreshNotifs;
    setInterval(refreshNotifs, 30000);
    loadNotifications();
  }})();
  </script>
</div>

<!-- Caméras -->
<div id="tab-cameras" class="panel" style="padding:0;background:transparent;border:none">
  <iframe id="cameras-frame" src="" style="width:100%;height:600px;border:none;border-radius:8px"></iframe>
  <script>
  (function(){{
    var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
    document.getElementById('cameras-frame').src = '/cameras?embed=1&token=' + token;
  }})();
  </script>
</div>

<!-- Énergie -->
<div id="tab-energy" class="panel" style="padding:16px">
  <div class="kpi-grid" style="margin-bottom:12px">
    <div class="kpi-card"><div class="icon">⚡</div><div class="val" id="e-pwr" style="font-size:28px">—</div><div class="lbl" id="e-pwr-sub">Chargement...</div></div>
    <div class="kpi-card"><div class="icon">📊</div><div class="val" id="e-net" style="font-size:22px">—</div><div class="lbl">Net</div></div>
    <div class="kpi-card"><div class="icon">📥</div><div class="val" id="e-imp" style="font-size:22px;color:#58a6ff">—</div><div class="lbl">Import</div></div>
    <div class="kpi-card"><div class="icon">📤</div><div class="val" id="e-exp" style="font-size:22px;color:#3fb950">—</div><div class="lbl">Export</div></div>
    <div class="kpi-card"><div class="icon">🔺</div><div class="val" id="e-peak" style="font-size:22px;color:#d29922">—</div><div class="lbl">Pic mois</div></div>
    <div class="kpi-card"><div class="icon">⚡</div><div class="val" id="e-volt" style="font-size:22px;color:#bc8cff">—</div><div class="lbl">Voltage</div></div>
  </div>
  <div style="display:flex;gap:8px;margin-bottom:12px" id="e-phases"></div>
  <div id="e-tables" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin-bottom:12px"></div>
  <div class="card chart-box" style="height:260px">
    <canvas id="powerChart"></canvas>
  </div>
  <div style="display:flex;gap:8px;margin:12px 0">
    <span style="flex:1"></span>
    <button onclick="switchEnergyMode('conso')" id="btn-e-conso" style="background:var(--card);color:var(--text);border:1px solid var(--border);border-radius:6px;padding:6px 14px;cursor:pointer;font-size:12px">⚡ Conso</button>
    <button onclick="switchEnergyMode('prod')" id="btn-e-prod" style="background:var(--card);color:var(--text);border:1px solid var(--border);border-radius:6px;padding:6px 14px;cursor:pointer;font-size:12px">☀️ Prod</button>
  </div>
  <div class="card chart-box" style="height:260px">
    <canvas id="energyHistoryChart"></canvas>
  </div>
  <div class="card chart-box" style="height:260px;margin-top:12px">
    <canvas id="dsmrChart"></canvas>
  </div>
  <script>
  (function(){{
    var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
    var powerChart = null;
    
    function loadSnapshot() {{
      fetch('/api/energy?token='+token).then(function(r){{return r.json()}}).then(function(d){{
        if(d.error) return;
        var pwr = d.power_now_w;
        var color = pwr < 0 ? '#3fb950' : '#f85149';
        var el = document.getElementById('e-pwr');
        if(el) {{ el.textContent = Math.abs(pwr)+' W'; el.style.color = color; }}
        var sub = document.getElementById('e-pwr-sub');
        if(sub) sub.textContent = pwr < 0 ? '☀️ Injection' : '⚡ Conso';
        var net = document.getElementById('e-net');
        if(net) {{ net.textContent = (d.net_kwh>0?'+':'')+d.net_kwh.toFixed(0)+' kWh'; net.style.color = d.net_kwh>0?'#3fb950':'#f85149'; }}
        var imp = document.getElementById('e-imp');
        if(imp) imp.textContent = d.import_total_kwh.toFixed(0)+' kWh';
        var exp = document.getElementById('e-exp');
        if(exp) exp.textContent = d.export_total_kwh.toFixed(0)+' kWh';
        var peak = document.getElementById('e-peak');
        if(peak) peak.textContent = d.peak_month_w+' W';
        var volt = document.getElementById('e-volt');
        if(volt) volt.textContent = d.voltage_v.toFixed(1)+' V';
        var ph = d.phases;
        var phasesEl = document.getElementById('e-phases');
        if(phasesEl && ph) {{
          phasesEl.innerHTML = ['l1','l2','l3'].map(function(p){{
            var phase = ph[p];
            return '<div class="kpi-card" style="flex:1"><div class="val" style="font-size:20px;color:'+(phase.w<0?'#3fb950':'#f85149')+'">'+phase.w+' W</div><div class="lbl" style="font-size:10px">'+phase.v.toFixed(1)+'V · '+phase.a.toFixed(1)+'A</div><div style="font-size:10px;color:var(--dim);margin-top:2px">'+p.toUpperCase()+'</div></div>';
          }}).join('');
        }}
      }});
    }}
    
    function loadHistory() {{
      fetch('/api/energy/history?token='+token).then(function(r){{return r.json()}}).then(function(history){{
        if(!history || !history.length) return;
        var labels = history.map(function(p){{return p.ts.substring(11,16)}});
        var values = history.map(function(p){{return Math.abs(p.w)}});
        var colors = history.map(function(p){{return p.w < 0 ? 'rgba(63,185,80,.4)' : 'rgba(248,81,73,.4)'}});
        var borders = history.map(function(p){{return p.w < 0 ? '#3fb950' : '#f85149'}});
        if(powerChart) powerChart.destroy();
        var ctx = document.getElementById('powerChart');
        if(!ctx) return;
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
    loadEnergyDaily();
    loadTelegram();
    
    var _energyHistChart = null;
    var _energyMode = 'conso';  // 'conso' ou 'prod'
    var _energyView = 'daily';  // 'daily' ou 'monthly'
    
    function loadTelegram() {{
      fetch('/api/energy/telegram?token='+token).then(function(r){{return r.json()}}).then(function(d){{
        if(d.error) return;
        var h = '';
        
        // Tableau Infos compteur
        h += '<div class=\"card\" style=\"padding:10px;font-size:12px\"><h4 style=\"margin:0 0 6px;font-size:12px;border:none;padding:0\">📡 Infos compteur</h4><table style=\"width:100%\">';
        h += '<tr><td style=\"color:var(--dim)\">Modèle</td><td style=\"font-weight:600\">'+d.meter+'</td></tr>';
        h += '<tr><td style=\"color:var(--dim)\">WiFi</td><td>'+d.wifi+'%</td></tr>';
        h += '<tr><td style=\"color:var(--dim)\">Tarif actif</td><td>'+(d.tariff==2?'🌙 Heures creuses':'☀️ Heures pleines')+'</td></tr>';
        h += '</table></div>';
        
        // Tableau Puissance instantanée
        h += '<div class=\"card\" style=\"padding:10px;font-size:12px\"><h4 style=\"margin:0 0 6px;font-size:12px;border:none;padding:0\">⚡ Puissance instantanée</h4><table style=\"width:100%\">';
        h += '<tr><td style=\"color:var(--dim)\">Totale</td><td style=\"font-weight:600;color:'+(d.power_total_w<0?'#3fb950':'#f85149')+'\">'+d.power_total_w+' W</td></tr>';
        var pp = d.phase_power || {{}};
        ['l1','l2','l3'].forEach(function(p){{ h += '<tr><td style=\"color:var(--dim)\">'+p.toUpperCase()+'</td><td>'+(pp[p]*1000).toFixed(0)+' W</td></tr>'; }});
        h += '<tr><td style=\"color:var(--dim)\">Moyenne</td><td>'+d.power_average_w+' W</td></tr>';
        h += '<tr><td style=\"color:var(--dim)\">Pic mois</td><td style=\"color:#d29922;font-weight:600\">'+d.peak_month_w+' W</td></tr>';
        h += '</table></div>';
        
        // Tableau Tension & Courant
        var pv = d.phase_voltage || {{}}, pc = d.phase_current || {{}};
        h += '<div class=\"card\" style=\"padding:10px;font-size:12px\"><h4 style=\"margin:0 0 6px;font-size:12px;border:none;padding:0\">🔌 Tension & Courant</h4><table style=\"width:100%\">';
        ['l1','l2','l3'].forEach(function(p){{ h += '<tr><td style=\"color:var(--dim)\">'+p.toUpperCase()+'</td><td>'+(pv[p]||0).toFixed(1)+' V · '+(pc[p]||0).toFixed(1)+' A</td></tr>'; }});
        h += '</table></div>';
        
        // Tableau Totaux compteur
        h += '<div class=\"card\" style=\"padding:10px;font-size:12px\"><h4 style=\"margin:0 0 6px;font-size:12px;border:none;padding:0\">📥📤 Totaux compteur</h4><table style=\"width:100%\">';
        h += '<tr><td style=\"color:var(--dim)\">Import total</td><td style=\"color:#58a6ff;font-weight:600\">'+d.import_total.toFixed(0)+' kWh</td></tr>';
        h += '<tr><td style=\"color:var(--dim)\">Import T1</td><td>'+d.import_t1.toFixed(0)+' kWh</td></tr>';
        h += '<tr><td style=\"color:var(--dim)\">Import T2</td><td>'+d.import_t2.toFixed(0)+' kWh</td></tr>';
        h += '<tr><td style=\"color:var(--dim)\">Export total</td><td style=\"color:#3fb950;font-weight:600\">'+d.export_total.toFixed(0)+' kWh</td></tr>';
        h += '<tr><td style=\"color:var(--dim)\">Export T1</td><td>'+d.export_t1.toFixed(0)+' kWh</td></tr>';
        h += '<tr><td style=\"color:var(--dim)\">Export T2</td><td>'+d.export_t2.toFixed(0)+' kWh</td></tr>';
        h += '</table></div>';
        
        document.getElementById('e-tables').innerHTML = h;
        
        // Graphique DSMR historique pics
        var hist = d.dsmr_history || [];
        if(hist.length > 1) {{
          var labels = hist.map(function(p){{return p.period_end.substring(0,7)}});
          var values = hist.map(function(p){{return p.peak_kw}});
          var ctx = document.getElementById('dsmrChart');
          if(ctx) {{
            if(window._dsmrChart) window._dsmrChart.destroy();
            window._dsmrChart = new Chart(ctx, {{
              type:'bar', data:{{labels:labels,datasets:[{{data:values,backgroundColor:'rgba(210,153,34,.3)',borderColor:'#d29922',borderWidth:1,borderRadius:4}}]}},
              options:{{responsive:true,maintainAspectRatio:false,
                plugins:{{legend:{{display:false}},title:{{display:true,text:'📊 Pic mensuel — 13 mois (DSMR)',color:'#8b949e',font:{{size:12}}}}}},
                scales:{{x:{{ticks:{{color:'#484f58',font:{{size:9}}}},grid:{{color:'#21262d'}}}},y:{{ticks:{{color:'#484f58',font:{{size:9}},callback:function(v){{return v+' kW'}}}},grid:{{color:'#21262d'}}}}}}
              }}
            }});
          }}
        }}
      }});
    }}
    
    function switchEnergyView(view) {{
      _energyView = view;
      ['daily','weekly','monthly','yearly'].forEach(function(v){{
        var btn = document.getElementById('btn-e-'+v);
        if(btn) btn.style.background = view===v ? 'var(--accent)' : 'var(--card)';
      }});
      if(view === 'daily') loadEnergyDaily();
      else if(view === 'weekly') loadEnergyWeekly();
      else if(view === 'monthly') loadEnergyMonthly();
      else loadEnergyYearly();
    }}
    
    function switchEnergyMode(mode) {{
      _energyMode = mode;
      document.getElementById('btn-e-conso').style.background = mode==='conso' ? 'var(--accent)' : 'var(--card)';
      document.getElementById('btn-e-prod').style.background = mode==='prod' ? 'var(--accent)' : 'var(--card)';
      if(_energyView === 'daily') loadEnergyDaily();
      else if(_energyView === 'weekly') loadEnergyWeekly();
      else if(_energyView === 'monthly') loadEnergyMonthly();
      else loadEnergyYearly();
    }}
    
    function loadEnergyDaily() {{
      fetch('/api/energy/daily?token='+token).then(function(r){{return r.json()}}).then(function(data){{
        if(!data || !data.length) return;
        var last7 = data.slice(-7);
        var labels = last7.map(function(d){{return d.date.substring(5)}});
        var field = _energyMode === 'prod' ? 'prod_kwh' : 'conso_kwh';
        var values = last7.map(function(d){{return d[field] || 0}});
        var title = _energyMode === 'prod' ? '☀️ Production solaire — 7 jours' : '⚡ Consommation — 7 jours';
        var color = _energyMode === 'prod' ? '#d29922' : '#f85149';
        var bg = _energyMode === 'prod' ? 'rgba(210,153,34,.3)' : 'rgba(248,81,73,.3)';
        renderEnergyHist(labels, values, title, color, bg);
      }});
    }}
    
    function loadEnergyMonthly() {{
      fetch('/api/energy/monthly?token='+token).then(function(r){{return r.json()}}).then(function(data){{
        if(!data || !data.length) return;
        var last12 = data.slice(-12);
        var labels = last12.map(function(d){{return d.month}});
        var field = _energyMode === 'prod' ? 'prod_kwh' : 'conso_kwh';
        var values = last12.map(function(d){{return d[field] || 0}});
        var title = _energyMode === 'prod' ? '☀️ Production solaire — 12 mois' : '⚡ Consommation — 12 mois';
        var color = _energyMode === 'prod' ? '#d29922' : '#f85149';
        var bg = _energyMode === 'prod' ? 'rgba(210,153,34,.3)' : 'rgba(248,81,73,.3)';
        renderEnergyHist(labels, values, title, color, bg);
      }});
    }}
    
    function loadEnergyWeekly() {{
      fetch('/api/energy/weekly?token='+token).then(function(r){{return r.json()}}).then(function(data){{
        if(!data || !data.length) return;
        var last54 = data.slice(-54);
        var labels = last54.map(function(d){{return d.week.substring(5)}});
        var field = _energyMode === 'prod' ? 'prod_kwh' : 'conso_kwh';
        var values = last54.map(function(d){{return d[field] || 0}});
        var title = _energyMode === 'prod' ? '☀️ Production solaire — 54 semaines' : '⚡ Consommation — 54 semaines';
        var color = _energyMode === 'prod' ? '#d29922' : '#f85149';
        var bg = _energyMode === 'prod' ? 'rgba(210,153,34,.3)' : 'rgba(248,81,73,.3)';
        renderEnergyHist(labels, values, title, color, bg);
      }});
    }}
    
    function loadEnergyYearly() {{
      fetch('/api/energy/yearly?token='+token).then(function(r){{return r.json()}}).then(function(data){{
        if(!data || !data.length) return;
        var labels = data.map(function(d){{return d.year}});
        var field = _energyMode === 'prod' ? 'prod_kwh' : 'conso_kwh';
        var values = data.map(function(d){{return d[field] || 0}});
        var title = _energyMode === 'prod' ? '☀️ Production solaire — Années' : '⚡ Consommation — Années';
        var color = _energyMode === 'prod' ? '#d29922' : '#f85149';
        var bg = _energyMode === 'prod' ? 'rgba(210,153,34,.3)' : 'rgba(248,81,73,.3)';
        renderEnergyHist(labels, values, title, color, bg);
      }});
    }}
    
    function renderEnergyHist(labels, values, title, color, bgColor) {{
      var ctx = document.getElementById('energyHistoryChart');
      if(!ctx) return;
      if(_energyHistChart) _energyHistChart.destroy();
      _energyHistChart = new Chart(ctx, {{
        type:'bar', data:{{labels:labels,datasets:[{{data:values,backgroundColor:bgColor,borderColor:color,borderWidth:1,borderRadius:4}}]}},
        options:{{responsive:true,maintainAspectRatio:false,
          plugins:{{legend:{{display:false}},title:{{display:true,text:title,color:'#8b949e',font:{{size:12}}}}}},
          scales:{{x:{{ticks:{{color:'#484f58',font:{{size:10}}}},grid:{{color:'#21262d'}}}},y:{{ticks:{{color:'#484f58',font:{{size:10}},callback:function(v){{return v+' kWh'}}}},grid:{{color:'#21262d'}}}}}}
        }}
      }});
    }}
    
    window.switchEnergyView = switchEnergyView;
    window.switchEnergyMode = switchEnergyMode;
  }})();
  </script>
</div>

<!-- Viessmann -->
<div id="tab-viessmann" class="panel" style="padding:16px">
  <div class="kpi-grid" id="v-kpi">
    <div class="kpi-card"><div class="icon">🔥</div><div class="val">—</div><div class="lbl">Chaudière</div></div>
    <div class="kpi-card"><div class="icon">🌡️</div><div class="val">—</div><div class="lbl">Extérieure</div></div>
    <div class="kpi-card"><div class="icon">🚿</div><div class="val">—</div><div class="lbl">Eau chaude</div></div>
    <div class="kpi-card"><div class="icon">🔧</div><div class="val">—</div><div class="lbl">Brûleur</div></div>
    <div class="kpi-card"><div class="icon">📐</div><div class="val">—</div><div class="lbl">Circuit 0</div></div>
    <div class="kpi-card"><div class="icon">☀️</div><div class="val">—</div><div class="lbl">Solaire</div></div>
  </div>
  <div class="card" style="font-size:12px;color:var(--dim)" id="v-info">Chargement...</div>
  <script>
  (function(){{
    var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
    fetch('/api/viessmann?token='+token).then(function(r){{return r.json()}}).then(function(d){{
      if(d.error) return;
      var cards = document.querySelectorAll('#v-kpi .kpi-card .val');
      var data = [d.boiler_temp+'°C', d.outside_temp+'°C', d.dhw_temp+'°C', (d.burner_modulation||'?')+'%', (d.circuit0_supply||'?')+'°C', (d.solar_production||'0')+'W'];
      cards.forEach(function(c,i){{ if(data[i]) c.textContent = data[i]; }});
      document.getElementById('v-info').innerHTML = 'Mode: <strong>'+(d.circuit0_mode||'?')+'</strong> · Programme: <strong>'+(d.circuit0_program||'?')+'</strong> · Consigne ECS: <strong>'+(d.dhw_target||'?')+'°C</strong> · Solaire total: <strong>'+(d.solar_cumulative||'?')+' kWh</strong> · MàJ: '+(d.timestamp||'?').substring(0,19);
    }});
  }})();
  </script>
</div>

<!-- Workflows -->
<div id="tab-wf" class="panel" style="padding:12px">
  <div id="wf-content" style="display:flex;flex-direction:column;gap:8px">
    <span style="color:var(--dim)">Chargement...</span>
  </div>
  <div style="font-size:10px;color:var(--dim);text-align:right;margin-top:4px" id="wf-updated"></div>
  <script>
  (function(){{
    var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
    
    function loadWorkflows() {{
      var panel = document.getElementById('wf-content');
      if (!panel) return;
      panel.innerHTML = '<span style="color:var(--dim)">⏳</span>';
      fetch('/api/wf?token='+token).then(function(r){{return r.json()}}).then(function(data){{
        if(data.error){{ panel.innerHTML='<span style="color:var(--red)">❌ '+data.error+'</span>'; return; }}
        var keys = Object.keys(data);
        if(!keys.length){{ panel.innerHTML='<span style="color:var(--dim)">Aucun workflow</span>'; return; }}
        var html = '<table style="width:100%;font-size:12px"><thead><tr><th>Workflow</th><th>Dernier</th><th>Statut</th><th></th></tr></thead><tbody>';
        keys.forEach(function(key){{
          var wf = data[key];
          var name = (wf.workflow||key).substring(0,55);
          var ts = (wf.timestamp||'?').substring(0,19);
          var status = wf.status==='ok' ? 'ok' : (wf.error ? 'error' : 'ok');
          var badge = status==='ok'?'ok':status==='error'?'err':'warn';
          html += '<tr><td style="max-width:200px;overflow:hidden;text-overflow:ellipsis;font-size:11px">'+name+'</td><td style="font-size:10px;color:var(--dim)">'+ts.replace('T',' ')+'</td><td><span class="badge '+badge+'">'+status+'</span></td><td style="white-space:nowrap"><button onclick="runWf(\\''+key+'\\',this)" style="background:var(--accent);color:#fff;border:none;border-radius:4px;padding:2px 8px;cursor:pointer;font-size:10px">▶</button> <button onclick="showWfLog(\\''+key+'\\',\\''+name.replace(/'/g,"\\'")+'\\')" style="background:var(--card);border:1px solid var(--border);color:var(--dim);border-radius:4px;padding:2px 6px;cursor:pointer;font-size:10px">📋</button></td></tr>';
        }});
        html += '</tbody></table>';
        panel.innerHTML = html;
        document.getElementById('wf-updated').textContent = new Date().toLocaleTimeString('fr-BE');
      }}).catch(function(e){{ panel.innerHTML='<span style="color:var(--red)">❌ '+e+'</span>'; }});
    }}
    
    window.loadWorkflows = loadWorkflows;
    
    window.runWf = function(name, btn) {{
      btn.textContent = '...'; btn.disabled = true;
      fetch('/api/wf/'+name+'/run?token='+token, {{method:'POST'}}).then(function(r){{return r.json()}}).then(function(d){{
        btn.textContent = d.ok ? '✅' : '❌';
        setTimeout(function(){{ btn.textContent = '▶'; btn.disabled = false; loadWorkflows(); }}, 3000);
      }}).catch(function(){{ btn.textContent = '❌'; }});
    }};
    
    window.showWfLog = function(key, name) {{
      var overlay = document.createElement('div');
      overlay.id = 'log-overlay';
      overlay.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.7);z-index:9999;display:flex;align-items:center;justify-content:center';
      overlay.onclick = function(e) {{ if(e.target===overlay) overlay.remove(); }};
      var box = document.createElement('div');
      box.style.cssText = 'background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:20px;max-width:650px;max-height:80vh;overflow-y:auto;width:90%;box-shadow:0 8px 32px rgba(0,0,0,.5)';
      box.innerHTML = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px"><h3 style="margin:0;border:none;padding:0;font-size:15px">📋 '+name+'</h3><span style="font-size:10px;color:var(--dim)">'+key+'</span></div><div id="log-content" style="font-size:11px;color:var(--dim)">Chargement...</div><button onclick="document.getElementById(\\'log-overlay\\').remove()" style="margin-top:12px;background:var(--accent);border:none;color:#fff;padding:6px 18px;border-radius:6px;cursor:pointer;font-size:12px">Fermer</button>';
      overlay.appendChild(box);
      document.body.appendChild(overlay);
      
      fetch('/api/wf?token='+token).then(function(r){{return r.json()}}).then(function(data){{
        var wf = data[key];
        if(!wf) {{ document.getElementById('log-content').innerHTML = 'Aucune donnée'; return; }}
        var html = '<table style="width:100%;font-size:11px">';
        Object.keys(wf).forEach(function(k){{
          var v = typeof wf[k]==='object' ? JSON.stringify(wf[k]).substring(0,200) : String(wf[k]);
          html += '<tr style="border-bottom:1px solid var(--border)"><td style="padding:4px 8px;color:var(--dim);font-weight:600;width:140px">'+k+'</td><td style="padding:4px 8px;max-width:400px;overflow:hidden;text-overflow:ellipsis">'+v+'</td></tr>';
        }});
        html += '</table>';
        document.getElementById('log-content').innerHTML = html;
      }});
    }};
  }}());
  </script>
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
