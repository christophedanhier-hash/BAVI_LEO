---
date: 2026-07-18
bureau: bureau-leo
auteur: Léo
version: v1
tags: [ia, evolution, chatgpt, loop-engineering, presentation, direction, notebooklm, pro]
statut: finalise
type: source-notebooklm
---

# L'Intelligence Artificielle : Évolution de 2020 à Juillet 2026
## Document source pour présentation — Direction Générale

---

## PARTIE 1 : La Révolution ChatGPT (2022-2024)

### 1.1 Avant ChatGPT — Le paysage IA en 2020-2022

- **GPT-3 (2020)** : Premier grand modèle de langage accessible via API par OpenAI. 175 milliards de paramètres. Révolutionne la perception de l'IA mais reste un outil de démonstration, pas un produit grand public.
- **DALL-E (2021)** : Génération d'images par IA. Premier signe que l'IA créative devient accessible.
- **Stable Diffusion (2022)** : Modèle open source de génération d'images. Démocratise la création visuelle par IA.
- **Limites de l'époque** : Pas d'interface conversationnelle intuitive. Les modèles sont accessibles via API, réservés aux développeurs. Pas de conscience grand public.

### 1.2 Le Big Bang — ChatGPT (Novembre 2022)

- **100 millions d'utilisateurs en 2 mois** — adoption la plus rapide de l'histoire.
- **Interface conversationnelle** : Le "prompt" devient un mot courant. L'IA devient grand public.
- **GPT-3.5 puis GPT-4 (Mars 2023)** : Sauts qualitatifs majeurs en raisonnement, compréhension, fiabilité.
- **Conséquences** :
  - Lancement d'une course mondiale (Microsoft/Bing Chat, Google Bard/Gemini, Anthropic Claude)
  - Prise de conscience des gouvernements (AI Act européen, Executive Order US)
  - Boom des investissements : +300% en 2023 vs 2022

### 1.3 La Démocratisation (2023-2024)

- **Multi-modalité** : GPT-4 Vision, DALL-E 3 — l'IA voit et génère des images.
- **Claude (Anthropic)** : Concurrent majeur, focus sur la sécurité et le "Constitutional AI".
- **Gemini (Google)** : Modèle multimodal natif, concurrence directe.
- **Mistral AI (France)** : Champion européen, modèles ouverts, focus souveraineté.
- **Open source** : Llama (Meta), Mistral, Mixtral — des modèles performants librement accessibles.
- **Premiers usages professionnels** : Copilot (Microsoft), assistants de code, chatbots d'entreprise.

---

## PARTIE 2 : L'Ère des Agents (2024-2026)

### 2.1 Du Chatbot à l'Agent

- **2024** : Les modèles ne se contentent plus de répondre, ils **agissent**.
- **Fonction Calling** : Les LLM appellent des APIs, exécutent du code, interagissent avec le monde réel.
- **Computer Use** (Claude, 2024) : L'IA contrôle directement l'interface utilisateur.
- **Codex / Claude Code** : Agents de développement autonomes qui écrivent, testent et déploient du code.

### 2.2 L'Explosion des Agents (2025-2026)

- **Multi-agents** : Plusieurs IA collaborant sur une même tâche (orchestrateur + spécialistes).
- **MCP Protocol (Model Context Protocol)** : Standard d'Anthropic pour connecter les agents aux outils et données.
- **Agent Marketplace** : Écosystème d'agents spécialisés vendus comme des apps.
- **Exemples concrets** :
  - Agents de recherche documentaire autonomes
  - Agents de veille automatisée
  - Agents de support client 24/7
  - Agents de génération de rapports
  - Agents d'audit de code et de sécurité

### 2.3 Le Paysage Actuel (Juillet 2026)

- **Modèles frontière** : GPT-5.6 (OpenAI), Claude Sonnet 5 / Opus (Anthropic), Gemini 3.5 (Google), DeepSeek V4 (Chine), Grok 4.5 (xAI)
- **Modèles ouverts** : Qwen 2.5 (Alibaba), Llama 4 (Meta), Mistral Large — performances proches des modèles fermés
- **Spécialisation** : Modèles dédiés (codage, robotique, vérification formelle, musique)
- **Agents en production** : Microsoft Copilot intégré aux licences M365, Google Agents pour le mid-market
- **Régulation** : AI Act européen en application progressive, NIS2 pour la cybersécurité

---

## PARTIE 3 : Le Nouveau Paradigme — Loop Engineering (2026)

### 3.1 Le Constat : Les Limites du Prompt Engineering Classique

**Prompt Engineering** = l'art de bien formuler sa demande à l'IA.
- ✅ Utile pour des requêtes simples, ponctuelles
- ❌ Limité pour des tâches complexes : résultats non vérifiés, répétitions, pas d'auto-correction
- ❌ Le système ne s'arrête pas quand l'objectif est atteint
- ❌ Pas de mémoire entre les itérations

### 3.2 La Révolution du Loop Engineering

**Concept popularisé en juin 2026 par :**
- **Peter Steinberger** (7 juin 2026) : Post viral (7M vues en 1 semaine) — "la compétence clé n'est plus de bien prompter, mais de concevoir la boucle qui fait tourner l'agent"
- **Addy Osmani** (8 juin 2026, Google) : Essai fondateur "Loop Engineering" — anatomie, automatisations, sous-agents, mémoire externe
- **Boris Tcharny** (Anthropic, créateur de Claude Code) : "Mon travail ne consiste plus à prompter l'IA, il consiste à écrire les boucles qui la promptent à ma place"

**Définition** : Le Loop Engineering est l'art de concevoir un système cyclique où l'IA agit, vérifie, et recommence jusqu'à ce que l'objectif soit atteint — sans intervention humaine entre les itérations.

### 3.3 Les 4 Couches de l'Interaction avec l'IA

```
1. Prompt Engineering        ← Bien formuler sa demande
2. Context Engineering       ← Fournir documents, données, historique
3. Hardness Engineering      ← Outils, contraintes, environnement, accès
4. Loop Engineering          ← Boucle : agir → vérifier → recommencer
```

### 3.4 Les 5 Composants d'une Boucle Efficace

**Composant 1 — L'Objectif Clair**
- Définition précise de ce que la boucle doit accomplir
- Critères de succès mesurables
- Exemple : "Générer 4 images valides d'un astronaute dans le métro parisien, vérifiées contre 5 critères"

**Composant 2 — Les Outils et Ressources**
- Sources de données, APIs, bases de connaissances
- Documents de référence (guides, chartes, normes)
- Connexions aux systèmes externes (YouTube, Instagram, emails)

**Composant 3 — Le Processus Cyclique**
- Agir : exécuter une action (rechercher, générer, analyser)
- Évaluer : vérifier le résultat contre les critères
- Itérer : corriger et recommencer si nécessaire
- Livrer : sortir de la boucle quand l'objectif est atteint

**Composant 4 — Le Processus de Vérification**
- L'IA ne livre jamais une réponse non vérifiée
- Auto-évaluation point par point avec critères explicites
- Détection des erreurs et des incohérences
- Comparaison avec les résultats précédents pour éviter les répétitions
- Garantit qu'aucune information n'est inventée pour "faire plaisir"

**Composant 5 — La Mémoire**
- L'agent se souvient de ce qu'il a déjà produit
- Pas de répétition entre les cycles
- Stockage des résultats intermédiaires
- Traçabilité des décisions (journal des itérations)

**Condition d'Arrêt** (Critical) :
- Doit être explicitement définie dans chaque boucle
- Exemples : "Quand 4 images valides sont obtenues", "Quand tous les messages du jour sont traités", "Quand le document est 100% conforme"
- Sans condition d'arrêt claire : boucle infinie, consommation inutile de tokens

### 3.5 Exemples Concrets de Boucles

**Exemple 1 — Recherche documentaire et vérification**
- Fournir un document source à l'IA
- Lancer une boucle : "Rédige une synthèse → Relis-la toi-même comme un vérificateur sévère → Corrige → Répète"
- Résultat : analyse approfondie avec pages citées, forces, limites signalées

**Exemple 2 — Création de contenu (YouTube accroche + description)**
- Objectif : accroche < 8 mots, crée de la curiosité
- Boucle : Proposer → Évaluer chaque critère → Recommencer si non conforme
- Résultat : titre validé + tableau d'évaluation

**Exemple 3 — Génération d'images cohérentes**
- 10 images du même personnage sans perte de constance
- Boucle : Générer une image → Vérifier 5 critères (casque fermé, panneau métro, végétation, mains, cadre) → Corriger → Valider → Image suivante
- Résultat : 4 images parfaitement cohérentes, journal des corrections

**Exemple 4 — Contrôle qualité automatisé**
- Relecture automatique des documents contre une charte graphique
- Boucle quotidienne : Vérifier conformité → Corriger écarts → S'arrêter quand 100% conforme
- Mémoire : ne pas traiter deux fois le même document

**Exemple 5 — Audit de sécurité**
- Scan de code source (HTML, PHP, SQL) pour vulnérabilités
- Boucle d'audit : Détecter faille → Corriger → Retester → Itérer jusqu'à zéro vulnérabilité critique
- Résultat : code sécurisé, rapport détaillé, fichiers corrigés

### 3.6 Claude Code : Les Commandes Spécifiques

- **`/goal`** : Définit un objectif. Claude exécute tout le travail sans revenir à chaque étape. Idéal pour des tâches longues.
- **`/loop`** : Transforme la session en boucle autonome. Claude vérifie périodiquement (toutes les heures, jours...) et continue même après fermeture de session.
- **Usage combiné** : `/goal` fixe la destination → `/loop` maintient l'itération dans le temps
- **Exemple** : `/goal` "Réponds à tous les commentaires YouTube en attente" → `/loop` "Vérifie les nouveaux commentaires toutes les heures, note-les dans un fichier"

---

## PARTIE 4 : Impact pour la Direction Générale

### 4.1 Opportunités Stratégiques

- **Productivité** : Les boucles automatisées traitent des tâches chronophages (veille, reporting, contrôle qualité) sans intervention humaine
- **Qualité** : Résultats vérifiés, auto-corrigés, sans les erreurs répétitives du prompt classique
- **Disponibilité** : Tâches qui tournent 24/7, même quand l'utilisateur a éteint son poste
- **Passage à l'échelle** : Une boucle conçue une fois peut traiter des volumes croissants sans effort supplémentaire

### 4.2 Points d'Attention

- **Coût token** : Une boucle qui tourne sans condition d'arrêt claire peut consommer des ressources inutilement
- **Gouvernance** : Nécessité de contrôler ce que les boucles font, auditer leurs décisions
- **Sécurité** : Un agent avec accès à des systèmes sensibles doit être strictement encadré (hardness engineering)
- **Compétences** : La compétence clé évolue — du "bien prompter" au "bien concevoir des boucles"

### 4.3 Les 3 Questions à se Poser

1. **Quelles tâches répétitives pourrions-nous automatiser avec des boucles ?** (veille, reporting, contrôle qualité)
2. **Quelles sont nos conditions d'arrêt ?** (sans quoi la boucle tourne à perte)
3. **Quelle est notre charte qualité ?** (critères précis, vérifiables par l'IA)

---

## Sources et Références

- Addy Osmani, "Loop Engineering" — Essai fondateur, 8 juin 2026
- Peter Steinberger — Post viral sur le nouveau paradigme, 7 juin 2026 (7M vues)
- Boris Tcharny (Anthropic) — Concept de "la boucle comme unité de travail"
- Barthélémy Nobili — Vidéo "Loop Engineering : la nouvelle norme de l'IA" (43 min), juillet 2026
- OpenAI — GPT-5.6, GPT-Live (2026)
- Anthropic — Claude Sonnet 5, Claude Code (2026)
- Google DeepMind — Gemini 3.5 Pro (2026)
- Mistral AI — Robostral Navigate, Leanstral 1.5 (2026)
- European Commission — AI Act, Digital Omnibus amendments (2026)
- Gartner — Agentic arbitrage forecast (2026)

---

*Document préparé pour NotebookLM — Juillet 2026*
