---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v5.0
modele: deepseek-v4-flash
tags: [hermes, guide, documentation, chapitre, agent-ia, chatbot, architecture, leo, bavi]
statut: ✅ À jour
type: guide
hide:
  - toc
---

> **Dernière mise à jour rédactionnelle :** 18/07/2026 à 13:00 — Léo 🦁
> **Dernier commit :** `f6da9c7` — 18/07/2026 à 12:18

# Partie I — Découvrir Hermès 🏁

---

## Chapitre 1 — Un agent IA, c'est quoi ?

> *La différence entre un chatbot et un assistant qui agit*

---

Si vous lisez ce livre, vous avez probablement déjà utilisé ChatGPT, Claude, ou Gemini. Vous tapez une question, l'IA répond. Simple, efficace.

Mais vous avez aussi ressenti la frustration : « *Peux-tu envoyer cet email à Paul ?* » → « Je suis désolé, je ne peux pas envoyer d'email. » C'est là que la différence entre **chatbot** et **agent** devient flagrante.

### Chatbot vs Agent : la différence fondamentale

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

### Ce que LEO fait que ChatGPT ne peut pas faire

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

### Les briques d'un agent IA

Derrière la magie, un agent comme Hermès est construit sur cinq piliers :

#### 1. 🧠 Le modèle (LLM)
Le cerveau. DeepSeek, Gemini, Ollama — c'est ce qui comprend votre demande et décide quoi faire. L'avantage d'Hermès ? Vous n'êtes pas enfermé chez un seul fournisseur : vous pouvez basculer de DeepSeek à Ollama (gratuit, local) en une commande.

#### 2. 🔧 Les outils
Là où le chatbot s'arrête (« je ne peux pas faire ça »), l'agent commence. Hermès dispose de tout un arsenal d'outils :

- **terminal** — exécute des commandes shell
- **read_file / write_file** — lit et écrit des fichiers
- **web** — cherche sur Internet
- **browser** — navigue comme un humain
- **cronjob** — planifie des actions
- **delegate_task** — délègue à des sous-agents

#### 3. 🧬 La mémoire
Un chatbot oublie tout entre deux conversations. Un agent se souvient :
- De votre nom, vos préférences, votre environnement
- Des leçons apprises (« ne pas envoyer deux fois le même email »)
- Des procédures qui ont fonctionné

#### 4. 🏃 Les actions planifiées
Un agent ne se contente pas de répondre — il agit dans le futur. Les **crons** sont le secret pour qu'un assistant devienne un véritable majordome numérique : il fait le café avant que vous ne vous réveilliez.

#### 5. 🎓 Les skills
C'est le secret le mieux gardé d'Hermès. Un **skill**, c'est un mode d'emploi que vous donnez à l'agent pour qu'il sache comment faire quelque chose. « Voici comment déployer un dashboard. Voici comment envoyer un email. Voici comment analyser un RSS. » Une fois écrit, ce savoir est réutilisable à l'infini.

### L'erreur à ne pas commettre

> « Je vais mettre tous mes modèles et outils dans le même agent et ça va marcher. »

**Non.** Un agent sans organisation, c'est le chaos. LEO a appris cette leçon à ses dépens (on vous racontera ça au chapitre 3). La clé, c'est la **structuration** :

- Des profils séparés pour des tâches différentes
- Des crons avec des horaires staggerés (décalés)
- Des skills qui encapsulent le savoir-faire
- Des bureaux qui organisent les connaissances

### 📝 À retenir

| Concept | À retenir |
|:--------|:----------|
| **Agent ≠ Chatbot** | Un chatbot répond. Un agent agit. |
| **LEO est un agent** | Il exécute des actions, pas seulement des réponses. |
| **5 piliers** | Modèle, outils, mémoire, crons, skills. |
| **Organisation** | Sans structure, un agent devient incontrôlable. |

---

**[Chapitre suivant → Pourquoi Hermès ?](01-decouvrir-hermes/ch02-pourquoi-hermes.md)**

---

## Chapitre 2 — Pourquoi Hermès ?

> *Il y a une dizaine d'agents IA open source. Pourquoi Hermès est le bon choix.*

---

Vous avez décidé de construire votre propre assistant IA. Bonne décision ! Maintenant, quel framework choisir ? Claude Code ? Codex ? OpenCode ? Il y a une dizaine d'options sur le marché, et Hermès n'est pas le plus connu.

Voici pourquoi LEO tourne sur Hermès — et pourquoi c'est le bon choix pour vous aussi.

### Le paysage des agents IA en 2026

| Agent | Éditeur | Langage | LLM imposé ? | Multi-plateforme ? | Skills ? | Prix |
|:------|:--------|:--------|:-------------|:------------------:|:--------:|:----:|
| **Hermes Agent** | Nous Research | Python | Non 🔓 | ✅ (15+) | ✅ | Gratuit |
| Claude Code | Anthropic | TypeScript | Claude (Anthropic) | ❌ CLI seul | ❌ | Payant |
| Codex CLI | OpenAI | Python (sandbox) | GPT (OpenAI) | ❌ CLI seul | Partiel | Payant |
| OpenCode | Communauté | Python | Non 🔓 | ❌ CLI seul | ❌ | Gratuit |
| Copilot CLI | GitHub | N/A | GPT (Microsoft) | ❌ CLI seul | ❌ | Abonnement |

#### Pourquoi les autres ne convenaient pas

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

#### Ce qui rend Hermès unique

##### 1. 🔓 Multi-provider : vous n'êtes pas enfermé

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

##### 2. 🌐 Multi-plateforme : votre agent partout

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

##### 3. 🧠 Skills : le super-pouvoir

Un skill, c'est un document qui dit à Hermès : « Voici comment faire X. » Vous écrivez le mode d'emploi une fois, Hermès l'utilise à chaque fois.

```markdown
# skill: deploy-dashboard

1. Générer le fichier index.html avec les données à jour
2. Faire un git add, commit, push
3. Forcer le rebuild GitHub Pages via l'API
4. Vérifier que le dashboard répond HTTP 200
```

LEO a **130+ skills** répartis en 22 catégories. Chaque skill encapsule une procédure — déployer un dashboard, envoyer un email, analyser un RSS, etc. Résultat : LEO sait faire des choses qu'on ne lui a jamais montrées, parce qu'il a le mode d'emploi.

> 🦁 **Exemple LEO :** Le skill `dashboard-deployment` contient toute la procédure de déploiement d'un dashboard HTML sur GitHub Pages. LEO peut déployer un nouveau dashboard en 30 secondes, sans erreur, parce que le skill lui dit exactement quoi faire.

##### 4. ⏱️ Cron : votre assistant qui travaille 24/7

Les crons Hermes ne sont pas de simples tâches shell. Chaque cron peut être :

- **Un script pur** (no_agent) — zéro token LLM, exécution directe
- **Un prompt LLM** — l'agent réfléchit et agit
- **Un script + un prompt** — collecte des données puis analyse

LEO a **38 crons Hermes + 6 crons hôte** dont la plupart en no_agent (0$ de consommation LLM pour les tâches répétitives) + un **auto-fix-daemon** qui tourne toutes les 15 minutes.

##### 5. 🗂️ Profils et gateways parallèles

Avec Hermès, vous pouvez avoir **plusieurs agents indépendants** sur la même machine :

| Profil | Bot Telegram | Provider | Rôle |
|:-------|:-------------|:---------|:-----|
| `default` | @hermes_leo_bot | DeepSeek Flash | Chat quotidien |
| `leo-copilot` | @hermes_leo_copilot_bot | DeepSeek V4 Pro | Code, infra, n8n |
| `bavi-leo` | @bavi_leo_voyages_bot | DeepSeek Flash | Voyages camping-car |

Chaque profil a son propre gateway, ses propres skills, sa propre mémoire. Et pourtant, ils peuvent partager des informations via des **symlinks** vers un fichier mémoire commun (`/opt/data/memories/`).

### 🦁 Pourquoi Christophe a choisi Hermès

> *Ce qui distingue Hermès des autres, c'est qu'il ne se contente pas de répondre — il agit. Là où un chatbot vous donne une réponse, Hermès peut envoyer l'email, mettre à jour le dashboard, lancer le backup, et classer vos messages. C'est la différence entre un conseiller qui parle et un assistant qui fait.*

— Inspiré de l'expérience de Christophe, créateur de LEO

**Le critère décisif :** Hermès a le meilleur rapport **puissance/flexibilité/prix**. Gratuit, open source, multi-provider, multi-plateforme, avec un système de skills qui le rend évolutif à l'infini.

### 📝 À retenir

| Critère | Hermès | Les autres |
|:--------|:------:|:----------:|
| Multi-provider | ✅ | ❌ (enfermé) |
| Multi-plateforme | ✅ (15+) | ❌ (CLI seul) |
| Skills | ✅ (130+) | ❌ |
| Crons | ✅ (avancés) | ❌ |
| Gratuit | ✅ | Souvent payant |
| Open source | ✅ | Variable |

---

**[Chapitre suivant → L'architecture LEO](01-decouvrir-hermes/ch03-architecture-leo.md)**

---

## Chapitre 3 — L'architecture LEO

> *Comment Christophe a construit un assistant IA qui tourne 24h/24*

---

LEO n'est pas un simple script lancé sur un Raspberry Pi. C'est un écosystème complet qui mobilise plusieurs machines, services cloud, et une infrastructure résiliente. Ce chapitre vous montre les plans — comme si vous ouvriez la boîte noire.

### Vue d'ensemble

```
Telegram ──→ Gateway Hermes ──→ Profil default ──→ DeepSeek Flash (dialogue)
                                    │
                                    ├──→ @hermes_leo_copilot_bot → DeepSeek V4 Pro (code/infra)
                                    │
                                    ├──→ Ollama API locale (batch, gratuit)
                                    │
                                    └──→ Gemini (fallback automatique)
```

#### Les profils Telegram actifs

| Bot | Profil | Provider | Rôle | Latence | Coût |
|:----|:-------|:---------|:-----|:-------:|:----:|
| 🤖 @hermes_leo_bot | `default` | DeepSeek Flash | Chat quotidien | < 2s | Payant |
| 🟪 @hermes_leo_copilot_bot | `leo-copilot` | DeepSeek V4 Pro | Code, infra, n8n | < 2s | Payant |
| 🧭 @bavi_leo_voyages_bot | `bavi-leo` | DeepSeek Flash | Voyages camping-car | < 2s | Payant |

Chaque bot est un **profil Hermes** isolé — son propre gateway, ses propres skills, sa propre mémoire. Mais ils partagent un fichier de configuration commun et peuvent échanger des informations.

### La hiérarchie des providers

L'un des atouts d'Hermès est de pouvoir utiliser **plusieurs LLMs** et de choisir le meilleur pour chaque tâche :

| Ordre | Provider | Coût | Quand |
|:-----:|:---------|:----:|:------|
| 🥇 | **DeepSeek Flash** | Payant | Réponse Telegram, conversation, raisonnement |
| 🥈 | **DeepSeek V4 Pro** (leo-copilot) | Payant | Code, infra, debug système |
| 🥉 | **Ollama** (qwen2.5:7b, local) | **Gratuit** 🏠 | Traitement batch, classification (CPU), tâches privées |
| 4e | **Gemini** (fallback) | **Gratuit** ☁️ | Secours si DeepSeek indisponible |

**Le principe économique :** 95% des tâches planifiées (crons) tournent en `no_agent` = 0 token LLM consommé. Les 5% restants utilisent d'abord Ollama (gratuit), puis DeepSeek seulement si nécessaire.

### L'infrastructure physique

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

### L'écosystème logiciel

#### Docker et s6

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

#### Les 1 dashboard (4 onglets)

Tous en **HTML statique** hébergés sur **GitHub Pages** — zéro backend, zéro base de données :

| Dashboard | URL | Onglets | Màj |
|:----------|:----|:--------|:---:|
| 🦁 **LEO Dashboard** | [lien](https://christophedanhier-hash.github.io/leo-dashboard/) | Synthèse, Analyses, Infra, BAVI — 20 KPI, 4 charts | */15 |

#### Les 38 crons (+ 6 crons hôte)

LEO a 38 crons Hermes + 6 crons hôte qui exécutent des tâches planifiées

| Vague | Horaires | Crons |
|:------|:---------|:------|
| **Horaire** | H:00-H:30 staggerés | machines-kpi, budget, dashboards (4), wiki-sync |
| **15 min** | */15 | n8n healthcheck, classifieur emails |
| **2h** | */2 | auto-commit repos, dashboard-watch |
| **Quotidien** | 06:00, 08:00, 18:00 | backup, veille IA, drive sync |
| **Autres** | Hebdo, 6h | credentials-check, doc-watch |

#### Les 5 wikis MkDocs

Chaque domaine a son propre wiki, hébergé sur GitHub Pages :

| Wiki | Pages | Contenu |
|:-----|:-----:|:--------|
| 🌐 **BAVI LEO** (portail central) | 40 | Portail + documentation bureaux |
| 📚 **Hermès Wiki** | 31 | Docs techniques Hermes |
| 🧭 **Voyages Wiki** | 7 | Roadbooks camping-car |
| 🔧 **Wiki OCA** | 10 | Documentation T600 |
| 🎓 **Emile Wiki** | 10 | Pédagogie et études |

#### Les 10 bureaux BAVI

BAVI = l'organisation des connaissances de LEO en bureaux spécialisés :

| Bureau | Rôle | Privé/Pro |
|:-------|:-----|:---------:|
| 🦁 **LEO** | Dossiers personnels, analyses | Privé |
| 🔧 **Michel** | Infrastructure Hermes | Privé |
| 🧭 **Sylvia** | Voyages camping-car | Privé |
| 🎓 **Emile** | Pédagogie, mémoire | Privé |
| 🩺 **Virginie** | Médical | Privé |
| 🏛️ **Robert** | Conseil stratégique IT — 16 experts | **PRO** |
| 💰 **Sophie** | Pilotage économique | **PRO** |
| 📋 **Gérard** | Documentation T600 | Technique |
| 🛡️ **AO** | Assurance Obligatoire | **PRO** |
| 📚 **Connaissance** | Base de connaissance centralisée — bibliothèque cas IA, référentiels | Privé |
| 📦 **Versioning** | Gestion des versions | Technique |

### Les leçons apprises

#### 12/06 — Trop de profils tue le profil

**Erreur :** Création d'un profil `local` pour Ollama. Arrêt du gateway `local` = perte totale d'accès Telegram.

**Leçon :** Structurer les profils par domaine (default/leo-copilot/bavi-leo), Ollama par API directe. **Fiabilité > flexibilité.**

#### 13/06 — La précipitation coûte cher

**Erreur :** Actions sans réflexion préalable = régressions multiples (mauvais token, OAuth expiré, envoi multiple d'email).

**Leçon :** Avant chaque action, identifier 2-3 approches, peser le pour/contre, choisir.

#### 14/06 — Les crons doivent être robustes

**Erreur :** Crons qui utilisaient le mauvais Python, scripts introuvables, identité Git manquante.

**Leçon :** Uniformisation — wrappers shell + no_agent + chemins absolus + identité Git dans le script.

#### 24/06 — Gemini API directe, pas de proxy

**Erreur :** Un proxy Copilot compliqué et instable entre Hermes et Gemini.

**Leçon :** API directe (OpenAI-compatible). Moins de couches = moins de pannes. Latence passée de ~15s à < 2s.

### 📊 Chiffres clés

| Métrique | Valeur |
|:---------|:-------|
| Crons actifs | **38 Hermes + 6 hôte** |
| Skills installés | **130+** |
| Bureaux BAVI | **10** |
| Experts Robert | **16** |
| Dashboards | **1** (central 4 onglets ✅) |
| Wikis | **5** (98 pages total) |
| Repos GitHub | **20** |
| Consommation DeepSeek/jour | **~quelques centimes** |
| Machine hôte | **1** (serveur LEO uniquement) |

### 📝 À retenir

- LEO = 1 serveur principal + 5 bots Telegram + 1 dashboard central (4 onglets) + 38 crons + 6 crons hôte + 130+ skills
- Tout tourne sur Hermes Agent dans un conteneur Docker supervisé par s6
- Le secret : une organisation stricte (profils, bureaux, skills) qui permet à l'agent de gérer la complexité
- Les erreurs du passé ont forgé les règles du présent

---

**[Chapitre suivant → Installation rapide](01-decouvrir-hermes/ch04-installation-rapide.md)**

---

*Document mis à jour le 18/07/2026 à 13:00 — Léo 🦁 | v5.0*
