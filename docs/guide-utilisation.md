# 📖 Guide d'utilisation — BAVI Knowledge Hub

## 🧠 Analyses Agent Pro

L'interface de visualisation des documents produits par les bureaux BAVI se trouve dans le menu **PRIVÉ → 🧠 Agent Pro**.

### Lire un document

1. Naviguer vers le bureau concerné dans le menu **🧠 Bureaux**
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

---

## 📥 Télécharger une analyse en PDF

Deux méthodes :

**Depuis le tableau des analyses :**
Cliquer sur l'icône **📥** dans la colonne Actions → le navigateur ouvre la boîte de dialogue d'impression → choisir **"Enregistrer en PDF"** comme destination.

**Depuis la page de l'analyse :**
Un bouton PDF (icône 📄) est disponible en haut de chaque page d'analyse → cliquer → imprimer → enregistrer en PDF.

> 💡 **Astuce** : Ctrl+P (ou Cmd+P sur Mac) fonctionne aussi depuis n'importe quelle page.

## 🗑️ Supprimer une analyse

La suppression ne se fait pas depuis le wiki (site statique). Pour supprimer une analyse :

**Méthode :** Demander à LEO :

> *"supprime l'analyse [titre]"*

LEO va alors :
1. Supprimer le fichier source dans `/opt/data/hermes-christophe/BAVI/AGENT-PRO/<bureau>/`
2. Régénérer les index automatiquement
3. Commit + push la suppression
4. L'analyse disparaît du tableau

> ⚠️ L'historique reste conservé dans Git — la version supprimée est toujours récupérable.
