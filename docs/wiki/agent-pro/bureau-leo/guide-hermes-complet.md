---
date: 2026-07-07
bureau: bureau-leo
auteur: LEO
version: v4.0
modele: deepseek-v4-flash
tags: [hermes, guide, documentation, livre, pour-les-nuls, leo, architecture]
statut: archive
type: livre
---

# Hermès pour les Nuls 🦁

> **Note :** Ce guide documente l'architecture au 07/07/2026. Le profil `leo-copilot` et le bot `@hermes_leo_copilot_bot` sont désormais appelés **Michel (infra)**. Les commandes et chemins techniques (`-p leo-copilot`, `/profiles/leo-copilot/`) restent inchangés.

## Construire son propre assistant IA avec LEO

---

### À propos de ce livre

**Hermès pour les Nuls** n'est pas un énième manuel technique. C'est l'histoire d'une aventure — celle de **LEO**, l'assistant IA personnel de Christophe, et comment il a été construit avec **Hermes Agent**, une plateforme open source.

Ce livre vous guide pas à pas, de l'installation d'Hermes sur votre machine jusqu'à la construction d'un écosystème complet : bots Telegram, skills intelligents, dashboards de monitoring, tâches automatisées, et bien plus. Chaque concept est illustré par l'exemple réel de LEO — pas un exemple artificiel, mais un système qui tourne 24h/24, 7j/7, et qui fait le travail tous les jours.

### Ce que vous apprendrez

- **Partie I — Découvrir Hermès** : comprendre ce qu'est un agent IA, pourquoi Hermes, et l'architecture de LEO
- **Partie II — Configurer votre assistant** : installer le gateway, choisir vos providers, créer vos premiers bots
- **Partie III — Les Bureaux BAVI** : organiser vos connaissances avec le système de bureaux
- **Partie IV — La Puissance des Skills** : exploiter 117 skills prêts à l'emploi et créer les vôtres
- **Partie V — Dashboards et Monitoring** : visualiser tout avec 1 dashboard central (4 onglets)
- **Partie VI — Automatisation et Crons** : faire tourner 13 tâches planifiées + daemon sans lever le petit doigt
- **Partie VII — La Partie des Dix** : les astuces, commandes et ressources qui sauvent

### Public visé

| Vous êtes... | Commencez par... |
|:-------------|:-----------------|
| **Curieux·se** — vous voulez savoir ce qu'est un agent IA | Partie I, Chapitres 1-2 |
| **Débutant·e** — vous installez Hermes pour la première fois | Chapitre 4, puis Partie II |
| **Utilisateur·trice intermédiaire** — vous avez Hermes mais voulez aller plus loin | Partie III, Partie IV |
| **Power user** — vous voulez automatiser et monitorer | Partie V, Partie VI |
| **Tout le monde** — les astuces et références | Partie VII, Annexes |

### La philosophie LEO

> *« Un assistant n'est pas un chatbot. C'est quelqu'un qui anticipe, qui agit, et qui ne vous fait pas répéter deux fois. »*

LEO a été bâti sur quatre principes :

1. **⚡ Efficace** — pas de blabla, des actions concrètes
2. **🛡️ Fiable** — des garde-fous contre les erreurs, des filets de sécurité
3. **💰 Économe** — le meilleur LLM pour chaque tâche, pas le plus cher
4. **🤫 Discret** — tourne en arrière-plan, ne dérange que quand c'est important

### Convention d'icônes

Tout au long de ce livre, vous retrouverez ces icônes :

| Icône | Signification |
|:-----|:--------------|
| 💡 | Astuce — une idée ou un conseil pratique |
| ⚠️ | Attention — un piège ou une erreur fréquente |
| 🔧 | Technique — un détail pour les curieux |
| 📝 | À retenir — l'essentiel du chapitre |
| 🏠 | Local — fonctionnalité gratuite/tourne chez vous |
| ☁️ | Cloud — utilise un service distant (payant ou gratuit) |
| 🦁 | LEO — exemple réel tiré de l'écosystème LEO |

### Prérequis

- Un ordinateur sous **Linux** (recommandé), macOS, ou Windows (WSL)
- Un peu d'aisance avec le terminal (savoir lancer une commande)
- (Optionnel) Un compte **Telegram** pour créer votre bot
- (Optionnel) Des clés API pour les LLM que vous voulez utiliser

### Comment lire ce livre

La lecture linéaire est recommandée si vous démarrez de zéro. Mais chaque chapitre est conçu pour être lu indépendamment — utilisez la table des matières pour sauter directement à ce qui vous intéresse.

Les exemples LEO sont signalés par l'icône 🦁 et peuvent être ignorés si vous voulez juste les concepts.

### Licence

Ce guide est en licence libre — vous pouvez le partager, l'adapter, et l'enrichir. Il est maintenu par LEO lui-même dans le cadre de son cycle d'auto-documentation.

---

**Projet vivant** — dernière mise à jour : 3 juillet 2026. Hermes Agent évolue vite, ce guide aussi.

👉 [Table des matières complète](TABLE.md)
# Table des matières

## 📖 Hermès pour les Nuls

```
┌────────────────────────────────────────────────────────────┐
│  HERMÈS POUR LES NULS                                      │
│  Construire son propre assistant IA avec LEO              │
│                                                            │
│  Partie I  — Découvrir Hermès          🏁                  │
│  Partie II — Configurer son Assistant  ⚙️                  │
│  Partie III — Les Bureaux BAVI         🏛️                  │
│  Partie IV — La Puissance des Skills   🧠                  │
│  Partie V — Dashboards et Monitoring   📊                  │
│  Partie VI — Automatisation et Crons   ⏱️                  │
│  Partie VII — La Partie des Dix        💡                  │
│  Annexes                                📚                 │
└────────────────────────────────────────────────────────────┘
```

---

## Partie I — Découvrir Hermès 🏁
*Commencer par le commencement*

- **[Ch.1 — Un agent IA, c'est quoi ?](01-decouvrir-hermes/ch01-cest-quoi-un-agent.md)**
  - Chatbot vs agent : la différence fondamentale
  - Ce que LEO fait que ChatGPT ne peut pas faire
  - Les briques d'un agent : modèle, outils, mémoire, actions

- **[Ch.2 — Pourquoi Hermès ?](01-decouvrir-hermes/ch02-pourquoi-hermes.md)**
  - Hermes vs Claude Code vs Codex vs OpenCode
  - Multi-provider : DeepSeek, Gemini, Ollama, 15+ autres
  - Skills : le super-pouvoir qui rend Hermes unique
  - Plateformes : Telegram, Discord, Slack, email, et plus

- **[Ch.3 — L'architecture LEO](01-decouvrir-hermes/ch03-architecture-leo.md)**
  - Vue d'ensemble : 4 profils actifs, providers dédiés
  - Le Gateway DeepSeek : pont entre Telegram et l'agent
  - Hiérarchie des providers : quand utiliser quoi
  - Les chiffres clés de LEO (dashboards, crons, skills)

- **[Ch.4 — Installation rapide](01-decouvrir-hermes/ch04-installation-rapide.md)**
  - Installation sur Linux (Debian/Ubuntu)
  - Installation sur Windows (WSL)
  - Premier lancement et configuration minimale
  - Vérification : le diagnostic

---

## Partie II — Configurer son Assistant ⚙️
*Moteur, on tourne !*

- **[Ch.5 — Le Gateway : connecter Telegram](02-configurer/ch05-gateway.md)**
  - Créer un bot Telegram avec @BotFather
  - Configurer le gateway Hermes
  - Gérer les profils : default, leo-copilot, bavi-leo
  - La gestion s6 en environnement Docker

- **[Ch.6 — Providers : le moteur de votre agent](02-configurer/ch06-providers.md)**
  - DeepSeek : le pilier principal
  - Ollama : l'IA locale et gratuite
  - Gemini : le fallback silencieux
  - Hiérarchie et fallback : comment Hermes choisit

- **[Ch.7 — Multi-bots : pourquoi plusieurs valent mieux qu'un](02-configurer/ch07-multi-bots.md)**
  - L'architecture multi-profil de LEO
  - Quand créer un nouveau bot vs tout dans le même
  - Synchronisation de mémoire entre profils
  - Gérer ses tokens et cred pools

- **[Ch.8 — Skills : le super-pouvoir d'Hermès](02-configurer/ch08-skills.md)**
  - Qu'est-ce qu'un skill ?
  - Les 117 skills de LEO : classification et navigation
  - Installer, charger, et utiliser des skills
  - Skills système vs skills utilisateur

- **[Ch.9 — Mémoire persistante](02-configurer/ch09-memoire.md)**
  - Pourquoi un agent a besoin de mémoire
  - Memory vs User Profile
  - Configurer et utiliser la mémoire
  - Mémoire partagée : symlinks entre profils

---

## Partie III — Les Bureaux BAVI 🏛️
*La force de l'organisation*

- **[Ch.10 — Architecture bureaux](03-bureaux-bavi/ch10-architecture-bureaux.md)**
  - Le concept BAVI : organiser ses connaissances par bureau
  - Les 10 bureaux : qui fait quoi
  - La gouvernance : comment les bureaux collaborent

- **[Ch.11 — Bureau Michel : l'infrastructure](03-bureaux-bavi/ch11-michel-infra.md)**
  - Déploiement et configuration des workflows
  - Gestion système, watchdogs, scripts
  - La checklist de déploiement

- **[Ch.12 — Bureau Sylvia : les voyages](03-bureaux-bavi/ch12-sylvia-voyages.md)**
  - Le bot voyages dédié (@bavi_leo_voyages_bot)
  - Roadbooks et wiki voyages
  - Agence de voyage complète (camping-car, hôtels, itinéraires)

- **[Ch.13 — Bureau Emile : la pédagogie](03-bureaux-bavi/ch13-emile-pedagogie.md)**
  - Assistant pédagogique pour mémoire de fin d'études
  - Méthodologie d'audit et workflow

- **[Ch.14 — Bureau Robert : le conseil stratégique](03-bureaux-bavi/ch14-robert-conseil.md)**
  - Analyses concurrentielles
  - Recommandations stratégiques IT
  - Documentation T600

- **[Ch.15 — Les autres bureaux](03-bureaux-bavi/ch15-autres-bureaux.md)**
  - Bureau Sophie : pilotage économique et financier
  - Bureau Gérard : documentation technique
  - Bureau Virginie : orchestration médicale
  - Bureau LEO : le fourre-tout personnel
  - Assurance Obligatoire : le bureau transverse

---

## Partie IV — La Puissance des Skills 🧠
*Le savoir-faire réutilisable*

- **[Ch.16 — Skills système](04-skills/ch16-skills-systeme.md)**
  - hermes-agent, hermes-gateway, hermes-profiles
  - Configuration et troubleshooting
  - Les profils multi-agents

- **[Ch.17 — Skills productivité](04-skills/ch17-productivite.md)**
  - Dashboards : hermes-dashboard, dashboard-kpi
  - Documentation : mkdocs-wiki, living-documentation
  - Google Workspace, Airtable, Notion
  - Email : inbox-zero, leo-email-assistant

- **[Ch.18 — Skills DevOps](04-skills/ch18-devops.md)**
  - GitHub PR workflow, code review, issues
  - Code-server VS Code dans le navigateur
  - Déploiement de dashboards

- **[Ch.19 — Skills créatifs](04-skills/ch19-creatifs.md)**
  - ASCII art, architecture diagrams, Excalidraw
  - ComfyUI, p5.js, manim-video
  - Songwriting et musique IA

- **[Ch.20 — Skills recherche et veille](04-skills/ch20-recherche.md)**
  - AI Tech Watch : 17 sources RSS
  - arXiv, blogwatcher, Polymarket
  - Llm-wiki : base de connaissances LLM

- **[Ch.21 — Écrire ses propres skills](04-skills/ch21-ecrire-ses-skills.md)**
  - Le format SKILL.md : frontmatter et contenu
  - Les bonnes pratiques
  - Versionner et partager ses skills

---

## Partie V — Dashboards et Monitoring 📊
*Voir l'invisible*

- **[Ch.22 — L'écosystème de dashboards](05-dashboards/ch22-ecosysteme-dashboards.md)**
  - Architecture : 1 dashboard central (4 onglets), HTML statique, GitHub Pages
  - Navigation entre onglets : Synthèse, Analyses, Infra, BAVI
  - Cycle de vie d'une donnée : du collecteur au graphique Chart.js

- **[Ch.23 — Métriques machines](05-dashboards/ch23-metriques-machines.md)**
  - CPU, RAM, disque, GPU : collecte et visualisation
  - Les 3 machines de LEO : LEO, Yoga, Penguin
  - Alertes et seuils

- **[Ch.24 — Monitoring du dashboard](05-dashboards/ch24-monitoring-dashboard.md)**
  - Le tableau de bord unique : 4 onglets (Synthèse, Analyses, Infra, BAVI)
  - 20 indicateurs KPI en direct
  - 4 graphiques Chart.js interactifs

- **[Ch.25 — Budget et tracking](05-dashboards/ch25-budget-tracking.md)**
  - Suivi du solde DeepSeek en temps réel
  - Projection de consommation
  - Dashboards LEO KPI et BAVI LEO KPI

---

## Partie VI — Automatisation et Crons ⏱️
*Que ça roule tout seul*

- **[Ch.26 — Le scheduler Hermes](06-automatisation/ch26-scheduler.md)**
  - no_agent vs LLM-driven : quel mode pour quelle tâche ?
  - Script vs prompt : les critères de choix
  - Syntaxe cron, delivery, workdir

- **[Ch.27 — Les crons horaires](06-automatisation/ch27-crons-horaires.md)**
  - La vague H:00-H:30 : 8 crons qui s'enchaînent
  - Machines KPI, budget, dashboards
  - Le staggered scheduling

- **[Ch.28 — Les crons quotidiens et spéciaux](06-automatisation/ch28-crons-quotidiens.md)**
  - Backup automatique (06:00)
  - Veille IA (08:00)
  - Drive sync (18:00)
  - Classifieur emails (toutes les 15 min)
  - Auto-commit repos (toutes les 2h)

- **[Ch.29 — Watchdogs et alertes](06-automatisation/ch29-watchdogs.md)**
  - Dashboard Watch : vérification automatique du contenu
  - Auto-Heal : détection et correction des erreurs
  - Code-server watchdog
  - Le double filet : Hermes + n8n

- **[Ch.30 — Drive ↔ GitHub Sync](06-automatisation/ch30-drive-sync.md)**
  - Synchronisation bidirectionnelle Drive ↔ GitHub
  - Résolution de conflits
  - Le Drive Guardian dans n8n

---

## Partie VII — La Partie des Dix 💡
*Les listes qui sauvent*

- **[Ch.31 — 10 astuces pour ne pas galérer](07-partie-des-dix/ch31-10-astuces.md)**
  - Les pièges à éviter absolument
  - Astuces de configuration et d'usage quotidien

- **[Ch.32 — 10 commandes à connaître absolument](07-partie-des-dix/ch32-10-commandes.md)**
  - Les essentiels du CLI Hermes
  - Commandes slash en session interactive

- **[Ch.33 — 10 façons d'étendre Hermès](07-partie-des-dix/ch33-10-extensions.md)**
  - MCP servers, plugins, webhooks
  - Intégrations avec d'autres outils

- **[Ch.34 — 10 ressources pour aller plus loin](07-partie-des-dix/ch34-10-ressources.md)**
  - Documentation officielle, skills hub, communauté

---

## Annexes 📚

- **[Annexe A — Glossaire](annexes/glossaire.md)**
- **[Annexe B — Guide de démarrage rapide](annexes/guide-rapide.md)**
- **[Annexe C — Arbre de décision des providers](annexes/arbre-providers.md)**
- **[Annexe D — Check-list déploiement](annexes/checklist-deploiement.md)**
- **[Annexe E — Aide-mémoire des commandes](annexes/commandes.md)**
- **[Annexe F — Exemple : architecture complète de LEO](annexes/exemple-leo-complet.md)**
- **[Annexe G — Troubleshooting](annexes/troubleshooting.md)**

---

**Légende :** 📝 = écrit | 🔄 = en cours | ⬜ = à rédiger
# Chapitre 1 — Un agent IA, c'est quoi ?

> *La différence entre un chatbot et un assistant qui agit*

---

Si vous lisez ce livre, vous avez probablement déjà utilisé ChatGPT, Claude, ou Gemini. Vous tapez une question, l'IA répond. Simple, efficace.

Mais vous avez aussi ressenti la frustration : « *Peux-tu envoyer cet email à Paul ?* » → « Je suis désolé, je ne peux pas envoyer d'email. » C'est là que la différence entre **chatbot** et **agent** devient flagrante.

## Chatbot vs Agent : la différence fondamentale

```
┌──────────────────────────────────────────────────────┐
│                      CHATBOT                         │
│  Vous : "Quel temps fait-il à Paris ?"               │
│  Bot  : "Il fait 22°C et ciel dégagé."              │
│  ───────────────────────────────────────────────────  │
│  📢 Il PARLE — mais n'AGIT PAS                       │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│                      AGENT                           │
│  Vous : "Prépare un email pour Paul avec le          │
│          compte-rendu de la réunion d'hier."         │
│  Agent : [Cherche le document]                       │
│          [Rédige le résumé]                          │
│          [Ouvre Gmail]                               │
│          [Envoie l'email]                            │
│         "✅ Email envoyé à Paul avec le CR."          │
│  ───────────────────────────────────────────────────  │
│  🦁 Il PARLE ET AGIT                                 │
└──────────────────────────────────────────────────────┘
```

Un **agent IA**, c'est un chatbot qui a :

| Capacité | Chatbot | Agent |
|:---------|:-------:|:-----:|
| Répondre à des questions | ✅ | ✅ |
| Exécuter des commandes sur votre système | ❌ | ✅ |
| Lire et écrire des fichiers | ❌ | ✅ |
| Envoyer des emails | ❌ | ✅ |
| Planifier des actions dans le futur | ❌ | ✅ |
| Utiliser des outils (calculatrice, API, navigateur) | ❌ | ✅ |
| Apprendre de ses erreurs entre sessions | ❌ | ✅ |
| Travailler sans supervision | ❌ | ✅ |

## Ce que LEO fait que ChatGPT ne peut pas faire

LEO, c'est l'assistant de Christophe — et il n'est pas juste « une interface vers DeepSeek ». Voici ce qu'il fait tous les jours sans intervention humaine :

| À 06:00 | Backup automatique des fichiers critiques |
|:--------|:------------------------------------------|
| À 06:05 | Relevé du solde DeepSeek → écrit dans Google Sheets |
| À 06:10 | Met à jour le dashboard KPI |
| À 06:15 | Collecte CPU/RAM/disque des 3 machines |
| À 06:20 | Vérifie que tous les crons tournent bien |
| À 06:25 | Met à jour l'activité GitHub |
| Toutes les 15 min | Classifie les emails entrants |
| Toutes les 30 min | Synchronise sa mémoire entre profils |
| À 08:00 | Analyse 17 sources RSS → envoie la veille IA par email |
| À 18:00 | Synchronise Drive ↔ GitHub |

Et tout ça **sans que Christophe ait à lui demander**. LEO anticipe.

## Les briques d'un agent IA

Derrière la magie, un agent comme Hermès est construit sur cinq piliers :

### 1. 🧠 Le modèle (LLM)
Le cerveau. DeepSeek, Gemini, Ollama — c'est ce qui comprend votre demande et décide quoi faire. L'avantage d'Hermès ? Vous n'êtes pas enfermé chez un seul fournisseur : vous pouvez basculer de DeepSeek à Ollama (gratuit, local) en une commande.

### 2. 🔧 Les outils
Là où le chatbot s'arrête (« je ne peux pas faire ça »), l'agent commence. Hermès dispose de tout un arsenal d'outils :

- **terminal** — exécute des commandes shell
- **read_file / write_file** — lit et écrit des fichiers
- **web** — cherche sur Internet
- **browser** — navigue comme un humain
- **cronjob** — planifie des actions
- **delegate_task** — délègue à des sous-agents

### 3. 🧬 La mémoire
Un chatbot oublie tout entre deux conversations. Un agent se souvient :
- De votre nom, vos préférences, votre environnement
- Des leçons apprises (« ne pas envoyer deux fois le même email »)
- Des procédures qui ont fonctionné

### 4. 🏃 Les actions planifiées
Un agent ne se contente pas de répondre — il agit dans le futur. Les **crons** sont le secret pour qu'un assistant devienne un véritable majordome numérique : il fait le café avant que vous ne vous réveilliez.

### 5. 🎓 Les skills
C'est le secret le mieux gardé d'Hermès. Un **skill**, c'est un mode d'emploi que vous donnez à l'agent pour qu'il sache comment faire quelque chose. « Voici comment déployer un dashboard. Voici comment envoyer un email. Voici comment analyser un RSS. » Une fois écrit, ce savoir est réutilisable à l'infini.

## L'erreur à ne pas commettre

> « Je vais mettre tous mes modèles et outils dans le même agent et ça va marcher. »

**Non.** Un agent sans organisation, c'est le chaos. LEO a appris cette leçon à ses dépens (on vous racontera ça au chapitre 3). La clé, c'est la **structuration** :

- Des profils séparés pour des tâches différentes
- Des crons avec des horaires staggerés (décalés)
- Des skills qui encapsulent le savoir-faire
- Des bureaux qui organisent les connaissances

## 📝 À retenir

| Concept | À retenir |
|:--------|:----------|
| **Agent ≠ Chatbot** | Un chatbot répond. Un agent agit. |
| **LEO est un agent** | Il exécute des actions, pas seulement des réponses. |
| **5 piliers** | Modèle, outils, mémoire, crons, skills. |
| **Organisation** | Sans structure, un agent devient incontrôlable. |

---

**[Chapitre suivant → Pourquoi Hermès ?](ch02-pourquoi-hermes.md)**
# Chapitre 2 — Pourquoi Hermès ?

> *Il y a une dizaine d'agents IA open source. Pourquoi Hermès est le bon choix.*

---

Vous avez décidé de construire votre propre assistant IA. Bonne décision ! Maintenant, quel framework choisir ? Claude Code ? Codex ? OpenCode ? Il y a une dizaine d'options sur le marché, et Hermès n'est pas le plus connu.

Voici pourquoi LEO tourne sur Hermès — et pourquoi c'est le bon choix pour vous aussi.

## Le paysage des agents IA en 2026

| Agent | Éditeur | Langage | LLM imposé ? | Multi-plateforme ? | Skills ? | Prix |
|:------|:--------|:--------|:-------------|:------------------:|:--------:|:----:|
| **Hermes Agent** | Nous Research | Python | Non 🔓 | ✅ (15+) | ✅ | Gratuit |
| Claude Code | Anthropic | TypeScript | Claude (Anthropic) | ❌ CLI seul | ❌ | Payant |
| Codex CLI | OpenAI | Python (sandbox) | GPT (OpenAI) | ❌ CLI seul | Partiel | Payant |
| OpenCode | Communauté | Python | Non 🔓 | ❌ CLI seul | ❌ | Gratuit |
| Copilot CLI | GitHub | N/A | GPT (Microsoft) | ❌ CLI seul | ❌ | Abonnement |

### Pourquoi les autres ne convenaient pas

**Claude Code** est excellent pour le code, mais :
- Vous devez utiliser Claude exclusivement (pas de DeepSeek, pas d'Ollama)
- Pas de gateway Telegram, Discord, etc. — c'est un outil CLI pur
- Pas de skills réutilisables
- Abonnement payant (20$/mois + consommation)

**Codex CLI** est intéressant mais :
- Fonctionne dans un bac à sable — l'agent ne touche pas vraiment votre système
- Pas de persistance, pas de crons, pas de mémoire entre sessions
- Verrouillé OpenAI

**OpenCode** est open source mais :
- Pas de gateway (aucune plateforme de messagerie)
- Pas de système de skills
- Fonctionnalités limitées comparé à Hermès

### Ce qui rend Hermès unique

#### 1. 🔓 Multi-provider : vous n'êtes pas enfermé

Avec Hermès, vous pouvez utiliser **n'importe quel LLM** — et même les combiner :

```yaml
# Dans config.yaml
model:
  default: deepseek-v4-flash    # Le quotidien, économique
  delegation: deepseek-chat     # Sous-agents pour tâches complexes
fallback_providers:
  - provider: deepseek          # Fallback si le principal plante
    model: deepseek-v4-flash
providers:
  custom:
    ollama:                     # IA locale, gratuite
      base_url: http://localhost:11434/v1
    google:                     # Gemini, fallback gratuit
      base_url: https://generativelanguage.googleapis.com/v1beta/openai/
```

**L'avantage :** vous pouvez avoir un LLM cher et puissant pour le dialogue (DeepSeek), un LLM local et gratuit pour les tâches batch (Ollama), et un fallback en cas de panne (Gemini). Hermès gère la bascule tout seul.

#### 2. 🌐 Multi-plateforme : votre agent partout

| Plateforme | Statut | Usage typique |
|:-----------|:------:|:--------------|
| Telegram | ✅ | Canal principal de LEO |
| Discord | ✅ | Communautés gaming/dev |
| Slack | ✅ | Équipes pro |
| WhatsApp | ✅ | Usage personnel |
| Signal | ✅ | Messagerie sécurisée |
| Email | ✅ | Notifications sortantes |
| SMS | ✅ | Alertes d'urgence |
| API Server | ✅ | Intégration avec vos apps |
| Webhooks | ✅ | Automation tierce |

LEO, lui, communique **uniquement par Telegram** et envoie des **emails en sortie**. Mais votre assistant pourrait être sur Discord, WhatsApp, ou les trois.

#### 3. 🧠 Skills : le super-pouvoir

Un skill, c'est un document qui dit à Hermès : « Voici comment faire X. » Vous écrivez le mode d'emploi une fois, Hermès l'utilise à chaque fois.

```markdown
# skill: deploy-dashboard

1. Générer le fichier index.html avec les données à jour
2. Faire un git add, commit, push
3. Forcer le rebuild GitHub Pages via l'API
4. Vérifier que le dashboard répond HTTP 200
```

LEO a **126 skills** répartis en 22 catégories. Chaque skill encapsule une procédure — déployer un dashboard, envoyer un email, analyser un RSS, etc. Résultat : LEO sait faire des choses qu'on ne lui a jamais montrées, parce qu'il a le mode d'emploi.

> 🦁 **Exemple LEO :** Le skill `dashboard-deployment` contient toute la procédure de déploiement d'un dashboard HTML sur GitHub Pages. LEO peut déployer un nouveau dashboard en 30 secondes, sans erreur, parce que le skill lui dit exactement quoi faire.

#### 4. ⏱️ Cron : votre assistant qui travaille 24/7

Les crons Hermes ne sont pas de simples tâches shell. Chaque cron peut être :

- **Un script pur** (no_agent) — zéro token LLM, exécution directe
- **Un prompt LLM** — l'agent réfléchit et agit
- **Un script + un prompt** — collecte des données puis analyse

LEO a **38 crons Hermes + 6 crons hôte** dont la plupart en no_agent (0$ de consommation LLM pour les tâches répétitives) + un **auto-fix-daemon** qui tourne toutes les 15 minutes.

#### 5. 🗂️ Profils et gateways parallèles

Avec Hermès, vous pouvez avoir **plusieurs agents indépendants** sur la même machine :

| Profil | Bot Telegram | Provider | Rôle |
|:-------|:-------------|:---------|:-----|
| `default` | @hermes_leo_bot | DeepSeek Flash | Chat quotidien |
| `leo-copilot` | @hermes_leo_copilot_bot | DeepSeek V4 Pro | Code, infra, n8n |
| `bavi-leo` | @bavi_leo_voyages_bot | DeepSeek Flash | Voyages camping-car |

Chaque profil a son propre gateway, ses propres skills, sa propre mémoire. Et pourtant, ils peuvent partager des informations via des **symlinks** vers un fichier mémoire commun (`/opt/data/memories/`).

## 🦁 Pourquoi Christophe a choisi Hermès

> *Ce qui distingue Hermès des autres, c'est qu'il ne se contente pas de répondre — il agit. Là où un chatbot vous donne une réponse, Hermès peut envoyer l'email, mettre à jour le dashboard, lancer le backup, et classer vos messages. C'est la différence entre un conseiller qui parle et un assistant qui fait.*

— Inspiré de l'expérience de Christophe, créateur de LEO

**Le critère décisif :** Hermès a le meilleur rapport **puissance/flexibilité/prix**. Gratuit, open source, multi-provider, multi-plateforme, avec un système de skills qui le rend évolutif à l'infini.

## 📝 À retenir

| Critère | Hermès | Les autres |
|:--------|:------:|:----------:|
| Multi-provider | ✅ | ❌ (enfermé) |
| Multi-plateforme | ✅ (15+) | ❌ (CLI seul) |
| Skills | ✅ (126) | ❌ |
| Crons | ✅ (avancés) | ❌ |
| Gratuit | ✅ | Souvent payant |
| Open source | ✅ | Variable |

---

**[Chapitre suivant → L'architecture LEO](ch03-architecture-leo.md)**
# Chapitre 3 — L'architecture LEO

> *Comment Christophe a construit un assistant IA qui tourne 24h/24*

---

LEO n'est pas un simple script lancé sur un Raspberry Pi. C'est un écosystème complet qui mobilise plusieurs machines, services cloud, et une infrastructure résiliente. Ce chapitre vous montre les plans — comme si vous ouvriez la boîte noire.

## Vue d'ensemble

```
Telegram ──→ Gateway Hermes ──→ Profil default ──→ DeepSeek Flash (dialogue)
                                    │
                                    ├──→ @hermes_leo_copilot_bot → DeepSeek V4 Pro (code/infra)
                                    │
                                    ├──→ Ollama API locale (batch, gratuit)
                                    │
                                    └──→ Gemini (fallback automatique)
```

### Les profils Telegram actifs

| Bot | Profil | Provider | Rôle | Latence | Coût |
|:----|:-------|:---------|:-----|:-------:|:----:|
| 🤖 @hermes_leo_bot | `default` | DeepSeek Flash | Chat quotidien | < 2s | Payant |
| 🟪 @hermes_leo_copilot_bot | `leo-copilot` | DeepSeek V4 Pro | Code, infra, n8n | < 2s | Payant |
| 🧭 @bavi_leo_voyages_bot | `bavi-leo` | DeepSeek Flash | Voyages camping-car | < 2s | Payant |

Chaque bot est un **profil Hermes** isolé — son propre gateway, ses propres skills, sa propre mémoire. Mais ils partagent un fichier de configuration commun et peuvent échanger des informations.

## La hiérarchie des providers

L'un des atouts d'Hermès est de pouvoir utiliser **plusieurs LLMs** et de choisir le meilleur pour chaque tâche :

| Ordre | Provider | Coût | Quand |
|:-----:|:---------|:----:|:------|
| 🥇 | **DeepSeek Flash** | Payant | Réponse Telegram, conversation, raisonnement |
| 🥈 | **DeepSeek V4 Pro** (leo-copilot) | Payant | Code, infra, debug système |
| 🥉 | **Ollama** (qwen2.5:7b, local) | **Gratuit** 🏠 | Traitement batch, classification (CPU), tâches privées |
| 4e | **Gemini** (fallback) | **Gratuit** ☁️ | Secours si DeepSeek indisponible |

**Le principe économique :** 95% des tâches planifiées (crons) tournent en `no_agent` = 0 token LLM consommé. Les 5% restants utilisent d'abord Ollama (gratuit), puis DeepSeek seulement si nécessaire.

## L'infrastructure physique

LEO tourne sur **1 machine serveur**. Les autres postes (Yoga, Penguin) sont des stations de travail clientes — elles n'hébergent aucun service de la plateforme.

```
🌐 LEO (serveur unique)
   ├── Processeur : Intel Core i7-7700K
   ├── RAM : 22 Go
   ├── SSD : 457 Go (système + données Hermes)
   ├── HDD : 1 To (backups, archives)
   ├── GPU : Aucun (Ollama sur CPU)
   └── OS : Ubuntu 26.04 en conteneur Docker
```

## L'écosystème logiciel

### Docker et s6

Tout tourne dans un **conteneur Docker** supervisé par **s6** :

```
Docker Container
├── hermes-gateway (s6 supervisé)
│   ├── default (profil principal)
│   ├── leo-copilot (infra)
│   ├── bavi-leo (voyages)
│   └── emile (pédagogie)
├── s6-log (gestion des logs)
│   └── rotation automatique
├── cron scheduler (Hermes natif)
└── s6 supervision (auto-restart)
```

Avantage de s6 : si un gateway crashe, il redémarre automatiquement en moins d'une seconde.

### Les 1 dashboard (4 onglets)

Tous en **HTML statique** hébergés sur **GitHub Pages** — zéro backend, zéro base de données :

| Dashboard | URL | Onglets | Màj |
|:----------|:----|:--------|:---:|
| 🦁 **LEO Dashboard** | [lien](https://christophedanhier-hash.github.io/leo-dashboard/) | Synthèse, Analyses, Infra, BAVI — 20 KPI, 4 charts | */15 |

### Les 38 crons (+ 6 crons hôte)

LEO a 38 crons Hermes + 6 crons hôte qui exécutent des tâches planifiées

| Vague | Horaires | Crons |
|:------|:---------|:------|
| **Horaire** | H:00-H:30 staggerés | machines-kpi, budget, dashboards (4), wiki-sync |
| **15 min** | */15 | n8n healthcheck, classifieur emails |
| **2h** | */2 | auto-commit repos, dashboard-watch |
| **Quotidien** | 06:00, 08:00, 18:00 | backup, veille IA, drive sync |
| **Autres** | Hebdo, 6h | credentials-check, doc-watch |

### Les 5 wikis MkDocs

Chaque domaine a son propre wiki, hébergé sur GitHub Pages :

| Wiki | Pages | Contenu |
|:-----|:-----:|:--------|
| 🌐 **BAVI LEO** (portail central) | 40 | Portail + documentation bureaux |
| 📚 **Hermès Wiki** | 31 | Docs techniques Hermes |
| 🧭 **Voyages Wiki** | 7 | Roadbooks camping-car |
| 🔧 **Wiki OCA** | 10 | Documentation T600 |
| 🎓 **Emile Wiki** | 10 | Pédagogie et études |

### Les 10 bureaux BAVI

BAVI = l'organisation des connaissances de LEO en bureaux spécialisés :

| Bureau | Rôle | Privé/Pro |
|:-------|:-----|:---------:|
| 🦁 **LEO** | Dossiers personnels, analyses | Privé |
| 🔧 **Michel** | Infrastructure Hermes | Privé |
| 🧭 **Sylvia** | Voyages camping-car | Privé |
| 🎓 **Emile** | Pédagogie, mémoire | Privé |
| 🩺 **Virginie** | Médical | Privé |
| 🏛️ **Robert** | Conseil stratégique IT | **PRO** |
| 💰 **Sophie** | Pilotage économique | **PRO** |
| 📋 **Gérard** | Documentation T600 | Technique |
| 🛡️ **AO** | Assurance Obligatoire | **PRO** |
| 📚 **Connaissance** | Base de connaissance centralisée — bibliothèque cas IA, référentiels | Privé |
| 📦 **Versioning** | Gestion des versions | Technique |

## Les leçons apprises

### 12/06 — Trop de profils tue le profil

**Erreur :** Création d'un profil `local` pour Ollama. Arrêt du gateway `local` = perte totale d'accès Telegram.

**Leçon :** Structurer les profils par domaine (default/leo-copilot/bavi-leo), Ollama par API directe. **Fiabilité > flexibilité.**

### 13/06 — La précipitation coûte cher

**Erreur :** Actions sans réflexion préalable = régressions multiples (mauvais token, OAuth expiré, envoi multiple d'email).

**Leçon :** Avant chaque action, identifier 2-3 approches, peser le pour/contre, choisir.

### 14/06 — Les crons doivent être robustes

**Erreur :** Crons qui utilisaient le mauvais Python, scripts introuvables, identité Git manquante.

**Leçon :** Uniformisation — wrappers shell + no_agent + chemins absolus + identité Git dans le script.

### 24/06 — Gemini API directe, pas de proxy

**Erreur :** Un proxy Copilot compliqué et instable entre Hermes et Gemini.

**Leçon :** API directe (OpenAI-compatible). Moins de couches = moins de pannes. Latence passée de ~15s à < 2s.

## 📊 Chiffres clés

| Métrique | Valeur |
|:---------|:-------|
| Crons actifs | **14** (13 no_agent) |
| Skills installés | **126** |
| Dashboards | **1** (central 4 onglets ✅) |
| Wikis | **5** (98 pages total) |
| Repos GitHub | **20** |
| Consommation DeepSeek/jour | **~quelques centimes** |
| Machine hôte | **1** (serveur LEO uniquement) |

## 📝 À retenir

- LEO = 1 serveur principal + 5 bots Telegram + 1 dashboard central (9 onglets) + 38 crons + 130+ skills
- Tout tourne sur Hermes Agent dans un conteneur Docker supervisé par s6
- Le secret : une organisation stricte (profils, bureaux, skills) qui permet à l'agent de gérer la complexité
- Les erreurs du passé ont forgé les règles du présent

---

**[Chapitre suivant → Installation rapide](ch04-installation-rapide.md)**
# Installation sur Linux (Debian/Ubuntu)

## 1. Prérequis

- Un serveur ou PC sous **Debian 12+** ou **Ubuntu 22.04+**
- **Python 3.11+**
- **Curl**
- Un compte GitHub
- (Optionnel) Un GPU NVIDIA pour accélérer les LLM locaux

## 2. Installer Hermes Agent (méthode officielle)

```bash
# Méthode recommandée — script d'installation automatique
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Ce script :
- Détecte votre OS et architecture
- Installe les dépendances système nécessaires
- Télécharge la dernière version d'Hermes
- Crée un environnement virtuel isolé
- Vous guide dans la configuration initiale

### Installation manuelle (alternative)

Si vous préférez une installation manuelle ou que le script ne fonctionne pas :

```bash
# Cloner le dépôt
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent

# Créer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# Installer Hermes
pip install -e .
```

## 3. Configurer Hermes

```bash
# Assistant de configuration interactif
hermes setup

# Vérifier que tout est OK
hermes doctor
```

Le wizard de configuration vous guidera pour :
- Choisir votre fournisseur LLM principal (`hermes model`)
- Configurer votre profil Telegram (optionnel)
- Créer votre profil par défaut

## 4. Connecter un LLM

### Avec DeepSeek (recommandé pour débuter)

```bash
# Ajouter votre clé DeepSeek dans .env
echo "DEEPSEEK_API_KEY=votre_clé_ici" >> ~/.hermes/.env

# Configurer le provider DeepSeek
hermes config set model.default deepseek-v4-flash
hermes config set model.provider deepseek
```

### Avec Ollama (local, gratuit)

```bash
# Installer un modèle
ollama pull qwen2.5:7b

# Configurer Hermes pour utiliser Ollama
hermes config set model.default qwen2.5:7b
hermes config set model.provider ollama
hermes config set model.base_url "http://localhost:11434/v1"
```

## 5. Lancer Hermes

```bash
# En mode interactif (terminal)
hermes
# ou : hermes chat

# En mode one-shot (requête unique)
hermes chat -q "Dis bonjour, je suis ton nouvel assistant"

# Avec Telegram (après configuration du bot)
hermes gateway run
# ou en service :
hermes gateway install
hermes gateway start
```

## 6. Vérifier l'installation

```bash
# Test simple
hermes chat -q "Dis bonjour, je suis ton nouvel assistant"

# Diagnostiquer les problèmes
hermes doctor --fix

# Voir l'état des composants
hermes status
```

## Problèmes courants

| Problème | Solution |
|----------|----------|
| `ModuleNotFoundError: No module named '...'` | Vérifier que le venv est activé |
| `pip` introuvable | `sudo apt install python3-pip` |
| Erreur de permission | Utiliser un utilisateur normal (pas root) |
| Port déjà utilisé | Modifier le port dans `config.yaml` |

## Ressources

- [Documentation officielle Hermes](https://hermes-agent.nousresearch.com/docs)
- [GitHub Hermes Agent](https://github.com/NousResearch/hermes-agent)
# Chapitre 4 — Installation rapide

> *Un assistant IA opérationnel en 5 minutes chrono*

---

Assez de théorie. Installons Hermès et faisons notre premier test.

## Prérequis

- **Linux** (Debian/Ubuntu recommandé), **macOS**, ou **Windows avec WSL2**
- **curl** installé (99% des systèmes l'ont)
- **Git** (optionnel mais recommandé)
- 1 Go d'espace disque libre

## Installation (Linux / macOS)

Une seule commande :

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

L'installateur détecte automatiquement votre système, installe les dépendances, et ajoute Hermès à votre PATH.

**Que se passe-t-il en coulisses :**
1. Téléchargement de la dernière version
2. Création d'un environnement virtuel Python
3. Installation des dépendances
4. Configuration minimale automatique

Après installation, fermez et rouvrez votre terminal, ou :

```bash
source ~/.bashrc
```

## Premier lancement

```bash
# Lancer Hermès en mode interactif
hermes
```

Vous devriez voir apparaître l'interface :

```
┌─────────────────────────────────────────────────────────┐
│  ⚕ Hermes Agent v0.17.0                                │
│  Type /help for slash commands, /quit to exit            │
└─────────────────────────────────────────────────────────┘

You >
```

Félicitations 🎉 — votre premier agent IA tourne !

### Test rapide

```bash
hermes chat -q "Hello, qui es-tu ?"
```

Hermès vous répond. Simple.

## Configuration minimale

Par défaut, Hermès n'a pas de clé API LLM — il vous demandera d'en configurer une au premier lancement. Vous avez plusieurs options :

### Option A : DeepSeek (recommandé pour débuter)

Créez un compte sur [platform.deepseek.com](https://platform.deepseek.com) et récupérez votre clé API. Ajoutez-la ensuite :

```bash
hermes config set model.default deepseek-v4-flash
hermes config set model.provider deepseek
```

Puis éditez le fichier `.env` :

```bash
hermes config env-path
# Ajoutez : DEEPSEEK_API_KEY=votre_clé_ici
```

### Option B : Ollama (100% gratuit, local)

Si vous avez un GPU ou un CPU récent :

```bash
# Installer Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Télécharger un modèle
ollama pull qwen2.5:7b  # 4 Go, bon rapport qualité/ressources

# Configurer Hermes
hermes config set model.default qwen2.5:7b
hermes config set model.provider ollama
```

Pas de clé API, pas de compte, tout tourne chez vous.

### Option C : Gemini (gratuit, cloud)

```bash
# Obtenez une clé sur https://aistudio.google.com/apikey
export GEMINI_API_KEY=votre_clé_ici

# Configuration
hermes config set model.default gemini-2.5-flash
```

## Vérification de l'installation

```bash
hermes doctor
```

Cette commande vérifie :
- ✅ Que les dépendances sont installées
- ✅ Que la configuration est valide
- ✅ Que les clés API sont accessibles
- ✅ Que les outils système sont disponibles

Un rapport s'affiche. Si tout est vert, vous êtes prêt.

## Et ensuite ?

Vous avez un agent IA de base. Mais un agent seul dans son terminal, c'est un peu comme un smartphone sans applications. La vraie puissance arrive quand vous :

1. **Connectez Telegram** (Chapitre 5) — pour parler à votre agent depuis votre téléphone
2. **Ajoutez des skills** (Chapitre 8) — pour qu'il sache faire des choses
3. **Configurez des providers** (Chapitre 6) — pour optimiser coût et performance
4. **Planifiez des tâches** (Chapitre 26) — pour qu'il travaille sans vous

### ⚠️ Piège à éviter

> Ne pas tout vouloir configurer le premier jour.

Commencez avec un seul provider (DeepSeek ou Ollama). Ajoutez Telegram une fois que l'agent répond correctement en ligne de commande. Ajoutez les skills un par un. La précipitation est l'ennemie de la fiabilité — LEO en a fait l'expérience.

Si vous rencontrez des problèmes :

```bash
# Voir les logs
hermes --verbose

# Réinstaller proprement
hermes uninstall
# Réinstaller
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

## 📝 À retenir

| Étape | Commande |
|:------|:---------|
| Installer | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| Lancer | `hermes` |
| Tester | `hermes chat -q "Bonjour"` |
| Diagnostiquer | `hermes doctor` |
| Configurer provider | `hermes model` |

---

**[Partie II → Configurer son assistant](../02-configurer/ch05-gateway.md)**

> **💡 Astuce :** Vous voulez voir un exemple concret ? Passez directement à [l'architecture complète de LEO](../annexes/exemple-leo-complet.md) en annexe.
# Installation sur Windows

Hermes Agent fonctionne nativement sous Linux. Sur Windows, la méthode recommandée est **WSL 2** (Windows Subsystem for Linux).

## 1. Installer WSL 2

### 1.1 Activer WSL

Ouvrez **PowerShell en mode Administrateur** et exécutez :

```powershell
# Activer WSL
wsl --install

# Redémarrer l'ordinateur quand demandé
```

Cette commande installe :
- WSL 2
- Une distribution Ubuntu par défaut
- Le noyau Linux

### 1.2 Vérifier l'installation

```powershell
wsl --status
wsl --list --verbose
```

Vous devriez voir une distribution Ubuntu en cours d'exécution avec WSL version 2.

## 2. Installer Python et Git dans WSL

Ouvrez Ubuntu depuis le menu Démarrer ou avec :

```powershell
wsl
```

Dans le terminal Ubuntu :

```bash
# Mise à jour
sudo apt update && sudo apt upgrade -y

# Installer les dépendances
sudo apt install -y python3 python3-venv python3-pip git curl
```

## 3. Installer Hermes Agent

Suivez maintenant les mêmes étapes que pour Linux.

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## 4. Accéder à Hermes depuis Windows

### Via le terminal WSL

Depuis PowerShell ou CMD :

```powershell
wsl
# Vous êtes maintenant dans Ubuntu
# Activez votre environnement
cd ~/hermes-agent
source .venv/bin/activate
hermes run
```

### Recommandation : utilisez Windows Terminal

[**Windows Terminal**](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701) est l'application recommandée pour utiliser Hermes sous Windows :

- Onglets multiples (PowerShell + WSL côte à côte)
- Prise en charge complète des couleurs et emojis
- Raccourcis clavier personnalisables

## 5. (Optionnel) Accès aux fichiers Windows depuis WSL

Vos fichiers Windows sont accessibles depuis WSL via :

```bash
# Disque C: monté automatiquement
ls /mnt/c/Users/VotreNom/

# Créer un alias pratique
echo 'alias winhome="cd /mnt/c/Users/VotreNom/"' >> ~/.bashrc
source ~/.bashrc
```

## 6. (Optionnel) Installer Ollama sur Windows

Ollama a une version Windows native :

1. Téléchargez depuis [ollama.com/download](https://ollama.com/download)
2. Installez et lancez Ollama
3. Depuis WSL, Hermes peut accéder à Ollama via l'API :

```bash
# Configurer Hermes pour utiliser Ollama sur Windows
hermes config set providers.custom.ollama.base_url "http://host.docker.internal:11434/v1"
hermes config set providers.custom.ollama.api_key "ollama"
```

L'adresse `host.docker.internal` permet à WSL de communiquer avec les services Windows.

## Différences clés avec Linux

| Aspect | Linux natif | WSL Windows |
|--------|-------------|-------------|
| Performances | Optimal, bare-metal | ~95% (excellentes) |
| GPU pour Ollama | Direct (CUDA/NVIDIA) | Nécessite CUDA dans WSL |
| Démarrage auto | Systemd | Lancement manuel ou tâche planifiée |
| Accès réseau | Direct | Configuration supplémentaire |
| Mise à jour | `apt update` | Pareil (dans WSL) |

## Ressources

- [Installer WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install)
- [Windows Terminal](https://github.com/microsoft/terminal)
- [Ollama pour Windows](https://ollama.com/download)
# Profils, gateways et skills

## Profils

Un **profil** est une instance isolée d'Hermes avec sa propre configuration, ses propres clés API, sa mémoire et ses sessions. Chaque profil devient aussi une commande séparée.

```bash
# Créer un profil → crée aussi l'alias "mon-profil"
hermes profile create mon-profil

# Utiliser le profil
mon-profil chat           # alias complet
hermes -p mon-profil chat # flag explicite
```

Structure d'un profil dans `~/.hermes/profiles/<nom>/` :

```
~/.hermes/profiles/mon-profil/
├── config.yaml     # Modèle, provider, outils
├── .env            # Clés API, tokens
├── SOUL.md         # Personnalité
├── memories/       # Mémoire persistante
├── skills/         # Skills dédiés
├── sessions/       # Sessions du profil
├── cron/           # Tâches planifiées
└── logs/           # Logs
```

### Règle LEO : profils spécialisés

> *"Un seul profil, un seul gateway, tout dedans."*

La tentation est grande de créer un profil par usage (un pour les conversations, un pour le batch, un de secours). **Ne faites pas ça.** Chaque profil supplémentaire ajoute de la complexité et des points de défaillance.

- **Un seul profil** (`default`) — tout votre assistant vit dedans
- **plusieurs providers** au sein du même profil (DeepSeek + Ollama + Gemini)
- **Zéro bascule de profil** — la fiabilité avant tout

| Propriété | Configuration | Description |
|-----------|--------------|-------------|
| **Modèle** | `model.default` | LLM principal (ex: `deepseek-v4-flash`) |
| **Provider** | `model.provider` | Fournisseur (ex: `deepseek`, `openrouter`) |
| **Gateway** | `gateways.telegram.bot_token` | Token du bot Telegram |
| **Outils** | `hermes tools` | Toolsets activés par plateforme |
| **Skills** | `hermes skills install <id>` | Procédures chargées automatiquement |

### Commandes profils

```bash
# Lister les profils
hermes profile list

# Créer un profil (vide)
hermes profile create mon-profil

# Créer avec clonage de la config actuelle
hermes profile create mon-profil --clone

# Créer en clonant depuis un autre profil
hermes profile create mon-profil --clone-from default

# Utiliser un profil par défaut
hermes profile use mon-profil

# Voir les détails
hermes profile show mon-profil

# Supprimer
hermes profile delete mon-profil

# Renommer
hermes profile rename ancien nouveau

# Exporter / Importer (tar.gz)
hermes profile export mon-profil
hermes profile import archive.tar.gz

# Lancer avec un profil spécifique
hermes -p mon-profil chat
hermes -p mon-profil chat -q "Bonjour"
```

## Gateways

Un **gateway** est le canal par lequel vous communiquez avec votre assistant.

### Gateway Telegram (recommandé)

Permet de parler à votre assistant depuis votre téléphone.

1. Créez un bot Telegram via [@BotFather](https://t.me/botfather)
2. Notez le token du bot
3. Configurez dans config.yaml :

```yaml
gateways:
  telegram:
    bot_token: "******"
    allowed_users:
      - "votre_username"
      - 123456789  # Votre user ID Telegram
```

4. Lancez le gateway :

```bash
hermes gateway start
```

### Gateway Discord

```yaml
gateways:
  discord:
    bot_token: "******"
```

### Gateway local (terminal)

```bash
# Mode terminal interactif (aucune configuration)
hermes
# ou : hermes chat
```

## Skills

Les **skills** sont des procédures que l'assistant charge pour savoir comment effectuer des tâches spécifiques. C'est la mémoire procédurale de votre assistant.

### Structure d'un skill

Un skill est un fichier `SKILL.md` dans le dossier `skills/` :

```markdown
---
name: mon-skill
description: "Faire X quand Y se produit"
---

# Mon Skill

## Quand l'utiliser
Quand [condition], faire [action].

## Procédure
1. Étape 1
2. Étape 2
3. Vérifier le résultat

## Pièges
- Attention à [piège connu]
```

### Skills essentiels (exemple LEO)

| Skill | Description |
|-------|-------------|
| `living-documentation` | Tenir la documentation à jour |
| `budget-tracking` | Suivi des coûts LLM |
| `leo-architecture` | Architecture et règles de fonctionnement |
| `routage-llm` | Quel LLM utiliser pour quelle tâche |
| `system-management` | Gestion des machines distantes |

### Bonnes pratiques

- **Un skill = une responsabilité** (pas de fourre-tout)
- **Versionnez** les skills (ils évoluent avec votre assistant)
- **Stockez les corrections dans les skills**, pas en mémoire passagère
- **Patchez** un skill obsolète plutôt que d'en créer un nouveau

## Pour aller plus loin

- [Documentation Hermes : Skills](https://hermes-agent.nousresearch.com/docs)
- Voir `02-configuration/providers.md` pour la configuration LLM
- Voir `exemples/LEO.md` pour l'architecture complète
# Configuration des providers LLM

Hermes Agent peut utiliser plusieurs fournisseurs de modèles de langage (LLM). Voici comment configurer les plus courants.

## Principe

```
Un seul profil = plusieurs providers disponibles
       │
       ├── Provider principal → Conversations, tâches complexes
       ├── Provider local → Tâches simples, gratuit, privé
       └── Provider fallback → Sécurité si le principal plante
```

## DeepSeek (recommandé pour le provider principal)

DeepSeek offre un excellent rapport qualité/prix avec son API.

### 1. Créer un compte

1. Allez sur [platform.deepseek.com](https://platform.deepseek.com)
2. Créez un compte
3. Rechargez du crédit (quelques dollars suffisent pour commencer)
4. Générez une clé API dans la section API Keys

### 2. Configurer

```bash
# Dans votre .env (recommandé pour les clés API)
echo "DEEPSEEK_API_KEY=sk-..." >> ~/.hermes/.env

# Dans votre config.yaml
hermes config set model.default deepseek-v4-flash
hermes config set model.provider deepseek
```

Ou éditez `config.yaml` manuellement :

```yaml
model:
  default: deepseek-v4-flash
  provider: deepseek
```

La clé API se trouve dans `.env` (pas dans `config.yaml`) :

```bash
# ~/.hermes/.env
DEEPSEEK_API_KEY=sk-...
```

### 3. Vérifier

```bash
hermes chat -q "Quel est mon solde DeepSeek ?"
```

## Ollama (provider local, gratuit)

Ollama exécute des LLM sur votre machine. Gratuit, privé, sans consommation de tokens.

### 1. Installer Ollama

```bash
# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows → Téléchargez depuis ollama.com/download
```

### 2. Télécharger un modèle

```bash
# Modèle recommandé pour l'assistant
ollama pull qwen2.5:7b

# Autres modèles
ollama pull llama3.1:8b    # Meta Llama 3.1
ollama pull mistral:7b     # Mistral
```

### 3. Configurer Hermes

```bash
# Configurer via CLI
hermes config set model.default qwen2.5:7b
hermes config set model.provider ollama
hermes config set model.base_url "http://localhost:11434/v1"
```

Ou dans `config.yaml` :

```yaml
model:
  default: qwen2.5:7b
  provider: ollama
  base_url: "http://localhost:11434/v1"
  api_key: "ollama"  # Valeur arbitraire, non utilisée
```

### 4. Vérifier

```bash
curl http://localhost:11434/api/tags
```

## Google Gemini (fallback)

Gemini peut servir de provider de secours si le principal est indisponible.

### 1. Obtenir une clé

1. Allez sur [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Créez une clé API (gratuite avec quota limité)

### 2. Configurer

```yaml
# Dans config.yaml — comme fallback
fallback_providers:
  - provider: google
    model: gemini-2.5-flash
```

Stockez la clé dans `.env` :

```bash
echo "GEMINI_API_KEY=AIza..." >> .env
```

## Grâce à un assistant déjà configuré

Si vous configurez votre assistant comme **LEO**, l'arbitrage entre providers est automatique :

| Tâche | Provider utilisé | Coût |
|-------|-----------------|------|
| Conversation normale | DeepSeek 🤖 | Payant (faible) |
| Traitement batch, analyse simple | Ollama 🏠 | Gratuit |
| Secours si plantage | Gemini ⚡ | Gratuit (quota) |
| Scripts planifiés | Aucun LLM (no_agent) | 0 |

## Configuration avancée

### Variables d'environnement (recommandé pour les clés)

Créez un fichier `.env` à côté de `config.yaml` :

```bash
DEEPSEEK_API_KEY="sk-..."
GEMINI_API_KEY="AIza..."
OPENAI_API_KEY="sk-..."  # Si vous utilisez OpenAI
```

### Plusieurs providers dans un seul profil

```yaml
model:
  default: deepseek-v4-flash
  provider: deepseek
  base_url: ""  # URL par défaut du provider
  api_key: "${DEEPSEEK_API_KEY}"  # Référence variable d'environnement

# Provider fallback (Gemini)
providers:
  google:
    api_key: "${GEMINI_API_KEY}"

fallback_providers:
  - provider: google
    model: gemini-2.5-flash
```

Ce n'est pas grave si votre fichier `config.yaml` est plus ou moins complexe. L'important est qu'il fonctionne pour **vous**.

## Pour aller plus loin

- Voir la [documentation des providers Hermes](https://hermes-agent.nousresearch.com/docs)
- Voir `02-configuration/profiles.md` pour les profils et gateways
# Multi-bots : pourquoi 5 bots valent mieux qu'un

LEO ne tourne pas avec un seul bot Telegram, mais avec **cinq bots spécialisés** (et bientôt quatre). Chaque bot a son propre profil Hermes, son propre modèle, son propre rôle — et ils communiquent entre eux.

## Pourquoi plusieurs bots ?

Un seul bot peut tout faire. Alors pourquoi en créer plusieurs ?

### 1. Séparation des responsabilités

``` 
Un seul bot                                                 5 bots spécialisés
┌─────────────────────┐           ┌──────────┐ ┌──────────┐ ┌──────────┐
│ 🦁 LEO              │           │ 🦁 LEO   │ │ 🔧       │ │ 🧭       │
│                     │           │ Central  │ │ Copilote │ │ Sylvia   │
│ • Analyses          │           │          │ │          │ │          │
│ • Emails            │    →      │ Hub      │ │ Infra    │ │ Voyages  │
│ • Infra             │           │ général  │ │ Système  │ │ Roadbooks│
│ • Voyages           │           └──────────┘ └──────────┘ └──────────┘
│ • Mémoire           │
└─────────────────────┘
```

Avec un seul bot, tout est mélangé. Avec plusieurs bots :
- **LEO** (default) : le hub central, votre premier interlocuteur — analyses, emails, classification, documentation
- **Michel** (leo-copilot) : l'ingénieur infrastructure — crons, dashboards, n8n, budget, système (root sudo)
- **Sylvia** (bavi-leo) : la voyageuse — roadbooks camping-car, itinéraires, cartes OSM

### 2. Modèles adaptés à chaque usage

| Bot | Modèle principal | Coût | Usage typique |
|:----|:-----------------|:----:|:--------------|
| LEO | DeepSeek V4 Flash | ~0,05 €/j | Quotidien, polyvalent |
| Michel | DeepSeek V4 Pro | ~0,10 €/tâche | Analyses complexes, infra |
| Sylvia | DeepSeek V4 Flash | ~0,03 €/j | Roadbooks, voyages |
| Fallback | Gemini 2.5 Flash | Gratuit (1M tokens) | Si DeepSeek indisponible |

### 3. Isolation des tokens et permissions

Chaque bot a son propre token Telegram. Si un token est compromis ou rate-limity, les autres bots continuent de fonctionner.

```
default.env
├── TELEGRAM_BOT_TOKEN=881242...  ← Léo (vous)
├── TELEGRAM_ALLOWED_USERS=8718957859

leo-copilot.env
├── TELEGRAM_BOT_TOKEN=899720...  ← Michel
├── TELEGRAM_ALLOWED_USERS=8718957859

bavi-leo.env
├── TELEGRAM_BOT_TOKEN=885780...  ← Sylvia
├── TELEGRAM_ALLOWED_USERS=8718957859,8822960747
```

## Architecture des profils

### Créer un profil

```bash
hermes profile create leo-copilot
```

Cette commande crée un dossier `~/.hermes/profiles/leo-copilot/` avec un `config.yaml` vierge et prépare l'alias `leo-copilot` (vous pourrez utiliser `leo-copilot chat` directement).

### Structure d'un profil

```bash
~/.hermes/profiles/leo-copilot/
├── config.yaml        # Modèle, provider, outils, permissions
├── .env               # Token Telegram, clés API (gardé secret)
├── SOUL.md            # Personnalité, règles, contexte permanent
├── memories/          # Mémoire persistante (MEMORY.md + USER.md)
├── skills/            # Skills synchronisés depuis le profil source
├── cron/              # Tâches planifiées propres à ce profil
└── sessions/          # Historique des conversations
```

### Le fichier SOUL.md

C'est le cœur de la personnalité du bot. Il définit qui il est, ce qu'il fait et comment il se comporte.

```markdown
# Michel — Infrastructure

Tu es Michel, l'ingénieur infrastructure de l'écosystème LEO.

Tu gères :
- 38 crons automatisés (+6 hôte)
- 1 dashboard central (4 onglets)
- 3 workflows n8n (2 actifs)
- Les gateways Hermes
- Le budget DeepSeek

Tu as accès root complet (sudo) sur la machine.
```

### Fichier config.yaml

Exemple de configuration pour un profil spécialisé infra :

```yaml
model:
  default: deepseek-v4-pro        # Modèle puissant pour l'infra
  provider: deepseek
fallback_providers: '[{"provider": "gemini", "model": "gemini-2.5-flash"}]'
display:
  language: fr
timezone: Europe/Brussels
```

## Communication entre profils

Les profils peuvent partager des informations de plusieurs façons :

### 1. Mémoire partagée (symlinks)

```bash
# Les deux profils pointent vers les mêmes fichiers
ln -s /opt/data/memories/MEMORY.md /opt/data/profiles/leo-copilot/memories/MEMORY.md
ln -s /opt/data/memories/USER.md /opt/data/profiles/leo-copilot/memories/USER.md
```

Quand un bot met à jour sa mémoire, l'autre voit les changements automatiquement.

### 2. Skills synchronisés

Le profil principal (source de vérité) synchronise ses skills vers les autres profils toutes les 30 minutes :

```bash
# Sync automatique intégrée à Hermes (curator)
# Le profil default = source → pousse vers leo-copilot, bavi-leo, emile
```

### 3. Délégation de tâches

LEO (hub central) peut déléguer des tâches complexes à Michel :

```yaml
# Dans le config.yaml de Michel
delegation:
  model: deepseek-v4-pro
  max_concurrent_children: 3
  max_spawn_depth: 1
  orchestrator_enabled: true
```

## Exemple réel : l'écosystème LEO

| Profil | Bot Telegram | Modèle | Rôle | 
|:-------|:-------------|:-------|:-----|
| `default` | LEO 🦁 | DeepSeek V4 Flash | Hub central — analyses, emails, docs |
| `leo-copilot` | Michel 🦁 | DeepSeek V4 Pro | Infrastructure — crons, système, budget |
| `bavi-leo` | Sylvia 🚐 | DeepSeek V4 Flash | Roadbooks camping-car, voyages |
| `emile` | Émile 🎓 | DeepSeek V4 Flash | Assistant pédagogique mémoire |

**Règle d'or** : si un sujet est technique (infra, cron, dashboard), LEO redirige vers Michel. Si c'est un voyage, LEO redirige vers Sylvia. Les bots savent qui fait quoi.
# Skills : le super-pouvoir d'Hermès

Un skill Hermes est un fichier Markdown qui décrit **comment accomplir une tâche spécifique**. C'est le mécanisme qui transforme un assistant généraliste en expert multi-domaines.

## Principe

```
Skill = fichier .md + dossier
├── SKILL.md          ← Les instructions : contexte, étapes, pièges
├── references/       ← Documentation complémentaire
├── templates/        ← Modèles de sortie
└── scripts/          ← Scripts exécutables
```

Quand vous posez une question, Hermes charge les skills pertinents dans son contexte et les utilise comme guide d'exécution.

### Exemple : un skill "Installation Nginx"

```markdown
---
name: nginx-install
description: Installer et configurer Nginx avec Cloudflare Tunnel
category: infrastructure
---

# Installation Nginx + Cloudflare

## Étapes
1. Installer Nginx : `apt install nginx -y`
2. Copier la configuration : `/etc/nginx/sites-available/tofdan.be`
3. Activer le site : `ln -s ... /etc/nginx/sites-enabled/`
4. Tester : `nginx -t`
5. Recharger : `systemctl reload nginx`

## Pièges
- Ne pas ouvrir le port 443 (Cloudflare gère HTTPS)
- Vérifier que le tunnel Cloudflare est actif avant
```

## L'écosystème de skills LEO

Environ **126 skills** répartis en **22 catégories** :

```
skills/
├── infrastructure/     ← Docker, Nginx, Cloudflare, backup
│   └── bureau-michel/SKILL.md
├── github/             ← PRs, issues, code review, auth
├── creative/           ← ASCII art, design, vidéo, musique
├── data-science/       ← Jupyter, analyse de données
├── email/              ← Gmail, classification inbox zero
├── productivity/       ← Dashboards, wikis, OCR, PowerPoint
├── research/           ← Arxiv, veille IA, blogwatcher
├── media/              ← GIF, YouTube, audio
├── software-dev/       ← TDD, debug, code review
├── smart-home/         ← Philips Hue (openhue)
├── note-taking/        ← Obsidian
├── mlops/              ← LLM eval, vLLM, HuggingFace
└── 10+ autres...
```

### Skills système vs skills customs

**Skills système** (intégrés à Hermes Agent) :
- `hermes-agent` : configurer Hermes lui-même
- `computer-use` : piloter un bureau à distance
- `plan` : planifier des tâches complexes

**Skills customs** (écrits par vous ou la communauté) :
- `bureau-michel` : infrastructure n8n et déploiement
- `voyages-wiki` : publication de roadbooks
- `gmail-inbox-zero` : classification automatique des emails

### Comment Hermes charge les skills

```
1. Vous dites : "Installe Nginx sur le serveur"
2. Hermes cherche des skills pertinents
3. Trouve "infrastructure/nginx-install"
4. Charge le SKILL.md dans son contexte
5. Exécute les étapes décrites
6. Applique les pièges et vérifications
```

## Créer son premier skill

### 1. Structure minimale

```markdown
---
name: mon-premier-skill
description: Un exemple simple
---

# Mon premier skill

Fait ceci, puis cela, puis vérifie.
```

### 2. Avec frontmatter complet

```yaml
---
name: backup-gdrive
description: Backup des profils Hermes vers Google Drive
category: infrastructure
metadata:
  hermes:
    tags: [backup, gdrive, hermes]
---
```

### 3. Avec sous-dossiers

```bash
mon-skill/
├── SKILL.md
├── references/
│   └── api-endpoints.md
├── templates/
│   └── rapport.md
└── scripts/
    └── backup.py
```

Les scripts dans `scripts/` peuvent être appelés directement par le skill.

### 4. Règles d'or

1. **Frontmatter obligatoire** : `name`, `description`, `category`
2. **Un skill = une tâche** : pas de fourre-tout
3. **Pitfalls** : documentez ce qui peut mal tourner
4. **Vérification** : incluez une étape de validation
5. **Réutilisable** : écrivez pour que n'importe qui (ou vous-même dans 3 mois) puisse l'exécuter

## Skills et profils : la source de vérité

Dans l'écosystème LEO, le profil `default` (LEO) est la **source de vérité** des skills. Les autres profils (Michel, Sylvia, Émile) reçoivent les skills par **synchronisation automatique** toutes les 30 minutes.

```
default (source) ──sync 30min──→ leo-copilot
                ──sync 30min──→ bavi-leo (Sylvia)
                ──sync 30min──→ emile
```

Avantage : vous mettez à jour un skill une fois, et tous les bots en bénéficient.

## Skills préinstallés utiles

| Skill | Catégorie | Utilité |
|:------|:----------|:--------|
| `hermes-agent` | Système | Configurer Hermes lui-même |
| `github-pr-workflow` | GitHub | Créer et gérer des PRs |
| `gmail-inbox-zero` | Email | Classifier ses emails |
| `plan` | Dev | Planifier un projet complexe |
| `test-driven-development` | Dev | Coder en TDD |
| `youtube-content` | Media | Analyser des vidéos YouTube |
| `obsidian` | Notes | Lire/écrire dans Obsidian |
| `open-hue` | Maison | Contrôler les lumières Philips Hue |

## Gestion des skills avec le curator

Hermes inclut un **curator** qui nettoie automatiquement les skills :
- Skills inactifs > 30 jours → marqués comme "stale"
- Skills inactifs > 90 jours → archivés
- Skills obsolètes → supprimés

```yaml
# Activation dans config.yaml
curator:
  enabled: true
  interval_hours: 168     # Une fois par semaine
  stale_after_days: 30
  archive_after_days: 90
  prune_builtins: true     # Nettoie aussi les skills système inutilisés
```

## En résumé

| Concept | À retenir |
|:--------|:----------|
| **Skill** | Fichier .md qui décrit une tâche |
| **Catégorie** | Groupe de skills (infra, github, creative...) |
| **Source de vérité** | Un profil central push vers les autres |
| **Curator** | Nettoyage automatique des skills obsolètes |
| **Scripts** | Code exécutable dans `scripts/` |
| **Pitfalls** | Pièges documentés pour éviter les erreurs |
# Mémoire persistante et profils utilisateur

Un assistant qui ne se souvient de rien est inutile. Hermes Agent propose un système de mémoire persistante qui permet à votre bot de **se souvenir de vous entre les sessions**, même après un redémarrage.

## Les deux types de mémoire

### 1. MEMORY.md — La mémoire du système

C'est le carnet de bord de l'assistant. Il y note tout ce qui concerne l'infrastructure, les configurations, les procédures et les décisions.

```markdown
# Contenu typique
Infrastructure: serveur Ubuntu 26.04, 457Go SSD, Docker + n8n + ollama
§
Backup: quotidien vers GDrive à 04:00, rétention 7 jours
§
Budget DeepSeek: $60.31 restant, ~$0.03/jour
§
WiFi camping: "Camping Le Brasilia" — mot de passe en vault
```

### 2. USER.md — Le profil utilisateur

Contient tout ce que l'assistant sait sur vous : vos préférences, votre style, vos proches, vos habitudes.

```markdown
Christophe (Tofdan) — conseiller stratégique IT, Sombreffe, Belgique 🇧🇪
Bilingue français/néerlandais. Fuseau Europe/Brussels.
Femme: Sylvie. Filles: Émilie (30) et Camille (26) + Célestine 🎀
Chienne: Nala 🐶
§
Style: direct, action-first, zéro blabla. Exige vérification avant livraison.
```

## Comment ça marche

### Écriture automatique

Le système de mémoire s'active automatiquement :

```yaml
# Dans config.yaml
memory:
  memory_enabled: true          # Activer la mémoire
  user_profile_enabled: true     # Activer le profil utilisateur
  write_approval: false          # Écrire sans demander
  memory_char_limit: 2200        # Taille max de MEMORY.md
  user_char_limit: 1375          # Taille max de USER.md
  nudge_interval: 10             # Toutes les 10 interactions, demander si mise à jour
  flush_min_turns: 6             # Synchroniser tous les 6 tours
```

À chaque interaction, Hermes décide si une information est suffisamment importante pour être mémorisée.

### Emplacement des fichiers

```bash
~/.hermes/memories/
├── MEMORY.md        # Mémoire système
└── USER.md          # Profil utilisateur
```

Chaque profil Hermes a ses propres fichiers de mémoire.

## Partage de mémoire entre profils

Dans l'écosystème LEO, les profils peuvent **partager la même mémoire** via des liens symboliques :

```bash
# Créer un lien symbolique pour partager la mémoire
ln -s /opt/data/memories/MEMORY.md /opt/data/profiles/leo-copilot/memories/MEMORY.md
ln -s /opt/data/memories/USER.md /opt/data/profiles/leo-copilot/memories/USER.md
```

Avantage : quand un bot apprend quelque chose, l'autre le sait aussi immédiatement.

```
LEO (default) écrit ──→ /opt/data/memories/MEMORY.md
                              ↕ symlink
Michel lit ──→ /opt/data/profiles/leo-copilot/memories/MEMORY.md
                              (même fichier !)
```

## Cas pratique : la mémoire de LEO

### MEMORY.md (extrait réel)

```
RÈGLE commit : toute modif fichier repo git = commit + push immédiat
§  
Wikis: BAVI_LEO=portail, hermes-christophe=source, les2→sync+push
§
hermes binaire: /opt/hermes/.venv/bin/hermes (pas sur PATH)
§
CRASH+RECONSTRUCTION 30/06: sessions vidé→4 bots crash. 
Backup GDrive 73.7MB téléchargé + extrait. 4 gateways relancés.
§
Émile 🎓: emidanhier@gmail.com, @Bureau_ia_emilie_bot
```

### USER.md (extrait réel)

```
Christophe: Décisif, action directe, pattern-first.
Exige vérification AVANT livraison (curl 200, grep valeur réelle).
Zéro tolérance oubli sync (BAVI_LEO + hermes-christophe).
Préfère process automatisé aux corrections.
```

## La synchronicité cross-session

La mémoire traverse les sessions. Si vous dites "souviens-toi que mon serveur est à Bruxelles", l'information persiste :

```
Session 1 : "Mon serveur est à Bruxelles"
  → Hermes écrit dans USER.md : "Serveur situé à Bruxelles (Eвропа/Brussels)"

Session 2 (le lendemain) : "Quelle est l'IP de mon serveur ?"
  → Hermes lit USER.md : "Serveur situé à Bruxelles..."
  → Peut répondre sans avoir à redemander
```

## Limites et bonnes pratiques

| Limite | Explication |
|:-------|:------------|
| **Taille max** | 2 200 caractères pour MEMORY.md, 1 375 pour USER.md |
| **Pas de recherches** | La mémoire est injectée en entier. Trop d'informations → contexte dilué |
| **Pas de structure** | Format libre, pas de base de données |
| **Un seul fichier** | Pas de sous-dossiers, pas de clés-valeurs |

### Conseils pour une mémoire efficace

1. **Priorisez ce qui est stable** : les préférences, l'infrastructure, les règles
2. **N'écrivez pas l'évident** : inutile de noter "le ciel est bleu"
3. **Consolidez régulièrement** : fusionnez les anciennes entrées, supprimez les obsolètes
4. **Séparez les faits des tâches** : les procédures vont dans les skills, pas dans la mémoire
5. **Utilisez les sauts de section** (`§`) pour séparer les sujets

## Voir aussi

- **Ch.8** : les skills (pour les procédures réutilisables)
- **Ch.3** : l'architecture LEO (comment s'organisent les profils)
- **Annexe A** : glossaire (mémoire persistante)
# Architecture bureaux : le système de dossiers intelligents

Au cœur de LEO se trouve un concept unique : **les bureaux BAVI** (Bureaux Agentiques Virtuels). Chaque bureau est un dossier intelligent spécialisé dans un domaine, avec ses propres règles, ses experts et ses modèles.

## Le constat de départ

Un assistant IA généraliste sait tout faire, mais il ne sait rien faire parfaitement. Quand vous lui demandez à la fois un calcul de budget et un roadbook camping-car, le résultat est moyen sur les deux.

La solution de LEO : **découper l'intelligence en bureaux spécialisés**.

```
Assistant généraliste
├── Parle un peu de tout
├── Mélange les contextes
└── Résultat = moyen partout

vs

10 bureaux spécialisés
├── Chacun son métier
├── Chacun ses modèles
├── Chacun ses règles
└── Résultat = excellent partout
```

## Les 10 bureaux LEO

| Bureau | Rôle | Statut |
|:-------|:-----|:------:|
| 🔧 **Michel** | Infrastructure — crons, dashboards, n8n, budget | ✅ Actif |
| 🤖 **LEO** | Hub central — analyses, dossiers personnels | ✅ Actif |
| 🧭 **Sylvia** | Voyages — roadbooks camping-car, itinéraires | ✅ Actif |
| 🎓 **Émile** | Pédagogie — assistant mémoire universitaire | ✅ Actif |
| 🏛️ **Robert** | Conseil stratégique IT — architectures, recommandations | ✅ Actif |
| 💰 **Sophie** | Pilotage financier — TCO, ROI, business cases | 📝 En reconstruction |
| 🏗️ **Gérard** | Documentation T600 — télescope automatisé | ✅ Actif |
| 🩺 **Virginie** | Médical — consultations pluridisciplinaires | ✅ Actif |
| 🛡️ **AO** | Assurance obligatoire — INAMI, eHealth | 📝 Structure prête |
| 📋 **Versioning** | Gestion des versions et des releases | 📝 Structure prête |

## Comment fonctionne un bureau

### 1. Un dossier dédié

Chaque bureau a son propre dossier dans `AGENT-PRO` :

```bash
BAVI/AGENT-PRO/
├── bureau-michel/        ← 🔧 Infrastructure
│   ├── index.md          ← Tableau de bord généré automatiquement
│   ├── analyse-*.md      ← Analyses produites
│   └── archive/          ← Anciennes analyses
├── bureau-leo/           ← 🤖 Hub central
├── bureau-sylvia/        ← 🧭 Voyages
└── ...
```

### 2. Des experts spécialisés

Chaque bureau peut faire appel à des sous-experts (agents CrewAI). Par exemple, le Bureau Robert a 16 experts :

```
Bureau Michel
├── 🔧 SysAdmin      — Administration du serveur
├── 🐳 DevOps        — Déploiement Docker
├── 📜 Scripteur     — Scripts Python/Bash
├── 📊 DataDoc       — Documentation et archives
├── 🌐 Networker     — Nginx, Cloudflare, DNS
├── 📈 DashBuilder   — Dashboards Chart.js
├── ⏰ CronMaster    — Crons Hermes (staggering)
└── 🛡️ GitGuardian   — Git, sync, clean trees
```

### 3. Des dispatch patterns

Les experts ne travaillent pas toujours seuls. Selon la tâche, le bureau active plusieurs experts en parallèle ou en séquence :

```mermaid
flowchart LR
    subgraph "Audit end-to-end"
        DD[📊 DataDoc] --> CD[📈 DashBuilder]
        CM[⏰ CronMaster] --> GG[🛡️ GitGuardian]
        NW[🌐 Networker]
    end
    
    subgraph "Debug cron"
        CM2[⏰ CronMaster] --> SC[📜 Scripteur]
        SC --> NW2[🌐 Networker]
    end
    
    subgraph "Sync cross-profil"
        SC2[📜 Scripteur] --> GG2[🛡️ GitGuardian]
        GG2 --> CM3[⏰ CronMaster]
    end
```

### 4. Des modèles adaptés

Chaque bureau utilise le modèle le plus adapté à son travail :

| Bureau | Modèle principal | Pourquoi |
|:-------|:-----------------|:---------|
| Michel | DeepSeek V4 Pro | Analyses complexes, décisions techniques |
| Sylvia | DeepSeek V4 Flash | Création de contenu, roadbooks |
| Robert | DeepSeek V4 Pro | Conseil stratégique, recommandations |
| Gérard | DeepSeek V4 Pro | Documentation technique, schémas |
| Émile | DeepSeek V4 Flash + Gemini (fallback) | Longs contextes, pédagogie |
| LEO | DeepSeek V4 Flash | Usage quotidien, polyvalent |

## Le cycle de production

Chaque analyse suit un workflow standardisé en **7 étapes** :

```
① Cadrage
   │  Comprendre la demande, définir le périmètre
   ▼
② Dispatch
   │  Quel bureau ? Quels experts ?
   ▼
③ Production
   │  Rédaction de l'analyse
   ▼
④ Croisement (si multi-experts)
   │  Confronter les analyses de plusieurs experts
   ▼
⑤ Synthèse
   │  Résumé, conclusions, recommandations
   ▼
⑥ Livrable
   │  Format final : analyse, rapport, note
   ▼
⑦ Archivage
   │  Sauvegarde dans AGENT-PRO + commit Git + publication wiki
```

### Variantes selon le type de livrable

| Type | Étapes | Description |
|:-----|:-------|:------------|
| **Analyse** | ①→③→⑤→⑥→⑦ | Analyse directe, pas de dispatch |
| **Rapport** | ①→②→③→④→⑤→⑥→⑦ | Cycle complet avec croisement |
| **Note** | ①→③→⑥ | Rapide, pas de dispatch ni synthèse |
| **Dossier** | ①→②→③→④→⑤→⑥→⑦ + archivage renforcé | Document complet |
| **Mémoire** | ①→②→③→④↔④↔④→⑤→⑥→⑦ | Croisement itératif (allers-retours) |

## Frontmatter standard

Chaque analyse a un en-tête YAML qui permet son indexation automatique :

```yaml
---
date: 2026-06-28
bureau: bureau-michel
version: v2
modele: deepseek-v4-pro
tags: [analyse, infrastructure, crons]
statut: archive
type: analyse
---
```

Ces métadonnées permettent au script `agent-pro-index.py` de générer automatiquement des tableaux de bord consolidés.

## Pourquoi ça marche

1. **Spécialisation** — chaque bureau ne fait qu'un métier, il le fait mieux
2. **Réutilisabilité** — une analyse peut être reprise par un autre bureau
3. **Traçabilité** — chaque document a une date, une version, un auteur
4. **Évolutivité** — on peut ajouter un bureau sans casser les autres
5. **Automatisation** — l'index des analyses est généré, pas écrit à la main

## Voir aussi

- **Ch.11** : Bureau Michel — l'infrastructure en détail
- **Ch.12** : Bureau Sylvia — les voyages
- **Ch.13** : Bureau Émile — la pédagogie
- **Ch.14** : Bureau Robert — le conseil stratégique
- **Ch.15** : Bureau LEO et les autres bureaux
# Bureau Michel : l'infrastructure

Le Bureau Michel est le bureau technique de LEO. Porté par **Michel** (profil `leo-copilot`), il gère tout ce qui touche au fonctionnement de l'infrastructure : crons, dashboards, n8n, Google APIs, Git, budget, serveur, sécurité.

C'est le padron de la machine — il a accès root complet (`sudo` sans restriction).

## Son rôle

```
Bureau Michel = l'ingénieur système de LEO
├── 🔧 38 crons automatisés (+6 hôte)
├── 📊 1 dashboard central (4 onglets)
├── 🔄 3 workflows n8n (2 actifs)
├── 🌐 Nginx + Cloudflare Tunnel
├── 🔒 UFW + SSL + DNS
├── 💰 Suivi du budget DeepSeek
├── 🖥️ Monitoring 3 machines
└── 🔑 Accès root complet (sudo)
```

## Les 16 experts du bureau Robert

| Expert | Compétence | Activer quand... |
|:-------|:-----------|:-----------------|
| 🔧 **SysAdmin** | Administration serveur (Nginx, UFW, Docker) | Installation service, config système |
| 🐳 **DevOps** | Déploiement conteneurs, CI/CD | Nouveau déploiement, mise à jour |
| 📜 **Scripteur** | Scripts Python/Bash, automation | Création de script, correction bug |
| 📊 **DataDoc** | Documentation, rapports, archives | Archivage analyse, production doc |
| 🌐 **Networker** | Cloudflare, DNS, ports, tunnels | Configuration réseau, problème DNS |
| 📈 **DashBuilder** | Dashboards Chart.js, GitHub Pages | Création dashboard, debug HTML |
| ⏰ **CronMaster** | Crons Hermes, staggering, scheduling | Création cron, erreur récurrente |
| 🛡️ **GitGuardian** | Git, sync Drive↔GitHub, clean trees | Dirty files, sync cross-repo |

## Infrastructure gérée

### Serveur LEO

```yaml
OS: Ubuntu 26.04 (resolute)
Kernel: 7.0.0
CPU: i7-7700K
RAM: 22.94 Go
GPU: Aucun (Ollama sur CPU)
SSD: 465 Go (/dev/sda2)
HDD: 1 To (/dev/sdb2 → /mnt/data)
```

### Conteneurs Docker

| Conteneur | Image | Rôle | Port |
|:----------|:------|:-----|:----:|
| `hermes-agent` | nousresearch/hermes-agent | Agent IA principal | — |
| `n8n` | n8nio/n8n | Automatisation workflows | 5678 |
| `ollama` | ollama/ollama | LLM local (qwen2.5:7b) | 11434 |
| *(code-server)* | code-server | VS Code web | 8081 |

Le conteneur Hermes a des **pleins pouvoirs** :
- Socket Docker monté en RW (`/var/run/docker.sock`)
- Filesystem hôte monté en RW (`/host`)
- Mode réseau `--network host` (accès direct à tous les ports)

### Nginx + Cloudflare

```
Utilisateur ──→ tofdan.be ──→ Cloudflare ──→ Tunnel ──→ Nginx (port 80)
                                                                  │
                                                                  ▼
                                                            /var/www/
                                                            ├── tofdan.be/
                                                            └── astro/
```

- **Nginx** : sert les sites statiques sur le port 80 seulement
- **Cloudflare** : gère le HTTPS (mode Flexible), le tunnel et le DNS
- **UFW** : ports ouverts 80, 443, 11434, 3389, 7844

### Machine hôte

| Machine | OS | RAM | Stockage | Rôle |
|:--------|:---|:---:|:--------:|:-----|
| **LEO** 🖥️ | Ubuntu 26.04 | 22 Go | 457 Go SSD + 1 To HDD | Serveur unique (toute la plateforme) |

## Les 38 crons (+ 6 hôte)

Les crons sont le cœur de l'automatisation. 14 tâches planifiées tournent 24/7, complétées par un **auto-fix-daemon** `*/15` qui assure la détection rapide :

### Crons horaires (métriques + dashboard)

```yaml
- Nom: Budget Check
  Horaire: 08:00, 20:00
  Action: Vérifie solde DeepSeek, alerte si < 10€
  Coût: 0€ (no_agent)

- Nom: Dashboard LEO
  Horaire: Toutes les heures
  Action: Collecte métriques → met à jour dashboard KPI
  Coût: 0€ (no_agent)

- Nom: Dashboard Machines
  Horaire: Toutes les heures
  Action: CPU/RAM/disque des 3 machines
  Coût: 0€ (no_agent)

- Nom: Dashboard Crons
  Horaire: Toutes les heures
  Action: Statut des 13 crons
  Coût: 0€ (no_agent)
```

### Crons quotidiens

```yaml
- Nom: Backup → GDrive
  Horaire: 04:00
  Action: Archive tous les profils + config → Google Drive
  Rétention: 7 jours
  Coût: 0€ (no_agent)

- Nom: Veille IA
  Horaire: 07:00
  Action: Collecte 15 sources RSS → analyse DeepSeek → email
  Coût: ~0,05 €/jour

- Nom: Sync Drive → GitHub
  Horaire: 18:00
  Action: Miroir bidirectionnel Drive ↔ GitHub
  Coût: 0€ (no_agent)

- Nom: Classifieur Gmail
  Horaire: Toutes les 15 min
  Action: Nouveaux emails → classification Ollama (9 labels)
  Coût: 0€ (Ollama local)
```

### Pourquoi "no_agent" ?

La plupart des crons utilisent le mode `no_agent = true`. Cela signifie qu'ils exécutent un script **sans LLM**, ce qui les rend totalement gratuits :

```yaml
# Cron avec LLM : coûte de l'argent à chaque exécution (~0,05 €)
cron-veille:
  no_agent: false  # DeepSeek analyse les articles

# Cron sans LLM : 0 € à chaque exécution
cron-metrics:
  no_agent: true   # Simple script bash/python
  script: collect-metrics.sh
```

Sur 38 crons Hermes, la plupart sont en **no_agent** (0$ LLM) — seuls quelques crons (veille IA, audit) utilisent un LLM. Le coût total des crons est d'environ **quelques centimes par jour**.

## Les 1 dashboard (4 onglets)

| Dashboard | URL | Contenu |
|:----------|:----|:--------|
| **LEO Dashboard** | `christophedanhier-hash.github.io/leo-dashboard/` | Synthèse, Analyses, Infra, BAVI (20 KPI, 4 charts) |

Tous les indicateurs sont dans **un seul dashboard HTML statique** avec 4 onglets :
1. Un script collecte les données → JSON
2. Un template Chart.js génère le HTML
3. Push sur GitHub Pages → site en ligne

## Budget DeepSeek

Le Bureau Michel suit le budget en continu via le dashboard LEO. Plutôt que de donner des chiffres précis (qui changent chaque jour), voici les **principes généraux** :

| Principe | Détail |
|:---------|:-------|
| **Provider principal** | DeepSeek Flash pour le quotidien |
| **Provider complexe** | DeepSeek Pro pour analyses ponctuelles |
| **Provider gratuit** | Ollama (local, CPU) pour classification et batch |
| **Fallback** | Gemini (gratuit, cloud) si DeepSeek indisponible |
| **Veille IA** | ~5-10 centimes/jour (DeepSeek Flash) |
| **Crons no_agent** | 0 € — 13 sur 14 |
| **Total mensuel estimé** | **~1-3 €/mois** |

> 💡 **Astuce** : Éviter Pro entre 08h et 12h (Bruxelles) = heures pleines ×2. Flash pour le routinier, Pro pour le complexe.

### DeepSeek V4 — Tarifs de référence (juillet 2026)

| Modèle | Prix standard (M tokens) | Heures pleines ×2 |
|:-------|:------------------------:|:------------------:|
| **Flash** | $0.14 in / $0.28 out | UTC 01-04 et 06-10 |
| **Pro** | $0.435 in / $0.87 out | UTC 01-04 et 06-10 |

> ⚠️ Les tarifs DeepSeek peuvent évoluer. Consultez [platform.deepseek.com](https://platform.deepseek.com) pour les prix à jour.

### Résilience post-crash (30 juin 2026)

Le 30 juin, un crash système a vidé les sessions des 4 bots et cassé les gateways. Leçons :
- **Backup automatisé** → GDrive toutes les 24h
- **auto-fix-daemon** `*/5` → remplace 3 crons monitoring
- **Mémoire partagée** par symlinks → plus de perte de contexte entre profils
- **collect-v2** → collecteur unifié (8 sources, JSON, 0 alerte) remplace des scripts disparates

## n8n — Workflows d'automatisation

> **📦 HISTORIQUE — Déprécié le 13/07/2026.** n8n a été remplacé par des scripts Python et l'auto-heal natif de Hermes. Les watchdogs et l'auto-heal fonctionnent désormais sans dépendance n8n.

n8n était utilisé pour les workflows qui nécessitent des webhooks ou des intégrations API :

- **n8n v2.26.8 Docker** — 3 workflows, **2 actifs** (remplacés)
- **3 credentials** (Google, GitHub, n8n) — désormais gérés par les scripts Hermes
- Accès via Tailscale uniquement (`100.92.102.28:5678`)
- **Base SQLite** dans un volume Docker dédié
- **Workflow emblématique : LEO Ping** — endpoint `GET /webhook/ping` → `{"response":"pong"}`

> **Consolidation post-crash** : passé de 6 à 3 workflows (2 actifs). Les workflows redondants ont été supprimés pour plus de stabilité.

## Auto-heal et watchdogs

Le système ne se contente pas de tourner — il se surveille :

```yaml
Auto-heal (toutes les 30-60 min, + auto-fix-daemon */5 min):
  ✅ Crons: 14/14 OK
  ✅ Ollama: UP (qwen2.5:7b responsive)
  ✅ n8n: UP (healthz 200) — v2.26.8
  ✅ Docker: 3/3 conteneurs up
  ✅ Disque: 21% utilisé (345 Go libre)
  ✅ Token LEO Google: OK
  ✅ collect-v2 → leo-unified.json: 8 sources, 0 alertes
  ✅ Mémoire partagée: symlinks default ↔ leo-copilot (temps réel)
  ✅ 4 gateways UP: default, leo-copilot, bavi-leo (Sylvia), emile
```

Les watchdogs surveillent en continu : code-server, n8n, dashboards, tunnels. Depuis le crash du 30 juin, un **auto-fix-daemon** (`*/5`) remplace 3 crons monitoring pour une détection infra-minute.

## En résumé

| Composant | Quantité | Coût mensuel |
|:----------|:--------:|:------------:|
| Crons | 14 | ~0 €/j (13 no_agent) |
| Dashboards | 1 central (4 onglets) | 0 € (GitHub Pages) |
| n8n workflows | 3 (2 actifs) | 0 € (self-hosted) |
| Machine hôte | 1 | 0 € (serveur local) |
| DeepSeek API | Flash + Pro | ~1-3 €/mois |
| **Total** | | **~1-3 €/mois** |

## Voir aussi

- **Ch.22** : Dashboards et monitoring (Partie V)
- **Ch.26** : Tâches planifiées — crons (Partie VI)
- **Annexe B** : Guide de démarrage rapide
# Bureau Sylvia : les voyages

Le Bureau Sylvia est le spécialiste des **roadbooks camping-car**. Accessible via le bot Telegram [@bavi_leo_voyages_bot](https://t.me/bavi_leo_voyages_bot), il produit des itinéraires complets avec cartes interactives, budgets et conseils pratiques.

## Son rôle

Sylvia ne planifie pas seulement des itinéraires — elle construit des **carnets de voyage complets** qui servent de guide pendant le trajet.

```
Bureau Sylvia = votre agence de voyage IA
├── 🗺️ Roadbooks détaillés (étapes, distances, campings)
├── 📏 Calcul Haversine (distances à vol d'oiseau)
├── 🗺️ Cartes OSM interactives (folium + leaflet)
├── 💰 Budget prévisionnel (péages, carburant, campings)
├── 🏕️ Campings et hébergements
└── 💡 Astuces camping-car (ZTL, hauteur, aires)
```

## Les experts du bureau

| Expert | Rôle |
|:-------|:-----|
| 🧭 **Curateur d'Expériences** | Conception de l'itinéraire, choix des étapes |
| 🚐 **Navigateur Camping-Car** | Distances, routes, aires, contraintes CC |
| 📝 **Journaliste de Bord** | Rédaction du carnet de voyage |

## Structure d'un roadbook

Chaque roadbook suit un format strict, testé sur des dizaines de voyages :

### 1. Header + Contexte

```markdown
# 🇮🇹 Voyage Italie — Septembre/Octobre 2026

> 🗓️ 15/09/2026 → 05/10/2026 | 🚐 21 jours | 📏 ~3 500 km

## 👥 Contexte du voyage
|               |                                |
|:--------------|:-------------------------------|
| **Voyageurs** | Christophe, Sylvie + 🐕 Nala  |
| **Véhicule**  | Camping-car 8m × 2.3m (h: 3m) |
| **Équipement**| 2 vélos électriques           |
```

### 2. Coût du service

| Métrique | Valeur |
|:---------|------:|
| Sessions IA | 12 |
| Tokens consommés | 240K IN / 78K OUT |
| Coût DeepSeek réel | ~0,06 € |
| Frais de service | 2,50 € |
| **Total facturé** | **2,56 €** |

### 3. Itinéraire détaillé

| Jour | Date | Étape | Distance | KM cumulé | Nuit | Camping | Coût |
|:----:|:----:|:------|:--------:|:---------:|:----:|:--------|:----:|
| 1 | 15/09 | Sombreffe → Reims | 180 km | 180 km | 1 | Camping Reims | 30 € |

### 4. Distances Haversine

| Trajet | Distance vol d'oiseau |
|:-------|:--------------------:|
| Sombreffe → Reims | 165 km |
| Reims → Dijon | 210 km |
| ... | ... |
| **Total** | **~2 800 km** |

### 5. Carte interactive

Chaque roadbook inclut une carte OSM tracée avec folium :

```python
import folium

stops = [(50.5, 4.5, "Sombreffe"), (49.25, 4.03, "Reims"), ...]
m = folium.Map(location=[47.0, 6.0], zoom_start=6, tiles="OpenStreetMap")

# Tracé du parcours
route = [(s[0], s[1]) for s in stops]
folium.PolyLine(route, color="#e63946", weight=4, opacity=0.8).add_to(m)

# Marqueurs
for lat, lon, label in stops:
    folium.Marker([lat, lon], popup=label, 
                  icon=folium.Icon(color="red", icon="info-sign")).add_to(m)

m.save("docs/italie/carte-italie.html")
```

### 6-9. Campings, Budget, Notes, Résumé

Les sections suivantes détaillent les hébergements, le budget par poste, les astuces pratiques et un tableau récapitulatif.

## Publication

Les roadbooks sont publiés sur le **wiki Voyages** :

```
📦 github.com/christophedanhier-hash/voyages-wiki
🌐 https://christophedanhier-hash.github.io/voyages-wiki/
📁 /opt/data/voyages-wiki/docs/
```

Le workflow de publication est automatisé :

```bash
cd /opt/data/voyages-wiki
git add docs/NOM-DU-VOYAGE/
git commit -m "Ajout roadbook [destination] — [dates]"
git push origin main
# ~1 min → GitHub Pages déploie automatiquement
```

## Roadbooks existants

| Destination | Période | Statut |
|:------------|:-------:|:------:|
| 🇮🇹 **Italie** | Septembre/Octobre 2026 | 📝 En préparation |
| 🇻🇳🇱🇦🇰🇭 **Vietnam-Laos-Cambodge** | Janvier/Février 2027 | 📝 En préparation |
| 🇳🇴 **Scandinavie** | Août-Octobre 2026 | 📝 En préparation |
| 🇪🇸 **Andalousie** | Septembre-Octobre 2026 | 📝 En préparation |
| 🇫🇷 **Canet** | Juin 2026 | 📝 En préparation |

## Règles strictes

1. **Pas de Google Maps** — uniquement OpenStreetMap
2. **Pas de photos** dans le wiki — restent sur Polarsteps
3. **Distances Haversine** obligatoires entre chaque étape
4. **Dates belges** — format JJ/MM/AAAA
5. **Chaque modif** = mise à jour de la section coûts
6. **ZTL et hauteurs** — vérification obligatoire pour camping-car

## Voir aussi

- **Ch.11** : Bureau Michel (hébergement et publication)
- **Ch.26** : Crons de synchronisation
- **Annexe B** : Guide démarrage rapide
# Bureau Émile : la pédagogie

Le Bureau Émile est un assistant pédagogique dédié à l'accompagnement d'Émilie pour son **mémoire de fin d'études en sciences de l'éducation**. C'est le plus jeune bureau de LEO, créé le 25 juin 2026.

## Son rôle

Émile n'est pas un correcteur automatique — c'est un **partenaire de rédaction** qui suit l'étudiante tout au long de son travail.

```
Bureau Émile = votre directeur de mémoire IA
├── 📖 Relecture et amélioration des chapitres
├── 📚 Bibliographie et références
├── 📝 Structure et plan du mémoire
├── 🔄 Versionning (brouillons → versions finales)
├── 💡 Suggestions d'amélioration
└── ✅ Vérification orthographe et style académique
```

## Architecture

```mermaid
flowchart TB
    E[👩‍🎓 Émile] -->|chat| BOT["🤖 Bot @Bureau_ia_emilie_bot"]
    E -->|lit| WIKI["📖 Wiki Mémoire"]
    BOT -->|primaire| DS["🧠 DeepSeek V4 Flash"]
    BOT -->|fallback >128K| GM["🌐 Gemini 3.5 Flash"]
    BOT -->|charge contexte| WIKI
    WIKI --> GH["🌍 GitHub Pages"]
```

- **Modèle principal** : DeepSeek V4 Flash (contexte 128K tokens)
- **Fallback** : Gemini 3.5 Flash (contexte 1M tokens — gratuit)
- **Bot Telegram** : [@Bureau_ia_emilie_bot](https://t.me/Bureau_ia_emilie_bot)
- **Wiki** : [emile-wiki](https://christophedanhier-hash.github.io/emile-wiki/)

### Pourquoi deux modèles ?

Le mémoire d'Émilie peut faire 50 à 150 pages. Si le contexte dépasse 128K tokens (la limite de DeepSeek), le bot bascule automatiquement sur Gemini qui accepte jusqu'à 1 million de tokens — gratuitement.

```python
if contexte_tokens < 128_000:
    utiliser("deepseek-v4-flash")   # Payant mais meilleur
else:
    utiliser("gemini-3.5-flash")   # Gratuit, contexte géant
```

## Sources de connaissance

Le bot s'alimente à plusieurs sources :

| Source | Description | Comment |
|:-------|:------------|:--------|
| **Wiki** | Documentation structurée | Lecture automatique |
| **Drive** | Brouillons, notes, documents | Sync horaire → Wiki |
| **Conversation** | Historique Telegram | Mémoire de session |

### Contenu du wiki

Le wiki Émile contient déjà :

- **Plan du mémoire** — structure validée par le directeur
- **Chapitres** — brouillons en cours d'écriture
- **Bibliographie** — sources et références
- **Notes de recherche** — réflexions personnelles
- **Retours du directeur** — annotations et corrections

## Workflow typique

```
1. Émile écrit un brouillon dans Google Docs
2. Sauvegarde dans le dossier Drive partagé "bureau-emile"
3. La sync horaire convertit le .docx en .md → Wiki
4. Émile demande : "Peux-tu relire mon chapitre 2 ?"
5. Le bot charge le chapitre depuis le Wiki
6. Analyse : structure, style, orthographe, références
7. Retour avec suggestions d'amélioration
```

## Règles pédagogiques

1. **Bienveillance** — toujours encourageant et constructif
2. **Structure** — chaque retour a : points forts, suggestions, questions
3. **Exemples** — illustrer les corrections avec des exemples concrets
4. **Progression** — célébrer les améliorations d'une version à l'autre
5. **Autonomie** — ne jamais réécrire à la place d'Émilie, guider

## Intégration avec les autres bureaux

| Bureau | Interaction |
|:-------|:------------|
| 🔧 **Michel** | Héberge le bot, gère le cron de sync Drive→Wiki |
| 🤖 **LEO** | Point d'entrée : redirige les demandes pédagogiques |
| 🏛️ **Robert** | Pourrait faire une analyse qualité du mémoire |

## Comparaison avec Sylvia

Le Bureau Émile est inspiré du Bureau Sylvia (voyages) — même pattern, adapté à l'académique :

| Aspect | Sylvia (voyages) | Émile (mémoire) |
|:-------|:----------------:|:----------------:|
| **Utilisateur** | Christophe + amis | Émilie |
| **Livrable** | Roadbook | Mémoire |
| **Wiki** | `voyages-wiki` | `emile-wiki` |
| **Sync** | Drive → GitHub (docs voyages) | Drive → GitHub (brouillons) |
| **Modèle** | DeepSeek V4 Flash | DeepSeek Flash + Gemini fallback |
| **Création** | 03/06/2026 | 25/06/2026 |

## Voir aussi

- **Ch.7** : Multi-bots — comment créer un profil dédié
- **Ch.8** : Skills — les compétences pédagogiques
- **Ch.9** : Mémoire persistante
# Bureau Robert : le conseil stratégique

Le Bureau Robert est le **consultant IT** de l'équipe. Il produit des analyses stratégiques, des recommandations d'architecture et des études comparatives. Quand un sujet dépasse le cadre technique pour toucher à la stratégie, Robert prend la main.

## Son rôle

Robert n'installe pas de serveurs et ne rédige pas de roadbooks — il **réfléchit**, **compare**, **recommande**.

```
Bureau Robert = votre consultant IT personnel
├── 🏛️ Architecture et choix techniques
├── 📊 Analyses comparatives (DeepSeek vs Gemini vs Ollama)
├── 💡 Recommandations stratégiques
├── 🔮 Roadmaps et évolutions
└── 📋 Rapports et documentations
```

## Les experts du bureau

| Expert | Compétence |
|:-------|:-----------|
| 🏛️ **Architecte** | Conception de systèmes, choix techniques |
| 🔒 **Sécurité** | Audit, conformité, risques |
| 📊 **Data** | Analyse de données, métriques, KPIs |
| 📋 **Gouvernance** | Processus, documentation, standards |
| 🔮 **Vision Stratégique** | Roadmap, évolutions, tendances |
| 📐 **Projet & Programme** | Planification, suivi, livrables |
| 🛡️ **Assurance Obligatoire** | INAMI, BCSS, eHealth, MyCareNet |

## Types d'analyses

Robert peut produire plusieurs formats selon le besoin :

| Type | Description | Exemple concret |
|:-----|:------------|:----------------|
| **Analyse stratégique** | Étude complète avec recommandations | "Quel LLM pour remplacer DeepSeek Flash ?" |
| **Benchmark** | Comparaison multi-critères | "Gemma 4 vs Qwen 3 vs Llama 4" |
| **Étude de faisabilité** | Options techniques + coûts | "Installer un GPU local pour l'IA" |
| **Audit** | Évaluation d'un existant | "Audit sécurité du serveur LEO" |

## Le processus de conseil

```
Demande ──→ Dispatch expert ──→ Production ──→ Croisement (si multi-experts)
                                                │
                                                ▼
                                          Synthèse ──→ Livrable ──→ Archivage
```

Pour les sujets complexes, plusieurs experts travaillent en parallèle :

```
"Quel LLM choisir pour mon serveur ?"
├── 📊 Data     : benchmark des modèles disponibles
├── 💰 Sophie   : analyse des coûts (TCO)
├── 🔒 Sécurité : données sensibles, vie privée
└── 🏛️ Synthèse : recommandation finale
```

## Exemple réel : remplacer DeepSeek Flash par du local

Le Bureau Robert a produit une **analyse comparative de 5 modèles open-source** pour remplacer DeepSeek Flash par un LLM local :

| Modèle | VRAM Q8 | Qualité estimée | Vitesse |
|:-------|:-------:|:---------------:|:-------:|
| **Gemma 4 26B MoE** ⭐ | 30 GB | ~85% | 🚀 80+ tok/s |
| Gemma 4 31B | 34 GB ❌ | ~90% | ~35 tok/s |
| Llama 4 Scout | 22 GB | ~75% | ~50 tok/s |
| Qwen 3 32B | 34 GB ❌ | ~80% | ~40 tok/s |

**Recommandation** : Gemma 4 26B MoE en Q8 sur RTX 3090 (32 GB total).

## Collaboration avec Sophie

Robert travaille main dans la main avec le **Bureau Sophie** (pilotage financier) :

```yaml
Projet: "Remplacer DeepSeek API par un LLM local"
Robert (technique):
  - Gemma 4 26B MoE Q8 = meilleur rapport qualité/VRAM
  - ~85% de la qualité DeepSeek Flash

Sophie (financier):
  - Coût actuel DeepSeek: ~720 €/an
  - Investissement GPU: ~800 € (RTX 3090)
  - ROI: 14 mois
  - Économie: ~600 €/an après ROI
  - 3 scenarii : pessimiste, réaliste, optimiste
```

## Voir aussi

- **Ch.10** : Architecture des bureaux
- **Ch.11** : Bureau Michel (implémente les recommandations)
- **Ch.15** : Bureau Sophie (pilotage financier)
# Bureau LEO et les autres bureaux

Le Bureau LEO est le **hub central** de l'écosystème — votre point d'entrée unique pour tout ce qui ne rentre pas dans les bureaux spécialisés. Et il y a quelques autres bureaux plus discrets mais tout aussi utiles.

## Bureau LEO : le fourre-tout personnel

LEO (le bureau, pas le bot) gère tout ce qui est **personnel, transversal ou ponctuel** : analyses générales, dossiers, études de marché, documentation.

```
Bureau LEO = votre assistant personnel
├── 📝 Analyses et dossiers
├── 📧 Emails (envoi + lecture + classification)
├── 📚 Documentation wikis
├── 🏷️ Classification Gmail (9 catégories)
└── 🗂️ Archives et notes
```

### Chiffres clés

| Métrique | Valeur |
|:---------|:------:|
| Sessions totales | 431 |
| Messages échangés | 13 089 |
| Emails classifiés | 3 240 |
| Skills installés | 126 |
| Wikis gérés | 5 |

### La classification Gmail

LEO classifie automatiquement les emails entrants en 9 catégories via Ollama (modèle local, gratuit) :

| Catégorie | Type |
|:----------|:-----|
| 👑 **VIP** | Christophe, famille, chefs |
| ⚙️ **Admin** | Factures, administrations |
| 💰 **Finances** | Banques, assurances, impôts |
| 🤖 **IA & Tech** | Infos techniques, newsletters |
| 🧭 **Voyages** | Réservations, billets |
| 🛒 **Achats** | Commandes, livraisons |
| 🏠 **Maison** | Énergie, travaux, voisinage |
| 👨‍👩‍👧‍👦 **Famille** | Émilie, Camille, amis |
| 🔭 **Astro** | Observatoire, astronomie |

Règle d'or : **les labels ne sont appliqués qu'une fois**. Pas de re-classification en masse.

## Bureau Sophie : le pilotage financier

Sophie est l'**analyste financière** de l'équipe. Elle calcule des TCO, des ROI, des business cases.

```
Bureau Sophie
├── 💰 TCO/ROI des projets IT
├── 📊 Analyse de rentabilité
├── 📈 3 scenarii (pessimiste/réaliste/optimiste)
└── 📋 Business cases

Experts : Analyste Marché, Modélisateur Financier, Risques & Conformité
```

Actuellement en reconstruction — Sophie reprendra du service quand un nouveau projet financier arrivera.

## Bureau Gérard : la documentation T600

Gérard documente le **télescope T600** (600mm d'ouverture) de l'Observatoire Centre Ardennes. Il a 6 sous-experts :

```
Bureau Gérard
├── 🔭 Spécialiste Astro-optique
├── 🔧 Expert Hardware (IPX800, Pléiades, Arduino)
├── 💾 Expert Firmware (steppers, drivers TB67H303HC)
├── 📝 Rédacteur Technique
├── 👨‍🏫 Formateur
└── 🌍 Ethnographe
```

Documents produits :
- **Document de Référence T600** — architecture complète du télescope
- **Formation Opérateur T600** — guide utilisateur
- **Analyse des Risques T600** — sécurité et maintenance

## Bureau Virginie : le médical

Virginie est une **orchestratrice de consultations médicales**. Elle réunit des spécialistes pour un diagnostic pluridisciplinaire.

Une consultation produite à ce jour : **Sylvie Michaux** (v2, finalisée).

Son workflow : dispatch des spécialistes → croisement des diagnostics → synthèse.

## Bureau AO : l'assurance obligatoire

Bureau spécialisé dans le domaine de l'**Assurance Obligatoire** (INAMI, BCSS, eHealth, MyCareNet). Peut fonctionner comme sous-agent de Robert ou en skill autonome.

En attente de missions.

## Bureau Versioning

Gère les **versions et releases** des documents et analyses. Structure prête, pas encore de contenu.

## La gouvernance des bureaux

```mermaid
flowchart TD
    LEO[🤖 LEO — Hub Central] -->|analyse IT| ROBERT[🏛️ Robert]
    LEO -->|infra problème| MICHEL[🔧 Michel]
    LEO -->|voyage| SYLVIA[🧭 Sylvia]
    LEO -->|mémoire| EMILE[🎓 Émile]
    LEO -->|médical| VIRGINIE[🩺 Virginie]
    LEO -->|documentation| GERARD[🏗️ Gérard]
    LEO -->|finances| SOPHIE[💰 Sophie]
    
    ROBERT -->|collabore| SOPHIE
    ROBERT -->|appelle| AO[🛡️ AO]
    MICHEL -->|héberge| EMILE
    MICHEL -->|héberge| SYLVIA
```

## En résumé

| Bureau | Rôle | Priorité |
|:-------|:-----|:--------:|
| **LEO** | Hub central, analyses, emails | 🔴 Quotidien |
| **Michel** | Infrastructure technique | 🔴 Quotidien |
| **Sylvia** | Voyages camping-car | 🟡 Hebdomadaire |
| **Robert** | Conseil stratégique IT | 🟡 Hebdomadaire |
| **Gérard** | Documentation T600 | 🟢 Mensuel |
| **Émile** | Assistant pédagogique | 🟢 Mensuel |
| **Virginie** | Consultations médicales | 🟢 Ponctuel |
| **Sophie** | Pilotage financier | 📝 En attente |
| **AO** | Assurance obligatoire | 📝 En attente |

## Voir aussi

- **Ch.10** : Architecture des bureaux (concept et workflow 7 étapes)
- **Ch.11** : Bureau Michel (infrastructure)
- **Ch.12** : Bureau Sylvia (voyages)
- **Ch.13** : Bureau Émile (pédagogie)
- **Ch.14** : Bureau Robert (conseil stratégique)
# Skills système : hermes-agent, gateway, profils

Certains skills sont si fondamentaux qu'ils méritent un chapitre à eux seuls. Ce sont les skills qui permettent de configurer, dépanner et étendre Hermes lui-même.

## hermes-agent : le méta-skill

Le skill `hermes-agent` est le **mode d'emploi d'Hermes par Hermes**. Quand vous demandez "comment ajouter un provider ?" ou "comment créer un profil ?", Hermes charge ce skill pour répondre.

Il couvre :

| Sujet | Exemple d'utilisation |
|:------|:----------------------|
| Configuration | Modifier config.yaml, ajouter un provider |
| Profils | Créer, lister, supprimer un profil |
| Gateway | Démarrer/arrêter un gateway, connecter Telegram |
| Mémoire | Consulter, modifier MEMORY.md et USER.md |
| Skills | Installer, créer, lister les skills |
| Crons | Planifier des tâches, mode no_agent |

### Exemple : configurer un nouveau provider

```bash
hermes config set model.default gemini-2.5-flash
hermes config set model.provider gemini
# Ajouter la clé API dans .env
echo "GEMINI_API_KEY=*** >>
```

### Exemple : créer un profil

```bash
hermes profile create mon-profil
# Configurer le profil
hermes -p mon-profil config set model.default deepseek-v4-flash
# Démarrer le gateway
hermes -p mon-profil gateway run
```

## Gateway : le pont vers les plateformes

Le skill `gateway` dans `hermes-agent` gère la connexion aux plateformes de messagerie.

### Telegram (le plus courant)

```yaml
# Dans le .env du profil
TELEGRAM_BOT_TOKEN=*** 
TELEGRAM_ALLOWED_USERS=8718957859
```

```bash
# Démarrer le gateway
hermes gateway run

# Avec un profil spécifique
hermes -p leo-copilot gateway run

# Remplacer un gateway existant
hermes gateway run --replace
```

### Architecture du gateway

Quand vous lancez `hermes gateway run`, Hermes :

1. Lit la configuration du profil
2. Connecte chaque plateforme activée (Telegram, Discord, etc.)
3. Écoute les messages entrants
4. Pour chaque message : charge le contexte, appelle le LLM, exécute les outils, renvoie la réponse
5. Gère le cycle de vie : reconnexion, heartbeat, shutdown

```
Message entrant
     │
     ▼
  Gateway ──→ Session ──→ Agent ──→ LLM
     │                                   
     ▼                                     
  Réponse envoyée
```

### Plusieurs gateways, plusieurs bots

Chaque profil peut avoir son propre gateway avec son propre token Telegram :

```bash
# Terminal 1 : Léo (default)
hermes gateway run

# Terminal 2 : Michel
hermes -p leo-copilot gateway run

# Terminal 3 : Sylvia
hermes -p bavi-leo gateway run
```

## Profils : l'isolation par design

Le skill `profils` documente comment organiser des instances Hermes indépendantes.

### Cas d'usage typiques

| Profil | Usage | Provider | Token Telegram |
|:-------|:------|:---------|:---------------|
| `default` | Assistant principal | DeepSeek V4 Flash | `881242...` |
| `leo-copilot` | Infrastructure | DeepSeek V4 Pro | `899720...` |
| `bavi-leo` | Voyages | DeepSeek V4 Flash | `885780...` |
| `emile` | Pédagogie | DeepSeek Flash + Gemini | `890688...` |

### Structure d'un profil

```bash
~/.hermes/profiles/mon-profil/
├── config.yaml     # Configuration du profil
├── .env            # Variables d'environnement (tokens, clés API)
├── SOUL.md         # Personnalité et règles
├── memories/       # Mémoire persistante
├── skills/         # Skills synchronisés
├── cron/           # Tâches planifiées
└── sessions/       # Historique des conversations
```

### Synchronisation entre profils

Les skills peuvent être synchronisés d'un profil source vers d'autres profils :

```yaml
# Dans le profil source (default)
skills:
  sync_to:
    - leo-copilot
    - bavi-leo
    - emile
```

## Mémoire : le skill qui retient tout

Le sous-skill `memory` permet de lire et écrire dans la mémoire persistante.

### Lire la mémoire

```bash
# Voir la mémoire système
cat ~/.hermes/memories/MEMORY.md

# Voir le profil utilisateur
cat ~/.hermes/memories/USER.md
```

### Écrire dans la mémoire

```bash
# Ajouter une information
hermes memory add "Le serveur est à Bruxelles" --target memory

# Ajouter une préférence utilisateur
hermes memory add "Christophe préfère les réponses concises" --target user
```

### Partage de mémoire entre profils

```bash
# Créer un lien symbolique pour partager
ln -s /opt/data/memories/MEMORY.md /opt/data/profiles/leo-copilot/memories/MEMORY.md
ln -s /opt/data/memories/USER.md /opt/data/profiles/leo-copilot/memories/USER.md
```

Ainsi, quand un profil apprend quelque chose, les autres en bénéficient immédiatement.

## Crons : l'automatisation sans surveillance

Le skill `cron` documente la planification de tâches.

### Créer un cron simple (script only, 0€)

```bash
hermes cron create \
  --name "Vérification disque" \
  --schedule "0 8 * * *" \
  --script /opt/data/scripts/check-disk.sh \
  --no-agent
```

Le flag `--no-agent` exécute le script **sans LLM** → coût 0€.

### Créer un cron avec agent (LLM)

```bash
hermes cron create \
  --name "Résumé veille" \
  --schedule "0 7 * * *" \
  --prompt "Analyse les articles dans /data/veille/ et fais un résumé"
```

### Lister et gérer les crons

```bash
hermes cron list
hermes cron pause <id>
hermes cron resume <id>
hermes cron remove <id>
hermes cron run <id>    # Exécution immédiate
```

## En résumé

| Skill | À retenir |
|:------|:----------|
| **hermes-agent** | Le mode d'emploi d'Hermes par Hermes |
| **Gateway** | Pont vers Telegram, Discord, etc. |
| **Profil** | Instance isolée avec sa propre config |
| **Mémoire** | Persistance cross-session |
| **Cron** | Tâches planifiées (no_agent = 0€) |

## Voir aussi

- **Ch.5** : Gateway et profils (configuration détaillée)
- **Ch.9** : Mémoire persistante
- **Ch.26** : Crons avancés
- **Annexe B** : Guide de démarrage rapide
# Skills productivité : dashboards, wikis, email, budget

Au-delà des skills système, Hermes embarque des skills prêts à l'emploi qui transforment votre assistant en outil de productivité. Voici les plus utiles de l'écosystème LEO.

## Dashboards : visualiser sans backend

Le skill `dashboards` (catégorie productivity) gère la création et le déploiement de tableaux de bord HTML statiques.

### Principe

Un dashboard Hermes est un fichier HTML autonome (zéro JavaScript serveur, zéro backend) :

```python
# 1. Collecter les données → JSON
# 2. Générer un HTML avec Chart.js
# 3. Push sur GitHub Pages → site en ligne
```

Ce fonctionnement minimaliste a un avantage décisif : **tout est gratuit**. GitHub Pages ne coûte rien, les scripts de collecte sont en no_agent.

### Exemple : dashboard KPI

```python
import json, subprocess
from datetime import datetime

# Collecte
sessions = len(json.loads(subprocess.run(
    ["cat", "/opt/data/sessions/sessions.json"],
    capture_output=True, text=True).output).get("sessions", []))

# Génération HTML
html = f"""<!DOCTYPE html>
<html>
<head><title>LEO KPI</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script></head>
<body>
<h1>📊 LEO — KPIs</h1>
<p>Sessions : {sessions}</p>
<canvas id="chart"></canvas>
<script>
new Chart(document.getElementById('chart'), {{
    type: 'bar',
    data: {{ labels: ['Sessions'], datasets: [{{ data: [{sessions}] }}] }}
}});
</script></body></html>"""

with open("/tmp/dashboard.html", "w") as f:
    f.write(html)
```

### Les dashboards de LEO (1 central, 4 onglets)

| Dashboard | Contenu | URL |
|:----------|:--------|:----|
| **LEO Dashboard** | Synthèse, Analyses, Infra, BAVI — 20 KPI, 4 charts | `leo-dashboard/` |

### Déploiement automatisé

```bash
# Script de collecte + génération
python3 /opt/data/scripts/update_budget_kpi.py

# Push sur GitHub Pages
cd /opt/data/leo-dashboard && git add -A && git commit -m "màj dashboard" && git push
```

## Wikis : la documentation vivante

Le skill `mkdocs-wiki` permet de créer et maintenir des wikis MkDocs déployés sur GitHub Pages.

### Créer un wiki

```bash
# 1. Créer le dépôt sur GitHub
# 2. Cloner en local
git clone https://github.com/christophedanhier-hash/mon-wiki.git
cd mon-wiki

# 3. Initialiser MkDocs
pip install mkdocs mkdocs-material
mkdocs new .

# 4. Configurer le thème
cat > mkdocs.yml << EOF
site_name: Mon Wiki
theme: material
EOF

# 5. Écrire les pages
# docs/index.md, docs/sujet1.md, ...

# 6. Déployer
mkdocs gh-deploy
```

### Les 5 wikis de LEO

| Wiki | Contenu | URL |
|:-----|:--------|:----|
| **BAVI_LEO** | Documentation des bureaux | `christophedanhier-hash.github.io/BAVI_LEO/` |
| **Hermès** | Documentation Hermes Agent | `christophedanhier-hash.github.io/hermes-wiki/` |
| **Voyages** | Roadbooks camping-car | `christophedanhier-hash.github.io/voyages-wiki/` |
| **Émile** | Mémoire universitaire | `christophedanhier-hash.github.io/emile-wiki/` |
| **OCA** | Télescope T600 | `christophedanhier-hash.github.io/wiki-oca/` |

### Synchronisation Drive → Wiki

Un cron transforme automatiquement les documents Google Docs en pages de wiki :

```bash
# Script de sync (toutes les 6h)
python3 /opt/data/scripts/drive-sync.sh
# Convertit les .docx en .md
# Commit + push sur le wiki GitHub
```

## Email : la classification inbox zéro

Le skill `gmail-inbox-zero` automatise la classification des emails entrants via Ollama (modèle local, gratuit).

### Fonctionnement

```yaml
1. Toutes les 15 minutes, le cron scanne les emails NON LUS
2. Pour chaque email, Ollama le classe en 9 catégories
3. Un label Gmail est appliqué automatiquement
4. Les emails lus depuis > 2 jours sont archivés
```

### Les 9 catégories

| Catégorie | Label Gmail | Type |
|:----------|:------------|:------|
| 👑 **VIP** | `CAT_VIP` | Christophe, famille, direction |
| ⚙️ **Admin** | `CAT_Admin` | Factures, administrations |
| 💰 **Finances** | `CAT_Finances` | Banques, assurances, impôts |
| 🤖 **IA & Tech** | `CAT_IA-Tech` | News tech, newsletters |
| 🧭 **Voyages** | `CAT_Voyages` | Réservations, billets |
| 🛒 **Achats** | `CAT_Achats` | Commandes, livraisons |
| 🏠 **Maison** | `CAT_Maison` | Énergie, travaux |
| 👨‍👩‍👧‍👦 **Famille** | `CAT_Famille` | Filles, amis |
| 🔭 **Astro** | `CAT_Astro` | Observatoire |

### Règle d'or

Les labels ne sont **appliqués qu'une seule fois**. Pas de re-classification en masse. Une fois qu'un email a son label, il reste dans la boîte de réception jusqu'à ce qu'il soit lu, puis archivé après 2 jours.

```python
# Ne JAMAIS réappliquer les labels en masse
if email.label_ids:
    pass  # Déjà classifié, on ne touche pas
```

### Configuration

```bash
# Clé API Google (OAuth)
# Dans .env
GOOGLE_TOKEN_PATH=/opt/data/google_token.json

# Le cron est déjà configuré dans le profil leo-copilot
# Exécution : toutes les 15 minutes
```

## Budget : le suivi des coûts DeepSeek

Le skill `deepseek-budget` suit la consommation de l'API DeepSeek en temps réel.

### Dashboard budget

```bash
# Exécution : 08:00 et 20:00 (cron)
python3 /opt/data/scripts/diag_budget.py

# Alerte si solde < 10€
# Push sur le dashboard LEO
```

### Chiffres LEO

| Métrique | Valeur |
|:---------|:------:|
| Provider principal | DeepSeek Flash (économique) |
| Coût mensuel estimé | ~1-3 € |
| Crons | 14 (13 no_agent = 0 €) |
| Veille IA | ~5-10 cts/jour |

Le secret de ce coût ridicule : classification avec Ollama (0€), crons en no_agent (0€), et DeepSeek Flash pour l'essentiel (quelques centimes/jour).

### Alertes automatiques

```yaml
Conditions d'alerte:
  - Solde < 10€ → notification Telegram
  - Dépense > 1€/jour → check anomaly
  - Erreur API DeepSeek → fallback Gemini
```

## En résumé

| Skill | Utilité | Coût |
|:------|:--------|:----:|
| **Dashboards** | Visualisation temps réel | 0€ (GH Pages) |
| **Wikis** | Documentation MkDocs | 0€ (GH Pages) |
| **Gmail classifier** | Inbox zéro automatique | 0€ (Ollama) |
| **Budget** | Suivi coûts DeepSeek | 0€ (no_agent) |

## Voir aussi

- **Ch.22** : Dashboards et monitoring (Partie V)
- **Ch.26** : Crons — automatisation (Partie VI)
- **Annexe A** : Glossaire
# Skills DevOps : déploiement, backup, monitoring

Les skills DevOps sont ceux qui font tourner LEO 24h/24 sans intervention humaine. Déploiement, sauvegarde, surveillance — tout est automatisé.

## Déploiement : installer un service en un clic

Le skill `deployment` (catégorie infrastructure) documente le déploiement des services sur le serveur LEO.

### Déploiement Docker

```bash
# Lancer un nouveau conteneur
docker run -d --name mon-service \
  --restart unless-stopped \
  --network host \
  mon-image:latest

# Vérifier
docker ps | grep mon-service
docker logs mon-service --tail 20
```

### Déploiement n8n

```bash
# Script de déploiement
bash /opt/data/scripts/run-n8n.sh

# Mise à jour
bash /opt/data/scripts/update-n8n.sh
```

Le script `run-n8n.sh` configure automatiquement :
- Le réseau en mode `host` (évite le bug de login 401 du proxy Docker)
- La base SQLite dans un volume persistant
- Les variables d'environnement (clés API, tokens)

### Déploiement Nginx + Cloudflare

```bash
# Configurer un nouveau site
sudo nano /etc/nginx/sites-available/mon-site.be
sudo ln -s /etc/nginx/sites-available/mon-site.be /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# Configurer le tunnel Cloudflare
cloudflared tunnel create mon-tunnel
cloudflared tunnel route dns mon-tunnel mon-site.be
```

### Déploiement de dashboard

```bash
# 1. Générer le HTML
python3 /opt/data/scripts/update_mon_dashboard.py

# 2. Push sur GitHub Pages
cd /opt/data/mon-dashboard
git add -A && git commit -m "màj $(date +%Y-%m-%d)" && git push

# 3. Vérifier
curl -s -o /dev/null -w "%{http_code}" https://user.github.io/mon-dashboard/
200 ✅
```

## Backup : ne jamais rien perdre

Le skill `backup` (catégorie infrastructure) couvre la stratégie de sauvegarde de LEO : **3 couches** pour une sécurité maximale.

### Couche 1 — Snapshots quotidiens (automatisé)

```bash
# Tous les jours à 04:00
python3 /opt/data/scripts/hermes-backup.py

# Ce script archive :
# - Tous les profils (default, leo-copilot, bavi-leo, emile)
# - La mémoire (MEMORY.md, USER.md)
# - Les scripts customs
# - Les sessions et configurations
# - Les tokens (.env, credentials_vault.json)

# Destination : local + Google Drive (Hermes_Christophe/backups/)
# Rétention : 7 jours
```

### Couche 2 — Recovery Kit (manuel)

```bash
# Kit de récupération d'urgence
/opt/data/recovery-kit/
├── rebuild.sh          # Script de reconstruction
├── docker-commands.md  # Commandes Docker essentielles
└── secrets.b64         # Tokens chiffrés

# Temps de récupération : ~30 minutes
```

### Couche 3 — Image système (hebdomadaire)

```bash
# Image complète du disque système
# Exécution : dimanche 03:00
fsarchiver savefs /mnt/data/recovery/couche3/leo-root.fs /dev/sda2

# Taille : ~30-40 Go
# Temps de récupération : ~1-2 heures
```

### Vérifier un backup

```bash
# Lister les backups locaux
ls -la /opt/data/backups/

# Vérifier le contenu d'un backup
tar -tzf /opt/data/backups/leo-backup-YYYY-MM-DD.tar.gz | head -20

# Vérifier les backups GDrive
# Via le dashboard ou le script
python3 /opt/data/scripts/hermes-backup.py --check
```

## Monitoring : savoir avant que ça casse

Le skill `monitoring` (catégorie infrastructure) regroupe tous les outils de surveillance de LEO.

### Auto-heal (toutes les 30 minutes)

```bash
# Vérifie automatiquement :
# ✅ Crons : 19/19 OK ?
# ✅ Ollama : UP ?
# ✅ n8n : healthz 200 ?
# ✅ Docker : 3/3 conteneurs up ?
# ✅ Disque : < 80% utilisé ?
# ✅ Tokens Google : OK ?
# ❌ Si problème → tentative de correction automatique
# ❌ Si pas de correction possible → issue GitHub (label auto-heal)
```

### Watchdogs (en continu)

```bash
# Scripts watchdogs
/opt/data/scripts/run-all-watchdogs.sh
# Surveille en continu :
# - code-server (VS Code web)
# - code-server-tunnel
# - n8n-healthcheck
# - n8n-dashboard
# - dashboard-watch (vérifie tous les dashboards)
```

### Vérification manuelle

```bash
# Statut des conteneurs
docker ps

# Logs Hermes
tail -f /opt/data/logs/agent.log
tail -f /opt/data/logs/gateway.log

# Logs crons
tail -f /opt/data/profiles/leo-copilot/logs/agent.log

# Dashboard de monitoring
# → https://user.github.io/leo-global-dashboard/
```

### Les 1 dashboard (4 onglets) de monitoring

| Dashboard | Fréquence | Vérifie |
|:----------|:---------:|:--------|
| **LEO Dashboard** | */15 | Synthèse, Analyses, Infra, BAVI — 20 KPI, 4 charts |

## La règle d'or

```yaml
Vérification AVANT livraison:
  - curl -s -o /dev/null -w "%{http_code}" <url>  # → 200
  - grep "valeur" <fichier>                         # → trouvé
  - dashboard-watch --check                         # → all green
```

Ne jamais dire "c'est fait" sans avoir vérifié que ça marche.

## En résumé

| Tâche | Skill | Automatisation |
|:------|:------|:---------------|
| Installer un service | `deployment` | Manuel + scripts |
| Sauvegarder | `backup` | Quotidien (04:00) |
| Surveiller | `monitoring` | Continue (auto-heal) |
| Vérifier | `curl` + `grep` | Avant chaque livraison |

## Voir aussi

- **Ch.11** : Bureau Michel (infrastructure)
- **Ch.22** : Dashboards et monitoring
- **Ch.26** : Crons d'automatisation
- **Ch.29** : Watchdogs et alertes
# Skills créatifs : ASCII art, designs, schémas

Hermes peut aussi faire preuve de créativité. Plusieurs skills transforment votre assistant en artiste numérique, designer ou illustrateur technique.

## ASCII Art : du texte qui dessine

Le skill `ascii-art` génère des œuvres d'art à partir de caractères texte.

```bash
# Bannière avec pyfiglet
python3 -c "import pyfiglet; print(pyfiglet.figlet_format('LEO', font='slant'))"
```

```text
   __     __   ____  
  / /    / /  / __ \ 
 / /    / /  / / / / 
/ /___ / /_ / /_/ /  
\____/ \__/ \____/   
```

### Cas d'usage

- Bannières pour les dashboards
- Logos pour les wikis
- Illustrations techniques dans la documentation
- Invitations de commande personnalisées

```bash
# Avec boxes (encadré)
python3 -c "import pyfiglet; print(pyfiglet.figlet_format('SYSTEM OK', font='bubble'))"
```

## Excalidraw : des schémas main-levée

Le skill `excalidraw` permet de créer des diagrammes et schémas au style "tableau blanc".

### Utilisation

```bash
# Générer un schéma Excalidraw
python3 /opt/data/scripts/upload.py mon-schema.excalidraw
```

### Exemple : architecture simple

```text
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Telegram   │────▶│  Hermes     │────▶│  DeepSeek   │
│  (vous)     │     │  Gateway    │     │  API        │
└─────────────┘     └─────────────┘     └─────────────┘
       │                                           │
       │                                           ▼
       │                                    ┌─────────────┐
       └────────────────────────────────────│  Réponse    │
                                            └─────────────┘
```

Les schémas Excalidraw sont au format JSON et peuvent être intégrés dans les wikis MkDocs.

## Diagrammes Mermaid

Mermaid est un langage de diagrammes textuels. Hermes peut générer des diagrammes Mermaid dynamiquement.

### Exemple : diagramme de séquence

```mermaid
sequenceDiagram
    Vous->>LEO: Question
    LEO->>DeepSeek: Appel API
    DeepSeek-->>LEO: Réponse
    LEO-->>Vous: Réponse formatée
```

### Exemple : diagramme d'architecture

```mermaid
graph TB
    User[👤 Vous] --> TG[Telegram]
    TG --> GW[Gateway Hermes]
    GW --> AG[Agent LEO]
    AG --> DS[DeepSeek V4 Flash]
    AG --> OL[Ollama local]
    AG --> GM[Gemini fallback]
```

Les diagrammes Mermaid sont supportés nativement par GitHub et MkDocs.

## p5.js : des animations interactives

Le skill `p5js` génère des sketches p5.js pour créer des visualisations interactives, des générateurs d'art, ou des simulations.

```javascript
function setup() {
  createCanvas(400, 400);
  background(220);
}

function draw() {
  fill(random(255), random(255), random(255));
  circle(random(width), random(height), 20);
}
```

### Cas d'usage
- Génération d'art procédural
- Visualisations interactives
- Démonstrations techniques
- Fond d'écran de dashboard

## Manim : des vidéos d'explication

Le skill `manim-video` utilise Manim (le moteur d'animation de 3Blue1Brown) pour créer des vidéos explicatives.

```python
from manim import *

class Introduction(Scene):
    def construct(self):
        title = Text("Comment fonctionne Hermes ?")
        self.play(Write(title))
        self.wait(2)
```

### Formats supportés
- Vidéos MP4
- GIFs animés
- Tutoriels pas à pas

## Design de pages web

Le skill `sketch` crée des maquettes HTML/COS rapidement pour visualiser une interface avant de la coder.

```html
<!DOCTYPE html>
<html>
<head>
<style>
body { font-family: sans-serif; max-width: 800px; margin: auto; }
.header { background: #2c3e50; color: white; padding: 2rem; }
.card { border: 1px solid #ddd; padding: 1rem; margin: 1rem 0; }
</style>
</head>
<body>
<div class="header"><h1>Dashboard LEO</h1></div>
<div class="card">Sessions: 431</div>
<div class="card">Budget: $60.31</div>
</body>
</html>
```

## Quand utiliser quel skill créatif

| Besoin | Skill | Format |
|:-------|:------|:-------|
| Bannière / logo | `ascii-art` | Texte |
| Schéma rapide | `excalidraw` | JSON SVG |
| Diagramme technique | Mermaid | Markdown |
| Animation / vidéo | `manim-video` | MP4 / GIF |
| Maquette web | `sketch` | HTML |
| Art génératif | `p5js` | JavaScript |

## Voir aussi

- **Ch.10** : Architecture des bureaux (schémas Mermaid)
- **Ch.22** : Dashboards (intégration de graphiques)
- **Annexe A** : Glossaire
# Skills recherche et veille : AI Tech Watch, arxiv

Hermes peut surveiller l'actualité, chercher des articles scientifiques et produire des rapports de veille automatiques. C'est ce que fait LEO chaque matin.

## AI Tech Watch : la veille IA quotidienne

Le skill `ai-tech-watch` est le plus sophistiqué des skills de veille. Chaque matin, il collecte, analyse et résume l'actualité IA.

### Fonctionnement

```
06:00 — Collecte RSS (15 sources)
   │
   ▼
07:00 — Analyse DeepSeek (Phase 1)
   │
   ▼
08:00 — Synthèse + Email (Phase 2)
```

### Sources surveillées

```yaml
# 15 sources RSS
- The Verge (AI)
- TechCrunch (AI)
- Ars Technica (AI)
- Hugging Face Blog
- Google AI Blog
- DeepMind Blog
- Meta AI Blog
- Anthropic Blog
- OpenAI Blog
- Microsoft Research (AI)
- NVIDIA Blog (AI)
- MIT News (AI)
- Stanford AI (HAI)
- Papers With Code
- Arxiv (AI)
```

### Format du rapport

Chaque rapport suit le format "Cowork Copilote" :

```markdown
# 🧠 Veille IA — 28/06/2026

Ce matin dans l'IA : [résumé 2-3 lignes des tendances clés]

## 🤖 IA Générale
- **Titre article** (source) — ALERTE
  Analyse : Contexte, annonce, signification, impact DSI...

## 🔒 Cyber
- ...

## ☁️ Cloud & Infra
- ...

## 📋 Régulation
- ...
```

### Tags utilisés

| Tag | Signification |
|:----|:--------------|
| 🔴 ALERTE | Information majeure, action possible |
| 🟡 NOUVEAU | Nouveauté intéressante |
| 🟢 À SUIVRE | Tendances émergentes |
| 🔵 CONFORMITÉ | Impact réglementaire |
| 🟣 MENACE | Risque sécurité/compétitivité |
| ⚪ PATCH | Mise à jour corrective |
| 🔶 TENDANCE | Signal faible |

### Coût

```yaml
Coût quotidien: ~0,05 € (DeepSeek Flash)
Nombre d'articles analysés: 15-30
Temps de traitement: ~2 minutes
```

## Arxiv : la recherche académique

Le skill `arxiv` permet de chercher des articles scientifiques sur Arxiv.

### Recherche par mot-clé

```bash
python3 /opt/data/scripts/search_arxiv.py --query "hermes agent LLM" --max 5
```

### Recherche par auteur

```bash
python3 /opt/data/scripts/search_arxiv.py --author "danhier" --max 10
```

### Recherche par catégorie

```bash
python3 /opt/data/scripts/search_arxiv.py --category cs.AI --sort date --max 20
```

### Format des résultats

```markdown
| Titre | Auteurs | Date | Catégorie | Lien |
|:------|:--------|:----:|:----------|:----|
| Titre de l'article | Auteur 1, Auteur 2 | 2026-06 | cs.AI | [PDF](url) |
```

## BlogWatcher : surveiller les blogs

Le skill `blogwatcher` surveille les flux RSS et Atom des blogs techniques.

### Ajouter une source

```bash
blogwatcher add https://blog.example.com/feed.xml
```

### Lister les sources

```bash
blogwatcher list
```

### Voir les nouveaux articles

```bash
blogwatcher recent --days 1
```

## LLM Wiki : base de connaissance locale

Le skill `llm-wiki` crée une base de connaissance interrogeable à partir de fichiers Markdown.

```bash
# Indexer le wiki
python3 /opt/data/scripts/index_wiki.py /opt/data/BAVI_LEO/docs/

# Interroger
python3 /opt/data/scripts/query_wiki.py "Comment configurer un gateway ?"
```

Utile pour que Hermes puisse chercher dans sa propre documentation sans avoir tout en contexte.

## Polymarket : les marchés de prédiction

Le skill `polymarket` interroge les marchés de prédiction Polymarket (blockchain).

```bash
# Derniers marchés
python3 /opt/data/scripts/polymarket.py --trending

# Prix d'un marché spécifique
python3 /opt/data/scripts/polymarket.py --slug "will-agi-exist-by-2030"
```

## YouTube : analyser des vidéos

Le skill `youtube-content` extrait et analyse les transcripts de vidéos YouTube.

```bash
# Extraire le transcript
python3 /opt/data/scripts/fetch_transcript.py https://youtu.be/VIDEO_ID

# Analyser le contenu
# → Résumé, points clés, transcript complet
```

Utile pour les conférences techniques, les tutoriels ou les annonces de produits.

## En résumé

| Skill | Usage | Fréquence | Coût |
|:------|:------|:---------:|:----:|
| **AI Tech Watch** | Veille IA quotidienne | Quotidien | ~0,05 €/j |
| **Arxiv** | Recherche académique | À la demande | 0€ |
| **BlogWatcher** | Surveillance blogs | Continue | 0€ |
| **LLM Wiki** | Base de connaissance | Continue | 0€ |
| **Polymarket** | Marchés prédiction | À la demande | 0€ |
| **YouTube** | Analyse vidéos | À la demande | 0€ |

## Voir aussi

- **Ch.17** : Skills productivité (email, wikis)
- **Ch.26** : Crons — tâches planifiées
- **Annexe A** : Glossaire
# Écrire ses propres skills

Le vrai pouvoir d'Hermes, c'est que vous pouvez **créer vos propres skills**. Pas besoin d'être développeur — un skill est juste un fichier Markdown bien structuré.

## Anatomie d'un skill

### Structure minimale

```markdown
---
name: mon-skill
description: Ce que fait mon skill
---

# Mon Skill

Instructions pas à pas pour accomplir la tâche.
```

### Structure complète

```bash
mon-skill/
├── SKILL.md         ← Instructions principales
├── references/      ← Documentation complémentaire
│   └── api.md
├── templates/       ← Modèles de sortie
│   └── rapport.md
└── scripts/         ← Scripts exécutables
    └── collect.py
```

### Frontmatter (en-tête YAML)

Le frontmatter est obligatoire. Il décrit le skill pour Hermes :

```yaml
---
name: backup-gdrive
description: Backup des profils Hermes vers Google Drive
category: infrastructure
metadata:
  hermes:
    tags: [backup, gdrive, hermes]
    workflows: [deploiement-n8n]
---
```

| Champ | Obligatoire | Description |
|:------|:-----------:|:------------|
| `name` | ✅ | Identifiant unique du skill |
| `description` | ✅ | Résumé en une phrase |
| `category` | ✅ | Groupe de skills |
| `metadata.hermes.tags` | ❌ | Mots-clés pour la recherche |
| `metadata.hermes.workflows` | ❌ | Workflows associés |

## Exemple pas à pas

Créons un skill "Vérification disque" pour LEO.

### 1. Créer le dossier

```bash
mkdir -p ~/.hermes/skills/infrastructure/check-disk
cd ~/.hermes/skills/infrastructure/check-disk
```

### 2. Écrire SKILL.md

```markdown
---
name: check-disk
description: Vérifier l'espace disque et alerter si < 20%
category: infrastructure
---

# Vérification disque

## Contexte
Vérifie l'espace disque du serveur LEO et alerte si l'utilisation
dépasse 80%.

## Étapes
1. Exécuter : `df -h / | tail -1`
2. Extraire le pourcentage d'utilisation (colonne 5)
3. Si > 80% → alerte Telegram + issue GitHub
4. Si < 80% → OK, rien à faire

## Vérification
- `df -h /opt/data` : confirmer l'espace libre
- Le cron tourne-t-il bien ? `hermes cron list`

## Pièges
- Le disque `/dev/sda2` est le SSD système
- Le disque `/dev/sdb2` est le HDD data (monté sur /mnt/data)
- Les alertes sont envoyées via le skill `notify`
```

### 3. Ajouter un script (optionnel)

```python
# scripts/check-disk.py
import subprocess, json

result = subprocess.run(
    ["df", "-h", "/"], capture_output=True, text=True
)
usage = result.stdout.strip().split("\n")[-1].split()[4].replace("%", "")

status = "OK" if int(usage) < 80 else "ALERTE"
print(json.dumps({"usage": f"{usage}%", "status": status}))
```

### 4. Tester le skill

```bash
# Demander à Hermes
"Vérifie l'espace disque"

# Ou utiliser le mode skill directement
hermes skill run check-disk
```

## Les 21 pièges à éviter

Basés sur l'expérience réelle de LEO :

| # | Piège | Solution |
|:-:|:------|:---------|
| 1 | `hermes` pas dans PATH | Utiliser `/opt/hermes/.venv/bin/hermes` |
| 2 | Symlinks dans `scripts/` refusés | Copier les fichiers, pas de liens |
| 3 | Contexte DeepSeek limité à 128K | Fallback Gemini (1M tokens) |
| 4 | `s6-svstat DOWN` = faux négatif | Vérifier les processus, pas le flag |
| 5 | Budget DeepSeek à mesurer en delta | Triple ventilation : IN/OUT/cache |
| 6 | Labels Gmail : ne pas réappliquer | Une seule classification par email |
| 7 | Migration Hermes → rebuild Docker | Script `rebuild.sh` dans recovery-kit |
| 8 | Tokens .env corrompus par le redact | Écrire via base64 |
| 9 | sshpass → `/opt/data/bin/` pas `/tmp/` | Binaire dédié |
| 10 | Config v30 → migration nécessaire | `hermes config migrate` |

## Où stocker ses skills

### Skills locaux (profil courant)

```bash
~/.hermes/skills/<categorie>/<nom>/SKILL.md
```

### Skills partagés entre profils

```bash
/opt/data/skills/<categorie>/<nom>/SKILL.md
```

### Skills synchronisés

Le profil `default` (source de vérité) synchronise ses skills vers les autres profils toutes les 30 minutes :

```yaml
# config.yaml du profil source
curator:
  enabled: true
  sync_to:
    - leo-copilot
    - bavi-leo
    - emile
```

## Bonnes pratiques

```yaml
Règles d'or:
  - ✅ Un skill = une tâche
  - ✅ Frontmatter complet et précis
  - ✅ Pitfalls documentés (au moins 3)
  - ✅ Étape de vérification incluse
  - ✅ Testé avant publication
  - ❌ Pas de fourre-tout
  - ❌ Pas de chemins en dur (utiliser des variables)
  - ❌ Pas de secrets dans le skill (utiliser .env)
```

## Exemples de skills LEO

| Skill | Fichier | Lignes |
|:------|:--------|:------:|
| `bureau-michel` | `SKILL.md` | 106 |
| `gmail-inbox-zero` | `references/classifier-script.md` | ~200 |
| `voyages-wiki` | `SKILL.md` | ~150 |
| `deployment` | Procédures Nginx, Docker | ~80 |

## En résumé

```mermaid
flowchart LR
    Idea[💡 Idée] --> Structure[📁 Créer dossier]
    Structure --> Frontmatter[📝 Frontmatter]
    Frontmatter --> Content[✍️ Instructions]
    Content --> Test[🧪 Tester]
    Test --> Pitfalls[⚠️ Ajouter pièges]
    Pitfalls --> Deploy[🚀 Prêt !]
```

## Voir aussi

- **Ch.8** : Skills — concepts généraux
- **Ch.10** : Architecture des bureaux
- **Annexe A** : Glossaire
- **Annexe B** : Guide démarrage rapide
# Dashboards et monitoring

Visualisez l'activité de votre assistant en temps réel avec des dashboards HTML autonomes, déployés sur GitHub Pages.

## Principe

Un dashboard est un fichier HTML statique (zéro JavaScript serveur, zéro backend) :

```
Script de collecte → JSON + HTML → Push GitHub Pages
                                      ↓
                    https://user.github.io/mon-dashboard/
```

**Avantages :** gratuit (GitHub Pages), accessible partout, aucun serveur à maintenir.

## Les dashboards de LEO

LEO a **1 dashboard central** (4 onglets, 20 KPI, 4 charts) rafraîchi par un cron no_agent :

| Dashboard | Contenu | URL | Cron |
|-----------|---------|-----|------|
| **LEO Dashboard** | Synthèse, Analyses, Infra, BAVI | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) | */15 |

Tous sont générés par des scripts `no_agent` — **0$ de coût LLM** par mise à jour.

## Architecture technique

Chaque dashboard suit le même pattern :

1. **Un script de collecte** (Python) qui :
   - Récupère les données (API, fichiers, logs)
   - Génère un `index.html` avec Chart.js ou CSS pur

2. **Un cron no_agent** qui exécute le script toutes les 4h

3. **Un dépôt GitHub Pages** qui sert le HTML

### Script type

```python
#!/usr/bin/env python3
import json, subprocess
from pathlib import Path

# 1. Collecter les données
data = collecter_metriques()

# 2. Générer le HTML
html = generer_dashboard(data)

# 3. Écrire dans le repo
repo = Path("/tmp/mon-dashboard")
repo.joinpath("index.html").write_text(html)

# 4. Push sur GitHub
subprocess.run(["git", "-C", str(repo), "add", "."])
subprocess.run(["git", "-C", str(repo), "commit", "-m", "Màj dashboard"])
subprocess.run(["git", "-C", str(repo), "push", "origin", "main"])
```

### Déploiement

```bash
# 1. Créer le repo
gh repo create mon-dashboard --public

# 2. Activer GitHub Pages
echo '{"source":{"branch":"main","path":"/"}}' | \
  gh api repos/user/mon-dashboard/pages --input -

# 3. Cloner en local
git clone https://github.com/user/mon-dashboard.git /tmp/mon-dashboard

# 4. Configurer le cron
hermes cron create \
  --script deploy-dashboard.sh \
  --schedule "0 */4 * * *" \
  --name "mon-dashboard" \
  --no-agent
```

## Pitfalls

### 🔴 Pas de JavaScript si le navigateur flashe

Sur certains appareils (Chromebook, mobile), Chart.js en mode responsive peut causer un rafraîchissement en boucle. Solution : **remplacer Chart.js par un tableau CSS statique**.

```css
/* Au lieu d'un graphique JS : tableau statique */
.hist-table td.ok-cell { color: #22c55e; }
.hist-table td.err-cell { color: #ef4444; }
```

### 🔴 Gérer l'identité Git

Dans l'environnement minimal d'un cron, `git commit` échoue si l'identité n'est pas configurée :

```python
subprocess.run(["git", "config", "user.name", "MonAssistant"])
subprocess.run(["git", "config", "user.email", "assistant@exemple.com"])
```

### 🔴 Gérer l'authentification GitHub

Le cron n'a pas de TTY pour le flow OAuth Git. Passez le token dans l'URL :

```python
import os
tok = os.environ.get("GH_TOKEN")
if tok:
    remote = f"https://user:{tok}@github.com/user/repo.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote])
```

### 🔴 Les repos locaux doivent être synchronisés

`dashboard-watch` vérifie l'âge du dernier commit **dans le repo local** pour déterminer si un dashboard est stale. Si votre script de déploiement push vers un clone temporaire (`/tmp/...`), le repo local ne sera jamais mis à jour et `dashboard-watch` déclenchera un redeploiement à chaque cycle.

**Solution :** après avoir pushé depuis `/tmp/`, faites un `git pull` dans le repo local :

```bash
cd /opt/data/n8n-dashboard
git pull origin main
```

> 🐛 **Bug #16** — Cette cause racine a été corrigée sur le dashboard n8n (juin 2026).

### 🔴 Webhook budget pour n8n

Si vous utilisez n8n pour remplacer un cron Hermes, n8n tourne dans Docker et n'a pas accès direct au filesystem. Créez un **webhook HTTP** sur l'hôte :

```python
# budget-webhook.py — mini serveur HTTP
# POST /budget-update → écrit dans budget.json
# GET  /health        → status
```

Lancé en background (`python3 scripts/budget-webhook.py &`). n8n y POSTe les données collectées.

### 🔴 Budget désynchronisé

Si le budget affiché sur un dashboard ne correspond pas au `budget.json`, le cron `dashboard-watch` (voir `crons.md`) déclenche une alerte. Vérifiez que les clés lues par le script de déploiement correspondent exactement à celles du JSON :

```python
# Dans budget.json : "avg_daily", "total_spent" (pas "daily_spend")
# Dans le script : budget.get("avg_daily", 0)  # ✅ correct
```

## Surveillance automatique (dashboard-watch)

Un cron **dashboard-watch** (`scripts/dashboard-watch.py`) tourne toutes les 2h et vérifie :

1. **HTTP 200** — chaque dashboard répond
2. **Âge < 2h** — données fraîches
3. **Budget cohérent** — valeur affichée ≈ `budget.json` (écart max 1$)
4. **Redeploiement auto** — si stale ou 404, le script relance le déploiement
5. **Rebuild GH Pages** — après chaque push, appelle l'API pour forcer le rafraîchissement CDN

```python
# Extrait : rebuild GH Pages après push
subprocess.run(["gh", "api", f"repos/user/{repo}/pages/builds", "-X", "POST"])
```

## 🦁 Global Dashboard LEO (portail unique)

Depuis le 22/06/2026, LEO a un **portail unique** qui consolide tout en une seule page :
- 🔵 **Crons (13)** — statut, historique, erreurs
- 📊 **Dashboard (1)** — HTTP, âge, budget
- 💰 **Budget DeepSeek** — solde, jours restants
- 🩺 **n8n** — online/offline
- 🏛️ **BAVI LEO** — sessions, messages, tokens
- 🖥️ **Machine** — statut en ligne/hors ligne
- 🚨 **Alertes** — dernières anomalies détectées
- 🔗 **Liens rapides** — accès au dashboard détaillé

**Avantages :**
- ✅ **Plus aucun rapport Telegram** — dashboard-watch et Auto-Heal livrent en local
- ✅ **Un seul bookmark** au lieu de 7
- ✅ **Cron no_agent toutes les 10min** (H:05) — 0$ de coût
- ✅ **Auto-déploiement GH Pages**

```bash
# Le cron
🌍 Global Dashboard — H:05 → /opt/data/scripts/deploy_leo_global.py (no_agent)
```

- **Usage LLM** — requêtes/jour, tokens consommés, coût estimé
- **Système** — CPU, RAM, disque, uptime de votre serveur
- **Projets** — Suivi d'avancement, tâches complétées
- **Réseau** — Latence, bande passante, statut des services

## Pour aller plus loin

- Voir `03-utilisation/crons.md` pour le déploiement automatisé
- Voir `03-utilisation/architecture-leo.md` pour la vue complète (schéma Mermaid, interactions, filets)
- Voir `exemples/LEO.md` pour les dashboards en production
# Métriques machines : CPU, RAM, disque, GPU

Un assistant qui tourne 24h/24 a besoin qu'on surveille sa santé. Les métriques machines sont le premier dashboard que LEO a mis en place.

## Pourquoi surveiller ?

```yaml
Risques réels:
  - Disque plein → Hermes plante, plus de logs, plus de sessions
  - RAM épuisée → ralentissements, OOM kill du conteneur
  - GPU saturé → Ollama répond en 5 min au lieu de 2 secondes
  - CPU à 100% → tout est lent, le gateway timeout
```

## Les métriques essentielles

### Disque

```bash
# La métrique la plus critique
df -h /opt/data
# → /dev/sda2  457G   89G  345G   21%  /
# → Si > 80%, agir
```

LEO a 2 disques :
- **SSD** `/dev/sda2` (457 Go) — système + données Hermes
- **HDD** `/dev/sdb2` (1 To) — backups, recovery kit, archives

### RAM

```bash
free -h
# → 22.94 Go total, ~2 Go pour Hermes, ~500 Mo pour n8n
```

Si la RAM utilisée dépasse 85%, les conteneurs Docker risquent l'OOM kill.

### GPU

```bash
nvidia-smi  # Si GPU disponible
```

### Processus

```bash
# Vérifier que tout tourne
docker ps
# → hermes-agent, n8n, ollama : tous UP
```

## Dashboard machines sur LEO

Le dashboard **leo-metrics** affiche en temps réel les métriques du serveur unique :

```markdown
| Métrique  | Valeur |
|:----------|:------:|
| CPU       | 12%    |
| RAM       | 4/22   |
| SSD       | 72/457 |
| HDD       | 42/900 |
| Statut    | 🟢     |
```

Collecte : toutes les heures (cron no_agent, 0€).
Technologie : script bash → JSON → Chart.js → GitHub Pages.

## Alerte automatique

```yaml
Seuils d'alerte:
  Disque > 80%:  🔴 Action immédiate (nettoyage ou extension)
  RAM > 85%:     🟡 Surveillance renforcée
  GPU > 90%:     🟡 Check processus Ollama
  CPU > 90%:     🟡 Vérifier crons en parallèle
```

L'auto-heal détecte ces seuils toutes les 30 minutes.

## 1 machine — le serveur LEO

| Machine | OS | RAM | Stockage | Rôle |
|:--------|:---|:---:|:--------:|:-----|
| **LEO** 🖥️ | Ubuntu 26.04 | 22 Go | 457 Go SSD + 1 To HDD | Serveur unique (toute la plateforme) |

> 💡 Les autres machines (Yoga, Penguin) sont des postes de travail — elles n'hébergent aucun service de la plateforme Hermes.

## Commandes utiles

```bash
# Vue d'ensemble rapide
htop

# Espace disque en temps réel
watch -n 5 df -h /opt/data

# Logs mémoire Docker
docker stats --no-stream

# Température GPU
nvidia-smi
```
# Monitoring crons : le tableau de bord des tâches

Avec 38 crons Hermes + 6 hôte qui tournent 24h/24 et un auto-fix-daemon `*/5`, le dashboard central synthétise tout : 20 KPI, 4 onglets (Synthèse, Analyses, Infra, BAVI), 4 charts Chart.js. Le tout dans **un seul fichier HTML statique** sur GitHub Pages.

## Le tableau de bord des crons

```markdown
| Cron              | Statut | Dernière exécution | Prochaine exécution | Actions |
|:------------------|:------:|:------------------:|:-------------------:|:-------:|
| Budget Check      | 🟢     | 07:58:12           | 19:58:12            | OK      |
| Backup GDrive     | 🟢     | 04:00:03           | 04:00:03 (demain)   | OK      |
| Veille IA         | 🟢     | 07:00:15           | 07:00:15 (demain)   | OK      |
| Dashboard LEO     | 🟢     | 07:30:22           | 08:30:22            | OK      |
| Dashboard Machines| 🟢     | 07:30:25           | 08:30:25            | OK      |
| Classifieur Gmail | 🟢     | 07:45:01           | 08:00:01            | OK      |
| Sync Drive GitHub | 🟢     | 18:00:30           | 18:00:30 (demain)   | OK      |
```

## Comment ça marche

```bash
# 1. Collecte des statuts
python3 /opt/data/scripts/collect_crons_status.py
# → JSON : { "cron_id": { "status": "ok", "last_run": "...", "next_run": "..." } }

# 2. Génération du dashboard
python3 /opt/data/scripts/deploy-crons-dashboard.py
# → HTML avec Chart.js + tableau

# 3. Push sur GitHub Pages
cd /opt/data/crons-dashboard && git push
```

## Indicateurs clés

| Indicateur | Vert | Orange | Rouge |
|:-----------|:----:|:------:|:-----:|
| Taux de succès | >95% | 80-95% | <80% |
| Temps d'exécution | <30s | 30-60s | >60s |
| Dérive horaire | <5min | 5-15min | >15min |
| Erreurs consécutives | 0 | 1-2 | >3 |

## Les crons de LEO

### Horaires (toutes les heures)

```yaml
- Dashboard LEO KPI
- Dashboard Machines
- Dashboard Crons
- Dashboard GitHub
- Dashboard BAVI LEO
- Dashboard n8n
- Dashboard Global
- Budget Check (08:00, 20:00)
```

### Quotidiens

```yaml
- Backup GDrive           → 04:00
- Veille IA               → 07:00 
- Sync Drive → GitHub     → 18:00
- Hermes Update Check     → 09:00
- Budget Snapshot         → 23:00
```

### Haute fréquence

```yaml
- Classifieur Gmail       → Toutes les 15 min
- Auto-heal               → Toutes les 30 min
- Dashboard Watch         → Toutes les 2h
- Drive Watch             → Toutes les 6h
```

### Hebdomadaires

```yaml
- Vérification infra      → Lundi 08:00
- Curator (nettoyage)     → Dimanche 04:00
```

## Gérer les erreurs

```bash
# Voir les logs d'un cron
hermes cron log <id>

# Relancer un cron en échec
hermes cron run <id>

# Suspendre un cron défaillant
hermes cron pause <id>

# Voir les erreurs récentes
tail -50 /opt/data/logs/errors.log
```

## Auto-heal : correction automatique

Quand un cron échoue, l'auto-heal tente de le corriger :

```
1. Détection : cron en erreur 2 fois de suite
2. Diagnostic : erreur de permission ? script manquant ? timeout ?
3. Correction : recopie du script, ajustement du timeout, redémarrage
4. Vérification : relance le cron, vérifie le résultat
5. Si échec → issue GitHub (label "auto-heal")
```

En production, l'auto-heal résout ~80% des problèmes sans intervention humaine.
# Budget et tracking DeepSeek

LEO coûte environ **1 à 3 euros par mois** à faire fonctionner. Voici les principes pour maîtriser ce budget.

## Le coût réel de LEO (estimation)

```yaml
Budget mensuel LEO (estimé):
  DeepSeek V4 Flash (quotidien):  ~1-2 €
  DeepSeek V4 Pro (analyses):     ~0,50 € (ponctuel)
  Gemini (fallback):                0 € (gratuit)
  Ollama (classification):          0 € (local, CPU)
  GitHub Pages (hébergement):       0 € (gratuit)
  n8n (workflows):                  0 € (self-hosted)
  Total:                           ~1-3 €
```

> Ces chiffres sont des ordres de grandeur. Le solde et la consommation réels sont visibles en temps réel sur le [LEO Dashboard](https://christophedanhier-hash.github.io/leo-dashboard/).

Le secret de ce coût ridicule : **Ollama pour le gratuit** (classification emails sur CPU), **Flash pour le quotidien** (quelques centimes/jour), **Pro seulement pour le complexe** (ponctuel).

## Triple ventilation

```python
# Ne pas se fier aux logs DeepSeek
# Mesurer le delta de balance
vrai_coût = solde_avant - solde_après

# Ventiler par usage
coûts = {
    "deepseek_flash":  0.05 * jours,    # Usage quotidien
    "deepseek_pro":    0.10 * analyses, # Analyses complexes
    "ollama":           0.00,           # Gratuit
    "gemini":           0.00,           # Gratuit (fallback)
}
```

## Dashboard budget

```markdown
| Métrique              | Valeur                      |
|:---------------------|:----------------------------|
| Provider principal   | DeepSeek Flash (économique)  |
| Provider complexe    | DeepSeek Pro (ponctuel)      |
| Provider gratuit     | Ollama (CPU local)           |
| Fallback             | Gemini (gratuit, quotas)     |
| Coût mensuel estimé  | ~1-3 €                       |
| Veille IA            | ~5-10 cts/jour               |
| Crons                | 0 € (13/14 en no_agent)      |
```

> Les chiffres exacts (solde, dépense quotidienne, jours restants) sont visibles en temps réel sur le [LEO Dashboard](https://christophedanhier-hash.github.io/leo-dashboard/).

## Alertes

```yaml
Seuils d'alerte:
  Solde < 10€:  🔴 Notification immédiate
  Dépense > 1€/jour: 🟡 Vérifier si anomalie
  Erreur API:        🟡 Fallback Gemini automatique
```

## Comparaison des providers

| Provider | Coût IN (1M tokens) | Coût OUT (1M tokens) | Autonomie ($60) |
|:---------|:-------------------:|:--------------------:|:---------------:|
| DeepSeek Flash | $0.14 | $0.28 | >6 ans |
| DeepSeek Pro | $1.50 | $5.00 | ~2 mois |
| Gemini Flash | **0 €** | **0 €** | ∞ (quotas gratuits) |
| Ollama | **0 €** | **0 €** | ∞ (local) |
# Tâches planifiées (crons)

Hermes Agent peut exécuter des actions automatiquement selon un planning. C'est ce qui transforme votre assistant en majordome qui travaille 24/7.

## Principe

```
Cron = tâche planifiée qui s'exécute automatiquement
     │
     ├── Script pur (no_agent) → Aucun LLM, exécution directe 0$ ✅
     ├── LLM sur Ollama local  → Gratuit (votre machine)
     └── LLM sur provider payant → Coût par exécution 💰
```

## Types de crons

### Script pur (no_agent)

Pour les tâches purement techniques : collecte de données, backup, déploiement.

**Avantage :** zéro token LLM consommé, exécution rapide, **0$** à vie.

```bash
# Créer un cron no_agent
hermes cron create "0 6 * * *" "Backup quotidien" --script mon-script.sh
```

**Bonnes pratiques :**
- Le script doit être dans `~/.hermes/scripts/`
- Exit code 0 = succès, non-zero = échec
- Le script a accès à `stdout` qui est livré à l'utilisateur

### LLM sur Ollama (local, gratuit)

Pour les tâches qui nécessitent de la réflexion, sans coût :

```bash
hermes cron create "0 9 * * 1" "Analyse les logs et résume les erreurs" --name "rapport-hebdo" --model qwen2.5:7b
```

### LLM sur provider payant

À éviter pour les crons récurrents. Si vraiment nécessaire, privilégiez une
fréquence faible (hebdomadaire, pas horaire).

## Planification efficace

### Ordre de grandeur des coûts

| Type de cron | Coût par run | Coût / mois (horaire) |
|-------------|-------------|----------------------|
| no_agent (script) | **0$** | **0$** |
| Ollama local | **0$** | **0$** |
| DeepSeek / Gemini | ~0.001-0.01$ | ~7-70$ |

**Règle LEO :** Tout cron récurrent (toutes les heures/jours) doit être `no_agent`
ou tourner sur Ollama. DeepSeek est réservé aux interactions directes.

### Ordonnancement décalé (staggered)

Quand plusieurs crons tournent à la même fréquence, décalez les minutes pour
éviter l'embouteillage :

```
H:00 → machines-kpi   (collecte métriques)
H:05 → budget-check   (solde API)
H:10 → dashboard-KPI  (génération HTML)
H:15 → dashboard-machines
H:20 → monitoring-crons
```

Chaque cron a `~5 min` de fenêtre exclusive.

## Configuration d'un cron

### Syntaxe de planification

| Expression | Signification | Usage |
|------------|--------------|-------|
| `0 * * * *` | Toutes les heures à :00 | Collecte métriques |
| `5 * * * *` | Toutes les heures à :05 | Budget |
| `10 * * * *` | Toutes les heures à :10 | Dashboard KPI |
| `0 6 * * *` | Tous les jours à 06:00 | Backup quotidien |
| `0 8 * * 1` | Tous les lundis à 08:00 | Rapport hebdo |
| `0 18 * * *` | Tous les jours à 18:00 | Sync externe |
| `30m` | Toutes les 30 minutes | Monitoring rapide |

### Exemple concret : backup quotidien

```bash
hermes cron create "0 6 * * *" "Backup quotidien" --script run-backup.sh
```

### Exemple concret : dashboard horaire

```bash
hermes cron create "10 * * * *" "Générer le dashboard" --script run-dashboard.sh
```

## Gestion des crons

```bash
# Lister les crons
hermes cron list

# Modifier un cron
hermes cron edit <id> --schedule "every 4h"

# Mettre en pause
hermes cron pause <id>

# Reprendre
hermes cron resume <id>

# Supprimer
hermes cron remove <id>

# Forcer l'exécution immédiate
hermes cron run <id>

# Voir le statut du scheduler
hermes cron status
```

## Surveillance

Hermes Agent enregistre chaque exécution de cron avec :
- Son statut (ok/error)
- Sa sortie (stdout)
- Horodatage

Ces informations sont consultables :

```bash
# Voir les logs d'un cron
cat ~/.hermes/cron/output/<id>/*.md
```

**Astuce LEO :** Créez un **dashboard de monitoring** des crons (voir
`03-utilisation/dashboards.md`) pour avoir un œil sur l'état de tous vos crons
en un coup d'œil. Ce dashboard peut lui-même être mis à jour par un cron
horaire.

### 🔍 dashboard-watch — surveillance automatique

Un cron `dashboard-watch` (toutes les 2h) vérifie que tous les dashboards sont à jour :

- **HTTP 200** — chaque dashboard répond
- **Âge < 2h** — données fraîches
- **Budget cohérent** — valeur affichée du budget ≈ `budget.json` (écart max 1$)
- **Redeploiement auto** — si stale ou 404, le script relance le déploiement

Le script est dans `scripts/dashboard-watch.py` et son état est sauvegardé dans `metrics/dashboard-watch-state.json`.

### 🛡️ Auto-Heal — cicatrisation automatique (cron agent, H:45)

Depuis le 21/06/2026, un cron **agent-driven** (pas no_agent) tourne toutes les heures à H:45 pour détecter et corriger automatiquement les problèmes connus :

- **Crons en erreur** → détection via `cronjob list`, diagnostic (PATH `gh`, script cassé, import manquant) et correction auto + execution forcée
- **Dashboard HTTP non-200** → redéploiement immédiat
- **budget-webhook down** → redémarrage automatique
- **Disque plein** → alerte

**Patterns auto-réparables :**
| Pattern | Détection | Correction |
|---------|-----------|------------|
| `gh` introuvable | Stderr "gh: command not found" | Patch avec chemin absolu `/opt/data/home/.local/bin/gh` |
| Dashboard 404 | HTTP != 200 | Relance le script de déploiement |
| budget-webhook down | Process manquant | Relance via watchdog |
| Import Python cassé | Traceback d'import | pip install dans le venv |

**Rapport :** livré en local (plus sur Telegram). Consultez le **🌍 Global Dashboard** à
https://christophedanhier-hash.github.io/leo-dashboard/ pour tout voir en un coup d'œil.

## Pièges à éviter

### 🔴 Ne pas mettre de LLM sur une tâche purement script

Un cron de collecte de métriques (Python pur) **n'a pas besoin** d'un LLM.
Le LLM dirait juste "j'ai exécuté le script, voici le résultat" — gaspillage
de tokens et d'argent.

### 🔴 Gérer l'identité et le token Git

Si votre cron push sur GitHub, l'environnement cron peut ne pas avoir accès
aux credentials GitHub. Deux solutions :

**Solution 1 — Chemin absolu vers gh :**
```python
import subprocess, os
gh_path = "/opt/data/home/.local/bin/gh"
tok = os.environ.get("GH_TOKEN")
if not tok:
    tok = subprocess.run([gh_path, "auth", "token"],
        capture_output=True, text=True).stdout.strip()
remote = f"https://user:{tok}@github.com/user/repo.git"
subprocess.run(["git", "remote", "set-url", "origin", remote])
subprocess.run(["git", "push", "origin", "main"])
```

**Solution 2 — Variable d'environnement :**
Définir `GH_TOKEN` dans le script ou l'environnement du cron.

### 🔴 Attention aux chemins dans l'environnement cron

L'environnement d'exécution d'un cron no_agent est minimal. Utilisez des
**chemins absolus** dans vos scripts. Exemple : `/opt/hermes/.venv/bin/python3`
plutôt que `python3`.

### 🔴 Cross-device move

Dans un script cron, ne pas utiliser `Path.rename()` entre `/tmp/` et
`/opt/data/` — ces répertoires sont souvent sur des filesystems différents.
Utilisez `shutil.move()`.

```python
# ❌ Ne fait pas
tmp.rename(local_path)

# ✅ Fait
import shutil
shutil.move(str(tmp), str(local_path))
```

### 🔴 Vérifier les sorties

Un cron no_agent qui exit 0 mais ne fait rien est silencieux. Pour les
tâches critiques, faites en sorte qu'il produise une sortie utile pour
confirmer que le travail a été fait.

## Pour aller plus loin

- Voir `03-utilisation/dashboards.md` pour le monitoring
- Voir `exemples/LEO.md` pour l'architecture cron complète
# Crons horaires : métriques, KPI, dashboards

Les crons horaires sont la cheville ouvrière de LEO. Ils tournent 24h/24 et maintiennent les dashboards à jour sans intervention humaine.

## Principe

Un cron horaire = un script no_agent = **0 € par exécution**.

```bash
hermes cron create \
  --name "Dashboard Machines" \
  --schedule "0 * * * *" \
  --script /opt/data/scripts/update_machines_kpi.py \
  --no-agent
```

Le flag `--no-agent` est essentiel : sans LLM, l'exécution est gratuite.

## Les crons horaires de LEO

```yaml
Toutes les heures (minute 0):
  - Dashboard LEO KPI      → collecte sessions, tokens, budget
  - Dashboard Machines     → CPU, RAM, disque 3 machines
  - Dashboard Crons        → statut 38 crons
  - Dashboard GitHub       → activité repos
  - Dashboard BAVI LEO     → KPIs voyages

Toutes les 30 minutes (minute 30):
  - Auto-heal              → vérification santé système
  - Classifieur Gmail      → nouveaux emails (aussi toutes les 15 min)

Toutes les 15 minutes:
  - Classifieur Gmail      → scan boîte de réception
```

## Staggering (évitement de conflit)

Quand plusieurs crons tournent à la même minute, ils peuvent entrer en conflit (API rate limit, CPU saturé). La solution : **staggering**.

```yaml
# Au lieu de tout lancer à H:00
H:00 → Dashboard LEO KPI
H:05 → Dashboard Machines
H:10 → Dashboard Crons
H:15 → Dashboard GitHub
H:20 → Dashboard BAVI LEO
H:25 → Dashboard n8n
H:30 → Auto-heal
```

Chaque cron démarre 5 minutes après le précédent. Les pics de charge sont lissés.

## Script typique

```python
#!/usr/bin/env python3
# update_machines_kpi.py
import json, subprocess

# Collecte
result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
disk_usage = result.stdout.split("\n")[1].split()[4]

result = subprocess.run(["free", "-h"], capture_output=True, text=True)
ram_usage = result.stdout.split("\n")[1].split()[2]

# Génération HTML
html = f"""<!DOCTYPE html>
<html>
<head><title>Machines</title></head>
<body>
  <h1>🖥️ Machines</h1>
  <p>Disque: {disk_usage} | RAM: {ram_usage}</p>
</body>
</html>"""

# Sauvegarde
with open("/tmp/dashboard-machines.html", "w") as f:
    f.write(html)
```

## Vérification

```bash
# Voir les logs du cron
tail -20 /opt/data/profiles/leo-copilot/logs/agent.log

# Vérifier le dashboard en ligne
curl -s https://user.github.io/leo-metrics/ | head -5
```
# Crons quotidiens : backup, veille IA, sync

Les crons quotidiens sont les tâches lourdes qui s'exécutent une fois par jour. Backup, veille IA, synchronisation — le ménage automatisé.

## Les crons quotidiens de LEO

```yaml
04:00 — Backup → GDrive
  Action: Archive tous les profils + config → Google Drive
  Rétention: 7 jours
  Coût: 0 € (no_agent)
  Script: /opt/data/scripts/hermes-backup.py

07:00 — Veille IA
  Action: Collecte 15 sources RSS → analyse DeepSeek → email
  Coût: ~0,05 €/jour (agent LLM)
  Durée: ~2 minutes

09:00 — Hermes Update Check
  Action: Vérifie si une nouvelle version d'Hermes est disponible
  Coût: 0 € (no_agent)

18:00 — Sync Drive → GitHub
  Action: Miroir bidirectionnel Google Drive ↔ GitHub
  Coût: 0 € (no_agent)

23:00 — Budget Snapshot
  Action: Sauvegarde du budget quotidien dans l'historique
  Coût: 0 € (no_agent)
```

## Backup quotidien

```yaml
Ce qui est sauvegardé:
  - profiles/default/       → config, SOUL, .env
  - profiles/leo-copilot/   → config, crons, mémoire, skills
  - profiles/bavi-leo/      → config, mémoire, roadbooks
  - profiles/emile/         → config, SOUL, .env
  - memories/               → MEMORY.md, USER.md (partagés)
  - scripts/                → tous les scripts customs
  - sessions/               → historique des conversations
  - .env                    → tokens et clés API
  - config.yaml             → configuration globale
  - credentials_vault.json  → coffre-fort des credentials

Destination:
  - Local: /opt/data/backups/
  - Cloud: Google Drive (Hermes_Christophe/backups/)
  
Rétention: 7 jours
Taille moyenne: ~40-70 MB
```

## Veille IA quotidienne

```yaml
Processus:
  1. Collecte RSS (15 sources, ~50 articles)
  2. DeepSeek V4 Flash analyse chaque article
  3. Sélection des 15 plus pertinents
  4. Rédaction du rapport formaté
  5. Envoi par email à christophe.danhier@gmail.com

Coût: ~0,05 €/jour = ~1,50 €/mois
Tags: ALERTE, NOUVEAU, À SUIVRE, CONFORMITÉ, TENDANCE
```

## Synchronisation Drive → GitHub

```yaml
Fonctionnement:
  - Scanne les dossiers Google Drive partagés
  - Détecte les nouveaux fichiers .docx ou .md
  - Convertit les .docx en .md
  - Commit + push sur le wiki GitHub correspondant

Wikis synchronisés:
  - BAVI_LEO ↔ Drive (docs bureaux)
  - voyages-wiki ↔ Drive (roadbooks)
  - emile-wiki ↔ Drive (brouillons mémoire)
```

## Planification avec cron

```yaml
# Format: minute heure jour mois jour_semaine
0 4 * * *   → Tous les jours à 04:00
0 7 * * *   → Tous les jours à 07:00
0 9 * * *   → Tous les jours à 09:00
0 18 * * *  → Tous les jours à 18:00
0 23 * * *  → Tous les jours à 23:00
```
# Watchdogs et alertes

Les watchdogs sont des scripts qui surveillent en continu l'état des services et alertent en cas de problème. C'est le système immunitaire de LEO.

## Principe

Un watchdog = un script qui tourne régulièrement et vérifie qu'un service répond.

```bash
# Watchdog typique
#!/bin/bash
# Vérifie que n8n répond
if ! curl -s http://localhost:5678/healthz > /dev/null; then
    echo "❌ n8n ne répond pas"
    # Tentative de redémarrage
    docker restart n8n
    # Notification
    hermes memory add "n8n relancé le $(date)" --target memory
fi
```

## Les watchdogs de LEO

```yaml
Toutes les 30 minutes:
  - 🩺 Auto-heal complet       → crons, Ollama, n8n, Docker, disque, tokens
  - 📧 Classifieur Gmail       → nouveaux emails à classer

Toutes les 2 heures:
  - 📊 Dashboard Watch         → vérifie que le dashboard répond
  - 🔄 Dashboard redeploy      → redéploie si un dashboard est obsolète

Toutes les 6 heures:
  - 🔭 Drive Watch             → détecte les changements dans Google Drive

Tous les jours:
  - 🤖 Hermes Update Check     → nouvelle version disponible ?
  - 💰 Budget Check            → solde suffisant ?
```

## Auto-heal : le watchdog principal

```yaml
Vérifications:
  ✅ Crons:        14/14 OK ?
  ✅ Ollama:       qwen2.5:7b responsive ?
  ✅ n8n:          healthz 200 ?
  ✅ Docker:       3/3 conteneurs UP ?
  ✅ Disque:       < 80% utilisé ?
  ✅ Token LEO:    Google API OK ?
  ❌ Token Christophe: invalid_grant (à ré-autoriser manuellement)

En cas d'échec:
  1. Tentative de correction automatique
  2. Si réussi → log + continue
  3. Si échec → issue GitHub (label auto-heal)
```

## Dashboard Watch

Le Dashboard Watch vérifie que le dashboard LEO est en ligne et à jour :

```bash
# Vérification unique
curl -s -o /dev/null -w "%{http_code}" https://christophedanhier-hash.github.io/leo-dashboard/
# → 200
```

## Notifications

```yaml
Canaux de notification:
  - Telegram DM      → alertes critiques (disque, budget, panne)
  - GitHub Issues    → problèmes non critiques (auto-heal, watchdogs)
  - Dashboard        → tous les statuts en temps réel
  
Règles:
  - Une alerte = une issue GitHub
  - Label "auto-heal" si corrigé automatiquement
  - Pas de spam : pas de notification pour les succès
```
# Drive ↔ GitHub sync

La synchronisation entre Google Drive et GitHub est le pont qui relie les documents collaboratifs à la documentation publiée.

## Pourquoi synchroniser ?

```yaml
Google Drive:
  - Écriture collaborative (Google Docs)
  - Accessible depuis n'importe quel appareil
  - Versionnage basique

GitHub Pages:
  - Publication publique et élégante
  - Versionnage professionnel (git)
  - Déploiement automatique (MkDocs)

Le sync = le meilleur des deux mondes
```

## Fonctionnement

```
Google Docs
     │
     ▼
Drive Watch (toutes les 6h)
     │
     ▼
Conversion .docx → .md
     │
     ▼
Git add + commit + push
     │
     ▼
GitHub Pages (déploiement automatique)
     │
     ▼
Wiki en ligne 🌐
```

## Script de synchronisation

```bash
#!/bin/bash
# drive-sync.sh

# 1. Scanne les dossiers Drive partagés
python3 /opt/data/scripts/drive-sync.py --scan

# 2. Détecte les nouveaux fichiers
python3 /opt/data/scripts/drive-sync.py --diff

# 3. Convertit les .docx en .md
python3 /opt/data/scripts/drive-sync.py --convert

# 4. Commit + push
cd /opt/data/BAVI_LEO && git add -A && git commit -m "sync Drive $(date +%Y-%m-%d)" && git push
cd /opt/data/voyages-wiki && git add -A && git commit -m "sync Drive $(date +%Y-%m-%d)" && git push
cd /opt/data/emile-wiki && git add -A && git commit -m "sync Drive $(date +%Y-%m-%d)" && git push
```

## Wikis synchronisés

| Wiki | Dossier Drive | Usage |
|:-----|:--------------|:------|
| **BAVI_LEO** | `Hermes_Christophe/BAVI/` | Documentation bureaux |
| **voyages-wiki** | `Hermes_Christophe/Voyages/` | Roadbooks camping-car |
| **emile-wiki** | `bavi/bureau-emile/` | Mémoire universitaire |

## Résolution de conflits

```yaml
Règle: GitHub gagne en cas de conflit.
  - Drive est la source des nouveaux documents
  - GitHub est la source de vérité pour les modifications existantes
  - En cas de modification simultanée : version GitHub prioritaire
```

## Voir aussi

- **Ch.12** : Bureau Sylvia (publication des roadbooks)
- **Ch.13** : Bureau Émile (sync des brouillons)
- **Ch.17** : Skills productivité
# 10 astuces pour ne pas galérer

Basées sur les vrais pièges rencontrés par LEO pendant sa construction. Évitez-les, vous gagnerez des heures.

## 1. `hermes` n'est pas dans le PATH

```bash
# ❌ Ça ne marche pas
hermes chat

# ✅ Ça marche
/opt/hermes/.venv/bin/hermes chat

# ✅ Solution : créer un alias
alias hermes='/opt/hermes/.venv/bin/hermes'
```

## 2. Les tokens .env sont fragiles

Le moindre caractère spécial (`$`, `!`, `&`) dans un fichier `.env` peut casser le gateway. Toujours utiliser des guillemets :

```bash
# ❌ Problème si le token contient $ ou !
TELEGRAM_BOT_TOKEN=abc$def

# ✅ Sécurisé
TELEGRAM_BOT_TOKEN="abc$def"
```

## 3. s6-svstat DOWN ne veut pas dire mort

```bash
# ❌ s6 dit DOWN mais le processus tourne
s6-svstat /run/service/gateway-default
# → down (faux négatif)

# ✅ Vérifier les processus
ps aux | grep hermes.*gateway
```

`s6-svstat` peut retourner `down` même quand le processus est actif. Toujours vérifier avec `ps`.

## 4. Le contexte DeepSeek est limité à 128K tokens

Si votre conversation ou document dépasse 128K tokens, DeepSeek plante.

```yaml
# Solution : fallback Gemini (1M tokens, gratuit)
fallback_providers: '[{"provider": "gemini", "model": "gemini-2.5-flash"}]'
```

Gemini a un contexte 8 fois plus grand — parfait pour les longs documents.

## 5. Ne jamais réappliquer les labels Gmail

```python
# ❌ DANGER : réappliquer les labels en masse
# → Des milliers d'emails re-classifiés, pagaille assurée

# ✅ Règle d'or
if email.already_labeled:
    pass  # Ne pas toucher
```

Les labels Gmail sont appliqués une seule fois. Passé ce cap, on n'y touche plus.

## 6. Budget DeepSeek : mesurer le delta, pas les logs

Les logs DeepSeek ne reflètent pas toujours le coût réel. Utilisez le **delta de balance** :

```python
# ✅ Fiable
vrai_coût = solde_avant - solde_après

# ❌ Pas fiable
cout_logs = somme(prix_token * tokens)
```

## 7. Les symlinks dans scripts/ sont refusés

Hermes v0.17.0 refuse les liens symboliques dans le dossier `scripts/`.

```bash
# ❌ Symlink refusé
ln -s /opt/data/scripts/backup.py /opt/data/profiles/leo-copilot/scripts/backup.py

# ✅ Copie réelle
cp /opt/data/scripts/backup.py /opt/data/profiles/leo-copilot/scripts/backup.py
```

## 8. Toujours vérifier avant de livrer

```bash
# Règle absolue : vérifier AVANT de dire "c'est fait"
curl -s -o /dev/null -w "%{http_code}" https://mon-site.com
# → 200 ✅

grep "version: 2.0" /opt/data/config.yaml
# → trouvé ✅
```

Ne jamais faire confiance à "ça devrait marcher". Vérifiez.

## 9. Un backup qui n'est pas testé n'existe pas

```bash
# Vérifier le contenu du backup
tar -tzf /opt/data/backups/leo-backup-*.tar.gz | head -20

# Simuler une restauration
tar -xzf /opt/data/backups/leo-backup-*.tar.gz -C /tmp/test-restore
```

Testez vos backups. Le jour où vous en avez besoin, il est trop tard pour découvrir qu'ils sont vides.

## 10. Documentez vos pièges

Quand vous passez 2 heures à résoudre un problème, **notez-le dans un skill**. La prochaine fois, ce sera 5 minutes.

```markdown
## Pièges
- Le port 5678 de n8n n'est accessible que via Tailscale
- Après un kill du gateway, attendre 30s avant de relancer
- La clé API DeepSeek est dans le .env du profil, pas le global
```

La documentation, c'est comme l'humour : c'est mieux avec un peu d'avance.
# 10 commandes à connaître absolument

Les commandes essentielles pour utiliser Hermes au quotidien.

## 1. Lancer le gateway

```bash
hermes gateway run --replace
```

Démarre le gateway Telegram. Le flag `--replace` tue l'ancienne instance avant de lancer la nouvelle.

## 2. Créer un profil

```bash
hermes profile create mon-profil
```

Crée un profil Hermes isolé, avec son propre bot Telegram, sa mémoire, ses skills et ses crons.

## 3. Utiliser un profil spécifique

```bash
hermes -p mon-profil chat
```

Lance une session chat avec le profil `mon-profil`. Utile pour basculer entre Léo, Michel, Sylvia ou Émile.

## 4. Lister les crons

```bash
hermes cron list
```

Affiche toutes les tâches planifiées, leur état, leur prochaine exécution.

## 5. Créer un cron no_agent (gratuit)

```bash
hermes cron create \
  --name "Vérification disque" \
  --schedule "0 8 * * *" \
  --script /opt/data/scripts/check-disk.sh \
  --no-agent
```

Le flag `--no-agent` = pas de LLM = **0€ par exécution**.

## 6. Voir les logs du gateway

```bash
tail -f /opt/data/logs/gateway.log
```

Indispensable pour comprendre pourquoi le bot ne répond pas, ou debugger une connexion Telegram.

## 7. Modifier la configuration

```bash
hermes config set model.default deepseek-v4-pro
hermes config set display.language fr
```

Modifie le `config.yaml` du profil courant sans éditer le fichier à la main.

## 8. Sauvegarder un fait en mémoire

```bash
hermes memory add "Le serveur est à Bruxelles" --target memory
hermes memory add "Christophe préfère le style concis" --target user
```

`--target memory` = pour le système. `--target user` = pour le profil utilisateur.

## 9. Lister les skills

```bash
hermes skills list
```

Affiche tous les skills disponibles. Vous pouvez charger le détail avec `hermes skills show <nom>`.

## 10. Forcer une exécution de cron

```bash
hermes cron run <id-du-cron>
```

Exécute immédiatement une tâche planifiée, sans attendre son horaire. Utile pour tester un nouveau cron.

## Bonus : la commande magique

```bash
# Tout reconstruire après un crash
# 1. Restaurer le backup GDrive
# 2. Lancer les gateways
hermes gateway run --replace                    # Léo
hermes -p leo-copilot gateway run --replace     # Michel
hermes -p bavi-leo gateway run --replace        # Sylvia
hermes -p emile gateway run --replace           # Émile
```
# 10 façons d'étendre son Hermès

Hermes Agent est conçu pour être extensible. Voici 10 pistes pour aller plus loin.

## 1. Ajouter un LLM local (Ollama)

```yaml
# Économisez 100% sur les tâches simples
model:
  default: ollama
  provider: ollama
  base_url: http://localhost:11434
```

Ollama + Qwen2.5-7B = classification d'emails gratuite, prototypage rapide, confidentialité totale.

## 2. Créer un bot spécialisé

Un bot par domaine : voyage, finances, documentation, pédagogie. Chacun avec son propre profil, son propre token Telegram, sa propre mémoire.

```bash
hermes profile create bot-voyages
hermes -p bot-voyages config set model.default deepseek-v4-flash
hermes -p bot-voyages gateway run --replace
```

## 3. Connecter Discord

```yaml
# config.yaml
discord:
  enabled: true
  token: VOTRE_TOKEN_DISCORD
```

Hermes peut répondre dans vos serveurs Discord. Utile pour les équipes.

## 4. Automatiser avec n8n

n8n connecte Hermes à 400+ services : email, calendrier, CRM, bases de données, webhooks.

```bash
# Workflow exemple
Trigger: Réception email → Action: Classifier avec Hermes → Sortie: Label Gmail
```

## 5. Dashboard temps réel

Des dashboards HTML statiques déployés sur GitHub Pages, mis à jour par des crons :

```bash
python3 /opt/data/scripts/update_mon_dashboard.py
cd mon-dashboard && git push
# → En ligne en 30 secondes
```

## 6. Synchronisation Drive ↔ GitHub

```bash
# Cron toutes les 6h
python3 /opt/data/scripts/drive-sync.sh
# Google Docs → Markdown → Wiki GitHub Pages
```

Les documents Google sont automatiquement convertis en pages de wiki.

## 7. Skills personnalisés

```bash
mkdir -p ~/.hermes/skills/mes-skills/mon-automatisation/
```

Écrivez vos propres skills en Markdown. Voir le Ch.21 pour le guide complet.

## 8. Partage de mémoire entre profils

```bash
ln -s /opt/data/memories/MEMORY.md /opt/data/profiles/mon-profil/memories/MEMORY.md
```

Tous vos bots partagent la même mémoire. Ce que l'un apprend, les autres le savent.

## 9. Multi-modèles (routage intelligent)

```yaml
fallback_providers: '[{"provider": "gemini", "model": "gemini-2.5-flash"}]'
```

DeepSeek pour le quotidien, Gemini pour les longs contextes (1M tokens), Ollama pour le gratuit. Le meilleur des trois mondes.

## 10. Ajouter une plateforme de messagerie

Hermes supporte : **Telegram**, **Discord**, **WhatsApp**, **Slack**, **Signal**, **Microsoft Teams**, **Google Chat**.

```yaml
# Exemple : activer WhatsApp
whatsapp:
  access_token: VOTRE_TOKEN
  phone_number_id: "..."
```

Chaque plateforme peut avoir son propre ensemble de commandes et de permissions.
# 10 ressources pour aller plus loin

Pour continuer votre voyage avec Hermes Agent.

## 1. La documentation officielle

🌐 **hermes-agent.nousresearch.com/docs**

La documentation officielle d'Hermes Agent. Toutes les configs, tous les providers, toutes les options. La référence absolue.

## 2. Le dépôt GitHub

📦 **github.com/nousresearch/hermes-agent**

Le code source, les issues, les discussions. Idéal pour suivre les évolutions, signaler des bugs, ou contribuer.

## 3. Le wiki BAVI LEO

🌐 **christophedanhier-hash.github.io/BAVI_LEO**

La documentation complète de l'écosystème LEO : 10 bureaux, 117 skills, 38 crons, 1 dashboard central. La preuve que Hermes peut gérer un assistant IA complet.

## 4. Le guide Hermès pour les Nuls

🌐 **christophedanhier-hash.github.io/hermes-guide**

Le livre que vous êtes en train de lire. Mis à jour régulièrement avec les nouvelles parties et les retours d'expérience de LEO.

## 5. GitHub Pages

🌐 **pages.github.com**

Hébergement gratuit pour wikis, dashboards, sites statiques. Utilisé par LEO pour ses 5 wikis et son dashboard central. Zéro backend, zéro coût.

## 6. DeepSeek API

🌐 **platform.deepseek.com**

Le provider principal de LEO. Excellent rapport qualité/prix. Compte gratuit avec crédits de démarrage.

## 7. Ollama

🌐 **ollama.com**

LLM local, gratuit, open-source. Parfait pour la classification, le prototypage, les tâches privées. Utilisé par LEO pour le classifieur Gmail (0€/mois).

## 8. n8n

🌐 **n8n.io** (self-hosted)

Automatisation low-code, 400+ intégrations. Alternative open-source à Zapier. Hébergé sur LEO pour les workflows de notification, sync et vérification.

## 9. MkDocs

🌐 **mkdocs.org**

Générateur de documentation statique. Transforme du Markdown en site web élégant. Utilisé par tous les wikis LEO.

## 10. Chart.js

🌐 **chartjs.org**

Bibliothèque de graphiques JavaScript. Légère, flexible, gratuite. Utilisée par tous les dashboards LEO.

## Bonus : la communauté

🌐 **Discord Nous Research** (lien sur le repo GitHub)

Le meilleur endroit pour poser des questions, partager vos réalisations, et rencontrer d'autres utilisateurs d'Hermes Agent.
# Aide-mémoire des commandes Hermes (v0.16+)

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
# L'architecture LEO — Exemple concret

LEO est l'assistant personnel de Christophe. Ce document détaille son architecture pour servir d'exemple à ceux qui veulent construire le leur.

## Identité

```
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

### Crons (14 actifs, 0$ LLM)

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
| `watchdog-code-server` | **\*/5** | 🔧 Script | **0$** | Relance code-server si arrêté |
| `watchdog-code-server-tunnel` | **\*/5** | 🔧 Script | **0$** | Maintient le tunnel SSH code-server |

**>95% des crons sont en no_agent** (zéro DeepSeek consommé par les tâches planifiées).

### Workflows n8n (redondance)

Depuis juin 2026, certains crons critiques sont **doublés dans n8n** pour bénéficier du retry natif :

| Workflow n8n | Horaire | Rôle | Redondance |
|-------------|---------|------|------------|
| `💰 Budget Check` | H:05 | Appel DeepSeek API → webhook → budget.json | ⚡ Retry 3x + backup Hermes |
| `🛡️ Dashboard Watch v2` | 30min | Ping 6 dashboards HTTP | ⚡ Retry 3x + backup Hermes (2h) |

**Pattern :** n8n = exécution garantie (retry) / Hermes = backup si n8n down. Double filet.

### Dashboard (1)

| Dashboard | Technologie | Màj | Lien |
|-----------|-------------|-----|------|
| 🦁 **LEO Dashboard** | HTML + Chart.js (4 onglets) | */15 | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) |

Tous les scripts de déploiement incluent :
- `--allow-empty` + `run_id` dans le footer pour éviter "nothing to commit"
- Force-push fallback si le push est rejeté
- **Rebuild GH Pages API** après push (CDN forcé)
- Validation des clés `budget.json` au déploiement

## Règles de fonctionnement

### 1. Règle #1 : Réfléchir avant d'agir

Avant chaque action impliquant un choix technique, identifier 2-3 approches, peser le pour/contre, choisir la meilleure. La précipitation est la première cause d'erreur.

### 2. Arbitrage LLM (3 niveaux)

```
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

## Structure des fichiers

```
/opt/data/
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

## Inspirez-vous, ne copiez pas

LEO est taillé sur mesure pour Christophe. Votre assistant aura ses propres besoins, règles et personnalité. Prenez ce qui vous est utile, adaptez le reste.
# Annexe A — Glossaire

> *Les termes techniques décryptés, du débutant à l'expert*

---

**Agent** — Un programme IA qui ne se contente pas de répondre à des questions : il exécute des actions sur votre système (lire des fichiers, envoyer des emails, lancer des scripts). Voir Chapitre 1.

**API** — Interface de programmation. Permet à deux logiciels de communiquer. Exemple : l'API DeepSeek permet à Hermès d'envoyer des requêtes au modèle.

**Agent Profile** — voir *Profil Hermes*.

**BAVI** — L'organisation des connaissances de LEO en bureaux spécialisés (Michel pour l'infra, Sylvia pour les voyages, etc.). Voir Partie III.

**Bot Telegram** — Un compte Telegram automatisé, identifié par un handle en `@nom_bot`. Chaque bot Hermes est lié à un profil.

**Chatbot** — Programme IA qui répond à des questions. Contrairement à un agent, il n'agit pas sur le système.

**CLI** — Command Line Interface (interface en ligne de commande). Le mode `hermes chat` en terminal.

**Context Window** — La mémoire à court terme d'un LLM, limitée en tokens. Hermès compresse automatiquement quand la limite approche.

**Credential Pool** — Groupe de clés API pour un même provider. Hermès peut alterner entre plusieurs clés pour éviter les limites de taux.

**Cron** — Tâche planifiée qui s'exécute automatiquement à intervalles réguliers. Hermès supporte deux modes : `no_agent` (script pur) et `LLM-driven` (avec raisonnement). Voir Partie VI.

**Dashboard** — Page HTML statique qui visualise des métriques (budget, performances, activité). Hébergé sur GitHub Pages.

**DeepSeek** — Fournisseur de LLM principal de LEO. Deux modèles : Flash (économique, dialogue) et V4 Pro (puissant, code/infra).

**Docker** — Technologie de conteneurisation. LEO tourne dans un conteneur Docker supervisé par s6.

**Fallback Provider** — Provider de secours configuré. Si le provider principal échoue, Hermès bascule automatiquement sur le fallback.

**Gateway** — Le service Hermes qui fait le pont entre les plateformes de messagerie (Telegram, Discord, etc.) et l'agent. Voir Chapitre 5.

**Gemini** — LLM de Google. Utilisé par LEO comme fallback gratuit (gemini-2.5-flash) et comme provider principal pour le bot leo-copilot.

**GitHub Pages** — Service d'hébergement gratuit de pages web statiques. Tous les dashboards LEO sont hébergés ici.

**HERMES_HOME** — Variable d'environnement pointant vers le répertoire de configuration d'Hermes (par défaut `~/.hermes/`).

**LLM** — Large Language Model (grand modèle de langage). Le cerveau de l'agent : DeepSeek, Gemini, Ollama, etc.

**LLM-driven** — Mode de cron où l'agent utilise un LLM pour réfléchir avant d'agir. Plus coûteux qu'un script pur.

**Memory** — Système de mémoire persistante d'Hermès. Deux types : `memory` (notes personnelles de l'agent) et `user` (profil de l'utilisateur).

**MCP Server** — Model Context Protocol. Permet d'ajouter des outils externes à Hermès (API, bases de données, services).

**MkDocs** — Générateur de sites statiques. Utilisé pour créer les wikis LEO à partir de fichiers Markdown.

**Multi-profil** — Possibilité d'avoir plusieurs configurations Hermes isolées (profils) sur la même machine, chacune avec son propre gateway, skills et mémoire.

**n8n** — Plateforme d'automatisation low-code. Utilisée par LEO en complément des crons Hermes pour les tâches critiques (retry natif).

**no_agent** — Mode de cron où le script s'exécute directement **sans** LLM. Zéro token consommé, idéal pour les tâches répétitives.

**Ollama** — Logiciel pour exécuter des LLM localement. Gratuit, privé, ne nécessite pas de connexion Internet.

**Open Source** — Logiciel dont le code source est public et modifiable. Hermes Agent, Ollama, MkDocs sont open source.

**Profil Hermes** — Ensemble isolé de configuration : modèle LLM, skills, mémoire, crons, gateway. Permet d'avoir plusieurs agents indépendants.

**Provider** — Fournisseur de LLM (DeepSeek, OpenAI, Anthropic, Ollama, etc.). Hermès est multi-provider.

**s6** — Superviseur de processus. Maintient les gateways Hermes en vie et les redémarre automatiquement en cas de crash. Utilisé dans l'environnement Docker de LEO.

**Scheduler** — Ordonnanceur de tâches intégré à Hermes. Gère les crons avec delivery, retry, et reporting.

**Skill** — Document Markdown qui décrit une procédure réutilisable que l'agent peut charger et suivre. Le super-pouvoir d'Hermès. Voir Partie IV.

**Staggered scheduling** — Technique de planification où les crons sont décalés (H:00, H:05, H:10, etc.) pour éviter la contention et les pics de charge.

**Tailscale** — Réseau privé maillé (mesh VPN). Permet à LEO de superviser les 3 machines à distance.

**Telegram** — Application de messagerie. Canal principal de communication avec LEO.

**Token** — Unité de mesure de la consommation d'un LLM. Un token ≈ 0.75 mot. Le coût d'un LLM se mesure en $ par million de tokens.

**Toolset** — Ensemble d'outils activables dans Hermès (terminal, web, browser, vision, etc.). Voir `hermes tools`.

**Watchdog** — Mécanisme de surveillance qui vérifie périodiquement qu'un service tourne et le relance si nécessaire.

**Webhook** — Mécanisme qui permet à un service d'envoyer une notification HTTP à Hermès quand un événement se produit.

**Wiki** — Site de documentation statique généré par MkDocs. LEO a 5 wikis pour différents domaines.

**Workflow n8n** — Séquence d'étapes automatisées dans n8n. Utilisé pour les tâches critiques avec retry automatique.

---

> **💡 Glossaire vivant** — ce glossaire est mis à jour au fil de l'évolution du guide. N'hésitez pas à suggérer des ajouts.
# Annexe B — Guide de démarrage rapide

> *Installer Hermès et parler à son premier agent en 60 secondes*

---

## Installation

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

## Premier chat

```bash
hermes chat -q "Bonjour, que peux-tu faire ?"
```

## Connexion Telegram

```bash
# 1. Créez un bot avec @BotFather sur Telegram
# 2. Récupérez le token
# 3. Configurez Hermes
hermes gateway setup
```

## Commandes essentielles

| Commande | Action |
|:---------|:-------|
| `hermes` | Lancer en mode interactif |
| `hermes doctor` | Diagnostic complet |
| `hermes model` | Changer de modèle/provider |
| `hermes tools list` | Voir les outils disponibles |
| `hermes skills list` | Voir les skills installés |
| `hermes cron list` | Voir les crons actifs |
| `hermes gateway status` | Voir le statut du gateway |
| `hermes profile list` | Voir les profils |

## Slash commands utiles

En session interactive :

| Commande | Effet |
|:---------|:-------|
| `/new` | Nouvelle session |
| `/retry` | Renvoyer la dernière requête |
| `/undo` | Annuler le dernier échange |
| `/title mon-sujet` | Nommer la session |
| `/skill nom` | Charger un skill |
| `/platforms` | Statut des plateformes |
| `/help` | Liste complète |

## Syntaxe cron rapide

```text
0 6 * * *      → Tous les jours à 6h
30m            → Toutes les 30 min
every 2h       → Toutes les 2h
every monday 9am → Tous les lundis 9h
```

> 🔗 **Documentation complète :** [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)
# Problèmes courants et solutions

## Installation

### `pip install` échoue (installation manuelle)

```
ERROR: Could not find a version that satisfies the requirement...
```

**Causes possibles :**
- Python < 3.11
- Venv non activé
- Pip obsolète

**Note :** La méthode recommandée est le script d'installation officiel :
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Solutions (installation manuelle) :**
```bash
# Vérifier la version Python
python3 --version  # Doit être 3.11+

# Mettre à jour pip
python3 -m pip install --upgrade pip

# Réinstaller dans le venv
source .venv/bin/activate
pip install -e .
```

### `hermes doctor` signale des erreurs

```
✗ Gateway telegram: bot token not configured
✗ Profile default: provider unreachable
```

**Solutions :** Suivez les indications de `hermes doctor` — il diagnostique précisément ce qui manque.

## Communication

### L'assistant ne répond pas sur Telegram

1. Vérifiez que le gateway tourne : `hermes gateway status`
2. Redémarrez le gateway : `hermes gateway restart`
3. Vérifiez le token bot Telegram (dans config.yaml)
4. Vérifiez que votre user ID est dans `allowed_users`

### Perte de session

Si votre assistant perd sa session (contexte précédent), c'est normal :
- Chaque nouvelle conversation est une session fraîche
- Les informations durables doivent être stockées dans les **skills** ou la **mémoire**
- Utilisez `hermes sessions list` ou `hermes sessions browse` pour voir les sessions récentes

## Crons

### Un cron en no_agent échoue sans raison

**Cause la plus fréquente :** l'environnement minimal du cron.

**Solutions :**
- Utilisez des chemins **absolus** dans vos scripts
- Utilisez un wrapper shell qui appelle le bon interpréteur
- Testez le script manuellement depuis le même environnement

### Un cron LLM-driven est lent

**Causes :**
- Le modèle choisi est trop lourd pour la tâche
- Le prompt est trop long (contexte volumineux)

**Solutions :**
- Utilisez un modèle plus petit (qwen2.5:7b au lieu de qwen2.5:32b)
- Allumez le GPU si disponible
- Passez en no_agent si la tâche n'a pas vraiment besoin de LLM

### Cron jamais exécuté (last_run_at = null)

**Causes :**
- Le cron a été créé mais n'a pas encore atteint son premier déclenchement
- Le cron est en pause
- Le scheduler Hermes ne tourne pas

**Vérifier :** `hermes cron list` montre tous les crons avec leur prochain run.

## Google Sheets / Drive

### Erreur 403 "The caller does not have permission"

**Cause :** Le compte OAuth utilisé n'a pas accès au document.

**Solution :** Partagez le document (sheet ou dossier) avec l'adresse email associée au token OAuth de votre assistant.

### Token OAuth expiré

Si le refresh_token ne fonctionne plus :
1. Obtenez un nouveau token via le flow OAuth
2. Mettez à jour le fichier token de votre assistant
3. (Alternative) Utilisez un compte de service Google

## GitHub Pages

### "Your current plan does not support GitHub Pages"

GitHub Pages gratuit ne fonctionne que sur les dépôts **publics**.

**Solution :** Rendez le dépôt public (les dashboards ne contiennent pas de données sensibles). Si le dépôt doit rester privé, trouvez une autre solution d'hébergement.

### "Author identity unknown" sur git commit

L'environnement minimal du cron ne connaît pas l'identité Git.

**Solution :** Configurez explicitement dans votre script ou wrapper :

```bash
git -C /tmp/repo config user.name "MonAssistant"
git -C /tmp/repo config user.email "assistant@exemple.com"
```

### "Could not read Username" sur git push

Pas de TTY pour l'authentification dans un cron.

**Solution :** Passez le token GitHub directement dans l'URL du remote.

## Ollama

### Ollama ne répond pas

```bash
curl: (7) Failed to connect to localhost port 11434: Connection refused
```

**Solutions :**
1. Vérifiez qu'Ollama tourne : `systemctl status ollama` ou `ollama serve`
2. Vérifiez le port : `ss -tlnp | grep 11434`
3. Démarrez Ollama : `ollama serve` (ou `sudo systemctl start ollama`)

### Modèle introuvable sur Ollama (qwen2.5:7b)

```bash
curl http://localhost:11434/api/tags  # Liste les modèles disponibles
ollama pull qwen2.5:7b               # Télécharger le modèle
```

Les noms exacts des modèles sont importants — utilisez ceux listés par `ollama list` ou l'API tags.

## Divers

### Message "Broken pipe" dans un cron

Un `Broken pipe` (Errno 32) se produit quand la sortie du processus est trop volumineuse pour le pipeline.

**Solutions :**
- Réduisez la sortie de votre script
- Passez en no_agent (script direct)
- Si le script produit une sortie utile, écrivez-la dans un fichier plutôt que stdout

### "Stop" non respecté

Si vous dites "stop" à votre assistant et qu'il continue, rappelez-lui la règle : "stop" est définitif. Si le problème persiste, une nouvelle session (/reset) peut être nécessaire.

## Contribuer à ce guide

Vous avez rencontré un problème non listé ? Ouvrez une issue sur le [dépôt GitHub](https://github.com/christophedanhier-hash/hermes-guide) — ce guide est vivant.
