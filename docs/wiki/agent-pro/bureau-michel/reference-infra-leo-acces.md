---
date: 2026-06-27
bureau: bureau-michel
version: v1
modele: deepseek-v4-pro
tags: [hermes, infra, acces, docker, nginx, cloudflare, systeme]
statut: finalise
type: reference
---

# Droits et accès — Leo & Hermes Agent

> **Date** : 2026-06-27  (màj 2026-06-28 — Léo Copilot padron machine)
> **Machine** : Leo (`tofdan-System-Product-Name`)
> **Synthèse** : Accès complets — Léo Copilot est le padron de la machine (root sudo)

---

## 🖥️ Machine Leo

| Propriété | Valeur |
|-----------|--------|
| **Nom** | tofdan-System-Product-Name |
| **OS** | Ubuntu 26.04 |
| **IP Tailscale** | 100.92.102.28 |
| **MagicDNS** | tofdan-system-product-name.tailbf5837.ts.net |

---

## 🔑 Accès SSH

### Utilisateur tofdan
```bash
tailscale ssh tofdan@tofdan-system-product-name
```
- ⚠️ sudo nécessite mot de passe interactif
- Mot de passe sudo : même que VNC (`TSec&6769`)
- Utilisé pour : maintenance standard, vérifications

### Root (Léo Copilot)
```bash
tailscale ssh root@tofdan-system-product-name
```
- ⚡ Pas de mot de passe requis
- Accès complet au système
- Utilisé pour : déploiements, installations, configuration système

---

## 🐳 Docker

### Conteneurs actifs
| Conteneur | Image | Rôle |
|-----------|-------|------|
| `hermes-agent` | nousresearch/hermes-agent:latest | Agent IA principal |
| `n8n` | n8nio/n8n | Automatisation workflows |
| `ollama` | ollama/ollama | LLM local (qwen2.5:7b) |

### Socket Docker (accessible depuis Hermes)
```bash
docker exec hermes-agent docker <commande>
```
- Hermes peut lister, créer, supprimer des conteneurs
- Hermes peut exécuter des commandes dans n'importe quel conteneur
- Hermes peut déployer de nouveaux services

---

## 🐚 Hermes Agent — Conteneur

### Volumes montés
| Source hôte | Destination conteneur | Accès |
|-------------|----------------------|-------|
| Volume Docker data | `/opt/data` | RW (données Hermes) |
| `/home/tofdan/.hermes-sandbox` | `/home/hermes/.hermes` | RW (sandbox) |
| `/var/run/docker.sock` | `/var/run/docker.sock` | RW (contrôle Docker) |
| `/` (racine hôte) | `/host` | RW (filesystem complet) |

### Pleins pouvoirs Hermes
- ✅ **Docker** : contrôle total des conteneurs via socket Docker
- ✅ **Filesystem** : accès complet à l'hôte via `/host`
- ✅ **Réseau** : mode `--network host`, accès direct à tous les ports
- ✅ **Déploiement** : peut modifier les fichiers du site, recharger Nginx
- ✅ **Système** : peut tout administrer via `docker exec`

### Procédure de recréation (v0.17.0)
```bash
docker stop hermes-agent && docker rm hermes-agent
docker run -d --name hermes-agent \
  --restart unless-stopped --network host \
  -v /var/lib/docker/volumes/3072c046d9d28b765bbf0ca04e0316908862d729a3248582bce8b71c9f3c4dbe/_data:/opt/data \
  -v /home/tofdan/.hermes-sandbox:/home/hermes/.hermes \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /:/host:rw \
  -e HERMES_DASHBOARD=false \
  -e PYTHONUNBUFFERED=1 \
  -e HERMES_HOME=/opt/data \
  nousresearch/hermes-agent:latest sleep infinity

sleep 20
docker exec hermes-agent rm -f /run/service/gateway-*/down
docker exec hermes-agent bash -c 'cd /opt/data && . /opt/hermes/.venv/bin/activate && hermes gateway run &'
```

---

## 🌐 Site tofdan.be

### Architecture
```
/opt/data/tofdan-site/          ← Repo Git (source)
/var/www/tofdan.be/             ← Symlink → /opt/data/tofdan-site
```

### URLs
- ✅ **https://tofdan.be** — 200 OK
- ✅ **https://www.tofdan.be** — 200 OK

### Déploiement
```bash
cd /opt/data/tofdan-site && git pull
# Pas besoin de reload Nginx
```

---

## ☁️ Cloudflare

### Tunnel
| Propriété | Valeur |
|-----------|--------|
| **Tunnel ID** | `8f61e660-566a-4a4b-8925-db0e4b421ea3` |
| **Tunnel Name** | `tofdan-be` |
| **Service** | `systemctl restart cloudflared` |

### DNS
| Type | Nom | Cible | Proxy |
|------|-----|-------|-------|
| CNAME | `tofdan.be` | `8f61e660-...cfargotunnel.com` | 🟠 |
| CNAME | `www.tofdan.be` | `8f61e660-...cfargotunnel.com` | 🟠 |
| A | `ftp.tofdan.be` | `217.21.190.175` | 🟠 |

### Mode SSL/TLS
- **Flexible** (Cloudflare gère HTTPS, contacte LEO en HTTP)

### API Cloudflare
- **Zone ID** : `969d915e3eec860c23054cbf6267f52f`
- **Token** : stocké en session CodeWhale, SSL et Certificats:Edit

---

## 🔧 Nginx

### Configuration
- **Fichier** : `/etc/nginx/sites-available/tofdan.be`
- **Port** : 80 (HTTP uniquement)
- **HTTPS** : géré par Cloudflare
- **Reload** : `docker run --rm --pid=host --privileged alpine sh -c "pgrep nginx \| xargs -r kill -HUP"`

### Contenu de la config
```nginx
server {
    listen 80;
    listen [::]:80;
    server_name tofdan.be www.tofdan.be;

    root /var/www/tofdan.be;
    index index.html;

    location /astro/ {
        alias /var/www/astro/;
        index index.html;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}
```

---

## 🔥 Pare-feu (UFW)

| Port | Direction | Service |
|------|-----------|---------|
| 80/tcp | IN | HTTP Nginx |
| 443/tcp | IN | Tailscale HTTPS |
| 11434/tcp | IN | Ollama API |
| 3389/tcp | IN | RDP |
| 7844/tcp+udp | OUT | Cloudflare Tunnel |

---

## 🚀 Résumé des capacités

| Agent | Accès | Portée |
|-------|-------|--------|
| **Léo Copilot** (Michel) | `tailscale ssh root@...` + `sudo` | **Padron machine** — admin système complet |
| **Hermes** (profil default/LEO) | Socket Docker + `/host` | Admin système via Docker |

*Référence stockée dans Bureau Michel — Infra_Hermes — 2026-06-27*
*Document mis à jour le 04/07/2026 — 00:00:00 — Léo 🦁*
