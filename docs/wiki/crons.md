# ⏰ Cronjobs Hermes — Inventaire complet

<!-- AUTO:START header -->
> **Généré automatiquement le 07/07/2026 à 12:00**
> Source : `profiles/leo-copilot/cron/jobs.json` (23 jobs)
<!-- AUTO:END header -->

## Résumé

| Catégorie | Total |
|-----------|:-----:|
| **Crons Hermes** (tous profils, consolidé) | **23** |
| **Crons hôte** (crontab tofdan@172.17.0.1) | **5** |
| **Total général** | **28** |

## Liste exhaustive des crons Hermes

<!-- AUTO:START hermes-crons -->

| # | Nom | Horaire | Mode | Statut |
|:-:|-----|:-------:|:----:|:------:|
| 1 | 💰 Budget Alert | `0 8,20 * * *` | script | ✅ |
| 2 | 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | script | ✅ |
| 3 | 📊 Unified Collector v2 | `*/15 * * * *` | LLM | ✅ |
| 4 | 📋 doc-crons-sync | `0 */6 * * *` | script | ⚠️ |
| 5 | 📓 vault-bavi-daily-journal | `0 23 * * *` | LLM | ✅ |
| 6 | 📓 vault-daily-journal (vault-leo) | `0 23 * * *` | LLM | ✅ |
| 7 | 📓 vault-default-daily-journal | `0 23 * * *` | LLM | ✅ |
| 8 | 📓 vault-emile-daily-journal | `0 23 * * *` | LLM | ✅ |
| 9 | 📖 doc-watch-auto | `0 */6 * * *` | script | ✅ |
| 10 | 📝 docs-update | `0 */4 * * *` | script | ✅ |
| 11 | 📦 Auto-Archive BAVI LEO (5min) | `every 5m` | script | ✅ |
| 12 | 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | script | ✅ |
| 13 | 🔄 Auto-commit wikis (toutes les heures) | `0 * * * *` | script | ✅ |
| 14 | 🔄 Déploiement auto tofdan.be | `0 * * * *` | script | ✅ |
| 15 | 🔄 Refresh Google Tokens (50min) | `*/50 * * * *` | script | ✅ |
| 16 | 🔄 drive-sync | `0 * * * *` | script | ✅ |
| 17 | 🔄 sync-skills-to-copilot | `*/30 * * * *` | script | ✅ |
| 18 | 🔍 Veille IA quotidienne | `0 7 * * *` | script | ✅ |
| 19 | 🔧 LEO Maintenance quotidienne | `0 3 * * *` | script | ✅ |
| 20 | 🚀 Deploy Unified Dashboard | `10 * * * *` | script | ✅ |
| 21 | 🛡️ LEO Health Check (script) | `*/15 * * * *` | script | ✅ |
| 22 | 🩺 Cron Health Watchdog (log scanner) | `*/15 * * * *` | script | ✅ |
| 23 | 🩺 GitHub Actions Watchdog | `*/15 * * * *` | script | ✅ |

<!-- AUTO:END hermes-crons -->

## Crons hôte

| # | Commande |
|:-:|----------|
| H1 | `0 */3 * * * cd /home/tofdan/scripts-hermes && python3 leo-snapshot.py ` |
| H2 | `0 23 * * * cd /home/tofdan/scripts-hermes && python3 backup-daily.py >` |
| H3 | `30 22 * * * cd /home/tofdan/scripts-hermes && python3 dashboard/budget` |
| H4 | `0 * * * * cd /home/tofdan/scripts-hermes && python3 dashboard/log_sess` |
| H5 | `0 2 * * * /opt/n8n-data/backup.sh >> /opt/n8n-data/backups/backup.log ` |

_Généré automatiquement le 07/07/2026 à 12:00_