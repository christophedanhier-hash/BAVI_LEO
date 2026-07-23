---
date: 2026-07-08
bureau: bureau-robert
version: v1
modele: qwen2.5:7b (local) avec deepseek comme provider
tags: [analyse, scope, skills, workflows, bavi-leo, pro]
statut: finalise
type: analyse
---

# 🏛️ Analyse du Bureau Robert — Conseil Stratégique IT

## 📋 Scope

Le **Bureau Robert** est l'orchestrateur du **cabinet de conseil virtuel IT**, dédié exclusivement aux analyses **PRO** (Solidaris, Assurance Obligatoire). Catégorie **PRO** 🏢.

**Périmètre fonctionnel :**
- Analyses stratégiques IT
- Notes, briefings, synthèses, arbitrages
- Coordination de 7 experts spécialisés (dispatch conditionnel)
- Architecture, Sécurité, Data, Gouvernance, Vision Stratégique, Projet & Programme, AO

**⚠️ Règle :** analyses PRO uniquement. Toute analyse personnelle (Michel, LEO, Sylvia, Emile, Virginie) va dans son bureau PRIVÉ.

## 🧠 Skills utilisés

| Skill | Rôle | Usage |
|-------|------|-------|
| **bureau-robert** ⭐ | Skill principal | Orchestrateur — 7 experts + interop |
| **assurance-obligatoire** | Expert AO transverse | Appelé en phase ③/④ pour impact INAMI/BCSS |
| **bureau-sophie** | Analyse financière | Appelé pour volet TCO/business case |

**Expertise :** DeepSeek V4 Flash (modèle standard).

## 👥 Sous-experts (dispatch conditionnel)

| # | Expert | Activer quand… |
|:-:|--------|----------------|
| 1 | **Architecture** | Sujet SI, urbanisation, patterns d'intégration |
| 2 | **Sécurité** | Cybersécurité, NIS2, RGPD, ISO 27001 |
| 3 | **Data** | Gouvernance des données, qualité |
| 4 | **Gouvernance** | COBIT, ITIL, CMMI |
| 5 | **Vision Stratégique** | Feuilles de route, transformation digitale |
| 6 | **Projet & Programme** | PMI/PMBOK, PRINCE2, SAFe |
| 7 | **Assurance Obligatoire** → appel skill AO | Impact métier AO |

## 🔄 Workflows définis

### Workflow complet — 7 phases BAVI

```
① CADRAGE → ② DISPATCH → ③ PRODUCTION → ④ CROISEMENT → ⑤ SYNTHÈSE → ⑥ LIVRABLE → ⑦ ARCHIVAGE
```

| Phase | Action | Parallélisable |
|:-----:|--------|:--------------:|
| ① **Cadrage** | Comprendre la demande, le contexte, les livrables | ❌ |
| ② **Dispatch** | Identifier les experts nécessaires (parmi 1-7) | ❌ |
| ③ **Production** | Chaque expert produit son analyse | ✅ |
| ④ **Croisement** | Confronter les analyses | ✅ |
| ⑤ **Synthèse** | Analyse transversale unifiée | ❌ |
| ⑥ **Livrable** | Format .md (interne) / Google Docs (partage) | ❌ |
| ⑦ **Archivage** | Wiki BAVI LEO + AGENT-PRO | ❌ |

### Règles absolues

- **Pas de décision** — Robert aide à décider, ne décide pas
- **Pas d'implémentation** — pas de code, config, déploiement
- **Dispatch conditionnel** — ne pas tous les activer par défaut

## 🔗 Interopérabilité

| Bureau | Quand appeler | Comment |
|--------|--------------|---------|
| 🛡️ **Assurance Obligatoire** | Analyse IT avec impact métier AO | Appel skill `assurance-obligatoire` (phase ③/④) |
| 💰 **Sophie** | Analyse avec volet financier (TCO) | Appel skill `bureau-sophie` (phase ③/④) |

## 📊 État

Le Bureau Robert n'a pas encore de documents déposés dans AGENT-PRO (pas d'analyse PRO produite à ce jour).

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)

