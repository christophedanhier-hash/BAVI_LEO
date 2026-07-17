// ── BAVI Analytics + Graph ──
(function(){
  var token = new URLSearchParams(window.location.search).get('token') || 'leo-panel-2026';
  
  // Analytics
  function loadBaviAnalytics() {
    fetch('/api/metrics?token='+token).then(function(r){return r.json()}).then(function(m){
      var bu = (m.bavi && m.bavi.bureaux) || [];
      var colors = {michel:'#a78bfa',sylvia:'#06b6d4',leo:'#818cf8',gerard:'#f97316',virginie:'#ec4899',emile:'#f59e0b',robert:'#3b82f6',sophie:'#22c55e',connaissance:'#14b8a6'};
      
      var total = bu.reduce(function(s,d){return s+(d.analyses||0)},0);
      var el = document.getElementById('analytics-kpi');
      if(el) el.innerHTML = 
        '<div class="card" style="padding:10px;text-align:center"><div style="font-size:24px;font-weight:700;color:#58a6ff">'+total+'</div><div style="font-size:10px;color:#8b949e">Analyses</div></div>'+
        '<div class="card" style="padding:10px;text-align:center"><div style="font-size:24px;font-weight:700;color:#3fb950">'+bu.length+'</div><div style="font-size:10px;color:#8b949e">Bureaux</div></div>'+
        '<div class="card" style="padding:10px;text-align:center"><div style="font-size:24px;font-weight:700;color:#d29922">'+bu.filter(function(d){return (d.analyses||0)>0}).length+'</div><div style="font-size:10px;color:#8b949e">Actifs</div></div>';
      
      var ctx1 = document.getElementById('baviBarChart');
      if(ctx1 && typeof Chart !== 'undefined') {
        if(ctx1._chart) ctx1._chart.destroy();
        ctx1._chart = new Chart(ctx1,{type:'bar',data:{labels:bu.map(function(d){return d.name}),datasets:[{data:bu.map(function(d){return d.analyses||0}),backgroundColor:bu.map(function(d){return colors[d.id]||'#94a3b8'}),borderRadius:4}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{y:{beginAtZero:true,ticks:{stepSize:1}}}}});
      }
      
      var sd = m.sessions_daily || [];
      var ctx2 = document.getElementById('baviSessChart');
      if(ctx2 && sd.length && typeof Chart !== 'undefined') {
        if(ctx2._chart) ctx2._chart.destroy();
        ctx2._chart = new Chart(ctx2,{type:'line',data:{labels:sd.map(function(d){return d.date.slice(5)}),datasets:[{label:'Sessions',data:sd.map(function(d){return d.sessions}),borderColor:'#a78bfa',tension:0.3,fill:true,backgroundColor:'rgba(167,139,250,.1)',pointRadius:1}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}}}});
      }
    }).catch(function(){});
  }
  
  // Graph pack circles
  function loadBaviGraph(bureau) {
    var container = document.getElementById('pack-container');
    if(!container) return;
    container.querySelectorAll('svg').forEach(function(s){s.remove()});
    var msg = document.getElementById('pack-msg');
    if(msg) msg.style.display = 'block';
    
    var url = bureau ? '/api/graph?bureau='+bureau+'&token='+token : '/api/graph?token='+token;
    fetch(url).then(function(r){return r.json()}).then(function(data){
      if(!data.nodes || !data.nodes.length) { if(msg) msg.textContent = 'Aucune analyse'; return; }
      if(msg) msg.style.display = 'none';
      
      var width = container.clientWidth || 700;
      var height = container.clientHeight || 400;
      
      var groups = {};
      data.nodes.forEach(function(n){
        var b = n.bureau || 'autre';
        if(!groups[b]) groups[b] = {active:[],archived:[],color:n.color};
        if(n.archived) groups[b].archived.push(n); else groups[b].active.push(n);
      });
      
      var children = Object.entries(groups).map(function(e){
        var bureau = e[0], g = e[1];
        var sub = [];
        if(g.active.length) sub.push({name:'Actif',color:g.color,archived:false,children:g.active.map(function(a){return Object.assign({},a,{value:1})})});
        if(g.archived.length) sub.push({name:'Archives',color:g.color,archived:true,children:g.archived.map(function(a){return Object.assign({},a,{value:1})})});
        return {name:bureau,color:g.color,children:sub};
      });
      
      var root = {name:'BAVI',children:children};
      var svg = d3.select('#pack-container').append('svg').attr('width',width).attr('height',height);
      var g = svg.append('g');
      svg.call(d3.zoom().scaleExtent([0.3,4]).on('zoom',function(e){g.attr('transform',e.transform)}));
      
      var pack = d3.pack().size([width,height]).padding(4);
      var hierarchy = d3.hierarchy(root).sum(function(d){return d.value||0});
      var nodes = pack(hierarchy).descendants();
      
      g.selectAll('circle.bureau').data(nodes.filter(function(d){return d.depth===1})).join('circle')
        .attr('cx',function(d){return d.x}).attr('cy',function(d){return d.y}).attr('r',function(d){return d.r})
        .attr('fill','none').attr('stroke',function(d){return d.data.color}).attr('stroke-width',2).attr('stroke-dasharray','4,3').attr('opacity',0.4);
      
      g.selectAll('circle.sub').data(nodes.filter(function(d){return d.depth===2})).join('circle')
        .attr('cx',function(d){return d.x}).attr('cy',function(d){return d.y}).attr('r',function(d){return d.r})
        .attr('fill','none').attr('stroke',function(d){return d.data.archived?'#64748b':d.data.color}).attr('stroke-width',1).attr('stroke-dasharray','2,2').attr('opacity',0.6);
      
      g.selectAll('circle.leaf').data(nodes.filter(function(d){return d.depth===3})).join('circle')
        .attr('cx',function(d){return d.x}).attr('cy',function(d){return d.y}).attr('r',function(d){return d.r-2})
        .attr('fill',function(d){return d.data.color}).attr('opacity',function(d){return d.data.archived?0.3:0.85})
        .attr('stroke','#1e293b').attr('stroke-width',0.5)
        .on('mouseenter',function(e,d){
          var tt = document.getElementById('graph-tooltip');
          var bureau = (d.ancestors().find(function(a){return a.depth===1})||{}).data||{};
          var meta = d.data;
          tt.innerHTML = '<strong style="font-size:11px">'+meta.name+'</strong>'+
            (meta.date?'<br><span style="opacity:.6;font-size:10px">📅 '+meta.date+'</span>':'')+
            '<br><span style="font-size:10px;opacity:.7">'+(bureau.name||'?')+' · '+(meta.archived?'📦 Archivé':'🟢 Actif')+'</span>';
          tt.style.display='block';
        })
        .on('mousemove',function(e){
          var tt = document.getElementById('graph-tooltip');
          tt.style.left = Math.min(e.clientX+12, window.innerWidth-200)+'px';
          tt.style.top = (e.clientY-60)+'px';
        })
        .on('mouseleave',function(){document.getElementById('graph-tooltip').style.display='none';});
      
      g.selectAll('text.alabel').data(nodes.filter(function(d){return d.depth===3})).join('text')
        .attr('x',function(d){return d.x}).attr('y',function(d){return d.y})
        .attr('text-anchor','middle').attr('dominant-baseline','middle')
        .attr('font-size',function(d){return Math.max(6,Math.min(10,d.r/3.5))}).attr('fill','#fff').attr('opacity',0.9)
        .text(function(d){return d.data.name.substring(0,Math.floor(d.r/4))});
      
      g.selectAll('text.blabel').data(nodes.filter(function(d){return d.depth===1})).join('text')
        .attr('x',function(d){return d.x}).attr('y',function(d){return d.y-d.r-4})
        .attr('text-anchor','middle').attr('font-size',11).attr('font-weight',700).attr('fill',function(d){return d.data.color})
        .text(function(d){return d.data.name.charAt(0).toUpperCase()+d.data.name.slice(1)});
      
      var active = data.nodes.filter(function(n){return !n.archived}).length;
      var archived = data.nodes.filter(function(n){return n.archived}).length;
      var elInfo = document.getElementById('pack-info');
      if(elInfo) elInfo.textContent = data.nodes.length+' analyses · '+active+' actives · '+archived+' archivées · '+Object.keys(groups).length+' bureaux';
    }).catch(function(){});
  }
  
  // Build filter buttons
  function buildGraphFilters() {
    var container = document.getElementById('graph-filters');
    if(!container) return;
    fetch('/api/graph?token='+token).then(function(r){return r.json()}).then(function(data){
      var bureaux = [];
      var seen = {};
      (data.nodes||[]).forEach(function(n){ if(n.bureau && !seen[n.bureau]){seen[n.bureau]=true;bureaux.push(n.bureau);} });
      var colors = {michel:'#a78bfa',sylvia:'#06b6d4',leo:'#818cf8',gerard:'#f97316',virginie:'#ec4899',emile:'#f59e0b',robert:'#3b82f6',sophie:'#22c55e'};
      var html = '<button class="graph-btn" data-bureau="" style="padding:4px 12px;background:var(--accent);color:#fff;border:none;border-radius:4px;cursor:pointer;font-size:11px">🌐 Tous</button>';
      bureaux.forEach(function(b){
        var c = colors[b]||'#94a3b8';
        html += '<button class="graph-btn" data-bureau="'+b+'" style="padding:4px 12px;background:var(--card);color:'+c+';border:1px solid '+c+';border-radius:4px;cursor:pointer;font-size:11px">'+b.charAt(0).toUpperCase()+b.slice(1)+'</button>';
      });
      container.innerHTML = html;
      container.querySelectorAll('.graph-btn').forEach(function(btn){
        btn.addEventListener('click',function(){
          container.querySelectorAll('.graph-btn').forEach(function(b){b.style.background='var(--card)'});
          btn.style.background='var(--accent)';
          loadBaviGraph(btn.getAttribute('data-bureau') || '');
        });
      });
    }).catch(function(){});
  }
  
  // Load on BAVI tab visibility
  var baviObserver = new MutationObserver(function(){
    var baviTab = document.getElementById('tab-bavi');
    if(baviTab && baviTab.style.display !== 'none' && !baviTab.classList.contains('_bavi-loaded')) {
      baviTab.classList.add('_bavi-loaded');
      if(typeof d3 !== 'undefined') { loadBaviGraph(''); buildGraphFilters(); }
      if(typeof Chart !== 'undefined') loadBaviAnalytics();
    }
  });
  var baviTab = document.getElementById('tab-bavi');
  if(baviTab) baviObserver.observe(baviTab, {attributes:true, attributeFilter:['style','class']});
  
  // Also load immediately
  setTimeout(function(){
    if(typeof d3 === 'undefined') {
      var s = document.createElement('script');
      s.src = 'https://d3js.org/d3.v7.min.js';
      s.onload = function(){ loadBaviGraph(''); buildGraphFilters(); };
      document.head.appendChild(s);
    } else { loadBaviGraph(''); buildGraphFilters(); }
    if(typeof Chart !== 'undefined') loadBaviAnalytics();
  }, 300);
})();
