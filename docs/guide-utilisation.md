# 📖 Guide d'utilisation — BAVI Knowledge Hub

## 🧠 Analyses Agent Pro

L'interface de visualisation des documents produits par les bureaux BAVI se trouve dans le menu **PRIVÉ → 🧠 Agent Pro**.

### Lire une analyse

1. Naviguer vers [PRIVÉ → 🧠 Agent Pro](wiki/agent-pro/index.md)
2. Choisir un bureau (Gérard, Robert, Sophie, Michel, Sylvie)
3. Cliquer sur le titre de l'analyse

Chaque analyse affiche :
- Son **numéro de version** (v1, v2, v3...)
- Son **statut** (📝 Brouillon / 🔄 En cours / ✅ Finalisé)
- Ses **tags** pour navigation par sujet
- Un **historique des versions** en bas de page

### Créer une nouvelle version d'une analyse

Pour repartir d'une analyse existante et l'améliorer :

**Méthode automatique (recommandée) :**
Demander à LEO : *"reprends l'analyse [titre] et crée la v2"*

LEO va alors :
1. Lire l'analyse existante
2. Incrémenter le numéro de version (v1 → v2)
3. Mettre à jour la date et le statut (en-cours)
4. Conserver l'ancienne version dans le tableau Versions
5. Modifier le contenu selon la demande
6. Régénérer les index automatiquement
7. Commit + push les changements

**Exemple concret :**
```
Utilisateur : "reprends l'étude d'installation n8n et crée la v2 avec la config SSL"
LEO → incrémente → modifie → archive v1 → commit → push → visible dans le wiki
```

### Comprendre le versioning

| Concept | Explication |
|:--------|:------------|
| **Version** | Numéro dans le frontmatter (`version: v1`) |
| **Historique** | Tableau Versions en bas de chaque analyse |
| **Git** | Toutes les versions sont conservées dans l'historique Git |
| **Index** | La colonne Version dans le tableau permet de voir toutes les versions |

Le frontmatter d'une analyse type :

```yaml
---
date: 2026-06-20
bureau: bureau-michel
version: v1
modele: deepseek-v4-pro
tags: [n8n, installation]
statut: finalise
---
```

### Statuts des analyses

| Statut | Signification | Action possible |
|:-------|:--------------|:----------------|
| 📝 Brouillon | Analyse en cours d'écriture | Lecture seule |
| 🔄 En cours | Analyse en révision / mise à jour | Peut être modifiée |
| ✅ Finalisé | Analyse terminée et validée | Peut servir de base à une v2 |

### Modèles utilisés

| Modèle | Usage |
|:-------|:------|
| **DeepSeek Flash** | 80% des analyses — rédaction, notes, suivi courant |
| **DeepSeek Pro** | 20% des analyses — infrastructure, code, décisions techniques |
| **Ollama** | Prototypage gratuit, tests |
