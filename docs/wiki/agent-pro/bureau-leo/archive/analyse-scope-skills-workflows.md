---
date: 2026-07-08
bureau: bureau-leo
version: v1
modele: deepseek-v4-flash
tags: [analyse, scope, skills, workflows, bavi-leo]
statut: finalise
type: analyse
---

# 🤖 Analyse du Bureau LEO — Dossiers & Analyses Personnelles

## 📋 Scope

Le **Bureau LEO** est le bureau **fourre-tout personnel** de Christophe. Il reçoit toutes les analyses, études de marché et documentations qui ne rentrent pas dans les autres bureaux PRIVÉ :

| Bureau | Domaine |
|--------|---------|
| 🔧 **Michel** | Infrastructure Hermes, dashboards |
| 🧭 **Sylvia** | Voyages, roadbooks |
| 🎓 **Emile** | Pédagogie, études |
| 🩺 **Virginie** | Médical |
| **LEO** 🟢 | **Tout le reste** |

**Périmètre fonctionnel :**
- Études de marché et comparatifs
- Analyses personnelles (achats, projets perso)
- Dossiers transversaux sans bureau dédié
- Documents qui ne sont ni PRO (Robert), ni infra (Michel), ni voyages (Sylvia)

## 🧠 Skills utilisés

| Skill | Rôle | Usage |
|-------|------|-------|
| **bureau-leo** ⭐ | Skill principal | Définit le rôle, la structure des documents, les règles |

**Expertise :** DeepSeek V4 Flash (modèle standard dialogue).

## 🔄 Workflows définis

### Workflow simplifié — 5 phases

```
① CADRAGE → ③ PRODUCTION → ⑤ SYNTHÈSE → ⑥ LIVRABLE → ⑦ ARCHIVAGE
```

Pas de dispatch (pas de sous-experts), pas de croisement. Production directe.

### Règles de stockage

- **Frontmatter YAML obligatoire** sur chaque document
- Format : `type: analyse|note|rapport|etude|reference`
- Source dans `AGENT-PRO/bureau-leo/`
- Index regénéré via `agent-pro-index.py`

## 📊 Travaux existants

| Document | Sujet | Statut |
|:---------|:------|:-------|
| `analyse-bot-leo-hub.md` | Analyse business LEO Hub | ✅ Finalisé |
| `etude-marche-quad-biplace.md` | Achat quad 2 places | 🔄 En cours |

## 🔗 Interopérabilité

Le Bureau LEO est **autonome et passif** — il stocke des analyses produites ailleurs. Il n'orchestre pas d'autres bureaux.

> 🤖 Dernier audit : 24/07/2026 à 07:57 (UTC+2)
