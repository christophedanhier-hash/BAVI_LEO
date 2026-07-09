---
date: 2026-07-09
bureau: bureau-michel
version: v1
modele: deepseek-v4-flash
tags: [microsoft, scout, autopilot, agent-autonome, ia]
statut: analyse
type: analyse
source: YouTube — Shane Young (PowerApps911)
---

# Analyse — Microsoft SCOUT (Autopilot)

> **Bureau :** Michel 🛠️
> **Source :** [Microsoft Scout Hands-On — Shane Young](https://youtu.be/PoSWJl3xWrI)
> **Date :** 09/07/2026
> **Modèle :** DeepSeek V4 Flash

---

## 💳 Coût du service BAVI LEO

| Métrique | Valeur |
|:---------|:------:|
| Tokens (transcription + analyse) | ~12 000 |
| Coût DeepSeek V4 Flash | ~$0.003 |
| Frais de service BAVI (×3.5) | $0.01 |
| **Total** | **$0.01** |

---

## 1. Résumé Exécutif

**Microsoft SCOUT** est le premier « Autopilot » de Microsoft — une nouvelle catégorie d'agent IA autonome qui tourne directement sur le poste de travail Windows de l'utilisateur. Contrairement à Copilot Chat (conversation one-off) et Co-work (exécution de recettes à la demande), Scout est conçu pour fonctionner **en arrière-plan, sans supervision humaine**, avec la capacité d'interagir avec le système de fichier local, le navigateur, PowerShell, et d'installer/exécuter du code (Python, npm).

> **Position clé :** SCOUT = l'agent personnel autonome de Microsoft. Pas un outil enterprise, pas un chatbot — un véritable assistant local.

---

## 2. Positionnement dans l'Écosystème Microsoft

| Outil | Type | Autonomie | Cible |
|:------|:-----|:---------:|:------|
| **Copilot Chat** | Conversation one-off | 🔴 Aucune | Tous |
| **Co-work** | Exécution de recettes (SOP) | 🟡 Sur demande | Tous |
| **Scout (Autopilot)** | Agent autonome local | 🟢 Continue | Individu |
| **Agent Builder** | Chatbot configurable | 🔴 Conversationnel | Teams/Web |
| **Copilot Studio** | Agent enterprise | 🟡 Configurable | Départements |

> **Citation clé :** *« CO-PILOT Chat c'est « fais ça maintenant ». CO-WORK c'est « va exécuter cette recette ». SCOUT c'est « tourne en fond et agis pour moi sans que j'aie à intervenir ». »*

---

## 3. Fonctionnalités Détaillées

### 3.1. Chat — Interface conversationnelle

Interface de dialogue avec **3 personnalités** configurables :

| Personnalité | Description |
|:-------------|:------------|
| Default (Helpful & Professional) | Neutre, professionnel |
| Sarcastic Teenager 🧑‍🎤 | Réponses sarcastiques, humour (« Si tu me laisses tranquille, je pourrai retourner regarder TikTok ») |
| Enthusiastic Intern | Dynamique, enthousiaste |

> La personnalité n'est pas un simple skin — elle modifie le ton des réponses et influence l'interaction.

### 3.2. Automations — Déclencheurs programmés

Système de déclencheurs similaire à Power Automate :

- **Schedule** : toutes les heures, quotidien, hebdomadaire
- **Trigger fichier** : quand un fichier est modifié/ajouté
- **Prompt lié** : action exécutée = un prompt pré-défini

**Exemple donné :** « Tous les jours à 16h, vérifie s'il y a de nouvelles vidéos YouTube, scrape-les et génère le contenu associé. »

Les permissions sont **granulaires par automation** — on peut interdire à une automation d'accéder au file system ou d'exécuter du code.

### 3.3. Heartbeats — Prompts rythmés

Mécanisme de **prompts automatiques sur un schedule régulier** :

- Fréquence : 30min, 1h, 2h, pendant les heures de travail ou 24/7
- Usage typique : trier la inbox, surveiller un dossier, checker l'arrivée d'un fichier

> **⚠️ Attention coût :** chaque heartbeat consomme des crédits GitHub Copilot. Ne pas mettre un heartbeat toutes les 15min 24/7 sans réflexion.

### 3.4. Skills — Recettes pré-packagées

Skills = recettes en **Markdown** (même format que les skills Hermes). Exemples pré-installés :

- Word, PowerPoint, Excel, Loop
- Build websites / HTML files
- Power Automate integration
- YouTube to blog (skill ajouté par le vidéaste)

**Ajout de skills :** l'utilisateur peut demander à Scout d'apprendre une tâche et de la transformer en skill réutilisable.

### 3.5. MCP Servers — Extensibilité

Support du **Model Context Protocol** (MCP) pour connecter des sources de données externes :

- Dataverse / Dynamics
- Power Apps
- Tout serveur MCP

> Le vidéaste ne l'a pas testé mais confirme que ça étend considérablement les capacités de Scout au-delà du « bac à sable » Microsoft.

---

## 4. Capacités Techniques Détaillées

### 4.1. Interaction Système de Fichier

Scout voit et interagit avec les dossiers locaux :
- A listé le contenu du dossier Downloads
- A identifié les plus gros fichiers .exe (PowerShell)
- A supprimé 31 installateurs = **4.4 Go libérés**

### 4.2. Exécution de Code

| Type | Exemple |
|:-----|:--------|
| **PowerShell** | Trouver et supprimer des fichiers, analyser le disque |
| **Python** | Écrire et exécuter des scripts pour scraper YouTube |
| **npm / Node.js** | Installer yt-dlp et l'utiliser |

> **Le vidéaste insiste :** il n'a jamais écrit une ligne de Python. Scout a fait tout le cycle : installer les dépendances, écrire le script, l'exécuter, sauvegarder le résultat.

### 4.3. Navigation Web

Via **Playwright** (framework d'automatisation navigateur) :
- Peut ouvrir un navigateur
- Naviguer sur des sites
- Scraper du contenu
- **Ne gère pas les mots de passe** (pas un password manager)

### 4.4. Mémoire

Scout apprend de l'utilisateur au fil du temps — mémoire intégrée qui s'enrichit avec l'usage. Les sessions sont conservées avec une durée configurable dans les paramètres.

---

## 5. Sécurité & Guardrails

### 5.1. Architecture de permissions

Chaque action sensible déclenche une **demande de permission** :

```
🔒 Scout veut exécuter PowerShell pour supprimer des fichiers :
   • Allow for this session
   • Deny
   • Allow always
```

### 5.2. Contraintes enterprise (le gros frein)

| Étape | Difficulté |
|:------|:----------:|
| Être une organisation **Microsoft Frontier** | Faible (déjà fait pour beaucoup) |
| Configurer une **politique Intune** sur les devices cibles | **Élevée** — nécessite Intune, GPO, déploiement IT |
| Remplir le **formulaire de consentement** (données hors safe bubble) | Moyenne |
| Avoir un **GitHub Copilot Business/Enterprise** license | Variable |
| **Windows 11** | Faible |

> **Le vidéaste :** *« Ces trois étapes m'ont pris des heures. C'est pour ça que vous ne voyez pas un flot de vidéos — c'est vraiment dur à setup. »*

### 5.3. Data Processing Outside Microsoft Bubble

Scout peut envoyer des données à des modèles externes (Gemini, etc.) si GitHub Copilot est configuré pour. L'utilisateur doit **explicitement consentir** à ce que ses données sortent du périmètre de protection Microsoft.

---

## 6. Modèles Disponibles & Coûts

| Modèle | Coût estimé | Usage recommandé |
|:-------|:-----------:|:-----------------|
| **Opus 47** | 💰💰💰💰💰 | Tâches complexes, raisonnement profond |
| **Sonic 46** | 💰💰💰 | Bon universel |
| **Gemini 31 Pro** | 💰💰💰 | Si besoin Google |
| **GPT 41** | 💰 | Tâches simples, économique |
| **Auto** | Variable | Choix automatique |

### 6.1. Modèle de licence

> **Ce n'est PAS inclus dans M365 Copilot.**

Licence requise : **GitHub Copilot Business** ou **Enterprise** avec crédits disponibles.

Les crédits sont consommés par :
- Chaque chat / requête
- Chaque heartbeat
- Chaque automation run

> **Conseil du vidéaste :** choisir le modèle adapté à la complexité de la tâche. Nettoyer son disque dur avec GPT 41 suffit — pas besoin d'Opus 47.

---

## 7. Limitations & Points d'Attention

### 7.1. Configuration complexe

Le principal frein à l'adoption est **la lourdeur du déploiement** :
- Nécessite Intune (outil de gestion de parc IT)
- Organisation Microsoft Frontier
- Processus de plusieurs heures pour un premier setup
- Impossible pour un utilisateur individuel sans admin IT

### 7.2. Coûts cachés

- Les crédits GitHub Copilot ne sont pas illimités
- Un heartbeat 24/7 peut épuiser rapidement les crédits
- Le modèle choisi impacte directement la consommation

### 7.3. Période frontier

Le produit est encore en phase « frontier » — susceptible de changer. API, licensing, fonctionnalités peuvent évoluer.

### 7.4. Pas de gestion des identifiants

Scout ne gère pas les mots de passe. Si une tâche nécessite une authentification, elle échoue (le vidéaste l'a constaté en tentant d'accéder à son compte YouTube).

---

## 8. Comparaison avec L'Écosystème Actuel

### 8.1. SCOUT vs Hermes Agent (Nous Research)

| Critère | SCOUT | Hermes Agent (LEO) |
|:--------|:-----:|:------------------:|
| Local/Cloud | **Local** (Windows) | **Local** (Linux/Docker) |
| Personnalités | 3 prédéfinies | Skills + mémoire personnalisée |
| Exécution code | ✅ PowerShell, Python, npm | ✅ Terminal, Python (venv) |
| Automations | ✅ Heartbeats + triggers | ✅ Crons (22 jobs) |
| MCP support | ✅ | Via skills |
| Prix | Crédits GitHub Copilot | DeepSeek API ($0.14–0.87/Mtok) |
| OS | **Windows 11 uniquement** | Linux (tout) |
| Setup | Complexe (Intune, Frontier) | Simple (Docker, pip) |
| Guardrails | Intune + permissions granulaires | Règles système + profiles |
| Skills | Markdown, format Microsoft | SKILL.md, format Hermes |

### 8.2. SCOUT vs n8n

| Critère | SCOUT | n8n (LEO) |
|:--------|:-----:|:----------:|
| UI No-code | ✅ | ✅ |
| Triggers programmés | ✅ Heartbeats | ✅ Crons |
| Exécution code | ✅ (sandboxé) | ✅ (Python/JS) |
| MCP/APIs | ✅ MCP | ✅ 400+ nodes |
| Local files | ✅ Natif | ❌ (cloud-first) |
| Prix | Crédits GH Copilot | Gratuit (self-hosted) |

---

## 9. Verdict & Recommandations

### Points Forts

- 🟢 **Premier agent véritablement autonome** de Microsoft — ouvre la catégorie « Autopilot »
- 🟢 **Interaction avec le système local** — brise le plafond de verre des agents cloud Microsoft
- 🟢 **Exécution de code** (PowerShell, Python, npm) — extrêmement puissant
- 🟢 **Personnalité** — l'aspect « Sarcastic Teenager » humanise l'interaction
- 🟢 **Skills en Markdown** — format simple, compatible mentalement avec Hermes
- 🟢 **MCP support** — extensible au-delà de l'écosystème Microsoft

### Points Faibles

- 🔴 **Setup extrêmement lourd** (Intune, Frontier, heures de config)
- 🔴 **Windows 11 uniquement** — pas de Linux, pas de Mac
- 🔴 **Licence GitHub Copilot requise** — coût récurrent basé sur les crédits
- 🔴 **Période frontier** — produit instable, risques de changement
- 🔴 **Données hors safe bubble** — peut exposer les données à des modèles externes
- 🔴 **Pas de password manager** — limite les usages authentifiés

### Recommandation LEO

Pour Christophe :
- **SCOUT n'est pas adapté à LEO** (serveur Linux, pas de Windows 11)
- **Intérêt à surveiller** : l'approche « Autopilot » (agent autonome local) confirme la direction du marché
- **Points à creuser pour LEO** : skills en Markdown, MCP servers, heartbeat pattern
- **Concurrence bien placée** : Hermes + n8n couvre déjà 90% de ce que SCOUT promet, avec plus de flexibilité et sans le lock-in Microsoft

> **Conclusion :** SCOUT valide la **vision des agents autonomes personnels** (la même que LEO). Mais son déploiement Windows-only et sa complexité de setup le rendent inaccessible pour l'infrastructure Linux de Christophe. Hermes Agent + n8n restent la meilleure option.

---

## 10. Références

- Vidéo source : [Microsoft Scout Hands-On — Shane Young](https://youtu.be/PoSWJl3xWrI)
- PowerApps911 : https://www.powerapps911.com
- Documentation Microsoft Scout (Frontier) : à confirmer
- Skill BAVI associé : `bavi-leo/bureau-michel`
