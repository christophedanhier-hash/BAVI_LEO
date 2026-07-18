---
date: 2026-07-18
bureau: bureau-leo
auteur: Léo
version: v1
tags: [video, loop-engineering, notebooklm, prompt, ia, presentation, pro]
statut: finalise
type: prompt-notebooklm
---

# 🎬 Prompt NotebookLM — Script Vidéo
## "Loop Engineering : La nouvelle norme de l'IA expliquée simplement"

### Contexte
Tu es Barthélémy Nobili (chaîne YouTube IA, 145k abonnés). Tu crées une vidéo pédagogique pour expliquer le Loop Engineering à un public francophone non technique — dirigeants, entrepreneurs, curieux tech.

### Format attendu
Vidéo de 15-20 minutes, structurée en 5 actes :

**ACTE 1 — L'accroche (0-2 min)**
- Constat : "Le prompt engineering, c'est fini. Non pas que ça ne marche plus, mais il y a 100x mieux."
- Question forte : "Et si au lieu de bien formuler vos questions, vous conceviez le système qui pose les questions à votre place ?"
- Peter Steinberger (7 juin 2026) : 7 millions de vues en une semaine
- Addy Osmani (Google, 8 juin 2026) : l'essai fondateur
- Boris Tcharny (Anthropic, créateur de Claude Code) : "Mon travail ne consiste plus à prompter l'IA, il consiste à écrire les boucles qui la promptent à ma place"

**ACTE 2 — Prompt vs Loop : la différence (2-5 min)**
- **Prompt Engineering** : "Je demande, l'IA répond, je vérifie, je demande mieux" → à chaque message, je recommence
- **Loop Engineering** : "Je conçois un système → l'IA agit, vérifie, corrige, recommence toute seule → résultat livré"
- Analogie du hamster dans sa roue : la boucle ne s'arrête que quand l'objectif est atteint
- Les 4 couches : Prompt → Context → Hardness → Loop

**ACTE 3 — L'anatomie d'une boucle (5-10 min)**
Détail des 5 composants avec exemples visuels :

1. **L'Objectif** : "Génère 4 images d'un astronaute dans le métro parisien"
2. **Les Outils** : Documents, APIs, bases de connaissances
3. **Le Processus** : Agir → Évaluer → Itérer → Livrer
4. **La Vérification** : L'IA se vérifie elle-même point par point
5. **La Mémoire** : L'agent se souvient de ce qu'il a déjà fait (pas de répétition)

⚠️ **Condition d'arrêt** : Oubliée 9 fois sur 10 → boucle infinie → tokens gaspillés

**ACTE 4 — 3 exemples parlants (10-15 min)**

*Exemple 1 : Analyse documentaire*
- "Rédige une synthèse, relis-la comme un correcteur sévère, corrige, répète"
- Résultat : analyse 10x plus complète qu'un prompt unique
- Le système cite les pages, détecte les erreurs, signale les incertitudes

*Exemple 2 : Création d'images cohérentes*
- 10 images du même personnage sans perte de constance
- 5 critères de validation (casque fermé, panneau métro, végétation, mains, cadre)
- La boucle rejette, reformule, régénère jusqu'à validation

*Exemple 3 : Veille automatisée*
- "Tous les jours à 8h, actualité sur le Loop Engineering"
- Vérification : ne jamais répéter une info déjà donnée
- Condition d'arrêt : "Quand tous les nouveaux articles du jour sont traités"

**ACTE 5 — Conclusion & Call to Action (15-18 min)**
- Le Loop Engineering : pas une mode, le nouveau standard
- "Le mettre de côté serait une erreur — les résultats sont incomparablement meilleurs"
- Où commencer : prendre une tâche répétitive, ajouter une boucle de vérification
- Ressources : Claude Code (`/goal` + `/loop`), ChatGPT (boucles dans le contexte), Gemini

### Style
- Dynamique, rythmé
- Exemples concrets montrés (captures d'écran, démos)
- Pas de jargon technique
- Alternance : concept → exemple → concept → exemple
- Questions rhétoriques pour maintenir l'attention
- Fichier .md attendu en sortie : script complet avec indications temps + visuels
