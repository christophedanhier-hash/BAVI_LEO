---
date: 2026-07-21
bureau: bureau-robert
projet: DEV-IA-SOLIDARIS
phase: 1
version: v1
tags: [template, extraction, prompt, methodologie, reutilisable, mainframe, pl1]
statut: finalise
type: template-extraction
---

# 🧩 Template d'Extraction — Analyse de Code Source
## Modèle réutilisable pour extraire connaissance business et IT

> **Usage :** À fournir à n'importe quel outil IA (Claude Code, Codex, BOB, GitHub Copilot, Kilo Code...)
> **Source :** Code source dans Git/VS Code
> **Langage cible :** PL/1, COBOL, Java, Python, etc.
> **Version template :** v1

---

## Instructions pour l'outil IA

# MISSION : ANALYSE ET EXTRACTION DE CONNAISSANCE

Tu es un expert en analyse de code legacy. Ta mission est d'analyser
une application source et d'en extraire la connaissance business et
technique sous forme structurée.

## RÈGLE ABSOLUE
Commence TOUJOURS par un inventaire exhaustif de TOUS les fichiers
sources disponibles. Ne passe à l'analyse qu'une fois l'inventaire
complété et vérifié. L'omission de sources est la première cause
d'échec des projets d'extraction.

## CONTEXTE DU PROJET

À compléter :
- Nom du projet : [NOM]
- Langage : [PL/1, COBOL, Java, Python...]
- Type : [Batch, Online, API, Microservice...]
- Sources : [Chemin du workspace Git]
- Objectif métier : [Description]

---

## PHASE A — CARTOGRAPHIE

### A1 — Inventaire exhaustif des sources
Liste récursivement tous les fichiers du workspace.
Classe-les par type :

| Type | Nombre | Exemples |
|------|--------|----------|
| Programmes principaux | | |
| Programmes appelés | | |
| Copybooks / Includes | | |
| Fichiers de données | | |
| Scripts / JCL | | |
| Configuration | | |
| Documentation | | |

Pour chaque fichier : nom, chemin, taille (lignes), type.

### A2 — Structure du workspace
Produis l'arborescence complète des répertoires.

### A3 — Points d'entrée
Identifie les points d'entrée de l'application :
- Batch : JCL, scripts, planificateur
- Online : transactions CICS, APIs, endpoints
- Autres : triggers, files d'attente

---

## PHASE B — EXTRACTION DES CONNAISSANCES

### B1 — Flux de données
Pour chaque point d'entrée identifié :
1. Quelles sont les données d'entrée ?
2. Quelles transformations subissent-elles ?
3. Quelles sont les données de sortie ?
4. Y a-t-il des effets de bord (fichiers, DB, messages) ?

Format : Diagramme Mermaid flowchart

### B2 — Flux de contrôle
Pour chaque programme/script :
1. Quel est son rôle ?
2. Quels programmes appelle-t-il ?
3. Par quels programmes est-il appelé ?
4. Quelles sont les conditions de branchement principales ?

Format : Diagramme Mermaid ou matrice d'appels

### B3 — Règles métier
Extrais TOUTES les règles métier du code :
- Conditions IF/THEN/ELSE
- Tables de décision
- Calculs et formules
- Validations et contrôles
- Codes retour et signification

Format : Tableau structuré

| Règle | Description | Localisation (fichier:ligne) | Type |
|-------|-------------|------------------------------|------|

### B4 — Glossaire
Extrais tous les termes techniques et abréviations :
- Noms de programmes
- Codes transaction
- Abréviations métier
- Acronymes techniques

Format : Tableau bilingue si applicable

| Terme | Définition | EN/NL/FR |
|-------|------------|----------|

### B5 — Dépendances techniques
Pour chaque composant, liste ses dépendances :
- Programmes appelés
- Copybooks / Includes utilisés
- Tables DB2 / Fichiers accédés
- APIs / Services externes

Format : Matrice de dépendances

---

## PHASE C — MODÉLISATION

### C1 — BPMN Processus métier
Modélise le processus métier principal en BPMN :
- Événement de début
- Activités (tâches manuelles, automatiques)
- Décisions / Gates
- Flux de séquence
- Événement de fin

Format : Mermaid flowchart (BPMN-like)

### C2 — Architecture applicative
Produis un schéma d'architecture :
- Composants applicatifs
- Dépendances entre composants
- Flux de données
- Interfaces externes

Format : Mermaid flowchart

### C3 — Schéma des données
Modélise les données :
- Entités principales (tables DB2, fichiers, structures)
- Relations entre entités
- Attributs clés

Format : Mermaid erDiagram

### C4 — Diagramme de déploiement
Comment l'application est déployée :
- Serveurs / partitions
- Flux réseau
- Stockage

Format : Mermaid flowchart

---

## PHASE D — SYNTHÈSE

### D1 — Analyse fonctionnelle par composant
Pour chaque programme/script majeur :
| Programme | Rôle | Entrées | Sorties | Appels | Règles |
|-----------|------|---------|---------|--------|--------|

### D2 — Analyse qualité du code
- Complexité cyclomatique (si mesurable)
- Duplication
- Constantes "hardcodées"
- Commentaires vs code
- Points d'attention pour modernisation

### D3 — Recommandations
- Points durs identifiés
- Opportunités de réécriture
- Risques de régression
- Dépendances critiques

---

## LIVRABLES ATTENDUS

1. 📄 Ce document complété (le template rempli)
2. 📊 Diagrammes Mermaid (BPMN, architecture, données, flux)
3. 📋 Tableaux (règles, glossaire, dépendances)
4. 📝 Synthèse exécutive (1 page max)

## RÈGLES DE QUALITÉ

- ✅ Tout diagramme doit être en Mermaid (pas d'ASCII art)
- ✅ Toute règle métier doit être localisée (fichier:ligne)
- ✅ L'inventaire doit être exhaustif (pas de sources oubliées)
- ✅ Le glossaire doit couvrir tous les acronymes du code
- ✅ La synthèse doit être compréhensible par un non-technicien

---

## Guide d'utilisation

### Application à une nouvelle application

```
1. Copier ce template dans un fichier .md
2. Remplir la section "Contexte du projet"
3. Donner le template + le workspace à l'outil IA choisi
4. Valider les livrables produits selon les règles de qualité
5. Itérer si nécessaire
```

### Outils compatibles

| Outil | Usage recommandé |
|:------|:-----------------|
| **Claude Code** | Analyse interactive, terminal |
| **Codex** | Automatisation par lots |
| **BOB** | Suivi du template 16 sections |
| **GitHub Copilot** | Analyse dans VS Code |
| **Kilo Code** | Agent autonome |

---

*Template d'extraction v1 — Produit par Robert 🏛️*
*Réutilisable pour toute application — PL/1, COBOL, Java, Python...*
