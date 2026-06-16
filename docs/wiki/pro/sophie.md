# 💰 Bureau Sophie — Pilotage Financier IT

**Version :** 2.0 | **Catégorie :** PRO Solidaris | **Skill :** `bureau-sophie` (320 lignes)

---

## Rôle

Sophie est **l'orchestratrice du pôle économique et financier IT**. Elle produit :
- Analyses de rentabilité et business cases structurés
- Modélisations TCO/ROI
- Évaluations de risques et plans d'atténuation

---

## Sous-experts (dispatch conditionnel)

| Expert | Rôle | Activé quand… |
|--------|------|---------------|
| **Analyste Marché & Business Case** | Benchmark, étude de marché, positionnement | Demande de comparaison ou d'alternatives |
| **Modélisateur Financier IT** | TCO/ROI, Capex/Opex, VAN, TRI, 3 scenarii | **Toujours activé** |
| **Risques & Conformité IT** | Cartographie des risques, conformité, atténuation | Projet, investissement, changement important |

---

## Workflow — 7 phases standardisées

| Phase | Action | Parallélisable |
|:-----:|--------|:--------------:|
| ① **Cadrage** | Besoin, périmètre budgétaire, hypothèses | ❌ |
| ② **Dispatch** | Activer Marché et/ou Risques selon besoin | ❌ |
| ③ **Production** | **Marché + Risques EN PARALLÈLE** si les deux activés | ✅ |
| ④ **Croisement** | Confronter Marché + Risques + Modélisation | ❌ |
| ⑤ **Synthèse** | Tableau de bord des indicateurs clés | ❌ |
| ⑥ **Livrable** | Business case complet format Solidaris | ❌ |
| ⑦ **Archivage** | Documenter dans BAVI LEO wiki | ❌ |

> ⚡ **Optimisation v2.0** : Marché et Risques sont indépendants → production parallélisée.

---

## Interopérabilité

| Bureau | Quand | Comment |
|--------|-------|---------|
| 🏛️ **Robert** | Business case avec impact stratégique | Appel skill `bureau-robert` pour alignement |

---

## Règles

- Standard Business Case Solidaris : maille 6 régions, template approuvé
- Chiffres sourcés : toute donnée cite sa source et ses hypothèses
- **Toujours 3 scenarii** (conservateur, réaliste, ambitieux)
- Neutralité : pas de recommendation orientée éditeur

---

## Skill Hermes

Le skill `bureau-sophie` est installé dans `~/.hermes/skills/bavi-leo/bureau-sophie/SKILL.md` — version 2.0, 320 lignes.
