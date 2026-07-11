# ⏰ Cronjobs Hermes — Inventaire complet

<!-- AUTO:START header -->
> **Généré automatiquement le 11/07/2026 à 12:00**
> Source : `profiles/leo-copilot/cron/jobs.json` (29 jobs)
<!-- AUTO:END header -->

## Résumé

| Catégorie | Total |
|-----------|:-----:|
| **Crons Hermes** (tous profils, consolidé) | **29** |
| **Crons hôte** (crontab tofdan@172.17.0.1) | **5** |
| **Total général** | **34** |

## Liste exhaustive des crons Hermes

<!-- AUTO:START hermes-crons -->

| # | Nom | Horaire | Mode | Statut |
|:-:|-----|:-------:|:----:|:------:|
| 1 | 💰 Budget Alert | `0 8,20 * * *` | script | ✅ |
| 2 | 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | script | ✅ |
| 3 | 📊 Synthèse Hebdomadaire LEO | `0 20 * * 0` | script | ⚠️ |
| 4 | 📊 Unified Collector v2 | `*/15 * * * *` | LLM | ✅ |
| 5 | 📋 doc-crons-sync | `0 */6 * * *` | script | ✅ |
| 6 | 📓 vault-bavi-daily-journal | `10 23 * * *` | LLM | ✅ |
| 7 | 📓 vault-daily-journal (vault-leo) | `0 23 * * *` | LLM | ✅ |
| 8 | 📓 vault-default-daily-journal | `5 23 * * *` | LLM | ✅ |
| 9 | 📓 vault-emile-daily-journal | `15 23 * * *` | LLM | ✅ |
| 10 | 📖 doc-watch-auto | `0 */6 * * *` | script | ✅ |
| 11 | 📝 docs-update | `0 */4 * * *` | script | ✅ |
| 12 | 📡 Machine KPI Collector | `*/5 * * * *` | script | ✅ |
| 13 | 📦 Auto-Archive BAVI LEO (5min) | `every 5m` | script | ✅ |
| 14 | 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | script | ✅ |
| 15 | 🔄 Auto-commit wikis (toutes les heures) | `0 * * * *` | script | ✅ |
| 16 | 🔄 Dashboard Server Watchdog | `*/2 * * * *` | script | ✅ |
| 17 | 🔄 Déploiement auto tofdan.be | `5 * * * *` | script | ✅ |
| 18 | 🔄 Rebuild Wiki BAVI local | `*/15 * * * *` | script | ✅ |
| 19 | 🔄 Rebuild Wiki Voyages local | `15 * * * *` | script | ✅ |
| 20 | 🔄 Refresh Google Tokens (50min) | `*/50 * * * *` | script | ✅ |
| 21 | 🔄 drive-sync | `0 * * * *` | script | ✅ |
| 22 | 🔄 sync-skills-to-copilot | `*/30 * * * *` | script | ✅ |
| 23 | 🔍 Veille IA quotidienne | `0 7 * * *` | script | ✅ |
| 24 | 🔧 LEO Maintenance quotidienne | `0 3 * * *` | script | ✅ |
| 25 | 🛡️ BAVI Server Watchdog | `*/5 * * * *` | script | ✅ |
| 26 | 🛡️ Cron Ownership Watchdog | `5,20,35,50 * * * *` | script | ✅ |
| 27 | 🛡️ LEO Health Check (script) | `2,17,32,47 * * * *` | script | ✅ |
| 28 | 🩺 Cron Health Watchdog (log scanner) | `3,18,33,48 * * * *` | script | ✅ |
| 29 | 🩺 GitHub Actions Watchdog | `4,19,34,49 * * * *` | script | ✅ |

<!-- AUTO:END hermes-crons -->

## Crons hôte

| # | Commande |
|:-:|----------|
| H1 | `0 */3 * * * cd /home/tofdan/scripts-hermes && python3 leo-snapshot.py ` |
| H2 | `0 23 * * * cd /home/tofdan/scripts-hermes && python3 backup-daily.py >` |
| H3 | `30 22 * * * cd /home/tofdan/scripts-hermes && python3 dashboard/budget` |
| H4 | `0 * * * * cd /home/tofdan/scripts-hermes && python3 dashboard/log_sess` |
| H5 | `0 2 * * * /opt/n8n-data/backup.sh >> /opt/n8n-data/backups/backup.log ` |

_Généré automatiquement le 11/07/2026 à 12:00_