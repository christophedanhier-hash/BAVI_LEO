# 🏠 Bureaux BAVI

<div id="kpi-row" style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px"></div>

<div id="bureaux-stats" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:16px 0">
  <em>Chargement...</em>
</div>

<script>
const colors = {michel:'#a78bfa', sylvia:'#06b6d4', leo:'#818cf8', gerard:'#f97316', virginie:'#ec4899', emile:'#f59e0b', robert:'#3b82f6', sophie:'#22c55e'};

function kpiCard(icon,val,label,color){
  return `<div style="background:var(--md-code-bg);border:1px solid var(--md-default-fg-color--lightest);border-radius:8px;padding:8px 14px;text-align:center;flex:1;min-width:80px">
    <div style="font-size:1.1rem;font-weight:700;color:${color||'var(--md-default-fg-color)'}">${icon} ${val}</div>
    <div style="font-size:.6rem;color:var(--md-default-fg-color--light);text-transform:uppercase">${label}</div>
  </div>`;
}

async function refreshBureaux() {
  try {
    const r = await fetch('/api/metrics');
    const m = await r.json();
    const bu = m.bavi.bureaux || [];
    const b = m.budget, c = m.crons, h = m.infra_health||{}, s = m.sessions;

    // KPI row
    document.getElementById('kpi-row').innerHTML =
      kpiCard('💰',`${b.balance} ${b.currency}`,'Budget','#22c55e')+
      kpiCard('⏱️',`${c.ok}/${c.total}`,'Crons OK',c.error>0?'#ef4444':'#22c55e')+
      kpiCard('🖥️',h.cpu||'?','CPU','')+
      kpiCard('💾',h.ram||'?','RAM','')+
      kpiCard('💿',h.disk||'?','Disque','')+
      kpiCard('💬',s.messages_today,'Msg aujourd\'hui','')+
      kpiCard('📊',s.total_tools,'Tool calls','');

    // Bureau cards
    const container = document.getElementById('bureaux-stats');
    container.innerHTML = bu.map(d => {
      const count = d.analyses || 0;
      const color = colors[d.id] || '#94a3b8';
      const status = count > 5 ? '✅ Actif' : count > 0 ? '🟡 En cours' : '⏳ En attente';
      return `<a href="/wiki/agent-pro/bureau-${d.id}/" style="text-decoration:none;color:inherit">
        <div style="background:var(--md-code-bg);border-left:4px solid ${color};border-radius:8px;padding:16px;transition:transform .15s,box-shadow .15s" onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 4px 12px rgba(0,0,0,.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
          <div style="font-size:1.5rem;margin-bottom:4px">${d.name}</div>
          <div style="font-size:0.8rem;color:var(--md-default-fg-color--light);margin-bottom:8px">${d.role}</div>
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span style="font-size:2rem;font-weight:700;color:${color}">${count}</span>
            <span style="font-size:0.75rem;color:var(--md-default-fg-color--lighter)">analyses</span>
          </div>
          <div style="font-size:0.7rem;margin-top:6px;color:var(--md-default-fg-color--light)">${status}</div>
        </div>
      </a>`;
    }).join('');
  } catch(e) {
    document.getElementById('bureaux-stats').innerHTML = '<em>Stats non disponibles</em>';
  }
}

refreshBureaux();
setInterval(refreshBureaux, 30000);
</script>
