# 🔗 Wiki Graph

<div id="graph-container" style="background:var(--md-code-bg);border:1px solid var(--md-default-fg-color--lightest);border-radius:8px;height:500px"></div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
(async function(){
  const container = document.getElementById('graph-container');
  const width = container.clientWidth || 800, height = container.clientHeight || 500;

  try {
    const r = await fetch('/api/graph');
    const data = await r.json();
    console.log('Graph data:', data.nodes.length, 'nodes');

    const svg = d3.select('#graph-container').append('svg')
      .attr('width', width).attr('height', height);

    const links = data.links.map(d => ({...d}));
    const nodes = data.nodes.map(d => ({...d}));

    const simulation = d3.forceSimulation(nodes)
      .force('link', d3.forceLink(links).id(d => d.id).distance(60))
      .force('charge', d3.forceManyBody().strength(-150))
      .force('center', d3.forceCenter(width/2, height/2));

    const link = svg.append('g')
      .selectAll('line').data(links).join('line')
      .attr('stroke', '#475569').attr('stroke-width', 0.8);

    const node = svg.append('g')
      .selectAll('circle').data(nodes).join('circle')
      .attr('r', d => 4 + Math.min(d.analyses || 0, 12))
      .attr('fill', d => d.color || '#64748b')
      .attr('stroke', '#1e293b').attr('stroke-width', 1);

    const label = svg.append('g')
      .selectAll('text').data(nodes).join('text')
      .text(d => d.name)
      .attr('font-size', 8).attr('dx', 6).attr('dy', 3)
      .attr('fill', '#94a3b8')
      .style('pointer-events', 'none');

    simulation.on('tick', () => {
      link.attr('x1', d => d.source.x).attr('y1', d => d.source.y)
          .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
      node.attr('cx', d => d.x).attr('cy', d => d.y);
      label.attr('x', d => d.x).attr('y', d => d.y);
    });

  } catch(e) {
    container.innerHTML = '<p style=\"color:#ef4444;padding:20px\">Erreur: '+e.message+'</p>';
  }
})();
</script>
