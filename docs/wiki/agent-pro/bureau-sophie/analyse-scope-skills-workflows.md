---
date: 2026-07-08
bureau: bureau-sophie
version: v1
modele: deepseek-v4-flash
tags: [analyse, scope, skills, workflows, bavi-leo, pro]
statut: finalise
type: analyse
---

# 💰 Analyse du Bureau Sophie — Pilotage Économique & Financier IT

## 📋 Scope

Le **Bureau Sophie** est l'orchestratrice du **pôle économique et financier IT**, dédié aux analyses PRO (Solidaris). Catégorie **PRO** 🏢.

**Périmètre fonctionnel :**
- Analyses de rentabilité et business cases
- Modélisations TCO/ROI
- Benchmark et études de marché IT
- Évaluations de risques et conformité
- 3 scenarii systématiques (conservateur, réaliste, ambitieux)

## 🧠 Skills utilisés

| Skill | Rôle | Usage |
|-------|------|-------|
| **bureau-sophie** ⭐ | Skill principal | Orchestratrice — 3 experts, dispatch conditionnel |

**Expertise :** DeepSeek V4 Flash.

## 👥 Sous-experts (dispatch conditionnel)

| Expert | Rôle | Activer quand… |
|--------|------|----------------|
| **Analyste Marché & Business Case** | Benchmark, étude de marché | Demande de comparaison, positionnement |
| **Modélisateur Financier IT** | TCO/ROI, Capex/Opex, VAN, TRI, scenarii | **Toujours activé** |
| **Risques & Conformité IT** | Cartographie des risques | Projet, investissement, changement important |

## 🔄 Workflows définis

### Workflow complet — 7 phases BAVI (parallélisable)

```
① CADRAGE → ② DISPATCH → ③ PRODUCTION → ④ CROISEMENT → ⑤ SYNTHÈSE → ⑥ LIVRABLE → ⑦ ARCHIVAGE
```

| Phase | Action | Parallélisable |
|:-----:|--------|:--------------:|
| ① **Cadrage** | Besoin, périmètre budgétaire, hypothèses | ❌ |
| ② **Dispatch** | Activer les experts nécessaires | ❌ |
| ③ **Production** | **Marché + Risques EN PARALLÈLE** si les deux activés | ✅ |
| ④ **Croisement** | Confronter Marché + Risques + Modélisation | ❌ |
| ⑤ **Synthèse** | Tableau de bord des indicateurs clés | ❌ |
| ⑥ **Livrable** | .md (interne) / Google Sheets (modèle financier) | ❌ |
| ⑦ **Archivage** | Wiki BAVI LEO | ❌ |

### Règles

- Standard Business Case Solidaris : maille 6 régions
- **Toujours 3 scenarii** (conservateur, réaliste, ambitieux)
- Chiffres sourcés
- Parallélisation Marché + Risques quand applicable

## 🔗 Interopérabilité

| Bureau | Quand appeler | Comment |
|--------|--------------|---------|
| 🏛️ **Robert** | Business case avec impact stratégique | Appel skill `bureau-robert` |

## 📊 État

Pas encore d'analyses déposées dans `docs/wiki/agent-pro/bureau-sophie/`.

> 🤖 Dernier audit : 24/07/2026 à 07:57 (UTC+2)

