# 🔗 Wiki Graph

<style>
#pack-container circle:hover{opacity:1!important;stroke:#fff;stroke-width:2}
</style>

<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px">
  <button onclick="loadPack('')" id="btn-all" style="padding:4px 12px;background:var(--md-accent-fg-color);color:#fff;border:none;border-radius:4px;cursor:pointer;font-size:.7rem">🌐 Tous</button>
  <button onclick="loadPack('michel')" style="padding:4px 12px;background:var(--md-code-bg);color:#a78bfa;border:1px solid #a78bfa;border-radius:4px;cursor:pointer;font-size:.7rem">🔧 Michel</button>
  <button onclick="loadPack('sylvia')" style="padding:4px 12px;background:var(--md-code-bg);color:#06b6d4;border:1px solid #06b6d4;border-radius:4px;cursor:pointer;font-size:.7rem">🧭 Sylvia</button>
  <button onclick="loadPack('leo')" style="padding:4px 12px;background:var(--md-code-bg);color:#818cf8;border:1px solid #818cf8;border-radius:4px;cursor:pointer;font-size:.7rem">🤖 Léo</button>
  <button onclick="loadPack('gerard')" style="padding:4px 12px;background:var(--md-code-bg);color:#f97316;border:1px solid #f97316;border-radius:4px;cursor:pointer;font-size:.7rem">📝 Gérard</button>
  <button onclick="loadPack('virginie')" style="padding:4px 12px;background:var(--md-code-bg);color:#ec4899;border:1px solid #ec4899;border-radius:4px;cursor:pointer;font-size:.7rem">🩺 Virginie</button>
  <button onclick="loadPack('emile')" style="padding:4px 12px;background:var(--md-code-bg);color:#f59e0b;border:1px solid #f59e0b;border-radius:4px;cursor:pointer;font-size:.7rem">🎓 Émile</button>
</div>

<div id="pack-container" style="background:var(--md-code-bg);border:1px solid var(--md-default-fg-color--lightest);border-radius:8px;height:520px;position:relative">
  <div id="pack-msg" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:var(--md-default-fg-color--light)">Chargement...</div>
</div>
<div id="graph-tooltip" style="display:none;position:fixed;background:#1e293b;color:#e2e8f0;border:1px solid #475569;border-radius:6px;padding:6px 10px;font-size:.7rem;z-index:999;pointer-events:none;max-width:220px;box-shadow:0 4px 12px rgba(0,0,0,.5)"></div>
<div id="pack-info" style="text-align:center;font-size:.7rem;color:var(--md-default-fg-color--light);margin-top:4px"></div>
<div style="display:flex;justify-content:center;gap:16px;margin-top:6px;font-size:.7rem;color:var(--md-default-fg-color--light)">
  <span>🟢 Actif</span><span>⚫ Archivé</span><span>◌ Bureau</span>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
function hexToRgb(hex){const r=parseInt(hex.slice(1,3),16),g=parseInt(hex.slice(3,5),16),b=parseInt(hex.slice(5,7),16);return{r,g,b}}

async function loadPack(bureau){
  document.querySelectorAll('button').forEach(b=>b.style.background='var(--md-code-bg)');
  const btn=document.getElementById(bureau?'btn-'+bureau:'btn-all');
  if(btn)btn.style.background='var(--md-accent-fg-color)';

  const container=document.getElementById('pack-container');
  container.querySelectorAll('svg').forEach(s=>s.remove());
  document.getElementById('pack-msg').style.display='block';

  const width=container.clientWidth||800,height=container.clientHeight||500;
  const url=bureau?'/api/graph?bureau='+bureau:'/api/graph';

  try{
    const r=await fetch(url);
    const data=await r.json();
    if(!data.nodes.length){document.getElementById('pack-msg').textContent='Aucune analyse';return}
    document.getElementById('pack-msg').style.display='none';

    // Build hierarchy: root > bureau > [Actif, Archives] > analyses
    const groups={};
    data.nodes.forEach(n=>{
      const b=n.bureau||'autre';
      if(!groups[b])groups[b]={active:[],archived:[],color:n.color};
      if(n.archived)groups[b].archived.push(n);else groups[b].active.push(n);
    });

    const children=Object.entries(groups).map(([bureau,g])=>{
      const sub=[];
      if(g.active.length)sub.push({name:'Actif',color:g.color,archived:false,children:g.active.map(a=>({...a,value:1}))});
      if(g.archived.length)sub.push({name:'Archives',color:g.color,archived:true,children:g.archived.map(a=>({...a,value:1}))});
      return {name:bureau,color:g.color,children:sub};
    });

    const root={name:'BAVI',children};
    const svg=d3.select('#pack-container').append('svg').attr('width',width).attr('height',height);
    const g=svg.append('g');

    // Zoom
    svg.call(d3.zoom().scaleExtent([0.3,4]).on('zoom',(e)=>{g.attr('transform',e.transform)}));

    const pack=d3.pack().size([width,height]).padding(4);
    const hierarchy=d3.hierarchy(root).sum(d=>d.value||0);
    const nodes=pack(hierarchy).descendants();

    // Bureau circles (depth 1)
    g.selectAll('circle.bureau').data(nodes.filter(d=>d.depth===1)).join('circle')
      .attr('cx',d=>d.x).attr('cy',d=>d.y).attr('r',d=>d.r)
      .attr('fill','none').attr('stroke',d=>d.data.color).attr('stroke-width',2)
      .attr('stroke-dasharray','4,3').attr('opacity',0.4);

    // Sub-group circles: Actif/Archives (depth 2)
    g.selectAll('circle.sub').data(nodes.filter(d=>d.depth===2)).join('circle')
      .attr('cx',d=>d.x).attr('cy',d=>d.y).attr('r',d=>d.r)
      .attr('fill','none').attr('stroke',d=>d.data.archived?'#64748b':d.data.color)
      .attr('stroke-width',1).attr('stroke-dasharray','2,2').attr('opacity',0.6);

    // Analyse circles (depth 3)
    g.selectAll('circle.leaf').data(nodes.filter(d=>d.depth===3)).join('circle')
      .attr('cx',d=>d.x).attr('cy',d=>d.y).attr('r',d=>d.r-2)
      .attr('fill',d=>d.data.color)
      .attr('opacity',d=>d.data.archived?0.3:0.85)
      .attr('stroke','#1e293b').attr('stroke-width',0.5)
      .on('mouseenter',(e,d)=>{
        const tt=document.getElementById('graph-tooltip');
        const bureau=d.ancestors().find(a=>a.depth===1)?.data?.name||'?';
        const meta=d.data;
        const parts=[];
        if(meta.date)parts.push(`📅 ${meta.date}`);
        if(meta.version)parts.push(`v${meta.version}`);
        if(meta.statut)parts.push(`📌 ${meta.statut}`);
        tt.innerHTML=`<strong style="font-size:.7rem">${meta.name}</strong>`+
          (parts.length?`<br><span style="opacity:.6;font-size:.6rem">${parts.join(' · ')}</span>`:'')+
          `<br><span style="font-size:.6rem;opacity:.7">${bureau} · ${meta.archived?'📦 Archivé':'🟢 Actif'}</span>`+
          (meta.tags?`<br><span style="font-size:.6rem;opacity:.4">🏷️ ${meta.tags}</span>`:'');
        tt.style.display='block';
      })
      .on('mousemove',(e)=>{
        const tt=document.getElementById('graph-tooltip');
        tt.style.left=Math.min(e.clientX+12,window.innerWidth-200)+'px';
        tt.style.top=(e.clientY-60)+'px';
      })
      .on('mouseleave',()=>{document.getElementById('graph-tooltip').style.display='none';});

    // Analyse labels (all circles with r > 8)
    g.selectAll('text.alabel').data(nodes.filter(d=>d.depth===3)).join('text')
      .attr('x',d=>d.x).attr('y',d=>d.y)
      .attr('text-anchor','middle').attr('dominant-baseline','middle')
      .attr('font-size',d=>Math.max(6,Math.min(10,d.r/3.5)))
      .attr('fill','#fff').attr('opacity',0.9)
      .text(d=>d.data.name.substring(0,Math.floor(d.r/4)));

    // Bureau labels
    g.selectAll('text.blabel').data(nodes.filter(d=>d.depth===1)).join('text')
      .attr('x',d=>d.x).attr('y',d=>d.y-d.r-4)
      .attr('text-anchor','middle').attr('font-size',11).attr('font-weight',700)
      .attr('fill',d=>d.data.color).text(d=>d.data.name.charAt(0).toUpperCase()+d.data.name.slice(1));

    // Sub-group labels
    g.selectAll('text.slabel').data(nodes.filter(d=>d.depth===2&&d.r>25)).join('text')
      .attr('x',d=>d.x).attr('y',d=>d.y-d.r+14)
      .attr('text-anchor','middle').attr('font-size',9)
      .attr('fill',d=>d.data.archived?'#64748b':d.data.color)
      .text(d=>d.data.archived?'📦 Archives':'Actif');

    const active=data.nodes.filter(n=>!n.archived).length;
    const archived=data.nodes.filter(n=>n.archived).length;
    document.getElementById('pack-info').textContent=`${data.nodes.length} analyses · ${active} actives · ${archived} archivées · ${Object.keys(groups).length} bureaux`;

  }catch(e){
    document.getElementById('pack-msg').textContent='Erreur: '+e.message;
  }
}

loadPack('');
</script>
