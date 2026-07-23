---
date: 2026-07-08
bureau: bureau-versioning
version: v1
modele: deepseek-v4-flash
tags: [analyse, scope, skills, workflows, bavi-leo]
statut: archive
type: analyse
---

# 📋 Analyse du Bureau Versioning — Gestion des Versions

## 📋 Scope

Le **Bureau Versioning** est un **skill transverse** qui gère les versions des documents produits par tous les bureaux BAVI LEO. Il n'est pas un bureau producteur d'analyses, mais un **service** utilisé par les autres bureaux.

**Périmètre fonctionnel :**
- Incrémentation des versions (v1 → v2 → v3…)
- Mise à jour du frontmatter (date, version, statut)
- Conservation du contenu existant + itération
- Ajout d'entrée dans la section Versions
- Synchronisation source (AGENT-PRO) ↔ wiki (BAVI_LEO)
- Auto-archive automatique des analyses (cron 5 min)
- Génération PDF des analyses

## 🧠 Skills utilisés

| Skill | Rôle | Usage |
|-------|------|-------|
| **bureau-versioning** ⭐ | Skill principal | Versioning des analyses BAVI |

## 🔄 Workflows définis

### Workflow versioning

```
① Identifier source → ② Lire frontmatter → ③ Incrémenter version → ④ Mettre à jour contenu → ⑤ Ajouter section Versions → ⑥ Synchroniser wiki → ⑦ Commit + push
```

### Auto-archive (automatisé)

```
📦 Utilisateur clique → Issue GitHub créée
⏱️ Cron 5 min → Vérifie issues label "archive"
📦 Fichier déplacé vers archive/ dans AGENT-PRO + wiki
🔄 Index regénéré via agent-pro-index.py
🚀 Commit + push GitHub
✅ Issue fermée automatiquement
```

### Suppression d'analyse

```
① rm fichier.md (source + wiki)
② python3 agent-pro-index.py --regenerate
③ git add + commit + push BAVI_LEO
✅ Analyse disparaît du tableau
```

## 🔗 Interopérabilité

**Utilisé par TOUS les bureaux** quand une analyse doit être :
- Mise à jour (nouvelle version)
- Archivée (déplacée vers archive/)
- Supprimée

## 📊 État

Cron auto-archive actif (toutes les 5 min, no_agent=true). Label `archive` créé sur BAVI_LEO.

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)

