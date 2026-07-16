// Widget KPI — sidebar BAVI local
(function(){
  const KPI_URL = '/api/metrics';
  
  function createWidget() {
    const nav = document.querySelector('.md-sidebar--primary .md-nav');
    if (!nav) return setTimeout(createWidget, 200);

    const widget = document.createElement('div');
    widget.id = 'kpi-widget';
    widget.style.cssText = 'margin-top:16px;padding:12px;background:var(--md-code-bg);border-radius:8px;font-size:0.75rem;border:1px solid var(--md-default-fg-color--lightest)';
    widget.innerHTML = '<div style="text-align:center;color:var(--md-default-fg-color--light)">Chargement KPI...</div>';
    nav.appendChild(widget);
    refreshKPI();
    setInterval(refreshKPI, 30000);
  }

  async function refreshKPI() {
    try {
      const r = await fetch(KPI_URL);
      const m = await r.json();
      const b = m.budget, c = m.crons, i = m.infra, h = m.infra_health||{};
      const widget = document.getElementById('kpi-widget');
      if (!widget) return;
      widget.innerHTML = `
        <div style="font-weight:700;margin-bottom:8px;color:var(--md-default-fg-color)">📊 KPI Live</div>
        <div style="display:flex;justify-content:space-between;margin-bottom:4px"><span>💰 Budget</span><span style="color:#22c55e">${b.balance} ${b.currency}</span></div>
        <div style="display:flex;justify-content:space-between;margin-bottom:4px"><span>⏱️ Crons</span><span style="color:${c.error>0?'#ef4444':'#22c55e'}">${c.ok}/${c.total}</span></div>
        <div style="display:flex;justify-content:space-between;margin-bottom:4px"><span>🌐 Gateway</span><span style="color:#22c55e">${i.gateway}</span></div>
        <div style="display:flex;justify-content:space-between;margin-bottom:4px"><span>🖥️ CPU</span><span>${h.cpu||'?'}</span></div>
        <div style="display:flex;justify-content:space-between;margin-bottom:4px"><span>💾 RAM</span><span>${h.ram||'?'}</span></div>
        <div style="display:flex;justify-content:space-between"><span>💿 Disque</span><span>${h.disk||'?'}</span></div>
      `;
    } catch(e) {}
  }

  createWidget();
})();
