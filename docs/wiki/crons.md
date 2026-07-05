# ⏰ Cronjobs Hermes — Inventaire complet

> **Audité le 5 juillet 2026** par Léo Copilot (DeepSeek Pro)

## Résumé

| Catégorie | Total |
|-----------|:-----:|
| **Crons Hermes** (dashboard) | **21** |
| Profil `default` | 6 |
| Profil `leo-copilot` | 13 |
| Profil `bavi-leo` | 1 |
| Profil `emile` | 1 |
| **Crons hôte** (crontab tofdan@172.17.0.1) | **5** |
| **Total général (Hermes + hôte)** | **26** |

---

## Liste exhaustive des 21 crons Hermes

### Profil `default` (6 crons)

| # | Nom | Horaire | Type | Statut |
|:-:|-----|:-------:|:----:|:------:|
| 1 | LEO Health Check bots | `*/15 * * * *` | no_agent (script) | ✅ ok |
| 2 | vault-daily-journal | `0 23 * * *` | agent + obsidian | ✅ ok |
| 3 | vault-default-daily-journal | `0 23 * * *` | agent + obsidian | ✅ ok |
| 4 | LEO Maintenance quotidienne | `0 3 * * *` | no_agent (script) | ✅ ok |
| 5 | LEO Backup quotidien → GDrive | `0 6 * * *` | no_agent (script) | ✅ ok |
| 6 | Auto-Archive BAVI LEO | every 5 min | no_agent (script) | ✅ ok |

### Profil `leo-copilot` (13 crons)

| # | Nom | Horaire | Type | Statut |
|:-:|-----|:-------:|:----:|:------:|
| 7 | LEO Full Backup quotidien (complet) | `0 2 * * *` | agent | ✅ ok |
| 8 | 🔍 Veille IA quotidienne | `0 7 * * *` | agent | ✅ ok |
| 9 | 🔄 Déploiement auto tofdan.be | `0 * * * *` | agent | ✅ ok |
| 10 | 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | no_agent (script) | ✅ ok |
| 11 | 📝 docs-update | `0 */4 * * *` | no_agent (script) | ✅ ok |
| 12 | 🔄 drive-sync | `0 * * * *` | no_agent (script) | ✅ ok |
| 13 | 📖 doc-watch-auto | `0 */6 * * *` | no_agent (script) | ✅ ok |
| 14 | 🩺 Auto-Heal Agent | `*/15 * * * *` | agent | ✅ ok |
| 15 | 🔄 sync-skills-to-copilot | `*/30 * * * *` | no_agent (script) | ✅ ok |
| 16 | 📦 Archive Watch — leo-tracker | `0 */6 * * *` | no_agent (script) | ✅ ok |
| 17 | 📊 Unified Collector v2 | `*/15 * * * *` | agent | ✅ ok |
| 18 | 🚀 Deploy Unified Dashboard | `10 * * * *` | no_agent (script) | ✅ ok |
| 19 | 💰 Budget Alert | `0 8,20 * * *` | no_agent (script) | ✅ ok |

### Profil `bavi-leo` (1 cron)

| # | Nom | Horaire | Type | Statut |
|:-:|-----|:-------:|:----:|:------:|
| 20 | vault-bavi-daily-journal | `0 23 * * *` | agent + obsidian | ❌ error (Broken pipe) |

### Profil `emile` (1 cron)

| # | Nom | Horaire | Type | Statut |
|:-:|-----|:-------:|:----:|:------:|
| 21 | vault-emile-daily-journal | `0 23 * * *` | agent + obsidian | ❌ error (Broken pipe) |

---

## Crons hôte (crontab — 5)

Ces crons tournent sur la machine hôte (tofdan@172.17.0.1), **indépendants** d'Hermes.

| # | Horaire | Commande | Rôle |
|:-:|:-------:|----------|------|
| H1 | `0 */3 * * *` | `leo-snapshot.py` | Snapshot mémoire tous les 3h |
| H2 | `0 23 * * *` | `backup-daily.py` | Backup quotidien |
| H3 | `30 22 * * *` | `budget-check.py && sheet-sync.py` | Vérif budget + sync sheets |
| H4 | `0 * * * *` | `log_session.py && sheet-sync.py` | Cost tracker horaire |
| H5 | `0 2 * * *` | `/opt/n8n-data/backup.sh` | Backup n8n |

---

## Explication de l'écart

Le **dashboard** affiche **"Scheduled Jobs (21)"** — c'est le total exact des jobs Hermes (tous profils, filtre "All profiles").

**Christophe voyait 18** probablement pour l'une des raisons suivantes :

1. **Filtre de profil** : Si Christophe regardait avec un filtre autre que "All profiles" (ex: seulement leo-copilot = 13), il ne voyait pas tous les jobs.
2. **Jobs récents** : 3 jobs ont été créés après le dernier comptage de Christophe :
   - `Auto-Archive BAVI LEO` (créé le 5 juillet 2026)
   - `vault-default-daily-journal` (créé le 4 juillet 2026)
   - `LEO Backup quotidien → GDrive` (créé le 4 juillet 2026)
3. **Avant le 4 juillet**, il y avait effectivement **18 jobs** : 13 (leo-copilot) + 1 (bavi-leo) + 1 (emile) + 3 anciens default = 18. L'ajout de 3 nouveaux jobs porte le total à 21.

**Conclusion : 21 est le chiffre correct** pour les crons Hermes dashboard. Le 18 de Christophe correspondait à l'état avant les ajouts des 4-5 juillet.

---

## Détail technique : où sont stockés les jobs

| Profil | Emplacement du fichier | Nombre |
|--------|----------------------|:------:|
| `default` | `/opt/data/cron/jobs.json` | 6 |
| `leo-copilot` | `/opt/data/profiles/leo-copilot/cron/jobs.json` | 13 |
| `bavi-leo` | `/opt/data/profiles/bavi-leo/cron/jobs.json` | 1 |
| `emile` | `/opt/data/profiles/emile/cron/jobs.json` | 1 |

> Note : les jobs du profil `default` sont stockés dans `/opt/data/cron/jobs.json` (racine), pas dans `/opt/data/profiles/default/cron/` (qui n'existe pas).

---

## Jobs avec erreur

- **vault-bavi-daily-journal** et **vault-emile-daily-journal** : erreur `RuntimeError: [Errno 32] Broken pipe`
  - Cause probable : le skill Obsidian n'est pas disponible ou configuré correctement dans les profils bavi-leo et emile.
  - Action recommandée : vérifier la configuration Obsidian dans ces profils.

---

*Rapport d'audit généré par Léo Copilot · 5 juillet 2026*
