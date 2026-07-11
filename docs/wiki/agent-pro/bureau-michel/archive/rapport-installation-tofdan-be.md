---
date: 2026-06-27
bureau: bureau-robert
version: v1.0
modele: deepseek-v4-pro
tags: [codewhale, tofdan, installation, nginx, cloudflare, infrastructure]
statut: finalise
type: rapport
---

# 🐋 CodeWhale — Installation tofdan.be sur Leo

> **Date** : 2026-06-27  
> **Agent** : CodeWhale (deepseek-v4-pro)  
> **Machine** : Leo (`tofdan-System-Product-Name`, IP Tailscale `100.92.102.28`)  
> **OS** : Ubuntu 26.04 (resolute), kernel 7.0.0-22-generic  
> **Contexte** : Stratégie d'hébergement — bureau-robert/strategie-tofdan-be

---

## 📦 Logiciels installés

| Logiciel | Version | Méthode |
|----------|---------|---------|
| **Nginx** | 1.28.3 | `apt install nginx` |
| **Certbot** | 4.0.0 | `apt install certbot python3-certbot-nginx` |
| **Cloudflared** | 2026.6.1 | Binaire GitHub → `/usr/local/bin/cloudflared` |

---

## 📁 Structure de fichiers sur Leo

```
/etc/nginx/sites-available/tofdan.be    ← Configuration virtual host Nginx
/etc/nginx/sites-enabled/tofdan.be      ← Lien symbolique (activé)
/var/www/tofdan.be/                     ← Racine du site
/var/www/tofdan.be/index.html           ← Page de test actuelle
/var/www/astro/                         ← Dossier prêt pour l'App Astro
/home/tofdan/.cloudflared/              ← Configuration Cloudflare Tunnel
/home/tofdan/.cloudflared/config.yml    ← Config ingress tunnel
/home/tofdan/.cloudflared/8f61e660-...json  ← Credentials tunnel
/etc/systemd/system/cloudflared.service ← Service systemd
```

---

## 🔧 Configuration Nginx

**Fichier** : `/etc/nginx/sites-available/tofdan.be`

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name tofdan.be www.tofdan.be;

    root /var/www/tofdan.be;
    index index.html;

    access_log /var/log/nginx/tofdan.be_access.log;
    error_log /var/log/nginx/tofdan.be_error.log;

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

## ☁️ Cloudflare Tunnel

| Propriété | Valeur |
|-----------|--------|
| **Tunnel ID** | `8f61e660-566a-4a4b-8925-db0e4b421ea3` |
| **Tunnel Name** | `tofdan-be` |
| **Statut** | ✅ **healthy** — 4 connexions QUIC |
| **Endpoints** | bru03 (x2), ams13 (x2) |
| **Service** | `systemctl [start|stop|restart|status] cloudflared` |
| **Logs** | `journalctl -u cloudflared` |

### Config ingress (`/home/tofdan/.cloudflared/config.yml`)

```yaml
tunnel: 8f61e660-566a-4a4b-8925-db0e4b421ea3
credentials-file: /home/tofdan/.cloudflared/8f61e660-566a-4a4b-8925-db0e4b421ea3.json

ingress:
  - hostname: tofdan.be
    service: http://localhost:80
  - hostname: www.tofdan.be
    service: http://localhost:80
  - service: http_status:404
```

---

## 🌐 DNS Cloudflare

### Nameservers
| Ancien (easyhost) | Nouveau (Cloudflare) |
|---|---|
| `ns1.easyhost.be` | `ryleigh.ns.cloudflare.com` |
| `ns2.easyhost.be` | `tanner.ns.cloudflare.com` |
| `ns3.easyhost.be` | *(supprimé)* |

### Enregistrements modifiés/ajoutés

| Type | Nom | Valeur | Proxy |
|------|-----|--------|-------|
| A | `tofdan.be` | `178.51.152.48` | 🟠 |
| A | `ftp.tofdan.be` | `217.21.190.175` | 🟠 |
| CNAME | `www.tofdan.be` | `8f61e660-566a-4a4b-8925-db0e4b421ea3.cfargotunnel.com` | 🟠 |

> ⚠️ **Ne pas proxifier** les CNAME mail : `autoconfig`, `autodiscover`, `mail` — les laisser en **DNS only** (gris).

---

## 🔥 Pare-feu (UFW)

```bash
sudo ufw status
# Ports ouverts : 80/tcp, 443/tcp, 11434/tcp (Ollama), 3389/tcp (RDP)
# Ports sortants : 7844/tcp, 7844/udp (Cloudflare Tunnel)
# Statut : actif
```

---

## 🧪 Vérification

```bash
# Test local
curl http://localhost/
# → HTTP 200 — « 🪐 tofdan.be — Site en construction »

# Test public
curl https://www.tofdan.be/
# → HTTP 200 — même page
```

---

## 🚫 Ce qui N'A PAS été fait (hors scope CodeWhale)

| Tâche | Responsable |
|-------|-------------|
| Développement HTML/CSS du site | 💻 GitHub Copilot |
| Copie fichiers App Astro → `/var/www/astro/` | 👤 Christophe |
| Port forwarding routeur (80/443) | ❌ Non nécessaire (Cloudflare Tunnel) |
| Certificat Let's Encrypt (`certbot`) | ❌ Remplacé par Cloudflare HTTPS |
| Monitoring uptime | 🔧 Michel (Michel) |

---

## ⚡ Commandes utiles pour maintenance

```bash
# Redémarrer Nginx
sudo systemctl restart nginx

# Redémarrer le tunnel
sudo systemctl restart cloudflared

# Logs tunnel
journalctl -u cloudflared -f

# Vérifier la config Nginx
sudo nginx -t

# Déployer nouveaux fichiers
sudo cp fichier.html /var/www/tofdan.be/
sudo chown www-data:www-data /var/www/tofdan.be/*
```

---

## 🔐 Accès

| Ressource | Méthode |
|-----------|---------|
| SSH | `tailscale ssh tofdan@tofdan-system-product-name` |
| sudo | Mot de passe standard (même que VNC) |

---

## 📝 Notes pour Hermes

- Le **Certbot** est installé mais **non utilisé** — Cloudflare gère le HTTPS automatiquement
- Le **port forwarding routeur** n'est pas nécessaire grâce au tunnel Cloudflare
- Les **mails** (MX, SRV, TXT) sont préservés via mailprotect.be
- Le tunnel Cloudflare démarre automatiquement au boot (`systemctl enable cloudflared`)
- L'App Astro doit être copiée dans `/var/www/astro/` avec `index.html` comme point d'entrée
- La page actuelle (`index.html`) est temporaire — à remplacer par le site développé via GitHub Copilot

---

*Rapport généré par 🐋 CodeWhale le 2026-06-27 — Stratégie bureau-robert/strategie-tofdan-be*
