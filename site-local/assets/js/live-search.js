const TOKEN='leo-panel-2026';
(function(){
  const TOKEN = 'leo-panel-2026';
  let timer = null, container = null, resultsEl = null;

  function createUI() {
    // Cache la recherche MkDocs
    const mkdocsSearch = document.querySelector('.md-search');
    if (!mkdocsSearch) return setTimeout(createUI, 200);

    // Crée notre container
    container = document.createElement('div');
    container.className = 'md-search';
    container.innerHTML = `
      <div class="md-search__inner">
        <form class="md-search__form" onsubmit="return false">
          <input id="live-search-input" class="md-search__input" type="text" placeholder="Rechercher..." autocomplete="off">
          <div id="live-search-results" class="live-results" style="display:none;position:absolute;top:100%;left:0;right:0;background:var(--md-default-bg-color);border:1px solid var(--md-default-fg-color--lightest);border-radius:0 0 6px 6px;max-height:400px;overflow-y:auto;z-index:100;box-shadow:0 8px 24px rgba(0,0,0,.2)"></div>
        </form>
      </div>`;
    
    mkdocsSearch.parentNode.replaceChild(container, mkdocsSearch);
    resultsEl = document.getElementById('live-search-results');
    
    document.getElementById('live-search-input').addEventListener('input', function(e){
      clearTimeout(timer);
      const q = e.target.value.trim();
      if (q.length < 2) { resultsEl.style.display = 'none'; return; }
      timer = setTimeout(() => search(q), 200);
    });

    // Click outside → hide
    document.addEventListener('click', function(e){
      if (!container.contains(e.target)) resultsEl.style.display = 'none';
    });
  }

  async function search(q) {
    try {
      const r = await fetch(`/api/search?q=${encodeURIComponent(q)}&token=${TOKEN}`);
      const data = await r.json();
      if (!data.results || !data.results.length) {
        resultsEl.innerHTML = '<div style="padding:12px;color:var(--md-default-fg-color--light);font-size:.85rem">Aucun résultat</div>';
        resultsEl.style.display = 'block';
        return;
      }
      resultsEl.innerHTML = data.results.map(r => `
        <a href="${r.path}" style="display:block;padding:10px 14px;text-decoration:none;color:var(--md-default-fg-color);border-bottom:1px solid var(--md-default-fg-color--lightest);transition:background .1s" onmouseover="this.style.background='var(--md-accent-fg-color--transparent)'" onmouseout="this.style.background=''">
          <div style="font-weight:600;font-size:.85rem;margin-bottom:2px">${r.title}</div>
          <div style="font-size:.75rem;color:var(--md-default-fg-color--light)">${r.snippet}</div>
        </a>
      `).join('');
      resultsEl.style.display = 'block';
    } catch(e) {
      resultsEl.innerHTML = '<div style="padding:12px;color:#ef4444;font-size:.85rem">Erreur de recherche</div>';
      resultsEl.style.display = 'block';
    }
  }

  createUI();
})();
