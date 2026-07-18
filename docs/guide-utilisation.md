---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v2
modele: deepseek-v4-flash
tags: [guide, utilisation, documentation, bavi-leo]
statut: ✅ À jour
type: guide
---

> **Dernière mise à jour rédactionnelle :** 18/07/2026 à 11:00 — Léo 🦁
> **Dernier commit :** `3bdd456` — 18/07/2026 à 10:30

# 📖 Guide d'utilisation — BAVI Knowledge Hub

## 🧠 Consulter un document

Tous les documents produits par les bureaux BAVI LEO sont accessibles depuis le menu du wiki :

1. Cliquer sur le **bureau** concerné dans la navigation (🔧 Michel, 🧭 Sylvia, 🤖 Léo, 📝 Gérard, 🩺 Virginie, 🎓 Émile, 🏛️ Robert, 💰 Sophie, 📚 Connaissance)
2. Le tableau liste tous les documents avec :
   - **Date** de création/mise à jour
   - **Version** (v1, v2, v3...)
   - **Titre** (cliquable pour lire)
   - **Tags** pour identifier le sujet
   - **Statut** (✅ Finalisé, 🔄 En cours, archive)
   - **Actions** : 📥 (télécharger PDF), 📦 (archiver), 🔗 (fichier brut)

### Modèles utilisés

| Modèle | Usage |
|:-------|:------|
| **DeepSeek Flash** | 80% des analyses — rédaction, notes, suivi courant |
| **DeepSeek Pro** | Analyse complexes, infrastructure, code |
| **Ollama Qwen 2.5** | 7B local — veille IA, prototypage, tests gratuits |
| **Gemini 3.5** | Fallback en cas d'indisponibilité DeepSeek |

---

## 📥 Télécharger un document en PDF

Deux méthodes :

**Depuis le tableau :**
Cliquer sur l'icône **📥** dans la colonne Actions → le navigateur ouvre l'impression → choisir **"Enregistrer en PDF"**.

**Depuis la page du document :**
Les boutons PDF (📥) et Fichier brut (🔗) sont disponibles en bas de chaque ligne.

> 💡 **Astuce** : Ctrl+P (ou Cmd+P sur Mac) fonctionne aussi depuis n'importe quelle page.

---

## 🗑️ Archiver un document

Pour archiver un document (le retirer du tableau mais le garder dans Git) :

1. Cliquer sur l'icône **📦** dans la colonne Actions
2. Une issue GitHub s'ouvre avec les infos pré-remplies
3. Soumettre l'issue → LEO archive le document automatiquement

> ⚠️ L'historique reste conservé dans Git — le document archivé est toujours récupérable via l'icône 🔄 dans la section Archivé.

---

## 🔄 Créer une mise à jour

Demander à LEO :

> *"reprends l'analyse [titre] et crée la v2"*

LEO va alors :
1. Lire l'analyse existante
2. Incrémenter la version (v1 → v2)
3. Mettre à jour la date et le statut
4. Conserver l'ancienne version dans Git
5. Modifier le contenu selon la demande
6. Commit + push

### Frontmatter d'un document type

```yaml
---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v1
modele: deepseek-v4-flash
tags: [sujet, mots-clés]
statut: ✅ Finalisé
type: analyse|rapport|note|dossier|guide
---
```

### Statuts

| Statut | Signification |
|:-------|:--------------|
| ✅ Finalisé | Document terminé et validé |
| 🔄 En cours | En révision / mise à jour |
| 📝 Brouillon | En cours d'écriture |
| archive | Déplacé dans l'archive |

---

*Document mis à jour le 18/07/2026 à 11:00 — Léo 🦁*