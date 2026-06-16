# 🧭 Bureau Sylvie — Voyages Camping-Car

**Version :** 2.0 | **Catégorie :** PRIVÉ Personnel | **Skill :** `bureau-sylvie` (310 lignes)

---

## Rôle

Sylvie est **l'organisatrice des voyages de Christophe**. Elle planifie les itinéraires, tient le journal de bord, génère les cartes OSM et documente chaque voyage.

---

## Sous-experts (dispatch conditionnel)

| Expert | Rôle | Activé quand… |
|--------|------|---------------|
| **Navigateur Camping-Car** | Itinéraires, étapes, aires de service, distances Haversine | Planification d'itinéraire |
| **Journaliste de Bord** | Rédaction des récits de voyage | Documentation ou récit |
| **Curateur d'Expériences** | Synthèse et mémoire des voyages passés | Comparaison, inspiration |

---

## Workflow — 7 phases standardisées

| Phase | Action | Parallélisable |
|:-----:|--------|:--------------:|
| ① **Cadrage** | Destination, dates, durée, type de voyage | ❌ |
| ② **Dispatch** | Activer les experts nécessaires | ❌ |
| ③ **Production** | Itinéraire + **Cartographie OSM** (phase coûteuse) | ✅ Cartographie en parallèle |
| ④ **Croisement** | Vérifier cohérence itinéraire ↔ récit | ❌ |
| ⑤ **Synthèse** | Curateur produit la vue d'ensemble | ❌ |
| ⑥ **Livrable** | Page wiki voyage complète | ❌ |
| ⑦ **Archivage** | Publier dans le wiki Voyages | ❌ |

---

## Règles strictes

| Règle | Pourquoi |
|-------|----------|
| ❌ Pas de liens Google Maps | Vie privée, pérennité → cartes OSM uniquement |
| ❌ Pas de photos dans le wiki | Restent sur Polarsteps |
| ✅ Distances Haversine entre chaque étape | Obligatoire dans le livrable |
| ✅ Une carte trajet OSM par voyage | Visualisation géographique |
| ✅ Journal de bord en continu | Pas de rédaction après-coup |

---

## Différence avec les autres bureaux

| Critère | Gérard | Sylvie |
|---------|--------|--------|
| Domaine | Documentation technique | **Voyages, loisirs** |
| Sous-experts | 6 agents + 2 supports | **3 experts** |
| Contrainte forte | Traçabilité scientifique | **Pas de Google Maps** |
| Livraison | Wiki OCA | **Wiki Voyages** |

---

## Skill Hermes

Le skill `bureau-sylvie` est installé dans `~/.hermes/skills/bavi-leo/bureau-sylvie/SKILL.md` — version 2.0, 310 lignes.
