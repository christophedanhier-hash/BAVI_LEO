---
date: 2026-06-24
bureau: bureau-michel
version: v2
modele: deepseek-v4-pro
tags: [amelioration, skill, infrastructure, bavi-leo]
statut: proposition
---

# Amélioration Bureau Michel — v1.1 → v2.0

## 📊 Contexte

**Bureau Michel v1.1** couvre ~38% des responsabilités réelles de Leo Copilot (5/13 domaines). L'essentiel est concentré sur les crons Python autonomes (ex-n8n). Les dashboards, crons, Hermes config, Google APIs, Git, mémoire, skills, machines et budget ne sont pas couverts par des patterns de dispatch.

**Objectif** : étendre le skill pour couvrir 100% des domaines infra avec des patterns de dispatch conditionnel, enrichir les pitfalls avec l'expérience récente (migration 0.17.0), et intégrer le partage cross-profil avec Leo Hermes.

---

## 🎯 Modifications proposées

### 1. Nouveaux sous-experts (5 → 8)

| Expert | Rôle | Activer quand… |
|--------|------|----------------|
| **DashBuilder** 🆕 | Dashboards HTML, Chart.js, GitHub Pages | Déploiement dashboard, debug HTML, màj template |
| **CronMaster** 🆕 | Crons Hermes, staggering, debugging | Création/audit cron, erreur récurrente, conflit horaire |
| **GitGuardian** 🆕 | Git repos, sync, clean trees, cross-repo | Dirty files, sync Drive↔GitHub, audit repos |

### 2. Dispatch patterns étendus (3 → 10)

| Scénario | Experts | Parallèle |
|----------|---------|:---------:|
| **Audit end-to-end** | DataDoc + CronMaster + DashBuilder + GitGuardian + Networker | ✅ (5 parallèles) |
| **Post-migration (0.17.0)** | SysAdmin + CronMaster + Scripteur + DataDoc | ✅ |
| **Déploiement dashboard** | DashBuilder + DevOps + DataDoc | ✅ |
| **Debug cron** | CronMaster + Scripteur + Networker | ❌ (séquentiel) |
| **Sync cross-profil** | Scripteur + GitGuardian + CronMaster | ❌ |
| **Classification email** | GoogleIntegrator 🆕 + Scripteur | ❌ |
| **Nettoyage Drive/Git** | GitGuardian + GoogleIntegrator | ✅ |

### 3. Pitfalls enrichis (+8)

Ajout des pièges découverts depuis le 19/06 :
- Migration Hermes dans le conteneur → rebuild Docker
- Symlinks dans scripts/ → refusés en 0.17.0
- Mémoire default → `.hermes/memories/` (plus `/memories/`)
- Config v30 → `hermes config migrate` après upgrade
- sshpass → `/opt/data/bin/sshpass` (pas `/tmp/`)
- s6-svstat DOWN → faux négatif, vérifier les processus
- `hermes` pas dans PATH → `/opt/hermes/.venv/bin/hermes`
- Labels Gmail différents par compte → détection auto

### 4. Section cross-profil 🆕

Documenter la frontière Leo Copilot ↔ Leo Hermes :
- Leo Copilot : dashboards, Drive, crons Python, machines, skills, Git, mémoire
- Leo Hermes : crons (default), wikis, Veille IA, backups, emails
- Règle : ne pas modifier les crons du profil default depuis leo-copilot

---

## 📈 Impact

| Métrique | Avant | Après |
|----------|:-----:|:-----:|
| Domaines couverts | 5/13 (38%) | 13/13 (100%) |
| Sous-experts | 5 | 8 |
| Dispatch patterns | 3 | 10 |
| Pitfalls | 13 | 21 |
| Cross-profil | Non documenté | Section dédiée |
| Templates delegate_task | 5 | 8 |

---

## 💰 Coût

Cette analyse a été produite directement (pas de sous-agents) — le skill amélioré sera lui-même le livrable.

---

## Prochaines étapes

- [ ] Appliquer le patch au skill `bureau-michel` (bavi-leo)
- [ ] Archiver cette analyse dans `BAVI/AGENT-PRO/bureau-michel/`
- [ ] Synchroniser avec Leo Hermes (mémoire)

---

*Analyse produite par le **Bureau Michel** — Modèle : **DeepSeek Pro** — Date : **24/06/2026***

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)

