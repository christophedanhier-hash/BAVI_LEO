---
date: 2026-07-08
bureau: bureau-virginie
version: v1
modele: qwen2.5:7b
providers: deepseek, openai, gemini, grok, anthropic
tags: [analyse, scope, skills, workflows, bavi-leo]
statut: finalise
type: analyse
---

# 🩺 Analyse du Bureau Virginie — Orchestration Médicale

## 📋 Scope

Le **Bureau Virginie** orchestre un **panel de médecins** pour le meilleur diagnostic possible. Catégorie **PRIVÉ** 🏠.

**Périmètre fonctionnel :**
- Recueil des symptômes et historique médical
- Activation conditionnelle des spécialistes pertinents
- Parallélisation des analyses médicales
- Croisement des diagnostics (convergences/divergences)
- Synthèse médicale unifiée par Virginie (médecin coordinateur)
- Rapport médical structuré complet
- Archivage dans le wiki BAVI

## 🧠 Skills utilisés

Update the skills list to match reality.

## 👥 Sous-experts — Panel médical (dispatch conditionnel)

Update the specializations and activation conditions to match reality.gerie, IRM, scanner | Imagerie disponible |

## 🔄 Workflows définis

### Workflow complet — 7 phases BAVI

```
① CADRAGE → ② DISPATCH → ③ PRODUCTION → ④ CROISEMENT → ⑤ SYNTHÈSE → ⑥ LIVRABLE → ⑦ ARCHIVAGE
```

| Phase | Description | Parallélisable |
|:-----:|-------------|:--------------:|
| ① **Cadrage** | Recueillir symptômes, historique, antécédents, traitements | ❌ |
| ② **Dispatch** | Activer UNIQUEMENT les spécialistes pertinents | ❌ |
| ③ **Production** | Chaque spécialiste analyse selon son domaine | ✅ |
| ④ **Croisement** | Confronter diagnostics, convergences/divergences | ✅ |
| ⑤ **Synthèse** | Virginie unifie → diagnostic + recommandations | ❌ |
| ⑥ **Livrable** | Rapport médical structuré complet | ❌ |
| ⑦ **Archivage** | Documenter dans le wiki BAVI | ❌ |

### Règle de dispatch

> N'activer que les spécialistes pertinents pour les symptômes décrits.
> Ne JAMAIS tous les activer par défaut.
> Le généraliste est TOUJOURS activé.

### Format livrable

Rapport détaillé avec sections obligatoires : analyses complètes par spécialiste (10-30 lignes), tableau de convergence/divergence, tableau médicamenteux complet par moment de la journée, alertes priorisées 🔴🟡🟢, contacts d'urgence, historique des versions.

## 🔗 Interopérabilité

| Bureau | Quand appeler | Comment |
|--------|--------------|---------|
| 🤖 **LEO** | Analyse personnelle de santé | Appel skill `bureau-leo` |
| 💰 **Sophie** | Si parcours de soins avec impact financier | Appel skill `bureau-sophie` |

> 🤖 Dernier audit : 24/07/2026 à 12:05 (UTC+2)
