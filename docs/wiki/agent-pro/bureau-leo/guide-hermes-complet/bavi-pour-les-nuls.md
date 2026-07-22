---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v2.0
modele: deepseek-v4-flash
tags: [bavi, leo, architecture, bureaux, bots, skills, hermes, crons, dashboard, gateway, pour-les-nuls, notebooklm]
statut: ✅ Nouveau
type: guide
hide:
  - toc
---

> **Dernière mise à jour redactionnelle :** 18/07/2026 a 14:30 - Leo 🦁
> **Usage :** Document source pour Google NotebookLM (presentation BAVI LEO v2)

# BAVI LEO pour les Nuls — Guide complet

## 1. Qu'est-ce que BAVI LEO ?

BAVI = **Bureaux Agentiques Virtuels - Intelligence**. C'est un ecosysteme complet qui transforme un assistant IA classique en une **equipe de 10 experts numeriques** specialises, chacun avec son role, ses outils, ses procedures, et ses canaux de communication.

Imaginez une entreprise ou :
- Chaque employe (bureau) est un expert dans son domaine
- Tous les employes communiquent entre eux via 5 standards (bots Telegram)
- Les procedures sont ecrites dans des fichiers (skills) : lisibles, versionnees, reutilisables
- Les taches recurrentes sont automatisees (crons) : personne ne doit rien demander
- Tout est visible en temps reel (dashboards)
- Rien ne se perd (GitHub, memoire persistante)

**L'innovation** : ce n'est pas un chatbot ameliore. C'est un **systeme d'exploitation pour agent IA** — une maniere de structurer, organiser et automatiser l'intelligence artificielle.

---

## 2. L'architecture complete

### 2.1 Vue d'ensemble

```text
                    ☀️ CHRISTOPHE (l'humain)
                            │
                    ┌───────┴───────┐
                    │               │
            [Telegram]         [Emails]
                    │               │
                    ▼               ▼
            ┌─────────────────────────────────┐
            │     GATEWAY HERMES (s6)         │
            │  8 profils, 5 bots Telegram     │
            │  Supervision + auto-restart      │
            └────────┬────────────────────────┘
                     │
          ┌──────────┼──────────┬──────────┐
          ▼          ▼          ▼          ▼
    ┌─────────┐ ┌─────────┐ ┌────────┐ ┌────────┐
    │ default │ │ michel │ │bavi-leo│ │ emile  │
    │  LEO    │ │ Michel  │ │ Sylvia │ │Pedago  │
    │ Flash   │ │V4 Pro   │ │ Flash  │ │Flash+GM│
    └────┬────┘ └────┬────┘ └───┬────┘ └───┬────┘
         │           │          │           │
         └───────────┼──────────┼───────────┘
                     ▼          ▼
            ┌──────────────────────────┐
            │     10 BUREAUX BAVI     │
            │  ┌────────────────────┐  │
            │  │  130+ SKILLS       │  │
            │  │  Procedures .md    │  │
            │  └────────────────────┘  │
            │  ┌────────────────────┐  │
            │  │  39 CRONS + 6 WD  │  │
            │  │  Tâches auto      │  │
            │  └────────────────────┘  │
            │  ┌────────────────────┐  │
            │  │  3 DASHBOARDS     │  │
            │  │  KPI temps réel   │  │
            │  └────────────────────┘  │
            │  ┌────────────────────┐  │
            │  │  MEMOIRE PERSIST.  │  │
            │  │  Sessions/Contextes│  │
            │  └────────────────────┘  │
            └──────────────────────────┘
                     │
                     ▼
            ┌────────────────────┐
            │    PROVIDERS LLM   │
            │ DeepSeek V4 Flash  │
            │ DeepSeek V4 Pro    │
            │ Ollama Qwen2.5:7b  │
            │ Gemini (fallback)   │
            └────────────────────┘
```

### 2.2 Les 5 bots Telegram

BAVI LEO parle via 5 robots Telegram distincts, chacun avec son profil Hermes isole :

```text
BOT                PROFIL      PROVIDER        ROLE
─────────────────────────────────────────────────────────
🤖 @hermes_leo_bot       default     DeepSeek Flash   Chat quotidien, analyses
🟪 @hermes_leo_copilot   leo-copilot DeepSeek V4 Pro  Code, infra, crons
🧭 @bavi_leo_voyages_bot bavi-leo    DeepSeek Flash   Voyages camping-car
🎓 @Bureau_ia_emilie_bot emile       Flash+Gemini     Pedagogie memoire
🏛 @bureau_robert_bot    bureau-robert DeepSeek Flash  Conseil strategique IT
```

Chaque bot est independant :
- Son propre gateway Telegram
- Ses propres skills charges
- Sa propre memoire persistante
- Son propre fournisseur LLM
- Mais ils partagent la meme configuration de base et peuvent s'appeler entre eux

### 2.3 L'infrastructure physique

```text
🌐 Machine LEO (serveur unique)
   CPU  : Intel Core i7-7700K (4 coeurs, 4.5 GHz)
   RAM  : 22 Go DDR4
   SSD  : 457 Go (systeme + donnees Hermes)
   HDD  : 1 To (backups, archives)
   GPU  : Aucun (Ollama sur CPU)
   OS   : Ubuntu 26.04 (conteneur Docker)

┌──────────────────────────────────────┐
│  DOCKER CONTAINER (supervise s6)     │
│                                      │
│  ├── hermes-gateway (s6 supervise)   │
│  │   ├── default (LEO, chat)         │
│  │   ├── leo-copilot (Michel infra)  │
│  │   ├── bavi-leo (Sylvia voyages)   │
│  │   └── emile (pedagogie)           │
│  ├── s6-log (rotation logs)          │
│  ├── cron scheduler (Hermes natif)   │
│  ├── s6 supervision (auto-restart)   │
│  ├── Ollama (Qwen2.5:7b local)       │
│  └── Scripts Python (collecteurs)    │
└──────────────────────────────────────┘
```

---

## 3. Les 10 bureaux BAVI

### 3.1 Tableau complet

```text
BUREAU         ROLE                          STATUT     MODELE
────────────────────────────────────────────────────────────────
🔧 Michel      Infrastructure, crons,        ✅ Actif   DeepSeek V4 Pro
               dashboards, budget, reseau
🤖 LEO         Hub central, dossiers         ✅ Actif   DeepSeek Flash
               personnels, analyses
🧭 Sylvia      Voyages camping-car,          ✅ Actif   DeepSeek Flash
               roadbooks, itineraires
🎓 Emile       Pedagogie, memoire            ✅ Actif   Flash + Gemini
               universitaire
🏛️ Robert      Conseil strategique IT,       ✅ Actif   DeepSeek V4 Pro
               16 experts
💰 Sophie      Pilotage financier,           📝 En      DeepSeek Flash
               TCO, ROI, business cases      reconstruction
🏗️ Gerard      Documentation T600,           ✅ Actif   DeepSeek V4 Pro
               telescope automatise
🩺 Virginie    Medical, consultations         ✅ Actif   DeepSeek Flash
               pluridisciplinaires
📚 Connaissance Base connaissance             ✅ Actif   DeepSeek Flash
               centralisee, referentiels
🛡️ AO          Assurance obligatoire,         📝 Pret    DeepSeek Flash
               INAMI, eHealth
```

### 3.2 Detail de chaque bureau

#### 🔧 Bureau Michel (Infrastructure)

Le plus gros bureau. Michel gere toute l'infrastructure technique :
- 39 crons Hermes + 6 watchdogs (supervision)
- 8 sous-experts specialises :

```text
SysAdmin    → Administration du serveur, installation
DevOps      → Docker, deploiement, CI/CD
Scripteur   → Scripts Python/Bash, automation
DataDoc     → Documentation technique, audits
Networker   → Nginx, Cloudflare, DNS, reseau
DashBuilder → Dashboards Chart.js
CronMaster  → Crons Hermes (staggering, supervision)
GitGuardian → Git, sync, clean trees
```

Michel utilise DeepSeek V4 Pro pour les taches complexes, et s'appuie sur Ollama (gratuit, local) pour les traitements batch.

#### 🏛️ Bureau Robert (Conseil strategique)

Robert est le "comite de direction" de BAVI LEO. Il dispose de **16 experts** organises en 2 groupes :

```text
EXPERTS IT (9)                          EXPERTS BUSINESS (7)
─────────────────────────────────────────  ───────────────────────────
🔷 Architecture IT                      🔶 Strategie digitale
🔷 Securite & conformite                🔶 Innovation & veille
🔷 Cloud & infrastructure               🔶 Gestion de projet
🔷 Donnees & IA                         🔶 Ressources humaines
🔷 Reseau & telecom                     🔶 Marketing & communication
🔷 DevOps & CI/CD                       🔶 Affaires reglementaires
🔷 Support & run                        🔶 Partenariats
🔷 Data engineering
🔷 Infrastructure critique
```

Robert a son propre bot Telegram, un canal de discussion strategique dedie, et peut dispatcher des analyses a plusieurs experts en parallele puis croiser leurs resultats.

#### 🤖 Bureau LEO (Hub central)

C'est le point d'entree principal de Christophe :
- Dialogue quotidien (DeepSeek Flash)
- Analyses et dossiers personnels
- Veille IA, classification d'emails
- Coordination des autres bureaux

LEO est le "chef d'orchestre" — il detecte quand une demande doit etre transferee a Michel (infra), Robert (strategie), ou Sophie (budget).

#### 🧭 Bureau Sylvia (Voyages)

Specialiste des roadbooks camping-car :
- Itineraires multi-pays avec cartes Folium/OpenStreetMap
- Distances Haversine entre chaque etape
- Cout total (peage, carburant, peage, camping)
- Verification ZTL et hauteurs pour camping-car
- Export PDF des roadbooks
- Bot Telegram dedie : @bavi_leo_voyages_bot

Prochains voyages en preparation : Toscane (Sep 2026), Vietnam-Laos-Cambodge (Jan 2027), Scandinavie (Aout-Oct 2026).

#### 🎓 Bureau Emile (Pedagogie)

Assistant pour le memoire de fin d'etudes d'Emilie (sciences de l'education) :
- Relecture et amelioration des chapitres
- Bibliographie et references academiques
- Structure et plan du memoire
- Versionning des brouillons
- Fallback automatique sur Gemini quand le contexte depasse 128K tokens (jusqu'a 1 million)

#### 💰 Bureau Sophie (Finances)

Pilotage economique et financier :
- Business cases pour tout investissement IT
- Calcul TCO/ROI sur 3 scenarii (prudent, median, optimiste)
- Parallelisation Marche + Risques pour gagner du temps
- Actuellement en reconstruction pour la version v2

#### 🏗️ Bureau Gerard (Documentation T600)

Documentation technique du telescope automatise T600 :
- 6 experts specialises : Electronique, Software, Mecanique, Tests, Reseau, Securite
- Plus de 400 fichiers de documentation
- Dispatch conditionnel par domaine technique

#### 🩺 Bureau Virginie (Medical)

Orchestration medicale pluridisciplinaire :
- Panel de medecins du generaliste aux specialistes
- Dispatch conditionnel pour un diagnostic optimal
- Parallélisation des analyses medicales
- Synthese finale par Virginie

#### 📚 Bureau Connaissance

Base de connaissance centralisee :
- Bibliotheque de cas d'usage IA
- Referentiels documentaires
- Cartographie des competences par bureau
- Point d'entree pour les nouvelles analyses

#### 🛡️ Bureau AO (Assurance obligatoire)

Lentille metier AO transverse :
- INAMI, BCSS, eHealth, MyCareNet
- Appelable depuis Robert ou directement
- Structure prete, en attente de deploiement

---

## 4. Le systeme de Skills

Les skills sont le "cerveau" de chaque bureau. Ce sont des fichiers markdown (.md) qui contiennent :

### 4.1 Structure d'un skill

```text
---
name: nom-du-skill
description: "Ce que fait ce skill"
version: vX.Y
author: LEO
tags: [domaine, mots-cles]
---

# Titre du skill

## Description
...

## Etapes (procedure)
1. ...
2. ...

## Pieges
| Piege | Solution |
...

## Fichiers lies
...
```

### 4.2 Les 130+ skills par domaine

```text
INFRASTRUCTURE (Michel) :
  deployment-checklist  : Checklist avant chaque modification
  cron-lifecycle        : Planifier, auditer, nettoyer les crons
  dashboard-kpi         : Systeme de dashboard KPI
  deepseek-pro          : Auto-routing vers DeepSeek Pro
  leo-architecture      : Architecture LEO complete
  leo-backup-dr         : Plan de reprise d'activite
  system-management     : Gestion des machines distantes
  machine-metrics       : Dashboard 3 machines
  workspace-hygiene     : Nettoyage des workspaces
  gmail-inbox-zero      : Classification d'emails
  n8n-automation        : (deprecie)

PRODUCTIVITE :
  google-workspace      : Gmail, Calendar, Drive, Docs, Sheets
  mkdocs-wiki           : Creation de wikis MkDocs
  budget-tracking       : Dashboard budget
  hermes-dashboard      : Dashboard KPI Hermes
  contacts-referentiel  : Fichier contacts centralise
  maps                  : Geocodage, POIs, routes
  nano-pdf              : Edition PDF

RECHERCHE (LEO) :
  ai-tech-watch         : Veille IA quotidienne (13 sources RSS)
  arxiv                 : Recherche sur arXiv
  blogwatcher           : Surveillance blogs et RSS
  llm-wiki              : Base de connaissance LLM
  polymarket            : Marches de prediction
  youtube-content       : Transcription YouTube

CREATIF :
  ascii-art             : ASCII art, images vers ASCII
  excalidraw            : Diagrammes main-levée
  manim-video           : Animations mathematiques
  p5js                  : Sketches creatifs
  claude-design         : Designs HTML/CSS
  songwriting-and-ai-music : Prompts musique Suno

BUREAUX METIER :
  bureau-robert         : Conseil strategique (16 experts)
  bureau-michel         : Infrastructure (8 sous-experts)
  bureau-sylvia         : Voyages camping-car
  bureau-emile          : Pedagogie universitaire
  bureau-virginie       : Orchestration medicale
  bureau-gerard         : Documentation T600
  bureau-sophie         : Pilotage financier
  bureau-leo            : Dossiers & analyses
  assurance-obligatoire : AO transverse
  bavi-leo-governance   : Gouvernance BAVI LEO
  bureau-versioning     : Gestion des versions
  workflow-qualite-livraison : Controle qualite
```

### 4.3 Comment un skill est utilise

1. Le bureau recoit une demande (via Telegram ou cron)
2. Il charge le skill correspondant au contexte
3. Le skill fournit les procedures, les regles, les pieges
4. Le LLM execute en suivant le skill
5. Le resultat est stocke dans le dossier du bureau

Avantage : les procedures sont **documentees, versionnees, reutilisables**. Un nouveau bureau peut heriter des skills existants.

---

## 5. Le systeme de Crons (automatisation)

### 5.1 Les 39 crons Hermes + 6 watchdogs

```text
CRONS HORAIRES (toutes les heures) :
  :00  - check-dashboard-kpi-refresh    → Rafraichit le dashboard
  :00  - update-machines-metrics         → Metriques 3 machines
  :05  - backup-dashboard-kpi           → Backup du dashboard
  :10  - depense-check                  → Verification budget
  :15  - sync-leo-email-credentials     → Sync emails
  :20  - deploy-global-dashboard        → Deploie dashboard global
  :25  - check-vpn-tailscale            → Verification VPN
  :30  - sync gmail-classifier          → Classification emails
  :35  - budget-check-v6                → Verification budget DeepSeek
  :40  - check-hermes-services          → Sante des services
  :45  - collect-generic-metrics        → Metriques generiques
  :50  - cleanup-hermes-temp            → Menage fichiers temp
  :55  - ping-leo-sessions              → Ping sessions actives

CRONS QUOTIDIENS (heure fixe) :
  06:00 - leo-backup                   → Backup quotidien
  06:05 - budget-check                 → Releve budget
  06:10 - dashboard-kpi-deploy         → Deploiement dashboard
  06:15 - machines-metrics-deploy      → Metriques machines
  06:20 - crons-healthcheck            → Verification tous crons
  06:25 - github-activity              → Activite GitHub
  08:00 - veille-IA                    → Veille IA + email
  18:00 - drive-github-sync            → Sync Drive ↔ GitHub

WATCHDOGS (supervision automatique) :
  check-gmail-watchdog         → Verifie que la classification tourne
  check-budget-watchdog        → Alerte si budget anormal
  check-dashboard-watchdog     → Verifie dashboard a jour
  check-system-watchdog        → Supervision systeme
  check-crons-watchdog         → Verifie que tous les crons tournent
  check-network-watchdog       → Ping reseau, DNS, VPN
```

### 5.2 Le pipeline no_agent (zero cout LLM)

95% des crons tournent en mode **no_agent** = execution directe du script, sans LLM. Exemple :

```text
Phase 1 : Collecte (no_agent, 0 token)
  Script Python → lit state.db 5 profils
               → mesure CPU/RAM/disque 3 machines
               → releve solde DeepSeek
               → ecrit JSON dans metrics/

Phase 2 : Deploiement (no_agent, 0 token)
  Script Python → lit JSON → genere HTML Chart.js
               → git commit + push → GitHub Pages
               → dashboard mis a jour

Cout total : 0 euro. Frequence : toutes les heures.
```

---

## 6. Les Dashboards

### 6.1 Le dashboard central (LEO Dashboard)

URL : https://christophedanhier-hash.github.io/leo-dashboard/

Un seul dashboard HTML statique (Chart.js) qui regroupe 4 onglets :

```text
ONGLET 1 : Sessions
  - Nombre de sessions actives (5 profils)
  - Messages echanges (24h/7j/30j)
  - Tokens consommes par profil
  - Latence moyenne par provider

ONGLET 2 : Budget
  - Solde DeepSeek actuel
  - Depense journaliere
  - Projection a 30 jours
  - Cout par bureau

ONGLET 3 : Crons & Services
  - Statut des 39 crons
  - Derniere execution reussie/echouee
  - Temps depuis dernier echec
  - Statut des 4 gateways

ONGLET 4 : Machines
  - CPU/RAM/DISK des 3 machines
  - Latence reseau
  - Processus actifs
  - Tempo de fonctionnement
```

### 6.2 Le collecteur unifie

Un script Python (`collect-v2.py`) centralise toutes les donnees :
- Lit les bases state.db des 5 profils
- Collecte les metriques des 3 machines via SSH
- Releve le solde DeepSeek via API
- Agrege tout en un seul JSON
- Declenche le deploiement du dashboard

---

## 7. Le workflow de production

Toute analyse ou document produit par BAVI LEO suit un cycle standardise en 7 phases :

```text
① CADRAGE
   Comprendre la demande, le contexte, les contraintes
   │
   ▼
② DISPATCH
   Quel bureau ? Quels sous-experts activer ?
   │
   ▼
③ PRODUCTION
   Chaque expert produit son analyse (parallele possible)
   │
   ▼
④ CROISEMENT (si multi-experts)
   Confronter les analyses, identifier divergences
   │
   ▼
⑤ SYNTHESE
   Resume, conclusions, recommandations
   │
   ▼
⑥ LIVRABLE
   Format final (.md) avec frontmatter YAML
   │
   ▼
⑦ ARCHIVAGE
   Dossier AGENT-PRO + wiki + commit git + push
```

Variantes selon le type :

```text
Analyse  : ①→③→⑤→⑥→⑦ (simple, pas de dispatch)
Rapport  : ①→②→③→④→⑤→⑥→⑦ (complet)
Note     : ①→③→⑥ (rapide)
Dossier  : ①→②→③→④→⑤→⑥→⑦ + archivage renforce
Memoire  : ①→②→③→④↔④↔④→⑤→⑥→⑦ (iteratif)
```

---

## 8. L'interoperabilite entre bureaux

Les bureaux peuvent s'appeler mutuellement :

```text
Demande : "Quel est l'impact budgetaire d'un nouveau serveur ?"
   │
   ├── Robert (analyse strategique)
   │    └── Strategie : nouveau serveur pertinent ?
   │
   ├── Michel (analyse technique)
   │    └── Technique : quel modele, quelle config ?
   │
   ├── Sophie (analyse financiere)
   │    └── Budget : TCO/ROI, impact budgetaire
   │
   └── Synthese croisee Robert + Michel + Sophie
        → Recommandation unique et chiffree
```

---

## 9. La memoire persistante

BAVI LEO utilise la memoire Hermes pour retenir :
- Les preferences de l'utilisateur (ton, format, regles)
- Les identifiants et tokens (stocks hors Git)
- Les lecons apprises (problemes deja rencontres et solutions)
- Les references croisees entre bureaux

Contrairement a un chatbot qui oublie tout entre deux sessions, BAVI LEO apprend en continu.

---

## 10. Les couts

```text
POSTE               COUT/MOIS     NOTES
─────────────────────────────────────────────
DeepSeek Flash       ~15-20 EUR     Usage quotidien, 4 bots
DeepSeek V4 Pro      ~5-10 EUR      Michel + Robert
Ollama local         Gratuit         Qwen2.5:7b sur CPU
Gemini fallback      Gratuit         Au-dela de 128K tokens
Hébergement          ~5 EUR          Serveur existant
Telegram             Gratuit         API libre
GitHub Pages         Gratuit         Hebergement wiki/dashboards
─────────────────────────────────────────────
TOTAL               < 30 EUR/mois
```

---

## 11. Les principes de gouvernance

1. **Specialisation** : chaque bureau ne fait qu'un metier, il le fait mieux
2. **Reutilisabilite** : une analyse peut etre reprise par un autre bureau
3. **Tracabilite** : chaque document a une date, version, auteur (frontmatter YAML)
4. **Evolutivite** : on peut ajouter un bureau sans casser les autres
5. **Automatisation** : l'index des analyses est genere automatiquement
6. **Resilience** : s6 supervise tout, auto-restart en cas de crash
7. **Zero confiance** : jamais de modification sans validation humaine
8. **Documentation d'abord** : toute modification est documentee avant d'etre livree
9. **Anti-regression** : verifier qu'aucun cron existant n'est en pause
10. **Commit avant livraison** : zero dirty files, toujours pusher

---

## 12. Comment debuter

1. Installer Hermes Agent : `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
2. Configurer un provider LLM (DeepSeek recommande)
3. Creer un premier bureau : `mkdir -p BAVI/AGENT-PRO/mon-bureau/`
4. Ecrire un premier skill : fichier .md avec procedure
5. Connecter Telegram : `hermes gateway connect telegram`
6. Ajouter un cron : `hermes cron create --schedule "0 6 * * *" --prompt "..."`

Le guide complet "Hermes pour les Nuls" detaille chaque etape dans ses 10 chapitres.

---

*Document complete le 18/07/2026 a 14:30 — Leo 🦁 | v2.0*

> 🤖 Dernier audit : 22 July 2026 à 07:40 (UTC+2)

