---
date: 2026-06-30
bureau: bureau-michel
version: v1
modele: deepseek-v4-flash
tags: [hermes, infra, acces, credentials, api-keys, audit, securite, leo-copilot]
statut: proposition
type: analyse
---

# 🔐 Audit Accès & Credentials — Léo Copilot

> **Machine** : Leo (`tofdan-System-Product-Name`) · Sombreffe, Belgique
> **Container** : hermes-agent (bridge → host fixé après crash)
> **Date** : 30/06/2026 (post-crash recovery)

---

## 🎯 Périmètre

Analyse de l'ensemble des accès, credentials et API keys nécessaires au fonctionnement de l'infrastructure LEO.

---

## 1. 🔑 Accès SSH

| Cible | Méthode | Statut | Détail |
|-------|---------|--------|--------|
| **Root Leo** (host) | `ssh -i id_ed25519 root@100.92.102.28` | ✅ OK | Clé SSH installée dans `authorized_keys` |
| **tofdan** (host) | `tailscale ssh tofdan@...` | ⚠️ Pas testé | `TSec&6769` pour sudo |
| **Penguin** | `ssh tofdan@192.168.1.101` | ❌ Pas d'accès | Nécessite double SSH depuis host |
| **Yoga** | `ssh tofdan@192.168.1.100` | ❌ Pas d'accès | Nécessite double SSH depuis host |

---

## 2. 🐳 Docker

| Conteneur | Image | Ports | Statut |
|-----------|-------|-------|--------|
| `hermes-agent` | nousresearch/hermes-agent | host | ✅ --network host |
| `n8n` | n8nio/n8n | 5678 | ✅ HTTP 200 |
| `ollama` | ollama/ollama | 11434 | ✅ qwen2.5:7b |

**Socket Docker** : ✅ accessible (RW), permet contrôle total des conteneurs.

---

## 3. 🔐 API Keys & Tokens

### 3.1 DeepSeek
| Propriété | Valeur |
|-----------|--------|
| **Clé API** | ✅ stockée dans `.env` + `credentials_vault.json` |
| **Modèle principal** | `deepseek-v4-flash` (Pro si complexe) |
| **Solde** | $60.31 (au 30/06 — paiement PayPal $53 le 29/06) |
| **Compte PayPal source** | christophe.danhier@gmail.com |

### 3.2 Gemini (fallback)
| Propriété | Valeur |
|-----------|--------|
| **Clé API** | ✅ stockée dans `.env` |
| **Modèle** | `gemini-2.5-flash` |

### 3.3 Google (OAuth)
| Token | Scopes | Statut |
|-------|--------|--------|
| `leo_email_token.json` | Gmail (lire/modifier/envoyer) | ✅ Rafraîchi 30/06 |
| `leo_sheets_token.json` | Drive read + Sheets read | ✅ Rafraîchi 30/06 |
| `leo_drive_token.json` | Drive FULL | ✅ Rafraîchi 30/06 |
| `leo_google_token.json` | Drive (ancien) | ❌ Mort (invalid_grant) |
| `gdrive-service-account.json` | Drive (service account) | ⚠️ Lecture seule (quota 0) |
| `google_token.json` | Drive (ancien Christophe) | ❌ Mort |
| `leo_token.json` | Drive (ancien Léo) | ❌ Mort |

### 3.4 GitHub
| Token | Type | Statut |
|-------|------|--------|
| `ghp_REDACTED` | Classic (repo scope) | ✅ Actif |
| Clé SSH `id_ed25519` | Auth + push | ✅ Installée sur host + GitHub |

### 3.5 Telegram
| Bot | Token | Profil | Statut |
|-----|-------|--------|--------|
| Léo Hermes Agent | `881242...kMZM` | default | ✅ |
| Léo Copilot | `899720...JZN4` | leo-copilot | ✅ |
| Bavi Leo | `885780..._h58` | bavi-leo | ✅ |
| Bureau Émile | `(token Émile)` | emile | ✅ |

### 3.6 n8n
| Propriété | Valeur |
|-----------|--------|
| **URL** | `http://localhost:5678` |
| **Login** | leodanhier@proton.me |
| **Password** | `TwomdIxBHNEmLpEq` |
| **API Key** | Corrompue (dans secrets.txt) |
| **Workflows** | 6 actifs (Ping, Dashboard Watch, LEO Check, Alerte, Drive→Issue, Gardien) |

### 3.7 Cloudflare
| Propriété | Valeur |
|-----------|--------|
| **Zone ID** | `969d915e3eec860c23054cbf6267f52f` |
| **Token** | Stocké en session CodeWhale uniquement |
| **Tunnel ID** | `8f61e660-566a-4a4b-8925-db0e4b421ea3` |

---

## 4. 📧 Emails

| Compte | Usage | Accès |
|--------|-------|-------|
| `leodanhieria@gmail.com` | Envoi (Léo) | ✅ OAuth + IMAP (mot de passe app) |
| `christophe.danhier@gmail.com` | Lecture seule | ✅ IMAP (mot de passe app: `bdia qlej lqdl swtv`) |

**Règles :**
- Envoyer depuis `leodanhieria@gmail.com`
- CC `christophe.danhier@gmail.com`
- Signature : *Léo, assistant de Christophe*
- Ne JAMAIS envoyer depuis christophe.danhier

---

## 5. 🌐 Sites Web

| Site | URL | Statut |
|------|-----|--------|
| tofdan.be | https://tofdan.be | ✅ (via Cloudflare tunnel) |
| hermes-wiki | https://christophedanhier-hash.github.io/hermes-wiki | ✅ |

**Nginx** : sur l'hôte (pas dans Docker), port 80, SSL via Cloudflare.

---

## 6. 🔄 Fichiers sensibles (permissions)

| Fichier | Permissions | Statut |
|---------|-------------|--------|
| `/opt/data/.env` | 600 | ✅ |
| `profiles/*/.env` | 600 | ✅ |
| `credentials_vault.json` | 600 | ✅ |
| `*token*.json` | 600 | ✅ (google_token.json fixé) |
| `.ssh/id_ed25519` | 600 | ✅ |

---

## 7. 📊 Bilan des accès

| Accès | Statut | Bloquant ? |
|-------|--------|------------|
| SSH Root host | ✅ | — |
| Docker | ✅ | — |
| Gateways (4) | ✅ | — |
| n8n | ✅ (via docker exec) | ⚠️ API key corrompue |
| GDrive | ✅ (OAuth Drive FULL) | — |
| DeepSeek API | ✅ | — |
| Gemini API | ✅ | — |
| GitHub (HTTPS + SSH) | ✅ | — |
| Gmail (envoi) | ✅ | — |
| Cloudflare | ❌ Token en session CodeWhale | ⚠️ Pas accessible depuis Hermes |
| Machines distantes (Yoga/Penguin) | ❌ SSH non configuré | ⚠️ |

---

## 8. 🎯 Recommandations

1. **Récupérer token Cloudflare** depuis CodeWhale → stocker dans `credentials_vault.json`
2. **Configurer accès Yoga/Penguin** via SSH depuis le host
3. **Régénérer clé API n8n** dans l'interface n8n
4. **Nettoyer les tokens morts** (`google_token.json`, `leo_token.json`, `leo_google_token.json`) — conserver uniquement les tokens actifs
5. **Ajouter `--privileged`** au conteneur hermes-agent pour accès complet aux capacités système (backup disque 1To, accès /dev)

---

*Document mis à jour le 04/07/2026 — 00:00:00 — Léo 🦁*
