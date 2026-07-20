---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v5.0
modele: deepseek-v4-flash
tags: [hermes, guide, documentation, annexes, cli, crons, architecture, leo]
statut: ✅ À jour
type: guide
hide:
  - toc
---

> **Dernière mise à jour rédactionnelle :** 18/07/2026 à 13:00 — Léo 🦁

# Annexe A — Référence CLI Hermès

> Dernière mise à jour : 18/07/2026

---

## Installation et lancement

```bash
# Installer Hermes (méthode recommandée)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Lancer Hermes en mode interactif
hermes
# ou : hermes chat

# Lancer Hermes avec une requête directe (one-shot)
hermes chat -q "Ton message ici"

# Assistant de configuration interactif
hermes setup

# Choisir modèle/fournisseur
hermes model

# Vérifier l'état de l'installation
hermes doctor

# Afficher la configuration
hermes config
```

## Profils

```bash
# Lister les profils
hermes profile list

# Créer un profil (vide)
hermes profile create <nom>

# Créer un profil (cloner la config actuelle)
hermes profile create <nom> --clone

# Créer un profil (tout cloner)
hermes profile create <nom> --clone-all

# Utiliser un profil par défaut
hermes profile use <nom>

# Voir les détails d'un profil
hermes profile show <nom>

# Supprimer un profil
hermes profile delete <nom>

# Renommer un profil
hermes profile rename <ancien> <nouveau>

# Exporter un profil (tar.gz)
hermes profile export <nom>

# Importer un profil
hermes profile import <fichier>

# Créer un alias de commande (wrapper)
hermes profile alias <nom>

# Lister tous les profils avec leur statut
hermes profile list
```

## Gateways

```bash
# Démarrer un gateway (premier plan)
hermes gateway run

# Installer le gateway comme service (systemd)
hermes gateway install

# Démarrer le service gateway
hermes gateway start

# Arrêter le service gateway
hermes gateway stop

# Redémarrer le service gateway
hermes gateway restart

# Voir le statut
hermes gateway status

# Configurer les plateformes
hermes gateway setup
```

## Crons

```bash
# Lister tous les crons
hermes cron list

# Créer un cron (script) — no_agent
hermes cron create "0 6 * * *" "Script de backup" --script mon-script.sh

# Créer un cron (LLM)
hermes cron create "0 9 * * *" "Analyse les logs d'erreur"

# Créer avec un skill attaché
hermes cron create "every 1h" "Vérifie les flux RSS" --skill blogwatcher

# Voir le statut du scheduler
hermes cron status

# Modifier un cron
hermes cron edit <id> --schedule "every 4h"

# Forcer l'exécution
hermes cron run <id>

# Mettre en pause
hermes cron pause <id>

# Reprendre
hermes cron resume <id>

# Supprimer
hermes cron remove <id>
```

## Sessions

```bash
# Lister les sessions récentes
hermes sessions list

# Explorateur interactif de sessions
hermes sessions browse

# Exporter une session en JSONL
hermes sessions export <fichier>

# Renommer une session
hermes sessions rename <id> <titre>

# Supprimer une session
hermes sessions delete <id>

# Nettoyer les vieilles sessions
hermes sessions prune

# Statistiques du store de sessions
hermes sessions stats
```

## Skills

```bash
# Lister les skills installés
hermes skills list

# Chercher un skill dans le hub
hermes skills search <requête>

# Installer un skill depuis le hub
hermes skills install <id>

# Inspecter un skill sans l'installer
hermes skills inspect <id>

# Configurer les skills par plateforme
hermes skills config

# Vérifier les mises à jour
hermes skills check

# Mettre à jour les skills obsolètes
hermes skills update

# Désinstaller un skill du hub
hermes skills uninstall <id>

# Parcourir tous les skills disponibles
hermes skills browse
```

## Outils (Toolsets)

```bash
# Interface interactive d'activation/désactivation
hermes tools

# Lister tous les outils et leur statut
hermes tools list

# Activer un toolset
hermes tools enable <nom>

# Désactiver un toolset
hermes tools disable <nom>
```

## Serveurs MCP

```bash
# Ajouter un serveur MCP
hermes mcp add <nom> --url <url>
hermes mcp add <nom> --command <cmd>

# Liste des serveurs configurés
hermes mcp list

# Tester la connexion
hermes mcp test <nom>

# Supprimer un serveur
hermes mcp remove <nom>
```

## Credential Pools (Auth)

```bash
# Gestionnaire interactif de credentials
hermes auth

# Ajouter un credential OAuth ou API
hermes auth add <provider>

# Lister les credentials
hermes auth list

# Supprimer un credential
hermes auth remove <provider> <index>

# Réinitialiser l'état d'épuisement
hermes auth reset <provider>
```

## Configuration

```bash
# Voir la configuration actuelle
hermes config

# Éditer config.yaml dans l'éditeur
hermes config edit

# Modifier un paramètre
hermes config set <chemin> <valeur>

# Voir le chemin de config.yaml
hermes config path

# Voir le chemin du fichier .env
hermes config env-path

# Vérifier les options manquantes
hermes config check

# Mettre à jour la config avec les nouvelles options
hermes config migrate
```

## Mise à jour et maintenance

```bash
# Mettre à jour Hermes
hermes update

# Désinstaller Hermes
hermes uninstall

# Voir les logs du gateway
hermes logs

# Dashboard web
hermes dashboard

# Statistiques d'utilisation (tokens/coût)
hermes insights

# Curateur de skills (maintenance automatique)
hermes curator status

# Kanban (file de travail multi-agent)
hermes kanban list
```

## Commandes Slash (en session interactive)

```bash
/new           Session fraîche
/retry         Renvoyer la dernière requête
/undo          Annuler le dernier échange
/title [nom]   Nommer la session
/model         Changer de modèle
/skill <nom>   Charger un skill
/tools         Gérer les outils
/cron          Gérer les crons
/yolo          Contourner l'approbation
/help          Liste complète des commandes
/quit          Quitter
```

## Syntaxe cron rapide

```text
* * * * *
│ │ │ │ │
│ │ │ │ └── Jour semaine (0-7, 0=dim)
│ │ │ └──── Mois (1-12)
│ │ └────── Jour mois (1-31)
│ └──────── Heure (0-23)
└────────── Minute (0-59)

Exemples :
0 6 * * *      → Tous les jours à 06:00
0 */4 * * *    → Toutes les 4h
0 8 * * 1      → Tous les lundis à 08:00
30m            → Toutes les 30 minutes
every 2h       → Toutes les 2 heures (langage naturel)
every monday 9am → Tous les lundis à 9h
```

---

# Annexe B — L'architecture LEO — Exemple concret

LEO est l'assistant personnel de Christophe. Cette section détaille son architecture pour servir d'exemple à ceux qui veulent construire le leur.

## Identité

```text
Nom : LEO
Type : Majordome numérique
Hôte : Linux (Debian-like)
Canal principal : Telegram
Profils : 1 seul (default)
```

## Providers LLM

| Provider | Rôle | Coût |
|----------|------|------|
| DeepSeek 🤖 | Principal (Telegram, conversations, tâches complexes) | Payant (solde sur dashboard) |
| Ollama 🏠 | Local, gratuit (batch, traitement bulk, qwen2.5:7b) | Gratuit (CPU) |
| Gemini ⚡ | Fallback automatique | Gratuit (quota API) |

## Communications

LEO communique uniquement par **Telegram** (pas d'autre canal). L'email est utilisé **en sortie uniquement** (LEO peut envoyer des emails depuis `leodanhieria@gmail.com`, mais ne reçoit pas de consignes par email).

## Tâches quotidiennes

### Crons (44 actifs — 39 crons Hermes + 6 watchdogs)

> **Note mise à jour v5.0 :** Le système de crons est passé à **39 crons Hermes + 6 watchdogs** depuis la version v4.0 du guide. Les watchdogs (code-server, tunnels, auto-heal) sont intégrés comme crons Hermes.

| Cron | Horaire | Type | Coût | Description |
|------|---------|------|------|-------------|
| `🌍 Global Dashboard` | **H:05** | 🔧 Script | **0$** | Portail unique monitoring consolidé |
| `machines-kpi` | **H:00** | 🔧 Script | **0$** | Collecte CPU/RAM/disque 3 machines |
| `budget-check-v6` | **H:05** | 🔧 Script | **0$** | Relevé solde DeepSeek + projection |
| `leo-dashboard` | ***/15** | 🔧 Script | **0$** | Dashboard central LEO (4 onglets, 20 KPI, 4 charts) |
| `leo-metrics` | **H:15** | 🔧 Script | **0$** | Dashboard 3 machines |
| `crons-dashboard` | **H:20** | 🔧 Script | **0$** | Monitoring de tous les crons (consolidé dans leo-dashboard) |
| `github-dashboard` | **H:25** | 🔧 Script | **0$** | Activité GitHub (repos Hermes vs Dev) |
| `wiki-sync` | **H:30** | 🔧 Script | **0$** | Synchronisation sources → Wiki MkDocs |
| `bavi-leo-dashboard` | H:05 | 🔧 Script | **0$** | Dashboard KPIs BAVI LEO |
| `dashboard-n8n` | */15 | 🔧 Script | **0$** | Dashboard monitoring n8n |
| `n8n-healthcheck` | */15 | 🔧 Script | **0$** | Ping n8n API |
| `dashboard-watch` | 30 */2 | 🔧 Script | **0$** | Surveillance dashboards + budget ✅ |
| `daily-backup` | 06:00 | 🔧 Script | **0$** | Backup fichiers critiques |
| `drive-sync` | 18:00 | 🔧 Script | **0$** | Sync Drive ↔ GitHub |
| `credentials-check` | Lun 09:00 | 🔧 Script | **0$** | Vérification tokens OAuth |
| `doc-watch-auto` | 00/06/12/18 | 🔧 Script | **0$** | Surveillance docs 5 wikis |
| `Classifieur emails` | 30m | 🧠 Ollama | **0$** 🏠 | Classification Gmail |
| Veille IA (phase 1) | 07:30 | 🔧 Script | **0$** | Collecte RSS 11 sources |
| Veille IA (phase 2) | 08:00 | 🤖 DeepSeek | ~0.05$ | Analyse + email Cowork |
| `check-hermes-update` | 09:00 | 🔧 Script | **0$** | Vérification nouvelle version Hermes |
| `🛡️ Auto-Heal` | **H:45** | 🧠 Agent | **0$** | Détection + correction auto des erreurs |
| `watchdog-code-server` | **\\*/5** | 🔧 Script | **0$** | Relance code-server si arrêté |
| `watchdog-code-server-tunnel` | **\\*/5** | 🔧 Script | **0$** | Maintient le tunnel SSH code-server |

**>95% des crons sont en no_agent** (zéro DeepSeek consommé par les tâches planifiées).

### Workflows n8n (obsolète depuis v5.0 — conservé pour référence historique)

> ⚠️ **Obsolète depuis la v5.0 (18/07/2026).** n8n a été déprécié au profit d'une gestion de crons entièrement unifiée dans Hermes. Les workflow listés ci-dessous sont fournis à titre historique uniquement.

Depuis juin 2026, certains crons critiques étaient **doublés dans n8n** pour bénéficier du retry natif :

| Workflow n8n | Horaire | Rôle | Redondance |
|-------------|---------|------|------------|
| `💰 Budget Check` | H:05 | Appel DeepSeek API → webhook → budget.json | ⚡ Retry 3x + backup Hermes |
| `🛡️ Dashboard Watch v2` | 30min | Ping 6 dashboards HTTP | ⚡ Retry 3x + backup Hermes (2h) |

**Pattern historique :** n8n = exécution garantie (retry) / Hermes = backup si n8n down. Double filet.

**Décision de dépréciation :** La complexité de maintenir deux systèmes (n8n + Hermes crons) ne justifiait plus le bénéfice marginal. Hermes gère désormais les retries et le monitoring directement. Les scripts n8n ont été migrés vers des crons Hermes.

### Dashboard (1)

| Dashboard | Technologie | Màj | Lien |
|-----------|-------------|-----|------|
| 🦁 **LEO Dashboard** | HTML + Chart.js (4 onglets) | */15 | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) |

Tous les scripts de déploiement incluent :
- `--allow-empty` + `run_id` dans le footer pour éviter "nothing to commit"
- Force-push fallback si le push est rejeté
- **Rebuild GH Pages API** après push (CDN forcé)
- Validation des clés `budget.json` au déploiement

---

## Règles de fonctionnement

### 1. Règle #1 : Réfléchir avant d'agir

Avant chaque action impliquant un choix technique, identifier 2-3 approches, peser le pour/contre, choisir la meilleure. La précipitation est la première cause d'erreur.

### 2. Arbitrage LLM (3 niveaux)

```text
Tâche → Script pur ? → no_agent (0 token)
       → A besoin d'un LLM ? → Ollama (gratuit)
                              → Gemini (fallback)
                              → DeepSeek (payant, premium)
       → Jamais sacrifier la qualité pour économiser
```

### 3. Anti-régression

- **1 envoi max** — email ou action : UNE SEULE tentative
- **Pas de réessai** après échec sans accord explicite
- **Corrections → skills** (pas en mémoire passagère)
- **Zéro répétition** — réponse concise, pas de blabla

### 4. Un seul profil

LEO a vécu la perte d'accès Telegram lors d'un basculement de profil. Leçon apprise : **un seul profil principal (default), des profils spécialisés pour les tâches dédiées**.

### 5. Sécurité email

- Envoi UNIQUEMENT depuis `leodanhieria@gmail.com`
- JAMAIS depuis `christophe.danhier@gmail.com`
- Christophe TOUJOURS en CC
- Si erreur : STOP net, ne pas réessayer

### 6. Crons : no_agent par défaut

Tout nouveau cron doit être **no_agent** sauf justification explicite. Les crons LLM coûtent de l'argent ; les scripts purs sont gratuits et plus fiables.

---

## Structure des fichiers

```text
~/Projets_Dev/
├── config.yaml           → Configuration Hermes
├── .env                  → Variables d'environnement (clés API)
├── google_token.json     → Token OAuth Google
├── hermes-backup.py      → Script de backup
├── deploy_dashboard.py   → Script déploiement dashboard KPI
├── deploy_machines.py    → Script déploiement métriques machines
├── update_budget_v6.py   → Script relevé budget DeepSeek
├── update_machines_kpi.py→ Script collecte métriques machines
└── scripts/
    ├── run-backup.sh
    ├── run-budget.sh
    ├── run-machines-kpi.sh
    ├── run-dashboard.sh
    ├── run-leo-metrics.sh
    ├── run-crons-dashboard.sh
    └── deploy-crons-dashboard.py
```

---

## Leçons apprises

### 12/06/2026 — Trop de profils

**Problème :** Création d'un profil `local` pour Ollama. Arrêt du gateway `local` = perte d'accès Telegram.

**Solution :** Structurer les profils par domaine (default/leo-copilot/bavi-leo), Ollama par API directe. Fiabilité > flexibilité.

### 13/06/2026 — Précipitation

**Problème :** Actions sans réflexion préalable = régressions (mauvais token, erreur OAuth, envoi multiple d'email).

**Solution :** Règle #1 : réfléchir avant d'agir. Toujours.

### 14/06/2026 — Crons instables

**Problème :** Crons qui utilisaient le mauvais Python, scripts introuvables, identité Git manquante, push qui échoue.

**Solution :** Uniformisation : wrappers shell + no_agent + identité Git et token dans le script.

---

> Inspirez-vous, ne copiez pas. LEO est taillé sur mesure pour Christophe. Votre assistant aura ses propres besoins, règles et personnalité. Prenez ce qui vous est utile, adaptez le reste.

---
*Fin de l'annexe — 07-annexes-cli.md — Hermès pour les Nuls 🦁 v5.0*

---

*Document mis à jour le 18/07/2026 à 13:00 — Léo 🦁 | v5.0*

> 🤖 Dernier audit : 20/07/2026 à 07:26 (UTC+2)

