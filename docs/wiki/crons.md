# ⏰ Cronjobs Hermes — Inventaire complet

<!-- AUTO:START header -->
> **Généré automatiquement le 18/07/2026 à 18:00**
> Source : `profiles/leo-copilot/cron/jobs.json` (38 jobs)
<!-- AUTO:END header -->

## Résumé

| Catégorie | Total |
|-----------|:-----:|
| **Crons Hermes** (tous profils, consolidé) | **38** |
| **Crons hôte** (crontab tofdan@172.17.0.1) | **6** |
| **Total général** | **44** |

## Liste exhaustive des crons Hermes

<!-- AUTO:START hermes-crons -->

| # | Nom | Horaire | Mode | Statut |
|:-:|-----|:-------:|:----:|:------:|
| 1 | Drive → Issue GitHub | `*/30 * * * *` | script | ✅ |
| 2 | Gardien du Drive | `0 */6 * * *` | script | ✅ |
| 3 | Save Contacts | `*/15 * * * *` | script | ✅ |
| 4 | ⚡ Énergie — HomeWizard P1 | `*/2 * * * *` | script | ✅ |
| 5 | 💰 Budget Alert | `0 8,20 * * *` | script | ✅ |
| 6 | 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | script | ✅ |
| 7 | 💾 Recovery State Export → GDrive (horaire) | `30 * * * *` | script | ✅ |
| 8 | 📊 Agrégation Énergie (horaire) | `0 * * * *` | script | ✅ |
| 9 | 📊 Synthèse Hebdomadaire LEO | `0 20 * * 0` | script | ✅ |
| 10 | 📊 Unified Collector v2 | `*/15 * * * *` | LLM | ✅ |
| 11 | 📋 Doc Watch Auto (sync documents) | `*/2 * * * *` | script | ✅ |
| 12 | 📋 doc-crons-sync | `0 */6 * * *` | script | ✅ |
| 13 | 📓 Journaux Quotidiens (4 vaults) | `0 23 * * *` | LLM | ✅ |
| 14 | 📝 Audit rédactionnel unifié (2 wikis, 1 passage) | `0 6 * * *` | LLM | ✅ |
| 15 | 📝 docs-update | `0 */4 * * *` | script | ✅ |
| 16 | 📡 Machine KPI Collector | `*/5 * * * *` | script | ✅ |
| 17 | 📦 Auto-Archive BAVI LEO (5min) | `every 5m` | script | ✅ |
| 18 | 📦 Cron Log Archiver (horaire) | `15 * * * *` | script | ✅ |
| 19 | 📧 Check Gmail — emails importants (30min) | `every 30m` | script | ✅ |
| 20 | 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | script | ✅ |
| 21 | 📷 Surveillance caméras — mouvement → Telegram | `*/5 * * * *` | script | ✅ |
| 22 | 🔄 Auto-commit wikis (toutes les heures) | `0 * * * *` | script | ✅ |
| 23 | 🔄 Déploiement auto tofdan.be | `5 * * * *` | script | ✅ |
| 24 | 🔄 Gateway Auto-Restart | `*/15 * * * *` | script | ✅ |
| 25 | 🔄 Rebuild Wiki BAVI local | `*/15 * * * *` | script | ✅ |
| 26 | 🔄 Rebuild Wiki Voyages local | `15 * * * *` | script | ✅ |
| 27 | 🔄 Refresh Google Tokens (50min) | `*/50 * * * *` | script | ✅ |
| 28 | 🔄 drive-sync | `0 * * * *` | script | ✅ |
| 29 | 🔄 sync-skills-to-copilot | `*/30 * * * *` | script | ✅ |
| 30 | 🔍 Audit Infra (cohérence globale) | `0 * * * *` | script | ✅ |
| 31 | 🔍 Veille IA quotidienne | `0 7 * * *` | script | ✅ |
| 32 | 🔧 LEO Maintenance quotidienne | `0 3 * * *` | script | ✅ |
| 33 | 🖥️ Dashboards Watchdog (8765+9119) | `*/2 * * * *` | script | ✅ |
| 34 | 🛡️ LEO Health Check (script) | `2,17,32,47 * * * *` | script | ✅ |
| 35 | 🛡️ Watchdog BAVI-LEO (Sylvia) | `*/5 * * * *` | script | ✅ |
| 36 | 🩺 Cron Watchdog v2 (logs + ownership) | `*/15 * * * *` | script | ✅ |
| 37 | 🩺 GitHub Actions Watchdog | `4,19,34,49 * * * *` | script | ✅ |
| 38 | Collecte Viessmann | `*/5 * * * *` | LLM | ✅ |

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

_Généré automatiquement le 18/07/2026 à 18:00_