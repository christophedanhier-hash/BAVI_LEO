---
date: 2026-07-08
bureau: bureau-emile
version: v1
modele: deepseek-v4-flash
tags: [analyse, scope, skills, workflows, bavi-leo]
statut: finalise
type: analyse
---

# 🎓 Analyse du Bureau Émile — Assistant Pédagogique

## 📋 Scope

Le **Bureau Émile** est dédié à l'accompagnement académique d'Émile pour son mémoire de fin d'études en sciences de l'éducation. Il fait partie de la catégorie **PRIVÉ** 🏠 de l'écosystème BAVI LEO.

**Périmètre fonctionnel :**
- Relecture et correction de chapitres de mémoire
- Accompagnement pédagogique personnalisé
- Gestion des sources et brouillons via Drive
- Publication des versions finales sur le wiki Emile

## 🧠 Skills utilisés

| Skill | Rôle | Usage |
|-------|------|-------|
| **bureau-emile** ⭐ | Skill principal | Contient la personnalité, les règles, l'architecture du bureau |
| **shared-bot-deployment** | Déploiement bot Telegram | Infrastructure du bot @Bureau_ia_emilie_bot |
| **source-of-truth** (Drive) | Sync Drive → wiki | Conversion docx → md pour alimenter le wiki |
| **mkdocs-wiki** | Wiki Emile | Structure MkDocs Material pour emile-wiki |

**Expertise :** DeepSeek V4 Flash (primaire) + Gemini 3.5 Flash (fallback >128K tokens).

## 🔄 Workflows définis

### Workflow standard — 7 phases BAVI (adapté)

```
① CADRAGE → ③ PRODUCTION → ⑥ LIVRABLE → ⑦ ARCHIVAGE
```

| Phase | Description | Statut |
|:-----:|-------------|:------:|
| ① **Cadrage** | Comprendre le besoin : chapitre à relire, sources à intégrer | ✅ |
| ③ **Production** | Analyse du chapitre, corrections, suggestions | ✅ |
| ⑥ **Livrable** | Retour structuré (commentaires, corrections) | ✅ |
| ⑦ **Archivage** | Mise à jour du wiki emile-wiki + Drive | 🟡 |

### Workflow Drive → Wiki (automatisé)

```
📄 Émile écrit → 📁 Drive bavi/bureau-emilie → 🔄 Cron sync → 📝 Conversion .docx → .md → 🚀 Push emile-wiki
```

- **Cron :** `emile-drive-sync` (toutes les heures) — à activer
- **Conversion :** .docx → .md automatique
- **Intermittent :** le bot charge le .md depuis le wiki pour avoir le contexte à jour

### Règle de bascule modèle

- **< 128K tokens →** DeepSeek V4 Flash (primaire)
- **> 128K tokens →** Gemini 3.5 Flash (fallback, contexte long gratuit)

## 📊 État actuel

| Élément | Statut |
|---------|:------:|
| Wiki emile-wiki | ✅ Déployé |
| Bot Telegram @Bureau_ia_emilie_bot | ✅ En ligne |
| Profil Hermes emile | ✅ Configuré |
| Cron Drive sync | 🟡 Script prêt, pas activé |
| Analyses dans AGENT-PRO | ✅ Dossier créé, 0 analyse |

## 🔗 Interopérabilité

Le Bureau Émile fonctionne de manière **autonome** — il n'appelle pas d'autres bureaux et n'est pas appelé par eux. Pas d'interopérabilité documentée.
