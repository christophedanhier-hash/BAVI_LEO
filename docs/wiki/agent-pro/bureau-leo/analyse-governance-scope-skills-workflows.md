---
date: 2026-07-08
bureau: bavi-leo-governance
version: v1
modele: deepseek-v4-flash
tags: [analyse, scope, skills, workflows, bavi-leo]
statut: finalise
type: analyse
---

# 🏗️ Analyse de la Gouvernance BAVI LEO — Framework d'Audit

## 📋 Scope

**BAVI LEO Governance** est le **framework central** qui définit l'architecture, les standards et les procédures de tout l'écosystème BAVI LEO. Ce n'est pas un bureau producteur d'analyses, mais le **squelette méthodologique** de tous les bureaux.

**Périmètre fonctionnel :**
- Définition de la structure standard d'un bureau BAVI LEO
- Grille d'audit par bureau (Orchestrateur, Sous-experts, Workflow, Interop)
- Workflow standardisé 7 phases (obligatoire pour tous)
- Variantes par type de livrable (analyse, rapport, note, dossier, mémoire, dashboard)
- Patterns d'interopérabilité entre bureaux
- Standards de documentation wiki
- Distribution des skills par profil Hermes
- Pricing & transparence (obligatoire sur tout livrable)
- Audit complet de l'écosystème (checklist 8 sections)
- Reconstruction de contenu perdu (git history)
- Nettoyage d'écosystème (procédure de suppression)

## 🧠 Skills utilisés

| Skill | Rôle | Usage |
|-------|------|-------|
| **bavi-leo-governance** ⭐ | Skill principal | Framework de gouvernance complet |

## 🔄 Workflows définis

### Workflow 7 phases standard (standard pour tous les bureaux)

```
① CADRAGE → ② DISPATCH → ③ PRODUCTION → ④ CROISEMENT → ⑤ SYNTHÈSE → ⑥ LIVRABLE → ⑦ ARCHIVAGE
```

### Variantes autorisées

| Situation | Ajustement |
|-----------|------------|
| Expert unique transverse (AO) | ① → ③ → ⑥ |
| Bureau cron-driven (Michel) | Collecte → Traitement → Dashboard |
| Phase absente justifiée | Mentionner explicitement pourquoi |

### Matrice des types de livrable

| Format | Phases | Usage |
|:-------|:------:|:------|
| **📄 Analyse** | ①→③→⑤→⑥→⑦ | Pas de dispatch, pas de croisement |
| **📋 Rapport** | ①→②→③→④→⑤→⑥→⑦ | Complet 7 phases |
| **📝 Note/Mémo** | ①→③→⑥ | Court et rapide |
| **📁 Dossier** | ①→②→③→④→⑤→⑥→⑦ | Archivage renforcé |
| **🧠 Mémoire/Étude** | ①→②→③→④↺→⑤→⑥→⑦ | Plusieurs rounds de croisement |
| **📊 Dashboard/KPI** | Collecte→Traitement→Publication | Cron-driven |
| **🗺️ Roadbook** | ①→③→④→⑤→⑥→⑦ | Croisement carto+logistique |

## 📊 Architecture PRO / PRIVÉ

| Catégorie | Bureaux |
|-----------|---------|
| **PRO** 🏢 | Robert (Conseil IT), Sophie (Finance), Assurance Obligatoire (Métier) |
| **PRIVÉ** 🏠 | Gérard (Doc T600), Sylvia (Voyages), LEO Admin (Infra), Virginie (Médical), Emile (Pédagogie), LEO (Personnel) |

### Distribution par profil Hermes

| Profil | Skills BAVI | Rôle |
|:-------|:------------|:------|
| **default** 🏠 | 10 : tous les bureaux | Gouvernance centrale |
| **leo-copilot** 🔧 | 4 : Michel, Emile, gouvernance, versioning | Infrastructure |
| **bavi-leo** 🧭 | 1 : Sylvia | Voyages uniquement |

## 🔗 Interopérabilité

La gouvernance est le **cadre commun** utilisé par TOUS les bureaux. Elle définit comment les bureaux communiquent entre eux (tableaux interop), comment les workflows s'adaptent, et comment la documentation est structurée.

## 📊 État

Version 1.10. Skill le plus volumineux de l'écosystème (80+ KB) avec 13 fichiers de référence et 1 template.
