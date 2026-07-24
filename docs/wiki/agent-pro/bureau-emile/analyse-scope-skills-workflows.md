---
date: 2026-07-08
bureau: bureau-emile
version: v1
modele: deepseek-v4-flash
tags: [analyse, scope, skills, workflows, bavi-leo]
statut: finalise
type: analyse
---

Ajouter un titre approprié basé sur la réalité.

## 📋 Scope

Ajouter les informations manquantes sur le périmètre fonctionnel.

**Périmètre fonctionnel :**
- Relecture et correction de chapitres de mémoire
- Accompagnement pédagogique personnalisé
- Gestion des sources et brouillons via Drive
- Publication des versions finales sur le wiki Emile

## 🧠 Skills utilisés

Mettre à jour les skills avec les informations de la réalité.

**Expertise :** DeepSeek Flash (primaire), Gemini 3.5 Flash (fallback), Qwen2.5:7b (Ollama local) selon disponibilité.

## 🔄 Workflows définis

Ajouter les informations manquantes sur les workflows.

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

Ajouter les informations manquantes sur les technologies utilisées. le bot charge le .md depuis le wiki pour avoir le contexte à jour

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

> 🤖 Dernier audit : 24/07/2026 à 12:02 (UTC+2)
