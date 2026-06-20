---
date: 2026-06-19
bureau: bureau-michel
modele: deepseek-v4-pro
tags: [n8n, analyse, options, installation]
statut: finalise
---

# n8n — Analyse options A vs B

**Date :** 19/06/2026
**Modèle :** DeepSeek Pro (deepseek-chat)
**Analyse déléguée :** via delegate_task
**Contexte :** Installer n8n sur LEO (conteneur Hermès Docker, réseau Tailscale, port 5678 libre)

---

## 1. Rappel du problème

Installation n8n v2.26.7 via npm (juin 2026) : login OK sur localhost:5678, 401 depuis 100.92.102.28:5678. Jamais résolu. n8n retiré définitivement.

## 2. Environnement actuel

| Élément | Valeur |
|:--------|:-------|
| Host | Debian 13 (conteneur Hermès Docker) |
| Docker | v26.1.5 sur l'hôte, **pas de socket** dans le conteneur |
| docker-compose.yml | `/opt/hermes/docker-compose.yml` (dans l'image, pas mounté) |
| Réseau | `network_mode: host` — partage pile réseau de l'hôte |
| Tailscale | 100.92.102.28 |
| Port 5678 | Libre |
| Image n8n officielle | `docker.n8n.io/n8nio/n8n` ou `n8nio/n8n` |

## 3. Options comparées

### Option A — n8n dans le docker-compose Hermès ❌ BLOQUÉE

**Principe :** Ajouter un service `n8n` dans `/opt/hermes/docker-compose.yml`

**Problème bloquant :** Le fichier `docker-compose.yml` est dans l'image Docker, pas mounté depuis l'hôte via volume. Impossible de le modifier depuis le conteneur.

**Solution dans une autre config :** Si on mountait le fichier, il faudrait :
1. Ajouter un volume `- ./docker-compose.yml:/opt/hermes/docker-compose.yml` dans le `docker run`
2. HUP ou restart le conteneur Hermès
3. n8n serait géré comme un service interne

**Risque permanent :** Un rebuild de l'image Hermès écrase le fichier.

### Option B — Conteneur Docker indépendant ✅ VIABLE

**Principe :** `docker run` séparé, volume persistants, réseau host.

```
docker volume create n8n_data

docker run -d \
  --name n8n \
  --restart unless-stopped \
  --network host \
  -e N8N_SECURE_COOKIE=false \
  -e N8N_HOST=100.92.102.28 \
  -e N8N_PORT=5678 \
  -e N8N_PROXY_HOPS=0 \
  -e N8N_DIAGNOSTICS_ENABLED=false \
  -e N8N_AI_ENABLED=false \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n:latest
```

**Accès :** `http://100.92.102.28:5678`

**Avantages :**
- Zéro impact sur Hermès
- Image officielle (pas notre npm artisanal)
- `--restart unless-stopped` → auto-restart après reboot LEO
- Volume Docker pour les données (backupable, `docker volume inspect`)
- Mise à jour simple : `docker pull && docker stop/rm && docker run`
- Version `latest` (pas la 2.26.7 buggée)

**Points clés anti-401 :**
| Variable | Pourquoi |
|:---------|:---------|
| `N8N_SECURE_COOKIE=false` | Cookie `Secure` non envoyé via HTTP pur (pas HTTPS sur Tailscale) |
| `N8N_HOST=100.92.102.28` | Cookie lié à la bonne IP |
| `N8N_PROXY_HOPS=0` | Pas de proxy → pas de `X-Forwarded-For` intercepté |

**Risques résiduels :**
- Le login 401 pourrait revenir si Tailscale modifie les en-têtes (encapsulation)
- Solution de repli : SSH tunnel `ssh -L 5678:localhost:5678 tofdan@100.92.102.28`
- n8n n'est pas accessible depuis l'intérieur du conteneur Hermès (localhost:5678 OK, mais Hermès n'a pas curl pour faire des API calls)

## 4. Recommandation

**Option B — Conteneur indépendant**

Plan en 3 phases :

**Phase 1 — Test** (10 min)
```bash
docker pull docker.n8n.io/n8nio/n8n:latest
docker run -d --name n8n-test \
  --rm --network host \
  -e N8N_SECURE_COOKIE=false \
  -e N8N_HOST=100.92.102.28 \
  -e N8N_PORT=5678 \
  docker.n8n.io/n8nio/n8n:latest
```
→ Vérifier accès `http://100.92.102.28:5678`
→ Tester login (créer compte owner)
→ Si 401 : `docker rm -f n8n-test` et SSH tunnel

**Phase 2 — Installation** (5 min)
```bash
bash /opt/data/n8n/run-n8n.sh
```

**Phase 3 — Validation**
- Créer compte owner
- Vérifier que les workflows persistent après restart
- Cron de vérification (toutes les heures) : `curl -s -o /dev/null -w "%{http_code}" http://localhost:5678`

## 5. Scripts disponibles

| Script | Chemin | Usage |
|:-------|:-------|:------|
| run-n8n.sh | `/opt/data/n8n/run-n8n.sh` | Installation initiale |
| update-n8n.sh | `/opt/data/n8n/update-n8n.sh` | Mise à jour avec backup |

## 6. Décision

En attente de décision de l'utilisateur.

| Option | Statut | Priorité |
|:-------|:-------|:---------|
| B — Conteneur indépendant | En attente | ⭐ Recommandée |
| A — Intégré docker-compose | ❌ Bloquée | — |
