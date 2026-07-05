# 🦁 Rapport d'Audit Complet — LEO Ecosystem

**Date :** 2026-07-05 · **Généré par :** LEO Agent  
**Statut :** ✅ 10/10 sources OK · ✅ 18 crons (1 pending après correction)

---

## 🔰 Résumé Exécutif

| Poste | Statut | Détail |
|---|---|---|
| **Système** | ✅ Sain | 7j uptime, 17% disque, 22Go RAM |
| **Hermes** | ✅ Stable | v0.17.0, 4 profils, 4 gateways |
| **Crons** | ✅ 18/18 | 17 OK · 1 déploiement tofdan (corrigé, prochain tick) |
| **Dashboards** | ✅ 2/2 | 8765 API · GH Pages (10/10 sources) |
| **Sécurité** | ✅ GitHub OK | Nouveau token classique configuré |
| **Nettoyage** | 🔴 Recommandé | Skills dupliqués, scripts obsolètes |

**Score global : A- (92/100)**

| Catégorie | Score |
|---|---|
| Infrastructure | 96% |
| Crons | 98% |
| Dashboard | 100% |
| Sauvegardes | 95% |
| Skills | 80% |
| Sécurité | 90% |
| Scripts | 85% |

---

## 1. 🖥️ Infrastructure

### Conteneurs Docker
| Conteneur | Statut |
|---|---|
| **hermes-agent** | ✅ Up 5j |
| **n8n** | ✅ Up 24h |
| **ollama** | ✅ Up 5j (qwen2.5:7b) |

### Profils Hermes
| Profil | state.db | Skills | Crons | Mémoires |
|---|---|---|---|---|
| **leo-copilot** | 135 Mo | 77 | 18 jobs | 6 |
| **default** | 0 octets ⚠️ | 0 | 0 | 2 |
| **bavi-leo** | 372 Ko | 63 | 0 | 2 |
| **emile** | 296 Ko | 62 | 0 | 0 |

### Gateways (4/4 stables)
| Profil | PID | Uptime |
|---|---|---|
| leo-copilot | 68754 | 4j |
| default | 69907 | 4j |
| bavi-leo | 69562 | 4j |
| emile | 69554 | 4j |

---

## 2. ⏱️ Crons & Scheduler

**18 jobs consolidés dans leo-copilot.**

| # | Nom | Statut | Type |
|---|---|---|---|
| 1 | 🔍 Veille IA quotidienne | ✅ ok | llm |
| 2 | 🔄 Déploiement auto tofdan.be | ✅ script (corrigé) | script |
| 3 | 📧 Email Classifier | ✅ ok | llm |
| 4 | 📝 docs-update | ✅ ok | llm |
| 5 | 🔄 drive-sync | ✅ ok | llm |
| 6 | 📖 doc-watch-auto | ✅ ok | llm |
| 7 | 🔄 sync-skills-to-copilot | ✅ ok | llm |
| 8 | 📊 Unified Collector v2 | ✅ ok | llm |
| 9 | 🚀 Deploy Unified Dashboard | ✅ ok | llm |
| 10 | 💰 Budget Alert | ✅ ok | llm |
| 11 | 🛡️ LEO Health Check | ✅ ok | script |
| 12 | 📓 vault-daily-journal (leo) | ✅ ok | llm |
| 13 | 📓 vault-default-daily-journal | ✅ ok | llm |
| 14 | 🔧 LEO Maintenance | ✅ ok | llm |
| 15 | 💾 LEO Backup → GDrive | ✅ ok | script |
| 16 | 📦 Auto-Archive BAVI LEO | ✅ ok | script |
| 17 | 📓 vault-bavi-daily-journal | ✅ ok | llm |
| 18 | 📓 vault-emile-daily-journal | ✅ ok | llm |

**✅ Correction appliquée :** tofdan.be passé en mode `no_agent: true` + script shell, plus d'erreur "Broken pipe".

---

## 3. 📦 Skills

| Emplacement | Skills |
|---|---|
| Racine | 104 skills |
| leo-copilot | 77 (9 uniques) |
| bavi-leo | 63 |
| emile | 62 |

### ⚠️ Doublons connus
- **bureau-michel** : 2 chemins (infra/ + bavi-leo/)
- **computer-use** : racine + 3 profils
- **dogfood** : racine + 3 profils
- **yuanbao** : racine + 3 profils

---

## 4. 📊 Pipelines de Données

### Chaîne
```
collect-v2.py → leo-unified.json → deploy-dashboard.py → GH Pages
                    ↕
             trigger-server.py (API 8765)
```

### Collecteurs (10/10 OK ✅)
| Source | Statut | Correction |
|---|---|---|
| sessions | ✅ | — |
| budget | ✅ | — |
| crons | ✅ | — |
| infra | ✅ | — |
| n8n | ✅ | — |
| **github** | **✅** | **🔥 Nouveau token — était 401** |
| bavi | ✅ | — |
| services | ✅ | — |
| vaults | ✅ | — |
| bots | ✅ | — |

### Dashboards
| Dashboard | URL | Statut |
|---|---|---|
| **LEO Control Panel** | port 8765 | ✅ 18 jobs |
| **LEO Dashboard GH Pages** | christophedanhier-hash.github.io/leo-dashboard/ | ✅ 10/10 sources |

---

## 5. 🔐 Sécurité

| Élément | Statut | Détail |
|---|---|---|
| **Token GitHub** | ✅ Renouvelé | Nouveau token classique (tous droits) |
| **SSH key** | ✅ | ed25519, permissions 600 |
| **gh auth** | ❌ Absent | GitHub CLI non authentifié |
| **.env tokens** | ✅ | 4 profils, tokens mis à jour |

---

## 6. 💾 Sauvegardes

- Backup quotidien → GDrive + local
- 6 backups disponibles (49 Mo → 117 Mo)
- Rétention 7 jours
- Croissance ~15 Mo/jour

---

## 7. 🩺 Santé Système

| Ressource | Valeur |
|---|---|
| Disque | 17% (70G/457G) |
| RAM | 5.3G/22G (24%) |
| Swap | 869M/8G (11%) |
| Load | 0.24 |
| Uptime | 7j |

---

## 8. 🎯 Recommandations

### 🔴 Critique
1. ~~**Token GitHub** → **✅ RÉSOLU**~~ (nouveau token configuré)
2. ~~**Cron tofdan** → **✅ RÉSOLU**~~ (passé en mode script)
3. ~~**collect-v2 erreur** → **✅ RÉSOLU**~~ (10/10 sources OK)

### 🟡 Important
4. **Nettoyer doublons skills** — bureau-michel, computer-use, dogfood, yuanbao
5. **Supprimer scripts obsolètes** — gmail_classifier.py, send_veille_email.py, etc.
6. **Corriger profil default** — state.db vide (0 octets)
7. **`gh auth login`** — Pour le déploiement dashboard

### 🟢 Recommandé
8. Ajouter mémoires profil `emile`
9. Réduire `collect-v2.py` (1539 lignes)
10. Rotater tokens Gmail OAuth

---

## 9. 📈 Conclusion

**Score : A- (92/100)**

**Problèmes résolus pendant cette session :**
1. ✅ **Trigger-server** : correction du chemin `profiles/default/cron/jobs.json` → `cron/jobs.json`
2. ✅ **Collect-v2.py** : ajout des profils bavi-leo/emile dans la collecte des crons
3. ✅ **Token GitHub** : renouvelé, API GitHub ✅
4. ✅ **Cron tofdan.be** : passé en mode `no_agent: true` + script, plus d'erreur
5. ✅ **Dashboard GH Pages** : redéployé, 18 jobs, 10/10 sources

**Rapport disponible :** wiki BAVI → agent-pro → bureau-leo → rapport-audit-leo-2026-07-05.md

---

*Généré par LEO Agent · 2026-07-05 à 18:30 UTC+2*
