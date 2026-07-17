# ⏰ Cronjobs Hermes — Inventaire complet

<!-- AUTO:START header -->
> **Généré automatiquement le 17/07/2026 à 12:00**
> Source : `profiles/leo-copilot/cron/jobs.json` (37 jobs)
<!-- AUTO:END header -->

## Résumé

| Catégorie | Total |
|-----------|:-----:|
| **Crons Hermes** (tous profils, consolidé) | **37** |
| **Crons hôte** (crontab tofdan@172.17.0.1) | **6** |
| **Total général** | **43** |
_Généré automatiquement le 17/07/2026 à 12:00_

## Crons hôte

| # | Commande |
|:-:|----------|
| H1 | `0 */3 * * * cd /home/tofdan/scripts-hermes && python3 leo-snapshot.py ` |
| H2 | `0 23 * * * cd /home/tofdan/scripts-hermes && python3 backup-daily.py >` |
| H3 | `30 22 * * * cd /home/tofdan/scripts-hermes && python3 dashboard/budget` |
| H4 | `0 * * * * cd /home/tofdan/scripts-hermes && python3 dashboard/log_sess` |
| H5 | `0 2 * * * /opt/n8n-data/backup.sh >> /opt/n8n-data/backups/backup.log ` |
| H6 | `*/5 * * * * /home/tofdan/.hermes/scripts/gateway-watchdog.sh` |

_Généré automatiquement le 17/07/2026 à 12:00_

<!-- 🤖 Auto-fix audit 2026-07-17 -->
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
| 14 | 📝 docs-update | `0 */4 * * *` | script | ✅ |
| 15 | 📡 Machine KPI Collector | `*/5 * * * *` | script | ✅ |
| 16 | 📦 Auto-Archive BAVI LEO (5min) | `every 5m` | script | ✅ |
| 17 | 📦 Cron Log Archiver (horaire) | `15 * * * *` | script | ✅ |
| 18 | 📧 Check Gmail — emails importants (30min) | `every 30m` | script | ✅ |
| 19 | 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | script | ✅ |
| 20 | 📷 Surveillance caméras — mouvement → Telegram | `*/5 * * * *` | script | ✅ |
| 21 | 🔄 Auto-commit wikis (toutes les heures) | `0