# 🔗 Wiki Graph

<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px">
  <button onclick="loadGraph('')" id="btn-all" style="padding:4px 12px;background:var(--md-accent-fg-color);color:#fff;border:none;border-radius:4px;cursor:pointer;font-size:.75rem">🌐 Tous</button>
  <button onclick="loadGraph('michel')" style="padding:4px 12px;background:var(--md-code-bg);color:#a78bfa;border:1px solid #a78bfa;border-radius:4px;cursor:pointer;font-size:.75rem">🔧 Michel</button>
  <button onclick="loadGraph('sylvia')" style="padding:4px 12px;background:var(--md-code-bg);color:#06b6d4;border:1px solid #06b6d4;border-radius:4px;cursor:pointer;font-size:.75rem">🧭 Sylvia</button>
  <button onclick="loadGraph('leo')" style="padding:4px 12px;background:var(--md-code-bg);color:#818cf8;border:1px solid #818cf8;border-radius:4px;cursor:pointer;font-size:.75rem">🤖 Léo</button>
  <button onclick="loadGraph('gerard')" style="padding:4px 12px;background:var(--md-code-bg);color:#f97316;border:1px solid #f97316;border-radius:4px;cursor:pointer;font-size:.75rem">📝 Gérard</button>
  <button onclick="loadGraph('virginie')" style="padding:4px 12px;background:var(--md-code-bg);color:#ec4899;border:1px solid #ec4899;border-radius:4px;cursor:pointer;font-size:.75rem">🩺 Virginie</button>
  <button onclick="loadGraph('emile')" style="padding:4px 12px;background:var(--md-code-bg);color:#f59e0b;border:1px solid #f59e0b;border-radius:4px;cursor:pointer;font-size:.75rem">🎓 Émile</button>
</div>

<div id="graph-container" style="background:var(--md-code-bg);border:1px solid var(--md-default-fg-color--lightest);border-radius:8px;height:500px">
  <div id="graph-msg" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:var(--md-default-fg-color--light);font-size:.85rem">Chargement...</div>
</div>
<div id="graph-info" style="text-align:center;font-size:.7rem;color:var(--md-default-fg-color--light);margin-top:6px"></div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
const bureaux = ['michel','sylvia','leo','gerard','virginie','emile'];
const colors = {michel:'#a78bfa',sylvia:'#06b6d4',leo:'#818cf8',gerard:'#f97316',virginie:'#ec4899',emile:'#f59e0b'};

async function loadGraph(bureau){
  document.querySelectorAll('button').forEach(b=>b.style.background='var(--md-code-bg)');
  const btn = document.getElementById(bureau?'btn-'+bureau:'btn-all');
  if(btn) btn.style.background='var(--md-accent-fg-color)';

  const container = document.getElementById('graph-container');
  container.querySelectorAll('svg').forEach(s=>s.remove());
  document.getElementById('graph-msg').style.display='block';
  document.getElementById('graph-info').textContent='';

  const width = container.clientWidth || 800, height = container.clientHeight || 500;
  const url = bureau ? '/api/graph?bureau='+bureau : '/api/graph';

  try {
    const r = await fetch(url);
    const data = await r.json();
    document.getElementById('graph-msg').style.display='none';
    document.getElementById('graph-info').textContent = data.nodes.length+' analyses, '+data.links.length+' liens';

    const nodeIds = new Set(data.nodes.map(n => n.id));
    const links = data.links.filter(l => nodeIds.has(l.source) && nodeIds.has(l.target));
    const nodes = data.nodes.map(d => ({...d}));

    if(!nodes.length){ document.getElementById('graph-msg').style.display='block'; document.getElementById('graph-msg').textContent='Aucune analyse'; return; }

    const svg = d3.select('#graph-container').append('svg')
      .attr('width', width).attr('height', height);

    const g = svg.append('g');
    svg.call(d3.zoom().scaleExtent([0.2, 4]).on('zoom', (e) => { g.attr('transform', e.transform); }));

    const simulation = d3.forceSimulation(nodes)
      .force('link', d3.forceLink(links).id(d => d.id).distance(50))
      .force('charge', d3.forceManyBody().strength(-120))
      .force('center', d3.forceCenter(0, 0));

    g.selectAll('line').data(links).join('line').attr('stroke', '#475569').attr('stroke-width', 0.6);
    g.selectAll('circle').data(nodes).join('circle')
      .attr('r', d => 4 + Math.min(d.analyses || 0, 10))
      .attr('fill', d => d.color || '#64748b')
      .attr('stroke', '#1e293b').attr('stroke-width', 1);
    g.selectAll('text').data(nodes).join('text')
      .text(d => d.name).attr('font-size', 7).attr('dx', 5).attr('dy', 2)
      .attr('fill', '#94a3b8');

    simulation.on('tick', () => {
      g.selectAll('line').attr('x1', d => d.source.x).attr('y1', d => d.source.y).attr('x2', d => d.target.x).attr('y2', d => d.target.y);
      g.selectAll('circle').attr('cx', d => d.x).attr('cy', d => d.y);
      g.selectAll('text').attr('x', d => d.x).attr('y', d => d.y);
    });
  } catch(e) {
    document.getElementById('graph-msg').textContent = 'Erreur';
  }
}

loadGraph('');
</script>
