# ✏️ Éditeur BAVI

<div id="editor-container">
  <div style="display:flex;gap:8px;margin-bottom:12px">
    <input id="editor-path" type="text" placeholder="chemin/fichier.md" style="flex:1;padding:8px;background:var(--md-code-bg);border:1px solid var(--md-default-fg-color--lightest);border-radius:6px;color:var(--md-default-fg-color);font-family:monospace;font-size:.85rem">
    <button onclick="loadFile()" style="padding:8px 16px;background:var(--md-primary-fg-color);color:#fff;border:none;border-radius:6px;font-weight:600;cursor:pointer">📂 Charger</button>
  </div>
  <textarea id="editor-content" style="width:100%;height:60vh;background:var(--md-code-bg);color:var(--md-default-fg-color);border:1px solid var(--md-default-fg-color--lightest);border-radius:8px;padding:14px;font-family:'Roboto Mono',monospace;font-size:.85rem;resize:vertical"></textarea>
  <div style="display:flex;gap:8px;margin-top:8px">
    <button onclick="saveFile()" style="padding:8px 20px;background:#22c55e;color:#fff;border:none;border-radius:6px;font-weight:600;cursor:pointer">💾 Sauvegarder</button>
    <span id="editor-status" style="font-size:.8rem;color:var(--md-default-fg-color--light);align-self:center"></span>
  </div>
  <div id="editor-preview" style="margin-top:16px;padding:16px;background:var(--md-code-bg);border:1px solid var(--md-default-fg-color--lightest);border-radius:8px;min-height:200px">
    <em style="color:var(--md-default-fg-color--light)">Prévisualisation — la sauvegarde recharge la page</em>
  </div>
</div>

<script>
async function loadFile(){
  const path = document.getElementById('editor-path').value.trim();
  if(!path) return;
  try {
    const r = await fetch('/api/editor/load?path='+encodeURIComponent(path));
    const d = await r.json();
    if(d.ok){
      document.getElementById('editor-content').value = d.content;
      document.getElementById('editor-status').textContent = '✅ Chargé: '+path;
    } else {
      document.getElementById('editor-status').textContent = '❌ '+d.error;
    }
  } catch(e) {
    document.getElementById('editor-status').textContent = '❌ Erreur';
  }
}

async function saveFile(){
  const path = document.getElementById('editor-path').value.trim();
  const content = document.getElementById('editor-content').value;
  if(!path) return;
  try {
    const r = await fetch('/api/editor/save',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({path, content})
    });
    const d = await r.json();
    document.getElementById('editor-status').textContent = d.ok ? '💾 Sauvegardé! Rebuild en cours...' : '❌ '+d.error;
    if(d.ok) setTimeout(()=>location.href='/'+path.replace('.md','/'), 1500);
  } catch(e) {
    document.getElementById('editor-status').textContent = '❌ Erreur';
  }
}

// Pré-remplir depuis le paramètre ?path=
const qp = new URLSearchParams(location.search);
if(qp.get('path')){
  document.getElementById('editor-path').value = qp.get('path');
  loadFile();
}
</script>
