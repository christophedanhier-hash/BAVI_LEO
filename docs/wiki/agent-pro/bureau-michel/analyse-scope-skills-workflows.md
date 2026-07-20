---
date: 2026-07-08
bureau: bureau-michel
version: v1
modele: deepseek-v4-flash
tags: [analyse, scope, skills, workflows, bavi-leo, infrastructure]
statut: finalise
type: analyse
---

# 🔧 Analyse du Bureau Michel — Infra_Hermes

## 📋 Scope

Le **Bureau Michel** est l'orchestrateur technique de l'infrastructure et du code. C'est le bureau qui **fait** — installations, scripts, Docker, réseau, debugging, gestion système. Catégorie **PRIVÉ** 🏠.

**Périmètre fonctionnel (large) :**
- Administration système (SysAdmin) : OS, services, Docker
- CI/CD DevOps : GitHub Actions, déploiements
- Réseau : DNS, proxy, ports, firewall, Tailscale
- Scripting Python/bash : automation, crons
- Documentation technique : audits, rapports
- Dashboard KPI, Ollama, Google APIs

**🔑 Accès root complet** — Michel a `sudo` sans restriction sur la machine LEO.

## 🧠 Skills utilisés

| Skill | Rôle | Usage |
|-------|------|-------|
| **bureau-michel** ⭐ | Skill principal | Orchestrateur — 5 experts, dispatch conditionnel, sous-agent DeepSeek Pro |
| **dashboard-kpi** | Dashboard KPI | Collecte et affichage des métriques |
| **bureau-versioning** | Versioning | Gestion des versions des analyses techniques |
| **system-management** | Gestion machines | Monitoring des 3 machines (LEO, Yoga, Penguin) |
| **machine-metrics** | Métriques machines | Collecte CPU/RAM/disque via SSH |
| **cron-lifecycle** | Gestion crons | Planification, audit, nettoyage |
| **doc-watch** | Doc watch | Capture état écosystème LEO toutes les 6h |
| **n8n-automation** | ❌ Retiré 13/07/2026 | Anciennement gestion API REST workflows |
| **self-hosted-services** | Services | Installation et gestion services auto-hébergés |
| **deepseek-pro** | Routage Pro | Délégation automatique tâches complexes |
| **hermes-multi-profile** | Multi-profile | Maintenance des profils Hermes |
| **bavi-leo-governance** | Gouvernance | Framework d'audit et structuration |

**Expertise :** DeepSeek Pro (deepseek-v4-pro) via sous-agent dédié `delegate_task`.

## 👥 Sous-experts (dispatch)

| Expert | Rôle | Modèle |
|--------|------|--------|
| **SysAdmin** | Installation, configuration, Docker | 🧠 DeepSeek Pro |
| **DevOps** | CI/CD, GitHub Actions, déploiements | 🧠 DeepSeek Pro |
| **Networker** | Debug réseau, DNS, proxy, ports, Tailscale | 🧠 DeepSeek Pro |
| **Scripteur** | Scripts Python/bash, automation, crons | 🧠 DeepSeek Pro |
| **DataDoc** | Documentation technique, audit, rapports | 🧠 DeepSeek Pro |

## 🔄 Workflows définis

### Workflow complet — 7 phases BAVI + sous-agent Pro

```
① CADRAGE → ② DISPATCH → ③ PRODUCTION → ④ CROISEMENT → ⑤ SYNTHÈSE → ⑥ LIVRABLE → ⑦ ARCHIVAGE
```

| Phase | Action | Sous-agent |
|:-----:|--------|:----------:|
| ① **Cadrage** | Comprendre la demande technique, contraintes | Direct |
| ② **Dispatch** | Activer les experts nécessaires | Direct |
| ③ **Production** | Chaque expert analyse via delegate_task + vérification artefacts existants | ✅ delegate_task (Pro) |
| ④ **Croisement** | Confronter les analyses | ✅ delegate_task (Pro) |
| ⑤ **Synthèse** | Synthèse technique unifiée | Direct |
| ⑥ **Livrable** | .md + plan de monitoring (watchdog + cron + dashboard) | Direct |
| ⑦ **Archivage** | Wiki BAVI + AGENT-PRO + déploiement monitoring | Direct |

### Adaptation au type de livrable

| Format | Phases | Usage |
|:-------|:------:|:------|
| Analyse | ①→③→⑤→⑥→⑦ | Simple, pas de dispatch |
| Rapport | ①→②→③→④→⑤→⑥→⑦ | 7 phases complètes (défaut) |
| Note/Mémo | ①→③→⑥ | Rapide |
| Dossier | ①→②→③→④→⑤→⑥→⑦ | Archivage renforcé |
| Dashboard | Collecte→Traitement→Publication | Cron-driven |

### Règle de livraison

Toute analyse produite par Michel est livrée **dans le wiki BAVI** (pas dans `~/Projets_Dev/`), avec frontmatter, index regénéré via `agent-pro-index.py`, et push GitHub immédiat.

## 🔗 Interopérabilité

| Bureau | Quand appeler | Comment |
|--------|--------------|---------|
| 🏛️ **Robert** | Impact stratégique avant installation | Appel skill `bureau-robert` (phase ①/②) |
| 💰 **Sophie** | Estimation coûts infrastructure (TCO) | Appel skill `bureau-sophie` (phase ①/②) |
| 📝 **Gérard** | Documentation technique liée au T600 | Appel skill `bureau-gerard` (phase ⑥) |

> 🤖 Dernier audit : 20/07/2026 à 07:26 (UTC+2)

