# ⏰ Cronjobs Hermes — Inventaire complet

<!-- AUTO:START header -->
> **Généré automatiquement le 13/07/2026 à 06:00**
> Source : `profiles/leo-copilot/cron/jobs.json` (40 jobs)
<!-- AUTO:END header -->

## Résumé

| Catégorie | Total |
|-----------|:-----:|
| **Crons Hermes** (tous profils, consolidé) | **40** |
| **Crons hôte** (crontab tofdan@172.17.0.1) | **6** |
| **Total général** | **46** |

## Liste exhaustive des crons Hermes

<!-- AUTO:START hermes-crons -->

| # | Nom | Horaire | Mode | Statut |
|:-:|-----|:-------:|:----:|:------:|
| 1 | Collecte Viessmann | `*/5 * * * *` | LLM | ✅ |
| 2 | Drive → Issue GitHub | `*/30 * * * *` | script | ⚠️ |
| 3 | Gardien du Drive | `0 */6 * * *` | script | ⚠️ |
| 4 | Save Contacts | `*/15 * * * *` | script | ✅ |
| 5 | ⚡ Énergie — HomeWizard P1 | `*/2 * * * *` | script | ✅ |
| 6 | 💰 Budget Alert | `0 8,20 * * *` | script | ✅ |
| 7 | 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | script | ✅ |
| 8 | 💾 Recovery State Export → GDrive (horaire) | `30 * * * *` | script | ✅ |
| 9 | 📊 Synthèse Hebdomadaire LEO | `0 20 * * 0` | script | ✅ |
| 10 | 📊 Unified Collector v2 | `*/15 * * * *` | LLM | ✅ |
| 11 | 📋 Doc Watch Auto (sync documents) | `*/2 * * * *` | script | ✅ |
| 12 | 📋 doc-crons-sync | `0 */6 * * *` | script | ✅ |
| 13 | 📓 vault-bavi-daily-journal | `10 23 * * *` | LLM | ✅ |
| 14 | 📓 vault-daily-journal (vault-leo-copilot) | `0 23 * * *` | LLM | ✅ |
| 15 | 📓 vault-default-daily-journal | `5 23 * * *` | LLM | ✅ |
| 16 | 📓 vault-emile-daily-journal | `15 23 * * *` | LLM | ✅ |
| 17 | 📝 docs-update | `0 */4 * * *` | script | ✅ |
| 18 | 📡 Machine KPI Collector | `*/5 * * * *` | script | ✅ |
| 19 | 📦 Auto-Archive BAVI LEO (5min) | `every 5m` | script | ✅ |
| 20 | 📧 Check Gmail Watchdog | `*/5 * * * *` | script | ✅ |
| 21 | 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | script | ✅ |
| 22 | 📷 Surveillance caméras — mouvement → Telegram | `*/5 * * * *` | script | ✅ |
| 23 | 🔄 Auto-commit wikis (toutes les heures) | `0 * * * *` | script | ✅ |
| 24 | 🔄 Dashboard LEO Watchdog (port 8765) | `*/2 * * * *` | script | ✅ |
| 25 | 🔄 Déploiement auto tofdan.be | `5 * * * *` | script | ✅ |
| 26 | 🔄 Gateway Auto-Restart | `*/15 * * * *` | script | ✅ |
| 27 | 🔄 Hermes Dashboard Watchdog (port 9119) | `*/2 * * * *` | script | ✅ |
| 28 | 🔄 Rebuild Wiki BAVI local | `*/15 * * * *` | script | ✅ |
| 29 | 🔄 Rebuild Wiki Voyages local | `15 * * * *` | script | ✅ |
| 30 | 🔄 Refresh Google Tokens (50min) | `*/50 * * * *` | script | ✅ |
| 31 | 🔄 drive-sync | `0 * * * *` | script | ✅ |
| 32 | 🔄 sync-skills-to-copilot | `*/30 * * * *` | script | ✅ |
| 33 | 🔍 Veille IA quotidienne | `0 7 * * *` | script | ✅ |
| 34 | 🔧 LEO Maintenance quotidienne | `0 3 * * *` | script | ✅ |
| 35 | 🛡️ BAVI Server Watchdog | `*/5 * * * *` | script | ✅ |
| 36 | 🛡️ Cron Ownership Watchdog | `5,20,35,50 * * * *` | script | ✅ |
| 37 | 🛡️ LEO Health Check (script) | `2,17,32,47 * * * *` | script | ✅ |
| 38 | 🛡️ Watchdog BAVI-LEO (Sylvia) | `*/5 * * * *` | script | ✅ |
| 39 | 🩺 Cron Health Watchdog (log scanner) | `3,18,33,48 * * * *` | script | ✅ |
| 40 | 🩺 GitHub Actions Watchdog | `4,19,34,49 * * * *` | script | ✅ |

<!-- AUTO:END hermes-crons -->

## Crons hôte

| # | Commande |
|:-:|----------|
| H1 | `0 */3 * * * cd /home/tofdan/scripts-hermes && python3 leo-snapshot.py ` |
| H2 | `0 23 * * * cd /home/tofdan/scripts-hermes && python3 backup-daily.py >` |
| H3 | `30 22 * * * cd /home/tofdan/scripts-hermes && python3 dashboard/budget` |
| H4 | `0 * * * * cd /home/tofdan/scripts-hermes && python3 dashboard/log_sess` |
| H5 | `0 2 * * * /opt/n8n-data/backup.sh >> /opt/n8n-data/backups/backup.log ` |
| H6 | `*/5 * * * * /home/tofdan/.hermes/scripts/gateway-watchdog.sh` |

_Généré automatiquement le 13/07/2026 à 06:00_