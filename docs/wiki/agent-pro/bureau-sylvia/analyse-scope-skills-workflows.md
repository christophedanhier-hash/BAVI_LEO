---
date: 2026-07-08
bureau: bureau-sylvia
version: v1
modele: deepseek-v4-flash
tags: [analyse, scope, skills, workflows, bavi-leo]
statut: finalise
type: analyse
---

# 🧭 Analyse du Bureau Sylvia — Agence de Voyage

## 📋 Scope

Le **Bureau Sylvia** est l'agence de voyage complète pour Christophe et ses amis. Catégorie **PRIVÉ** 🏠. Déployé comme **bot Telegram** [@bavi_leo_voyages_bot](tg://resolve?domain=bavi_leo_voyages_bot) sur un profil Hermes isolé (`bavi-leo`).

**Périmètre fonctionnel :**
- Tous types de voyages : camping-car, voiture, avion, train, moto, bus
- Hébergements : campings, hôtels, locations, aires CC, auberges
- Transports : location vélo/moto/voiture, billets train/avion, ferries
- Roadbooks complets avec cartes OSM interactives
- Points d'intérêt, visites, logistique voyage (ZTL, parkings, péages)
- Budget voyage
- **Contexte multi-utilisateurs** (groupe Telegram partagé)

## 🧠 Skills utilisés

| Skill | Rôle | Usage |
|-------|------|-------|
| **bureau-sylvia** ⭐ | Skill principal | Agente de voyage — scope complet, 14+ sections |
| **maps** (OSRM/Nominatim) | Cartographie | Géocodage POIs, distances routières |
| **gmail-inbox-zero** | Gmail | Lecture emails de réservation |
| **leo-email-assistant** | Envoi email | Confirmation réservation via LEO |
| **google-workspace** | Google Workspace | Docs/Sheets pour partage |
| **mkdocs-wiki** | Wiki voyages | Structure MkDocs Material |
| **bureau-versioning** | Versioning | Gestion versions roadbooks |

**Expertise :** DeepSeek V4 Flash (modèle unique).

## 🔄 Workflows définis

### Workflow roadbook — 6 phases BAVI

```
① CADRAGE → ③ PRODUCTION → ④ CROISEMENT → ⑤ SYNTHÈSE → ⑥ LIVRABLE → ⑦ ARCHIVAGE
```

Pas de dispatch en tant que tel (pas de sous-experts formels), mais production itinéraire intégrée.

### Workflows opérationnels détaillés (A à L)

| Workflow | Description |
|:---------|:------------|
| **A. Carte OSM Folium** | Génération carte interactive avec marqueurs, légende, cercles distance |
| **B. Historique destination** | Recherche web de 2-3 faits marquants par étape |
| **C. Carte POI ville** | Batch géocodage + marqueurs groupés par catégorie |
| **D. Extraction tokens + coûts** | Calcul coût DeepSeek + mise à jour KPIs |
| **E. Génération PDF** | WeasyPrint → PDF with sanitized content |
| **F. Création page wiki** | Index.md + mkdocs.yml + docs/index.md |
| **G. Roadbook express** | Format allégé pour mini-voyages |
| **H. Suivi en direct** | Live tracking pendant le voyage |
| **I. Dépannage technique** | Recherche ressources réparation CC |
| **J. Roadbook hôtel** | Format spécifique hôtel + voiture de location |
| **K. Conseils achat CC** | Recommandation modèles camping-car |
| **L. Récupération fichiers skill** | Après suppression accidentelle |

### Triple mise à jour atomique

Toute modification d'itinéraire déclenche **automatiquement** la mise à jour des 3 fichiers **avant commit** :
1. `index.md` (texte du roadbook)
2. `carte.html` (carte folium)
3. `roadbook-*.pdf` (PDF)

### Processus multi-utilisateurs

Chaque roadbook est rattaché à un **propriétaire identifié** (Christophe, Pascal, etc.) avec tarification différente selon le profil.

## 🔗 Interopérabilité

| Bureau | Quand appeler | Comment |
|--------|--------------|---------|
| 🤖 **LEO** (bureau-leo) | Analyse personnelle de voyage | Appel skill `bureau-leo` |
| 💰 **Sophie** | Impact financier du voyage | Appel skill `bureau-sophie` (rare) |

## 📊 État

Roadbooks actifs : Scandinavie 2026, Italie, Canet. Bot Telegram déployé et actif.
