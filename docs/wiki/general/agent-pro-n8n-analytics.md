# n8n — Analyse options A vs B

**Date :** 19/06/2026
**Modèle :** DeepSeek Pro

---

## Rappel du problème

Installation n8n v2.26.7 via npm (juin 2026) : login OK sur localhost:5678, **401** depuis l'IP Tailscale (100.92.102.28:5678). Jamais résolu après 2h de debug.

## Environnement LEO

| Élément | Valeur |
|:--------|:-------|
| Hermès | v0.16.0 dans un conteneur Docker |
| Docker | v26.1.5 sur l'hôte, **pas de socket** dans le conteneur |
| Réseau | `network_mode: host` — partage pile réseau de l'hôte |
| Tailscale | 100.92.102.28 |
| Port 5678 | Libre |

## Comparaison

### Option A — Intégré au docker-compose Hermès ❌ BLOQUÉE

Le fichier `/opt/hermes/docker-compose.yml` est dans l'image Docker, pas mounté. Impossible à modifier depuis le conteneur.

### Option B — Conteneur Docker indépendant ✅ RECOMMANDÉE

```bash
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

**Garantie anti-401 :**

| Variable | Rôle |
|:---------|:-----|
| `N8N_SECURE_COOKIE=false` | Cookie non-Secure OK pour HTTP (pas HTTPS sur Tailscale) |
| `N8N_HOST=100.92.102.28` | Cookie lié à la bonne IP |
| `N8N_PROXY_HOPS=0` | Pas de proxy → pas de `X-Forwarded-For` intercepté |

**Plan en 3 phases :**

1. **Test** : `docker run` avec `--rm`, vérifier login HTTP
2. **Installation** : `bash /opt/data/n8n/run-n8n.sh`
3. **Validation** : créer compte owner, vérifier persistence

**Scripts disponibles :** `run-n8n.sh` et `update-n8n.sh` dans `/opt/data/n8n/`
