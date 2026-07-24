---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v2
modele: deepseek
tags: [guide, utilisation, documentation, bavi-leo]
statut: ✅ À jour
type: guide
---

> **Dernière mise à jour rédactionnelle :** 18/07/2026 à 11:00 — Léo 🦁
> **Dernier commit :** `3bdd456` — 18/07/2026 à 10:30

# 📖 Guide d'utilisation — BAVI Knowledge Hub

## 🧠 Consulter un document

Vérifier l'actualité des profils et bots utilisés dans les instructions.

1. Cliquer sur le **bureau** concerné dans la navigation (🔧 Michel, 🧭 Sylvia, 🤖 Léo, 📝 Gérard, 🩺 Virginie, 🎓 Émile, 🏛️ Robert, 💰 Sophie, 📚 Connaissance)
2. Le tableau liste tous les documents avec :
   - **Date** de création/mise à jour
   - **Version** (v1, v2, v3...)
   - **Titre** (cliquable pour lire)
   - **Tags** pour identifier le sujet
   - **Statut** (✅ Finalisé, 🔄 En cours, archive)
   - **Actions** : 📥 (télécharger PDF), 📦 (mettre à l'archive — retire du tableau actif), 🔗 (fichier brut)

### Modèles utilisés

Mettre à jour les modèles utilisés dans la documentation.

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

## 🗑️ Supprimer un document

Pour supprimer définitivement un document (retirer du tableau + supprimer le fichier) :

Demander à LEO :

> *"supprime l'analyse [titre]"*

LEO va alors :
1. Supprimer le fichier source dans le dépôt
2. Régénérer l'index automatiquement
3. Commit + push la suppression
4. Le document disparaît du tableau

> ⚠️ L'historique Git conserve une trace — le fichier supprimé est toujours récupérable via `git log`.

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
modele: deepseek
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

> 🤖 Dernier audit : 24/07/2026 à 12:11 (UTC+2)
