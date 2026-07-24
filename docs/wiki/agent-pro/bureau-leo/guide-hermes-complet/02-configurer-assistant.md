---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v5.0
modele: deepseek-v4-flash
tags: [hermes, guide, documentation, chapitre, installation, profils, providers, skills, memoire, leo, bavi]
statut: ✅ À jour
type: guide
hide:
  - toc
---

> **Dernière mise à jour rédactionnelle :** 18/07/2026 à 13:00 — Léo 🦁
> **Dernier commit :** `f6da9c7` — 18/07/2026 à 12:18

# Partie II — Configurer son assistant 🛠️

---

## Chapitre 4 — Installation rapide

> *Un assistant IA opérationnel en 5 minutes chrono*

---

Assez de théorie. Installons Hermès et faisons notre premier test.

### Prérequis

- **Linux** (Debian/Ubuntu recommandé), **macOS**, ou **Windows avec WSL2**
- **curl** installé (99% des systèmes l'ont)
- **Git** (optionnel mais recommandé)
- 1 Go d'espace disque libre

### Installation (Linux / macOS)

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

#### Installation manuelle (alternative)

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

### Premier lancement

```bash
# Lancer Hermès en mode interactif
hermes
```

Vous devriez voir apparaître l'interface :

```text
┌─────────────────────────────────────────────────────────┐
│  ⚕ Hermes Agent v0.17.0                                │
│  Type /help for slash commands, /quit to exit            │
└─────────────────────────────────────────────────────────┘

You >
```

Félicitations 🎉 — votre premier agent IA tourne !

#### Test rapide

```bash
hermes chat -q "Hello, qui es-tu ?"
```

Hermès vous répond. Simple.

### Configuration minimale

Par défaut, Hermès n'a pas de clé API LLM — il vous demandera d'en configurer une au premier lancement. Vous avez plusieurs options :

#### Option A : DeepSeek (recommandé pour débuter)

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

#### Option B : Ollama (100% gratuit, local)

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

#### Option C : Gemini (gratuit, cloud)

```bash
# Obtenez une clé sur https://aistudio.google.com/apikey
export GEMINI_API_KEY=votre_clé_ici

# Configuration
hermes config set model.default gemini-3.5-flash
```

### Vérification de l'installation

```bash
hermes doctor
```

Cette commande vérifie :
- ✅ Que les dépendances sont installées
- ✅ Que la configuration est valide
- ✅ Que les clés API sont accessibles
- ✅ Que les outils système sont disponibles

Un rapport s'affiche. Si tout est vert, vous êtes prêt.

### Et ensuite ?

Vous avez un agent IA de base. Mais un agent seul dans son terminal, c'est un peu comme un smartphone sans applications. La vraie puissance arrive quand vous :

1. **Connectez Telegram** (Chapitre 5) — pour parler à votre agent depuis votre téléphone
2. **Ajoutez des skills** (Chapitre 8) — pour qu'il sache faire des choses
3. **Configurez des providers** (Chapitre 6) — pour optimiser coût et performance
4. **Planifiez des tâches** (Chapitre 26) — pour qu'il travaille sans vous

#### ⚠️ Piège à éviter

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

### 📝 À retenir

| Étape | Commande |
|:------|:---------|
| Installer | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| Lancer | `hermes` |
| Tester | `hermes chat -q "Bonjour"` |
| Diagnostiquer | `hermes doctor` |
| Configurer provider | `hermes model` |

---

## Chapitre 5 — Installation sur Linux (Debian/Ubuntu)

### Prérequis système

- Un serveur ou PC sous **Debian 12+** ou **Ubuntu 22.04+**
- **Python 3.11+**
- **Curl**
- Un compte GitHub
- (Optionnel) Un GPU NVIDIA pour accélérer les LLM locaux

### Installer Hermes Agent

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

### Configurer Hermes

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

### Connecter un LLM

#### Avec DeepSeek (recommandé pour débuter)

```bash
# Ajouter votre clé DeepSeek dans .env
echo "DEEPSEEK_API_KEY=votre_clé_ici" >> ~/.hermes/.env

# Configurer le provider DeepSeek
hermes config set model.default deepseek-v4-flash
hermes config set model.provider deepseek
```

#### Avec Ollama (local, gratuit)

```bash
# Installer un modèle
ollama pull qwen2.5:7b

# Configurer Hermes pour utiliser Ollama
hermes config set model.default qwen2.5:7b
hermes config set model.provider ollama
hermes config set model.base_url "http://localhost:11434/v1"
```

### Lancer Hermes

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

### Vérifier l'installation

```bash
# Test simple
hermes chat -q "Dis bonjour, je suis ton nouvel assistant"

# Diagnostiquer les problèmes
hermes doctor --fix

# Voir l'état des composants
hermes status
```

### Problèmes courants

| Problème | Solution |
|----------|----------|
| `ModuleNotFoundError: No module named '...'` | Vérifier que le venv est activé |
| `pip` introuvable | `sudo apt install python3-pip` |
| Erreur de permission | Utiliser un utilisateur normal (pas root) |
| Port déjà utilisé | Modifier le port dans `config.yaml` |

### Ressources

- [Documentation officielle Hermes](https://hermes-agent.nousresearch.com/docs)
- [GitHub Hermes Agent](https://github.com/NousResearch/hermes-agent)

---

## Chapitre 6 — Installation sur Windows

Hermes Agent fonctionne nativement sous Linux. Sur Windows, la méthode recommandée est **WSL 2** (Windows Subsystem for Linux).

### 1. Installer WSL 2

#### 1.1 Activer WSL

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

#### 1.2 Vérifier l'installation

```powershell
wsl --status
wsl --list --verbose
```

Vous devriez voir une distribution Ubuntu en cours d'exécution avec WSL version 2.

### 2. Installer Python et Git dans WSL

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

### 3. Installer Hermes Agent

Suivez maintenant les mêmes étapes que pour Linux.

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 4. Accéder à Hermes depuis Windows

#### Via le terminal WSL

Depuis PowerShell ou CMD :

```powershell
wsl
# Vous êtes maintenant dans Ubuntu
# Activez votre environnement
cd ~/hermes-agent
source .venv/bin/activate
hermes run
```

#### Recommandation : utilisez Windows Terminal

[**Windows Terminal**](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701) est l'application recommandée pour utiliser Hermes sous Windows :

- Onglets multiples (PowerShell + WSL côte à côte)
- Prise en charge complète des couleurs et emojis
- Raccourcis clavier personnalisables

### 5. (Optionnel) Accès aux fichiers Windows depuis WSL

Vos fichiers Windows sont accessibles depuis WSL via :

```bash
# Disque C: monté automatiquement
ls /mnt/c/Users/VotreNom/

# Créer un alias pratique
echo 'alias winhome="cd /mnt/c/Users/VotreNom/"' >> ~/.bashrc
source ~/.bashrc
```

### 6. (Optionnel) Installer Ollama sur Windows

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

### Différences clés avec Linux

| Aspect | Linux natif | WSL Windows |
|--------|-------------|-------------|
| Performances | Optimal, bare-metal | ~95% (excellentes) |
| GPU pour Ollama | Direct (CUDA/NVIDIA) | Nécessite CUDA dans WSL |
| Démarrage auto | Systemd | Lancement manuel ou tâche planifiée |
| Accès réseau | Direct | Configuration supplémentaire |
| Mise à jour | `apt update` | Pareil (dans WSL) |

### Ressources

- [Installer WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install)
- [Windows Terminal](https://github.com/microsoft/terminal)
- [Ollama pour Windows](https://ollama.com/download)

---

## Chapitre 7 — Profils, gateways et skills

Un **profil** est une instance isolée d'Hermes avec sa propre configuration, ses propres clés API, sa mémoire et ses sessions. Chaque profil devient aussi une commande séparée.

```bash
# Créer un profil → crée aussi l'alias "mon-profil"
hermes profile create mon-profil

# Utiliser le profil
mon-profil chat           # alias complet
hermes -p mon-profil chat # flag explicite
```

### Structure d'un profil

```text
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
- **Plusieurs providers** au sein du même profil (DeepSeek + Ollama + Gemini)
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

### Gateways

Un **gateway** est le canal par lequel vous communiquez avec votre assistant.

#### Gateway Telegram (recommandé)

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

#### Gateway Discord

```yaml
gateways:
  discord:
    bot_token: "******"
```

#### Gateway local (terminal)

```bash
# Mode terminal interactif (aucune configuration)
hermes
# ou : hermes chat
```

### Skills

Les **skills** sont des procédures que l'assistant charge pour savoir comment effectuer des tâches spécifiques. C'est la mémoire procédurale de votre assistant.

#### Structure d'un skill

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

#### Skills essentiels (exemple LEO)

| Skill | Description |
|-------|-------------|
| `living-documentation` | Tenir la documentation à jour |
| `budget-tracking` | Suivi des coûts LLM |
| `leo-architecture` | Architecture et règles de fonctionnement |
| `routage-llm` | Quel LLM utiliser pour quelle tâche |
| `system-management` | Gestion des machines distantes |

#### Bonnes pratiques

- **Un skill = une responsabilité** (pas de fourre-tout)
- **Versionnez** les skills (ils évoluent avec votre assistant)
- **Stockez les corrections dans les skills**, pas en mémoire passagère
- **Patchez** un skill obsolète plutôt que d'en créer un nouveau

### Pour aller plus loin

- [Documentation Hermes : Skills](https://hermes-agent.nousresearch.com/docs)
- Voir `03-bureaux-bavi.md` pour l'architecture des bureaux LEO
- Voir `04-skills.md` pour le détail des skills système

---

## Chapitre 8 — Configuration des providers LLM

Hermes Agent peut utiliser plusieurs fournisseurs de modèles de langage (LLM). Voici comment configurer les plus courants.

### Principe

```text
Un seul profil = plusieurs providers disponibles
       │
       ├── Provider principal → Conversations, tâches complexes
       ├── Provider local → Tâches simples, gratuit, privé
       └── Provider fallback → Sécurité si le principal plante
```

### DeepSeek (recommandé pour le provider principal)

DeepSeek offre un excellent rapport qualité/prix avec son API.

#### 1. Créer un compte

1. Allez sur [platform.deepseek.com](https://platform.deepseek.com)
2. Créez un compte
3. Rechargez du crédit (quelques dollars suffisent pour commencer)
4. Générez une clé API dans la section API Keys

#### 2. Configurer

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

#### 3. Vérifier

```bash
hermes chat -q "Quel est mon solde DeepSeek ?"
```

### Ollama (provider local, gratuit)

Ollama exécute des LLM sur votre machine. Gratuit, privé, sans consommation de tokens.

#### 1. Installer Ollama

```bash
# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows → Téléchargez depuis ollama.com/download
```

#### 2. Télécharger un modèle

```bash
# Modèle recommandé pour l'assistant
ollama pull qwen2.5:7b

# Autres modèles
ollama pull llama3.1:8b    # Meta Llama 3.1
ollama pull mistral:7b     # Mistral
```

#### 3. Configurer Hermes

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

#### 4. Vérifier

```bash
curl http://localhost:11434/api/tags
```

### Google Gemini (fallback)

Gemini peut servir de provider de secours si le principal est indisponible.

#### 1. Obtenir une clé

1. Allez sur [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Créez une clé API (gratuite avec quota limité)

#### 2. Configurer

```yaml
# Dans config.yaml — comme fallback
fallback_providers:
  - provider: google
    model: gemini-3.5-flash
```

Stockez la clé dans `.env` :

```bash
echo "GEMINI_API_KEY=AIza..." >> .env
```

### Grâce à un assistant déjà configuré

Si vous configurez votre assistant comme **LEO**, l'arbitrage entre providers est automatique :

| Tâche | Provider utilisé | Coût |
|-------|-----------------|------|
| Conversation normale | DeepSeek 🤖 | Payant (faible) |
| Traitement batch, analyse simple | Ollama 🏠 | Gratuit |
| Secours si plantage | Gemini ⚡ | Gratuit (quota) |
| Scripts planifiés | Aucun LLM (no_agent) | 0 |

### Configuration avancée

#### Variables d'environnement (recommandé pour les clés)

Créez un fichier `.env` à côté de `config.yaml` :

```bash
DEEPSEEK_API_KEY="sk-..."
GEMINI_API_KEY="AIza..."
OPENAI_API_KEY="sk-..."  # Si vous utilisez OpenAI
```

#### Plusieurs providers dans un seul profil

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
    model: gemini-3.5-flash
```

Ce n'est pas grave si votre fichier `config.yaml` est plus ou moins complexe. L'important est qu'il fonctionne pour **vous**.

### Pour aller plus loin

- Voir la [documentation des providers Hermes](https://hermes-agent.nousresearch.com/docs)
- Voir le Chapitre 7 pour les profils et gateways
- Voir les tarifs DeepSeek sur [platform.deepseek.com](https://platform.deepseek.com)

---

## Chapitre 9 — Multi-bots : pourquoi 5 bots valent mieux qu'un

LEO ne tourne pas avec un seul bot Telegram, mais avec **cinq bots spécialisés** (et bientôt moins). Chaque bot a son propre profil Hermes, son propre modèle, son propre rôle — et ils communiquent entre eux.

### Pourquoi plusieurs bots ?

Un seul bot peut tout faire. Alors pourquoi en créer plusieurs ?

#### 1. Séparation des responsabilités

```text
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

#### 2. Modèles adaptés à chaque usage

| Bot | Modèle principal | Coût | Usage typique |
|:----|:-----------------|:----:|:--------------|
| LEO | DeepSeek V4 Flash | ~0,05 €/j | Quotidien, polyvalent |
| Michel | DeepSeek V4 Pro | ~0,10 €/tâche | Analyses complexes, infra |
| Sylvia | DeepSeek V4 Flash | ~0,03 €/j | Roadbooks, voyages |
| Fallback | Gemini 2.5 Flash | Gratuit (1M tokens) | Si DeepSeek indisponible |

#### 3. Isolation des tokens et permissions

Chaque bot a son propre token Telegram. Si un token est compromis ou rate-limity, les autres bots continuent de fonctionner.

```text
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

### Architecture des profils

#### Créer un profil

```bash
hermes profile create leo-copilot
```

Cette commande crée un dossier `~/.hermes/profiles/leo-copilot/` avec un `config.yaml` vierge et prépare l'alias `leo-copilot` (vous pourrez utiliser `leo-copilot chat` directement).

#### Structure d'un profil

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

#### Le fichier SOUL.md

C'est le cœur de la personnalité du bot. Il définit qui il est, ce qu'il fait et comment il se comporte.

```markdown
# Michel — Infrastructure

Tu es Michel, l'ingénieur infrastructure de l'écosystème LEO.

Tu gères :
- 42 crons (39 actifs) automatisés (+6 hôte)
- 1 dashboard central (4 onglets)
- n8n (retiré 13/07/2026 — 3 workflows historiques)
- Les gateways Hermes
- Le budget DeepSeek

Tu as accès root complet (sudo) sur la machine.
```

#### Fichier config.yaml

Exemple de configuration pour un profil spécialisé infra :

```yaml
model:
  default: deepseek-v4-pro        # Modèle puissant pour l'infra
  provider: deepseek
fallback_providers: '[{"provider": "gemini", "model": "gemini-3.5-flash"}]'
display:
  language: fr
timezone: Europe/Brussels
```

### Communication entre profils

Les profils peuvent partager des informations de plusieurs façons :

#### 1. Mémoire partagée (symlinks)

```bash
# Les deux profils pointent vers les mêmes fichiers
ln -s ~/.hermes/memories/MEMORY.md ~/.hermes/profiles/leo-copilot/memories/MEMORY.md
ln -s ~/.hermes/memories/USER.md ~/.hermes/profiles/leo-copilot/memories/USER.md
```

Quand un bot met à jour sa mémoire, l'autre voit les changements automatiquement.

#### 2. Skills synchronisés

Le profil principal (source de vérité) synchronise ses skills vers les autres profils toutes les 30 minutes :

```bash
# Sync automatique intégrée à Hermes (curator)
# Le profil default = source → pousse vers leo-copilot, bavi-leo, emile
```

#### 3. Délégation de tâches

LEO (hub central) peut déléguer des tâches complexes à Michel :

```yaml
# Dans le config.yaml de Michel
delegation:
  model: deepseek-v4-pro
  max_concurrent_children: 3
  max_spawn_depth: 1
  orchestrator_enabled: true
```

### Exemple réel : l'écosystème LEO

| Profil | Bot Telegram | Modèle | Rôle | 
|:-------|:-------------|:-------|:-----|
| `default` | LEO 🦁 | DeepSeek V4 Flash | Hub central — analyses, emails, docs |
| `leo-copilot` | Michel 🦁 | DeepSeek V4 Pro | Infrastructure — crons, système, budget |
| `bavi-leo` | Sylvia 🚐 | DeepSeek V4 Flash | Roadbooks camping-car, voyages |
| `emile` | Émile 🎓 | DeepSeek V4 Flash | Assistant pédagogique mémoire |

**Règle d'or** : si un sujet est technique (infra, cron, dashboard), LEO redirige vers Michel. Si c'est un voyage, LEO redirige vers Sylvia. Les bots savent qui fait quoi.

---

## Chapitre 10 — Skills : le super-pouvoir d'Hermès

Un skill Hermes est un fichier Markdown qui décrit **comment accomplir une tâche spécifique**. C'est le mécanisme qui transforme un assistant généraliste en expert multi-domaines.

### Principe

```text
Skill = fichier .md + dossier
├── SKILL.md          ← Les instructions : contexte, étapes, pièges
├── references/       ← Documentation complémentaire
├── templates/        ← Modèles de sortie
└── scripts/          ← Scripts exécutables
```

Quand vous posez une question, Hermes charge les skills pertinents dans son contexte et les utilise comme guide d'exécution.

#### Exemple : un skill "Installation Nginx"

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

### L'écosystème de skills LEO

Environ **28 skills** répartis en **22 catégories** :

```text
skills/
├── infrastructure/     ← Docker, Nginx, Cloudflare, backup
│   └── michel *(anciennement bureau-michel)*/SKILL.md
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

#### Skills système vs skills customs

**Skills système** (intégrés à Hermes Agent) :
- `hermes-agent` : configurer Hermes lui-même
- `computer-use` : piloter un bureau à distance
- `plan` : planifier des tâches complexes

**Skills customs** (écrits par vous ou la communauté) :
- `michel *(anciennement bureau-michel)* : infrastructure et déploiement (n8n retiré)
- `voyages-wiki` : publication de roadbooks
- `gmail-inbox-zero` : classification automatique des emails

#### Comment Hermes charge les skills

```text
1. Vous dites : "Installe Nginx sur le serveur"
2. Hermes cherche des skills pertinents
3. Trouve "infrastructure/nginx-install"
4. Charge le SKILL.md dans son contexte
5. Exécute les étapes décrites
6. Applique les pièges et vérifications
```

### Créer son premier skill

#### 1. Structure minimale

```markdown
---
name: mon-premier-skill
description: Un exemple simple
---

# Mon premier skill

Fait ceci, puis cela, puis vérifie.
```

#### 2. Avec frontmatter complet

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

#### 3. Avec sous-dossiers

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

#### 4. Règles d'or

1. **Frontmatter obligatoire** : `name`, `description`, `category`
2. **Un skill = une tâche** : pas de fourre-tout
3. **Pitfalls** : documentez ce qui peut mal tourner
4. **Vérification** : incluez une étape de validation
5. **Réutilisable** : écrivez pour que n'importe qui (ou vous-même dans 3 mois) puisse l'exécuter

### Skills et profils : la source de vérité

Dans l'écosystème LEO, le profil `default` (LEO) est la **source de vérité** des skills. Les autres profils (Michel, Sylvia, Émile) reçoivent les skills par **synchronisation automatique** toutes les 30 minutes.

```text
default (source) ──sync 30min──→ leo-copilot
                ──sync 30min──→ bavi-leo (Sylvia)
                ──sync 30min──→ emile
```

Avantage : vous mettez à jour un skill une fois, et tous les bots en bénéficient.

### Skills préinstallés utiles

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

### Gestion des skills avec le curator

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

### En résumé

| Concept | À retenir |
|:--------|:----------|
| **Skill** | Fichier .md qui décrit une tâche |
| **Catégorie** | Groupe de skills (infra, github, creative...) |
| **Source de vérité** | Un profil central push vers les autres |
| **Curator** | Nettoyage automatique des skills obsolètes |
| **Scripts** | Code exécutable dans `scripts/` |
| **Pitfalls** | Pièges documentés pour éviter les erreurs |

---

## Chapitre 11 — Mémoire persistante et profils utilisateur

Un assistant qui ne se souvient de rien est inutile. Hermes Agent propose un système de mémoire persistante qui permet à votre bot de **se souvenir de vous entre les sessions**, même après un redémarrage.

### Les deux types de mémoire

#### 1. MEMORY.md — La mémoire du système

C'est le carnet de bord de l'assistant. Il y note tout ce qui concerne l'infrastructure, les configurations, les procédures et les décisions.

```markdown
# Contenu typique
Infrastructure: serveur Ubuntu 26.04, 457Go SSD, Docker + ollama (n8n retiré 13/07)
§
Backup: quotidien vers GDrive à 04:00, rétention 7 jours
§
Budget DeepSeek: $60.31 restant, ~$0.03/jour
§
WiFi camping: "Camping Le Brasilia" — mot de passe en vault
```

#### 2. USER.md — Le profil utilisateur

Contient tout ce que l'assistant sait sur vous : vos préférences, votre style, vos proches, vos habitudes.

```markdown
Christophe (Tofdan) — conseiller stratégique IT, Sombreffe, Belgique 🇧🇪
Bilingue français/néerlandais. Fuseau Europe/Brussels.
Femme: Sylvie. Filles: Émilie (30) et Camille (26) + Célestine 🎀
Chienne: Nala 🐶
§
Style: direct, action-first, zéro blabla. Exige vérification avant livraison.
```

### Comment ça marche

#### Écriture automatique

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

#### Emplacement des fichiers

```bash
~/.hermes/memories/
├── MEMORY.md        # Mémoire système
└── USER.md          # Profil utilisateur
```

Chaque profil Hermes a ses propres fichiers de mémoire.

### Partage de mémoire entre profils

Dans l'écosystème LEO, les profils peuvent **partager la même mémoire** via des liens symboliques :

```bash
# Créer un lien symbolique pour partager la mémoire
ln -s ~/.hermes/memories/MEMORY.md ~/.hermes/profiles/leo-copilot/memories/MEMORY.md
ln -s ~/.hermes/memories/USER.md ~/.hermes/profiles/leo-copilot/memories/USER.md
```

Avantage : quand un bot apprend quelque chose, l'autre le sait aussi immédiatement.

```text
LEO (default) écrit ──→ ~/.hermes/memories/MEMORY.md
                              ↕ symlink
Michel lit ──→ ~/.hermes/profiles/leo-copilot/memories/MEMORY.md
                              (même fichier !)
```

### Cas pratique : la mémoire de LEO

#### MEMORY.md (extrait réel)

```text
RÈGLE commit : toute modif fichier repo git = commit + push immédiat
§  
Wikis: BAVI_LEO=portail, hermes-christophe=source, les2→sync+push
§
hermes binaire: /opt/hermes/.venv/bin/hermes (pas sur PATH)
§
CRASH+RECONSTRUCTION 30/06: sessions vidé→5 bots crash. 
Backup GDrive 73.7MB téléchargé + extrait. 4 gateways relancés.
§
Émile 🎓: emidanhier@gmail.com, @Bureau_ia_emilie_bot
```

#### USER.md (extrait réel)

```text
Christophe: Décisif, action directe, pattern-first.
Exige vérification AVANT livraison (curl 200, grep valeur réelle).
Zéro tolérance oubli sync (BAVI_LEO + hermes-christophe).
Préfère process automatisé aux corrections.
```

### La synchronicité cross-session

La mémoire traverse les sessions. Si vous dites "souviens-toi que mon serveur est à Bruxelles", l'information persiste :

```text
Session 1 : "Mon serveur est à Bruxelles"
  → Hermes écrit dans USER.md : "Serveur situé à Bruxelles (Europe/Brussels)"

Session 2 (le lendemain) : "Quelle est l'IP de mon serveur ?"
  → Hermes lit USER.md : "Serveur situé à Bruxelles..."
  → Peut répondre sans avoir à redemander
```

### Limites et bonnes pratiques

| Limite | Explication |
|:-------|:------------|
| **Taille max** | 2 200 caractères pour MEMORY.md, 1 375 pour USER.md |
| **Pas de recherches** | La mémoire est injectée en entier. Trop d'informations → contexte dilué |
| **Pas de structure** | Format libre, pas de base de données |
| **Un seul fichier** | Pas de sous-dossiers, pas de clés-valeurs |

#### Conseils pour une mémoire efficace

1. **Priorisez ce qui est stable** : les préférences, l'infrastructure, les règles
2. **N'écrivez pas l'évident** : inutile de noter "le ciel est bleu"
3. **Consolidez régulièrement** : fusionnez les anciennes entrées, supprimez les obsolètes
4. **Séparez les faits des tâches** : les procédures vont dans les skills, pas dans la mémoire
5. **Utilisez les sauts de section** (`§`) pour séparer les sujets

### Voir aussi

- **Ch.10** : les skills (pour les procédures réutilisables)
- **03-bureaux-bavi.md** : l'architecture LEO (comment s'organisent les profils)
- **07-annexes-cli.md** : glossaire (mémoire persistante)

---

**[Chapitre suivant → Partie III : Les Bureaux BAVI](03-bureaux-bavi.md)**

---

*Document mis à jour le 18/07/2026 à 13:00 — Léo 🦁 | v5.0*

> 🤖 Dernier audit : 24/07/2026 à 11:25 (UTC+2)
