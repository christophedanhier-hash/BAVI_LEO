---
date: 2026-06-20
bureau: bureau-michel
version: v1
modele: deepseek-v4-pro
tags: [n8n, installation, docker, rapport]
statut: finalise
---

# Étude d'Installation — n8n sur LEO
**Bureau :** Michel 🔧  
**Date :** 20 juin 2026  
**Experts :** SysAdmin · Networker · DataDoc  
**Modèle :** DeepSeek Pro

---

## 1. Résumé exécutif

Ce rapport étudie l'installation de **n8n** (plateforme d'automatisation workflow open source, v2.27.1 stable) sur le serveur **LEO** — Debian 13 (trixie) hébergeant déjà Hermes Agent, Ollama et Tailscale.

**Conclusion :** L'installation est **faisable immédiatement** avec un niveau de risque faible. La méthode **Docker (`network=host`)** est recommandée pour sa simplicité opérationnelle, son isolation, sa faible empreinte mémoire (~300–500 Mo RAM) et sa maintenance quasi nulle. Deux scripts de déploiement sont déjà prêts dans `/opt/data/n8n/`.

La seule contrainte technique identifiée est un **bug de routage Docker NAT ↔ Tailscale** impactant certains appels API internes (login POST 401) — sans conséquence pour l'usage normal via navigateur. Un SSH tunnel ou l'IP locale contourne le problème si nécessaire.

| Métrique | Valeur |
|:---------|:-------|
| Méthode retenue | Docker (`--network host`) |
| Port | 5678 (libre) |
| Base de données | SQLite (intégrée, volume Docker) |
| Stockage persisté | Volume Docker `n8n_data` |
| Redémarrage auto | `--restart unless-stopped` |
| Accès réseau | `http://100.92.102.28:5678` (Tailscale) |
| Temps estimé déploiement | 5 minutes |
| Risque global | **Faible** |

---

## 2. Options d'installation — Tableau comparatif

| Critère | **A — Docker `--network host`** (recommandée) | **B — Docker bridge (`-p 5678:5678`)** | **C — npm local** |
|:--------|:----------------------------------------------|:---------------------------------------|:------------------|
| **Isolation** | ✅ Conteneur, réseau hôte | ✅ Conteneur, bridge Docker | ❌ Process hôte (pas d'isolation) |
| **Port utilisé** | 5678 direct (hôte) | 5678 → 5678 (docker-proxy) | 5678 direct |
| **Dépendances** | Docker Engine v26.1.5 | Docker Engine v26.1.5 | Node.js v22.22.3 + npm |
| **RAM additionnelle** | ~300–500 Mo | ~300–500 Mo | ~250–400 Mo |
| **Stockage image** | ~307 Mo (image) + données | ~307 Mo (image) + données | ~200–400 Mo (node_modules) |
| **Mise à jour** | `docker pull` + recreate | `docker pull` + recreate | `npm update n8n` |
| **Redémarrage après reboot** | ✅ `--restart unless-stopped` | ✅ `--restart unless-stopped` | ⚠️ Watchdog cron nécessaire |
| **Bug Docker NAT / login 401** | ✅ **Absent** (pas de docker-proxy) | ❌ **Présent** (docker-proxy intermédiaire) | ✅ Absent (pas de Docker) |
| **Accès depuis Tailscale** | ✅ Direct 100.92.102.28:5678 | ⚠️ Via docker-proxy (bug possible) | ✅ Direct |
| **Compatibilité Hermes co-hébergé** | ✅ Aucun conflit (ports disjoints : 5678 vs 11434/18791/18792) | ✅ Aucun conflit | ✅ Aucun conflit |
| **Sauvegarde** | Volume Docker | Volume Docker | Backup fichier |
| **Scripts existants** | ✅ `run-n8n.sh` + `update-n8n.sh` | ❌ À adapter | ❌ Scripts watchdog seulement |
| **Maintenance** | **Très faible** | **Faible** | **Moyenne** (watchdog, logs, mises à jour npm) |
| **Risque** | **Très faible** | **Faible** (bug login 401 contournable) | **Moyen** (pas d'isolation, pas de restart policy) |

### Justification du choix A

Le mode `--network host` est le meilleur compromis pour LEO :

1. **Absence du bug Docker NAT** — En mode host, le conteneur partage la pile réseau de l'hôte. Pas de docker-proxy, donc pas d'altération des requêtes POST entrantes. Le login API fonctionne aussi bien via `localhost` que via l'IP Tailscale.
2. **Pas de conflit de ports** — 5678 est libre. Hermes utilise 18791/18792, Ollama utilise 11434. Aucun overlap.
3. **Simplicité maximale** — Un seul `docker run` sans configuration réseau complexe.
4. **Restart policy native** — Docker gère le redémarrage après reboot sans besoin de systemd ou watchdog.

---

## 3. Analyse réseau et compatibilité stack

### 3.1 Topologie réseau actuelle

```
Internet / Tailnet
       │
       ▼
  ┌───────────────────────────────────┐
  │        LEO — Debian 13           │
  │  Tailscale IP: 100.92.102.28     │
  │  Réseau Docker: 172.17.0.0/16    │
  │                                   │
  │  ┌─────────┐  ┌──────────┐       │
  │  │ Ollama  │  │ Hermes   │       │
  │  │ :11434  │  │ :18791   │       │
  │  └─────────┘  │ :18792   │       │
  │               └──────────┘       │
  │                                   │
  │  ┌─────────────────────────┐     │
  │  │  n8n (--network host)   │     │
  │  │  Port 5678              │     │
  │  │  SQLite: volume n8n_data│     │
  │  └─────────────────────────┘     │
  └───────────────────────────────────┘
```

### 3.2 Ports occupés vs libres

| Port | Service | Statut |
|:----|:--------|:-------|
| 11434 | Ollama | **Occupé** |
| 18791 | Hermes Agent | **Occupé** |
| 18792 | Hermes Agent | **Occupé** |
| **5678** | **n8n (cible)** | **✅ Libre** |
| 80 | HTTP | Libre |
| 443 | HTTPS | Libre |
| 3000 | — | Libre |
| 8080 | — | Libre |
| 8443 | — | Libre |

**Aucun conflit de ports avec la stack existante.**

### 3.3 Chemin d'accès utilisateur

**Recommandé :** L'utilisateur accède à n8n via `http://100.92.102.28:5678` depuis son navigateur (n'importe quel nœud du tailnet). Le trajet est direct : navigateur → Tailscale → host LEO → n8n conteneur. Pas de rebouclage Docker, pas de TLS à gérer (le tailnet est déjà chiffré).

**Via Tailscale Serve (optionnel) :** Exposition Funnel ou Serve avec sous-chemin :
```bash
sudo tailscale serve --bg --set-path=/n8n 5678
# → https://leo.tailnet-name.ts.net/n8n
```

### 3.4 Bug connu : login POST 401 via Docker NAT

**Contexte :** Si l'option B (bridge Docker, `-p 5678:5678`) était utilisée, le docker-proxy altère le body des requêtes POST, faisant échouer la comparaison bcrypt sur `/rest/login`. Seul le login est impacté — GET et le reste de l'API fonctionnent.

**Solution :** Utiliser l'option A (`--network host`) élimine ce problème. Si, pour une raison quelconque, le mode bridge devait être utilisé, les contournements sont :
- SSH tunnel : `ssh -L 5678:localhost:5678 leo` puis navigateur → `http://localhost:5678`
- Appels API via `localhost` ou `172.17.0.2` depuis l'intérieur du tailnet
- Accès navigateur direct depuis un nœud Tailscale **externe** (non concerné par le bug)

---

## 4. Prérequis détaillés

### 4.1 Système

| Composant | Requis | LEO | Conforme |
|:----------|:-------|:----|:---------|
| OS | Linux (Debian/Ubuntu) | Debian 13 (trixie) | ✅ |
| Architecture | x86_64 / arm64 | x86_64 | ✅ |
| RAM | ≥ 1 Go (mini), ≥ 4 Go (prod légère) | 22.94 Go | ✅ |
| Disque libre | ≥ 10 Go | 371 Go | ✅ |
| Docker Engine | ≥ 20.10 | v26.1.5 | ✅ |
| Docker Compose | Recommandé (non requis pour option A) | **Absent** | ⚠️ Non bloquant |
| Node.js | ≥ 18 (option C uniquement) | v22.22.3 | ✅ (non requis) |
| GPU (optionnel) | NVIDIA pour AI nodes | RTX 3050, CUDA 13.2 | ✅ |

### 4.2 Réseau

| Condition | Statut |
|:----------|:-------|
| Port 5678 libre | ✅ Libre |
| Accès Tailscale à LEO | ✅ 100.92.102.28 |
| Résolution DNS tailnet | ✅ Fonctionnelle |
| Latence tailnet | < 5 ms (serveur local) |

### 4.3 Docker Engine — Vérification

```bash
docker --version
# Docker version 26.1.5

docker info --format '{{.Driver}}'
# overlay2 (OK)

docker system df
# Vérifier l'espace utilisé par les images existantes
```

**Note :** Docker Compose (`docker compose` ou `docker-compose`) n'est pas installé sur LEO. **Ce n'est pas un blocage** — la méthode recommandée utilise `docker run` seul, sans Compose. L'absence de Compose est un argument supplémentaire pour privilégier l'option A (simple `docker run`).

---

## 5. Procédure recommandée (pas à pas)

### 5.1 Préparation

```bash
# Connexion à LEO (depuis le poste d'administration)
ssh leo@100.92.102.28

# Vérifier que le port 5678 est libre
ss -tlnp | grep 5678 || echo "✅ Port 5678 libre"

# Créer le volume persistant (une seule fois)
docker volume create n8n_data

# Vérifier
docker volume inspect n8n_data --format '{{.Mountpoint}}'
# /var/lib/docker/volumes/n8n_data/_data
```

### 5.2 Lancement du conteneur

```bash
# Définir les variables
IMAGE="docker.n8n.io/n8nio/n8n:latest"
CONTAINER_NAME="n8n"
VOLUME_NAME="n8n_data"
TAILSCALE_IP="100.92.102.28"

# Pull de l'image
docker pull "$IMAGE"

# Lancement
docker run -d \
  --name "$CONTAINER_NAME" \
  --restart unless-stopped \
  --network host \
  -e N8N_SECURE_COOKIE=false \
  -e N8N_HOST="$TAILSCALE_IP" \
  -e N8N_PROTOCOL=http \
  -e N8N_PORT=5678 \
  -e N8N_LISTEN_ADDRESS=0.0.0.0 \
  -e N8N_PROXY_HOPS=0 \
  -e WEBHOOK_URL="http://$TAILSCALE_IP:5678/" \
  -e N8N_RUNNERS_ENABLED=true \
  -e GENERIC_TIMEZONE=Europe/Paris \
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
  -v "$VOLUME_NAME":/home/node/.n8n \
  "$IMAGE"
```

### 5.3 Vérification

```bash
# Conteneur en cours d'exécution ?
docker ps --filter name=n8n --format 'table {{.Names}}\t{{.Status}}'

# n8n répond ?
curl -s -o /dev/null -w "%{http_code}" http://localhost:5678/
# Devrait retourner 200 (page HTML) ou 302 (redirect)

# Healthcheck
curl -s http://localhost:5678/healthz
# {"status":"ok"}

# Logs
docker logs n8n -n 20
```

### 5.4 Première connexion

1. Navigateur → `http://100.92.102.28:5678`
2. Créer le compte propriétaire (email + mot de passe)
3. Configurer les préférences (timezone Europe/Paris, etc.)
4. **(Optionnel)** Désactiver l'interface AI si souhaité (voir §7.5)

### 5.5 Scripts automatisés (déjà présents)

Deux scripts sont déjà disponibles dans `/opt/data/n8n/` :

- **`run-n8n.sh`** — Déploiement complet (pull + création du volume + lancement)
  ```bash
  cat /opt/data/n8n/run-n8n.sh | ssh leo@100.92.102.28 bash
  ```

- **`update-n8n.sh`** — Mise à jour (backup SQLite + pull + recreate)
  ```bash
  cat /opt/data/n8n/update-n8n.sh | ssh leo@100.92.102.28 bash
  ```

Ces scripts sont utilisables directement depuis le poste d'administration.

---

## 6. Plan de déploiement progressif (phases)

### Phase 1 — Installation initiale (T0, 5 min)

| Action | Durée | Responsable |
|:-------|:------|:------------|
| Vérifier prérequis (port, Docker) | 30 s | DataDoc |
| Créer volume Docker `n8n_data` | 10 s | SysAdmin |
| Pull image n8n:latest (~307 Mo) | 1 min | SysAdmin |
| Lancer conteneur (docker run) | 10 s | SysAdmin |
| Vérifier conteneur + healthz | 20 s | SysAdmin |
| Créer compte propriétaire web | 2 min | DataDoc |
| **Total** | **~4 min** | |

### Phase 2 — Configuration de base (T0+15 min)

| Action | Durée | Détails |
|:-------|:------|:--------|
| Configurer timezone / préférences | 2 min | Europe/Paris |
| Créer une clé API n8n | 1 min | Via interface web |
| Configurer Tailscale Serve (optionnel) | 2 min | `sudo tailscale serve --bg --set-path=/n8n 5678` |
| Désactiver télémétrie / PostHog | 2 min | Voir §7.5 |
| Créer workflow test (webhook → log) | 5 min | Validation fonctionnelle |
| **Total** | **~12 min** | |

### Phase 3 — Tests de validation (T0+30 min)

| Test | Critère | Méthode |
|:-----|:--------|:--------|
| Accessibilité HTTP | ✅ 200/302 sur :5678 | `curl -w "%{http_code}" http://localhost:5678/` |
| Healthcheck | ✅ `{"status":"ok"}` | `curl http://localhost:5678/healthz` |
| Login web | ✅ Formulaire visible | Navigateur |
| Webhook sortant | ✅ Workflow s'exécute | Test webhook avec Request Bin |
| Redémarrage conteneur | ✅ n8n réponde après `docker restart` | `docker restart n8n` + healthcheck |
| Reboot simulé | ✅ n8n démarre après reboot | `docker stop n8n` + `docker start n8n` |
| Persistance données | ✅ Workflows conservés | Après restart |
| Accès Tailscale | ✅ Réponse sur 100.92.102.28:5678 | Depuis un autre nœud du tailnet |

### Phase 4 — Durcissement et maintenance (T0+1h, continu)

- Configurer une rotation des logs Docker
- Mettre en place une sauvegarde périodique du volume `n8n_data`
- Documenter les accès et clés API dans le coffre du Bureau Michel

---

## 7. Risques et mitigations

| Risque | Probabilité | Impact | Mitigation |
|:-------|:------------|:-------|:-----------|
| **Perte de données (volume)** | Faible | Élevé | Backup régulier du volume Docker `n8n_data` → copie vers `/opt/data/backups/` |
| **Bug login 401 via Docker NAT** | N/A (option A) | N/A | Éliminé par `--network host`. Si bridge, utiliser SSH tunnel |
| **Mise à jour cassante** | Faible | Moyen | Script `update-n8n.sh` fait backup SQLite avant pull. Vérifier les breaking changes sur github.com/n8n-io/n8n |
| **Consommation mémoire** | Faible | Faible | n8n+Node utilise ~300 Mo. LEO a 22.94 Go. Marge confortable |
| **Exposition du port 5678** | Faible | Moyen | Le réseau est Tailscale (chiffré, authentifié). Pas d'exposition Internet public |
| **Co-hébergement avec Hermes** | Très faible | Faible | Pas de conflit de ports. Hermes et n8n partagent la RAM — suffisante |
| **Cache navigateur AI-first** | Moyen | Faible | Désactiver via `N8N_ENV_FEAT_026_easy_ai_workflow=control` (voir §5.4) |

### 7.1 Plan de sauvegarde

```bash
# Script de sauvegarde du volume n8n (à exécuter périodiquement)
BACKUP_DIR="/opt/data/backups/n8n"
mkdir -p "$BACKUP_DIR"
DATE=$(date +%Y%m%d_%H%M%S)

# Sauvegarde via tar dans un conteneur temporaire
docker run --rm -v n8n_data:/source -v "$BACKUP_DIR":/backup alpine \
  tar czf "/backup/n8n_data_$DATE.tar.gz" -C /source .

# Conservation : 7 sauvegardes glissantes
ls -t "$BACKUP_DIR"/n8n_data_*.tar.gz | tail -n +8 | xargs -r rm
```

---

## 8. Maintenance et mise à jour

### 8.1 Mise à jour de n8n

```bash
# Via le script existant (recommandé)
cat /opt/data/n8n/update-n8n.sh | ssh leo@100.92.102.28 bash

# Ou manuellement
docker pull docker.n8n.io/n8nio/n8n:latest
docker stop n8n && docker rm n8n
docker run -d \
  --name n8n \
  --restart unless-stopped \
  --network host \
  -e N8N_SECURE_COOKIE=false \
  -e N8N_HOST="100.92.102.28" \
  -e N8N_PROTOCOL=http \
  -e N8N_PORT=5678 \
  -e WEBHOOK_URL="http://100.92.102.28:5678/" \
  -e N8N_RUNNERS_ENABLED=true \
  -e GENERIC_TIMEZONE=Europe/Paris \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n:latest
```

### 8.2 Logs

```bash
docker logs n8n -n 50          # Dernières lignes
docker logs n8n -f             # Follow temps réel
docker logs n8n --since 1h     # Dernière heure
```

### 8.3 Arrêt / redémarrage

```bash
docker stop n8n                # Arrêt propre
docker start n8n               # Redémarrage
docker restart n8n             # Redémarrage rapide
docker exec -it n8n sh         # Shell interactif dans le conteneur
```

### 8.4 Surveillance

```bash
# Script de vérification existant
/opt/data/skills/infrastructure/system-management/scripts/check-n8n.sh

# Ou directement
curl -sf http://localhost:5678/healthz || docker restart n8n
```

### 8.5 Fréquence recommandée des opérations

| Opération | Fréquence |
|:----------|:----------|
| Mise à jour n8n | Mensuelle (ou avant chaque breaking change) |
| Sauvegarde volume | Hebdomadaire |
| Rotation logs Docker | Mensuelle (ou selon taille) |
| Vérification santé | Continue (watchdog ou docker healthcheck) |
| Revue des workflows | Trimestrielle |

---

## 9. Recommandation finale

### Décision : **Mise en production approuvée** ✅

**Méthode retenue : Docker `--network host` (option A)**

Justification technique :

1. **Disponibilité immédiate** — Tous les prérequis sont déjà satisfaits. Docker Engine v26.1.5, port 5678 libre, RAM et disque largement suffisants.
2. **Risque minimal** — Absence de conflit avec la stack existante (Hermes sur 18791/18792, Ollama sur 11434). Le mode `--network host` élimine le seul bug connu (login 401 via docker-proxy).
3. **Maintenance quasi nulle** — Restart policy native, mise à jour en une commande (`update-n8n.sh`), volume persisté.
4. **Scripts prêts** — Deux scripts opérationnels dans `/opt/data/n8n/` : `run-n8n.sh` (déploiement) et `update-n8n.sh` (mise à jour).
5. **Levier AI potentiel** — GPU NVIDIA RTX 3050 disponible pour les workflows utilisant des modèles IA locaux via Ollama (déjà présent sur :11434).

### Actions immédiates (T0)

```bash
# 1. Connexion à LEO
ssh leo@100.92.102.28

# 2. Déploiement (via script existant ou docker run)
docker volume create n8n_data
docker pull docker.n8n.io/n8nio/n8n:latest
docker run -d --name n8n --restart unless-stopped --network host \
  -e N8N_SECURE_COOKIE=false -e N8N_HOST=100.92.102.28 \
  -e N8N_PROTOCOL=http -e N8N_PORT=5678 -e N8N_LISTEN_ADDRESS=0.0.0.0 \
  -e N8N_PROXY_HOPS=0 -e WEBHOOK_URL=http://100.92.102.28:5678/ \
  -e N8N_RUNNERS_ENABLED=true -e GENERIC_TIMEZONE=Europe/Paris \
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n:latest

# 3. Vérification
curl -w "\n%{http_code}" http://localhost:5678/healthz
# Attendu : {"status":"ok"} suivi de 200
```

### Plan d'action recommandé

| Ordre | Action | Qui |
|:------|:-------|:----|
| 1 | Exécuter `run-n8n.sh` sur LEO | SysAdmin |
| 2 | Créer compte propriétaire sur `http://100.92.102.28:5678` | DataDoc |
| 3 | Configurer clé API + désactiver PostHog/IA | DataDoc |
| 4 | Créer workflow test (webhook + log) | DataDoc |
| 5 | Documenter les identifiants dans le coffre du Bureau | DataDoc |
| 6 | Planifier sauvegarde hebdomadaire du volume | SysAdmin |

---

## Versions

| Version | Date | Description |
|:--------|:-----|:------------|
| v1 | 20/06/2026 | Version initiale — Étude d'installation n8n sur LEO |

---

**Rapport produit par le Bureau Michel (DataDoc — DeepSeek Pro)**  
**Experts contributeurs :** SysAdmin (analyse système et Docker) · Networker (analyse réseau et routage) · DataDoc (synthèse, rédaction, recommandation)  
**Prochaine revue :** 20 juillet 2026 (M+1 après déploiement)

---
*Document mis à jour le 04/07/2026 — 22:48:00 — Léo 🦁*
