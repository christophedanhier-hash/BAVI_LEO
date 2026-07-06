# ⏰ Cronjobs Hermes — Inventaire complet

<!-- AUTO:START header -->
> **Généré automatiquement le 06/07/2026 à 21:41** par le script `doc-crons-sync.py`
> Source : `profiles/leo-copilot/cron/jobs.json` (22 jobs actifs)
<!-- AUTO:END header -->

## Résumé

| Catégorie | Total |
|-----------|:-----:|
| **Crons Hermes** (tous profils, consolidé) | **22** |
| **Crons hôte** (crontab tofdan@172.17.0.1) | **5** |
| **Total général (Hermes + hôte)** | **27** |

---

## Liste exhaustive des crons Hermes

> ⚠️ Tous les crons sont **consolidés** dans le profil `leo-copilot` par le scheduler Hermes.
> Les autres profils (default, bavi-leo, emile) ont 0 cron — tout est centralisé.

<!-- AUTO:START hermes-crons -->

| # | Nom | Horaire | Mode | Statut | Skills |
|:-:|-----|:-------:|:----:|:------:|:------:|
| 1 | 💰 Budget Alert | `0 8,20 * * *` | script (no_agent) | ✅ | — |
| 2 | 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | script (no_agent) | ✅ | — |
| 3 | 📊 Unified Collector v2 | `*/15 * * * *` | agent LLM | ✅ | — |
| 4 | 📓 vault-bavi-daily-journal | `0 23 * * *` | agent LLM | ✅ | obsidian |
| 5 | 📓 vault-daily-journal (vault-leo) | `0 23 * * *` | agent LLM | ✅ | obsidian |
| 6 | 📓 vault-default-daily-journal | `0 23 * * *` | agent LLM | ✅ | obsidian |
| 7 | 📓 vault-emile-daily-journal | `0 23 * * *` | agent LLM | ✅ | obsidian |
| 8 | 📖 doc-watch-auto | `0 */6 * * *` | script (no_agent) | ✅ | — |
| 9 | 📝 docs-update | `0 */4 * * *` | script (no_agent) | ✅ | — |
| 10 | 📦 Auto-Archive BAVI LEO (5min) | `every 5m` | script (no_agent) | ✅ | — |
| 11 | 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | script (no_agent) | ✅ | — |
| 12 | 🔄 Auto-commit wikis (toutes les heures) | `0 * * * *` | script (no_agent) | ✅ | — |
| 13 | 🔄 Déploiement auto tofdan.be | `0 * * * *` | script (no_agent) | ✅ | — |
| 14 | 🔄 Refresh Google Tokens (50min) | `*/50 * * * *` | script (no_agent) | ✅ | — |
| 15 | 🔄 drive-sync | `0 * * * *` | script (no_agent) | ✅ | — |
| 16 | 🔄 sync-skills-to-copilot | `*/30 * * * *` | script (no_agent) | ✅ | — |
| 17 | 🔍 Veille IA quotidienne | `0 7 * * *` | script (no_agent) | ✅ | — |
| 18 | 🔧 LEO Maintenance quotidienne | `0 3 * * *` | script (no_agent) | ✅ | — |
| 19 | 🚀 Deploy Unified Dashboard | `10 * * * *` | script (no_agent) | ✅ | — |
| 20 | 🛡️ LEO Health Check (script) | `*/15 * * * *` | script (no_agent) | ✅ | — |
| 21 | 🩺 Cron Health Watchdog (log scanner) | `*/15 * * * *` | script (no_agent) | ✅ | — |
| 22 | 🩺 GitHub Actions Watchdog | `*/15 * * * *` | script (no_agent) | ✅ | — |

<!-- AUTO:END hermes-crons -->

---

## Crons hôte (crontab — 5)

Ces crons tournent sur la **machine hôte** (tofdan@172.17.0.1), indépendants d'Hermes.

<!-- AUTO:START host-crons -->

| # | Horaire | Commande |
|:-:|:-------:|----------|
| H1 | `0 */3 * * *` | cd /home/tofdan/scripts-hermes && python3 leo-snapshot.py >> /home/tof |
| H2 | `0 23 * * *` | cd /home/tofdan/scripts-hermes && python3 backup-daily.py >> /home/tof |
| H3 | `30 22 * * *` | cd /home/tofdan/scripts-hermes && python3 dashboard/budget-check.py && |
| H4 | `0 * * * *` | cd /home/tofdan/scripts-hermes && python3 dashboard/log_session.py &&  |
| H5 | `0 2 * * *` | /opt/n8n-data/backup.sh >> /opt/n8n-data/backups/backup.log 2>&1 |

<!-- AUTO:END host-crons -->

---

## Répartition par profil (archivé)

> ℹ️ Depuis la consolidation des crons, tous les jobs Hermes sont gérés par le profil `leo-copilot`.
> Les autres profils n'ont plus de crons — ils délèguent via le scheduler central.
> Cette section est conservée pour référence historique.

| Profil | Crons | Note |
|--------|:----:|------|
| `leo-copilot` | 22 | Consolidateur — scheduler central |
| `default` | 0 | Consolidé vers leo-copilot |
| `bavi-leo` | 0 | Consolidé vers leo-copilot |
| `emile` | 0 | Consolidé vers leo-copilot |

_Documentation générée automatiquement par `doc-crons-sync.py` le 06/07/2026 à 21:41_
