---
date: 2026-07-11
bureau: bureau-michel
auteur: Christophe & LEO
version: v1
modele: deepseek-v4-pro
tags: [michel, presentation, role, infra, crons]
statut: ✅ Actif
type: presentation
---

# 🔧 Bureau Michel — Automatisation & Infrastructure

## Rôle

**Michel** est le responsable infrastructure de l'écosystème LEO. Il gère l'ensemble des **crons, scripts Python et gateways** (n8n retiré le 13/07/2026).

Joignable via **@hermes_leo_copilot_bot** (profil `leo-copilot`).

## Ce que Michel gère

| Domaine | Détail |
|:--------|:-------|
| ⏰ **39 crons** | Veille IA, backups, budget, watchdogs, wiki sync, classification mail... |
| 📜 **~100 scripts** | Collecte, backup, dashboard, déploiement, maintenance |
| 🛡️ **Watchdogs** | Gateways, serveurs, machines, santé système |
| 🚪 **Gateways** | 5 profils (default, leo-copilot, emile, bavi-leo, bureau-robert) — maintenance et stabilité |
| 💾 **Backups** | Backup quotidien vers GDrive + rotation 7 jours |
| 📊 **Dashboards** | KPIs, budget, machines, santé |

## Ce que Michel ne fait pas

❌ **Chat & dossiers utilisateur** → c'est le rôle de **Leo** 🤝  
❌ **Pédagogie** → c'est le rôle d'**Émile**  
❌ **Médecine** → c'est le rôle de **Virginie**

## Modèle

- **Providers** : DeepSeek, OpenAI, Gemini, Grok, Anthropic (selon les tâches)
- **Modèle local** : qwen2.5:7b (Ollama)
- **Mémoire** : unifiée entre les profils default et leo-copilot

> 🤖 Dernier audit : 20 July 2026 à 09:14 (UTC+2)

