# 📈 Analytics BAVI

<div id="analytics-kpi" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px;margin-bottom:16px"></div>

<div class="chart-box"><h3>📊 Analyses par bureau</h3><canvas id="bureauBarChart" height="150"></canvas></div>
<div class="chart-box"><h3>📈 Sessions / jour (30j)</h3><canvas id="sessionsLineChart" height="150"></canvas></div>

<style>
.chart-box{background:var(--md-code-bg);border:1px solid var(--md-default-fg-color--lightest);border-radius:8px;padding:14px;margin-bottom:12px}
.chart-box h3{font-size:.8rem;color:var(--md-default-fg-color--light);margin-bottom:8px}
</style>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
<script>
(async function(){
  try {
    const r = await fetch('/api/metrics');
    const m = await r.json();
    const bu = m.bavi.bureaux || [];
    const colors = {michel:'#a78bfa',sylvia:'#06b6d4',leo:'#818cf8',gerard:'#f97316',virginie:'#ec4899',emile:'#f59e0b',robert:'#3b82f6',sophie:'#22c55e'};
    
    // KPI
    const total = bu.reduce((s,d)=>s+(d.analyses||0),0);
    document.getElementById('analytics-kpi').innerHTML = `
      <div class="kpi-card"><div class="v">${total}</div><div class="l">Total analyses</div></div>
      <div class="kpi-card"><div class="v">${bu.length}</div><div class="l">Bureaux</div></div>
      <div class="kpi-card"><div class="v">${bu.filter(d=>(d.analyses||0)>0).length}</div><div class="l">Bureaux actifs</div></div>
      <div class="kpi-card"><div class="v">${bu.filter(d=>(d.analyses||0)>5).length}</div><div class="l">Très actifs</div></div>
    `;
    
    // Bar chart
    new Chart(document.getElementById('bureauBarChart'),{type:'bar',data:{labels:bu.map(d=>d.name),datasets:[{data:bu.map(d=>d.analyses||0),backgroundColor:bu.map(d=>colors[d.id]||'#94a3b8'),borderRadius:4}]},options:{responsive:true,plugins:{legend:{display:false}},scales:{y:{beginAtZero:true,ticks:{stepSize:1}}}}});

    // Sessions line
    const sd = m.sessions_daily||[];
    if(sd.length){
      new Chart(document.getElementById('sessionsLineChart'),{type:'line',data:{labels:sd.map(d=>d.date.slice(5)),datasets:[{label:'Sessions',data:sd.map(d=>d.sessions),borderColor:'#a78bfa',tension:.3,fill:true,backgroundColor:'rgba(167,139,250,.1)',pointRadius:1}]},options:{responsive:true,plugins:{legend:{display:false}}}});
    }
  } catch(e) {}
})();
</script>
<style>
.kpi-card{background:var(--md-code-bg);border:1px solid var(--md-default-fg-color--lightest);border-radius:8px;padding:14px;text-align:center}
.kpi-card .v{font-size:1.6rem;font-weight:700;color:var(--md-default-fg-color)}
.kpi-card .l{font-size:.65rem;color:var(--md-default-fg-color--light);margin-top:2px;text-transform:uppercase}
</style>
