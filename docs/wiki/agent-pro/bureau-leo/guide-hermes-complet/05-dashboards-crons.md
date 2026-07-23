---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v5.0
modele: deepseek-v4-flash
tags: [hermes, guide, dashboards, monitoring, crons, budget, watchdogs, auto-heal, drive-sync, backup, veille-ia]
statut: ✅ À jour
type: guide
hide:
  - toc
---

> **Dernière mise à jour rédactionnelle :** 18/07/2026 — Léo 🦁
> **Partie V+VI — Dashboards, Monitoring, Crons & Watchdogs :** 39 crons (gérés par leo-copilot), 1 dashboard central (4 onglets, 20 KPI), auto-heal, sync Drive ↔ GitHub | **Audit rédactionnel :** ✅ conforme | **n8n** retiré le 13/07/2026

# Partie V — Dashboards et Monitoring

Visualisez l'activité de votre assistant en temps réel avec des dashboards HTML autonomes, déployés sur GitHub Pages.

---

## Principe

Un dashboard est un fichier HTML statique (zéro JavaScript serveur, zéro backend) :

```text
Script de collecte → JSON + HTML → Push GitHub Pages
                                      ↓
                    https://user.github.io/mon-dashboard/
```

**Avantages :** gratuit (GitHub Pages), accessible partout, aucun serveur à maintenir.

## Les dashboards de LEO

LEO a **1 dashboard central** (4 onglets, 20 KPI, 4 charts) rafraîchi par un cron no_agent :

| Dashboard | Contenu | URL | Cron |
|-----------|---------|-----|------|
| **LEO Dashboard** | Synthèse, Analyses, Infra, BAVI | [leo-dashboard](http://localhost:8765/dashboard) | */15 |

Tous sont générés par des scripts `no_agent` — **0$ de coût LLM** par mise à jour.

## Architecture technique

Chaque dashboard suit le même pattern :

1. **Un script de collecte** (Python) qui :
   - Récupère les données (API, fichiers, logs)
   - Génère un `index.html` avec Chart.js ou CSS pur

2. **Un cron no_agent** qui exécute le script toutes les 4h

3. **Un dépôt GitHub Pages** qui sert le HTML

### Script type

```python
#!/usr/bin/env python3
import json, subprocess
from pathlib import Path

# 1. Collecter les données
data = collecter_metriques()

# 2. Générer le HTML
html = generer_dashboard(data)

# 3. Écrire dans le repo
repo = Path("/tmp/mon-dashboard")
repo.joinpath("index.html").write_text(html)

# 4. Push sur GitHub
subprocess.run(["git", "-C", str(repo), "add", "."])
subprocess.run(["git", "-C", str(repo), "commit", "-m", "Màj dashboard"])
subprocess.run(["git", "-C", str(repo), "push", "origin", "main"])
```

### Déploiement

```bash
# 1. Créer le repo
gh repo create mon-dashboard --public

# 2. Activer GitHub Pages
echo '{"source":{"branch":"main","path":"/"}}' | \
  gh api repos/user/mon-dashboard/pages --input -

# 3. Cloner en local
git clone https://github.com/user/mon-dashboard.git /tmp/mon-dashboard

# 4. Configurer le cron
hermes cron create \
  --script deploy-dashboard.sh \
  --schedule "0 */4 * * *" \
  --name "mon-dashboard" \
  --no-agent
```

## Pitfalls

### 🔴 Pas de JavaScript si le navigateur flashe

Sur certains appareils (Chromebook, mobile), Chart.js en mode responsive peut causer un rafraîchissement en boucle. Solution : **remplacer Chart.js par un tableau CSS statique**.

```css
/* Au lieu d'un graphique JS : tableau statique */
.hist-table td.ok-cell { color: #22c55e; }
.hist-table td.err-cell { color: #ef4444; }
```

### 🔴 Gérer l'identité Git

Dans l'environnement minimal d'un cron, `git commit` échoue si l'identité n'est pas configurée :

```python
subprocess.run(["git", "config", "user.name", "MonAssistant"])
subprocess.run(["git", "config", "user.email", "assistant@exemple.com"])
```

### 🔴 Gérer l'authentification GitHub

Le cron n'a pas de TTY pour le flow OAuth Git. Passez le token dans l'URL :

```python
import os
tok = os.environ.get("GH_TOKEN")
if tok:
    remote = f"https://user:{tok}@github.com/user/repo.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote])
```

### 🔴 Les repos locaux doivent être synchronisés

`dashboard-watch` vérifie l'âge du dernier commit **dans le repo local** pour déterminer si un dashboard est stale. Si votre script de déploiement push vers un clone temporaire (`/tmp/...`), le repo local ne sera jamais mis à jour et `dashboard-watch` déclenchera un redeploiement à chaque cycle.

**Solution :** après avoir pushé depuis `/tmp/`, faites un `git pull` dans le repo local :

```bash
cd ~/Projets_Dev/n8n-dashboard
git pull origin main
```

> 🐛 **Bug #16** — Cette cause racine a été corrigée sur le dashboard n8n (juin 2026).

### 🔴 Webhook budget pour n8n (⚠️ héritage)

> **Note :** n8n est déprécié depuis juillet 2026. Ceci est conservé pour les déploiements hérités.

Si vous utilisez n8n pour remplacer un cron Hermes, n8n tourne dans Docker et n'a pas accès direct au filesystem. Créez un **webhook HTTP** sur l'hôte :

```python
# budget-webhook.py — mini serveur HTTP
# POST /budget-update → écrit dans budget.json
# GET  /health        → status
```

Lancé en background (`python3 scripts/budget-webhook.py &`). n8n y POSTe les données collectées.

### 🔴 Budget désynchronisé

Si le budget affiché sur un dashboard ne correspond pas au `budget.json`, le cron `dashboard-watch` déclenche une alerte. Vérifiez que les clés lues par le script de déploiement correspondent exactement à celles du JSON :

```python
# Dans budget.json : "avg_daily", "total_spent" (pas "daily_spend")
# Dans le script : budget.get("avg_daily", 0)  # ✅ correct
```

## Surveillance automatique (dashboard-watch)

Un cron **dashboard-watch** (`scripts/dashboard-watch.py`) tourne toutes les 2h et vérifie :

1. **HTTP 200** — chaque dashboard répond
2. **Âge < 2h** — données fraîches
3. **Budget cohérent** — valeur affichée ≈ `budget.json` (écart max 1$)
4. **Redeploiement auto** — si stale ou 404, le script relance le déploiement
5. **Rebuild GH Pages** — après chaque push, appelle l'API pour forcer le rafraîchissement CDN

```python
# Extrait : rebuild GH Pages après push
subprocess.run(["gh", "api", f"repos/user/{repo}/pages/builds", "-X", "POST"])
```

## 🦁 Global Dashboard LEO (portail unique)

Depuis le 22/06/2026, LEO a un **portail unique** qui consolide tout en une seule page :
- 🔵 **Crons (44)** — statut, historique, erreurs
- 📊 **Dashboard (1)** — HTTP, âge, budget
- 💰 **Budget DeepSeek** — solde, jours restants
- 🩺 **n8n** — online/offline
- 🏛️ **BAVI LEO** — sessions, messages, tokens
- 🖥️ **Machine** — statut en ligne/hors ligne
- 🚨 **Alertes** — dernières anomalies détectées
- 🔗 **Liens rapides** — accès au dashboard détaillé

**Avantages :**
- ✅ **Plus aucun rapport Telegram** — dashboard-watch et Auto-Heal livrent en local
- ✅ **Un seul bookmark** au lieu de 7
- ✅ **Cron no_agent toutes les 10min** (H:05) — 0$ de coût
- ✅ **Auto-déploiement GH Pages**

```bash
# Le cron
🌍 Global Dashboard — H:05 → ~/.hermes/profiles/leo-copilot/scripts/deploy_leo_global.py (no_agent)
```

- **Usage LLM** — requêtes/jour, tokens consommés, coût estimé
- **Système** — CPU, RAM, disque, uptime de votre serveur
- **Projets** — Suivi d'avancement, tâches complétées
- **Réseau** — Latence, bande passante, statut des services

### Pour aller plus loin

- Voir `03-utilisation/crons.md` pour le déploiement automatisé
- Voir `03-utilisation/architecture-leo.md` pour la vue complète (schéma Mermaid, interactions, filets)
- Voir `exemples/LEO.md` pour les dashboards en production

---

# Métriques machines : CPU, RAM, disque, GPU

Un assistant qui tourne 24h/24 a besoin qu'on surveille sa santé. Les métriques machines sont le premier dashboard que LEO a mis en place.

## Pourquoi surveiller ?

```yaml
Risques réels:
  - Disque plein → Hermes plante, plus de logs, plus de sessions
  - RAM épuisée → ralentissements, OOM kill du conteneur
  - GPU saturé → Ollama répond en 5 min au lieu de 2 secondes
  - CPU à 100% → tout est lent, le gateway timeout
```

## Les métriques essentielles

### Disque

```bash
# La métrique la plus critique
df -h /opt/data
# → /dev/sda2  457G   89G  345G   21%  /
# → Si > 80%, agir
```

LEO a 2 disques :
- **SSD** `/dev/sda2` (457 Go) — système + données Hermes
- **HDD** `/dev/sdb2` (1 To) — backups, recovery kit, archives

### RAM

```bash
free -h
# → 22.94 Go total, ~2 Go pour Hermes, ~500 Mo pour n8n
```

Si la RAM utilisée dépasse 85%, les conteneurs Docker risquent l'OOM kill.

### GPU

```bash
nvidia-smi  # Si GPU disponible
```

### Processus

```bash
# Vérifier que tout tourne
docker ps
# → hermes-agent, n8n, ollama : tous UP
```

## Dashboard machines sur LEO

Le dashboard **leo-metrics** affiche en temps réel les métriques du serveur unique :

```markdown
| Métrique  | Valeur |
|:----------|:------:|
| CPU       | 12%    |
| RAM       | 4/22   |
| SSD       | 72/457 |
| HDD       | 42/900 |
| Statut    | 🟢     |
```

Collecte : toutes les heures (cron no_agent, 0€).
Technologie : script bash → JSON → Chart.js → GitHub Pages.

## Alerte automatique

```yaml
Seuils d'alerte:
  Disque > 80%:  🔴 Action immédiate (nettoyage ou extension)
  RAM > 85%:     🟡 Surveillance renforcée
  GPU > 90%:     🟡 Check processus Ollama
  CPU > 90%:     🟡 Vérifier crons en parallèle
```

L'auto-heal détecte ces seuils toutes les 30 minutes.

## 1 machine — le serveur LEO

| Machine | OS | RAM | Stockage | Rôle |
|:--------|:---|:---:|:--------:|:-----|
| **LEO** 🖥️ | Ubuntu 26.04 | 22 Go | 457 Go SSD + 1 To HDD | Serveur unique (toute la plateforme) |

> 💡 Les autres machines (Yoga, Penguin) sont des postes de travail — elles n'hébergent aucun service de la plateforme Hermes.

## Commandes utiles

```bash
# Vue d'ensemble rapide
htop

# Espace disque en temps réel
watch -n 5 df -h /opt/data

# Logs mémoire Docker
docker stats --no-stream

# Température GPU
nvidia-smi
```

---

# Partie VI — Automatisation et Crons

Avec **39 crons Hermes + 6 crons hôte** qui tournent 24h/24 et un auto-fix-daemon `*/5`, LEO est entièrement automatisé. Le dashboard central synthétise tout : 20 KPI, 4 onglets (Synthèse, Analyses, Infra, BAVI), 4 charts Chart.js. Le tout dans **un seul fichier HTML statique** sur GitHub Pages.

---

## Monitoring crons : le tableau de bord des tâches

### Le tableau de bord des crons

```markdown
| Cron              | Statut | Dernière exécution | Prochaine exécution | Actions |
|:------------------|:------:|:------------------:|:-------------------:|:-------:|
| Budget Check      | 🟢     | 07:58:12           | 19:58:12            | OK      |
| Backup GDrive     | 🟢     | 04:00:03           | 04:00:03 (demain)   | OK      |
| Veille IA         | 🟢     | 07:00:15           | 07:00:15 (demain)   | OK      |
| Dashboard LEO     | 🟢     | 07:30:22           | 08:30:22            | OK      |
| Dashboard Machines| 🟢     | 07:30:25           | 08:30:25            | OK      |
| Classifieur Gmail | 🟢     | 07:45:01           | 08:00:01            | OK      |
| Sync Drive GitHub | 🟢     | 18:00:30           | 18:00:30 (demain)   | OK      |
```

### Comment ça marche

```bash
# 1. Collecte des statuts
python3 ~/.hermes/profiles/leo-copilot/scripts/collect_crons_status.py
# → JSON : { "cron_id": { "status": "ok", "last_run": "...", "next_run": "..." } }

# 2. Génération du dashboard
python3 ~/.hermes/profiles/leo-copilot/scripts/deploy-crons-dashboard.py
# → HTML avec Chart.js + tableau

# 3. Push sur GitHub Pages
cd ~/Projets_Dev/crons-dashboard && git push
```

### Indicateurs clés

| Indicateur | Vert | Orange | Rouge |
|:-----------|:----:|:------:|:-----:|
| Taux de succès | >95% | 80-95% | <80% |
| Temps d'exécution | <30s | 30-60s | >60s |
| Dérive horaire | <5min | 5-15min | >15min |
| Erreurs consécutives | 0 | 1-2 | >3 |

## Les crons de LEO

### Horaires (toutes les heures)

```yaml
- Dashboard LEO KPI
- Dashboard Machines
- Dashboard Crons
- Dashboard GitHub
- Dashboard BAVI LEO
- Dashboard n8n
- Dashboard Global
- Budget Check (08:00, 20:00)
```

### Quotidiens

```yaml
- Backup GDrive           → 04:00
- Veille IA               → 07:00
- Sync Drive → GitHub     → 18:00
- Hermes Update Check     → 09:00
- Budget Snapshot         → 23:00
```

### Haute fréquence

```yaml
- Classifieur Gmail       → Toutes les 15 min
- Auto-heal               → Toutes les 30 min
- Dashboard Watch         → Toutes les 2h
- Drive Watch             → Toutes les 6h
```

### Hebdomadaires

```yaml
- Vérification infra      → Lundi 08:00
- Curator (nettoyage)     → Dimanche 04:00
```

## Gérer les erreurs

```bash
# Voir les logs d'un cron
hermes cron log <id>

# Relancer un cron en échec
hermes cron run <id>

# Suspendre un cron défaillant
hermes cron pause <id>

# Voir les erreurs récentes
tail -50 ~/Projets_Dev/logs/errors.log
```

## Auto-heal : correction automatique

Quand un cron échoue, l'auto-heal tente de le corriger :

```text
1. Détection : cron en erreur 2 fois de suite
2. Diagnostic : erreur de permission ? script manquant ? timeout ?
3. Correction : recopie du script, ajustement du timeout, redémarrage
4. Vérification : relance le cron, vérifie le résultat
5. Si échec → issue GitHub (label "auto-heal")
```

En production, l'auto-heal résout ~80% des problèmes sans intervention humaine.

---

# Budget et tracking DeepSeek

LEO coûte environ **1 à 3 euros par mois** à faire fonctionner. Voici les principes pour maîtriser ce budget.

## Le coût réel de LEO (estimation)

```yaml
Budget mensuel LEO (estimé):
  DeepSeek V4 Flash (quotidien):  ~1-2 €
  DeepSeek V4 Pro (analyses):     ~0,50 € (ponctuel)
  Gemini (fallback):                0 € (gratuit)
  Ollama (classification):          0 € (local, CPU)
  GitHub Pages (hébergement):       0 € (gratuit)
  n8n (workflows): ❌ Retiré 13/07/2026
  Total:                           ~1-3 €
```

> Ces chiffres sont des ordres de grandeur. Le solde et la consommation réels sont visibles en temps réel sur le [LEO Dashboard](http://localhost:8765/dashboard).

Le secret de ce coût ridicule : **Ollama pour le gratuit** (classification emails sur CPU), **Flash pour le quotidien** (quelques centimes/jour), **Pro seulement pour le complexe** (ponctuel).

## Triple ventilation

```python
# Ne pas se fier aux logs DeepSeek
# Mesurer le delta de balance
vrai_coût = solde_avant - solde_après

# Ventiler par usage
coûts = {
    "deepseek_flash":  0.05 * jours,    # Usage quotidien
    "deepseek_pro":    0.10 * analyses, # Analyses complexes
    "ollama":           0.00,           # Gratuit
    "gemini":           0.00,           # Gratuit (fallback)
}
```

## Dashboard budget

```markdown
| Métrique              | Valeur                      |
|:---------------------|:----------------------------|
| Provider principal   | DeepSeek Flash (économique)  |
| Provider complexe    | DeepSeek Pro (ponctuel)      |
| Provider gratuit     | Ollama (CPU local)           |
| Fallback             | Gemini (gratuit, quotas)     |
| Coût mensuel estimé  | ~1-3 €                       |
| Veille IA            | ~5-10 cts/jour               |
| Crons                | 0 € (13/14 en no_agent)      |
```

> Les chiffres exacts (solde, dépense quotidienne, jours restants) sont visibles en temps réel sur le [LEO Dashboard](http://localhost:8765/dashboard).

## Alertes

```yaml
Seuils d'alerte:
  Solde < 10€:  🔴 Notification immédiate
  Dépense > 1€/jour: 🟡 Vérifier si anomalie
  Erreur API:        🟡 Fallback Gemini automatique
```

## Comparaison des providers

| Provider | Coût IN (1M tokens) | Coût OUT (1M tokens) | Autonomie ($60) |
|:---------|:-------------------:|:--------------------:|:---------------:|
| DeepSeek Flash | $0.14 | $0.28 | >6 ans |
| DeepSeek Pro | $1.50 | $5.00 | ~2 mois |
| Gemini Flash | **0 €** | **0 €** | ∞ (quotas gratuits) |
| Ollama | **0 €** | **0 €** | ∞ (local) |

---

# Tâches planifiées (crons)

Hermes Agent peut exécuter des actions automatiquement selon un planning. C'est ce qui transforme votre assistant en majordome qui travaille 24/7.

## Principe

```text
Cron = tâche planifiée qui s'exécute automatiquement
     │
     ├── Script pur (no_agent) → Aucun LLM, exécution directe 0$ ✅
     ├── LLM sur Ollama local  → Gratuit (votre machine)
     └── LLM sur provider payant → Coût par exécution 💰
```

## Types de crons

### Script pur (no_agent)

Pour les tâches purement techniques : collecte de données, backup, déploiement.

**Avantage :** zéro token LLM consommé, exécution rapide, **0$** à vie.

```bash
# Créer un cron no_agent
hermes cron create "0 6 * * *" "Backup quotidien" --script mon-script.sh
```

**Bonnes pratiques :**
- Le script doit être dans `~/.hermes/scripts/`
- Exit code 0 = succès, non-zero = échec
- Le script a accès à `stdout` qui est livré à l'utilisateur

### LLM sur Ollama (local, gratuit)

Pour les tâches qui nécessitent de la réflexion, sans coût :

```bash
hermes cron create "0 9 * * 1" "Analyse les logs et résume les erreurs" --name "rapport-hebdo" --model qwen2.5:7b
```

### LLM sur provider payant

À éviter pour les crons récurrents. Si vraiment nécessaire, privilégiez une
fréquence faible (hebdomadaire, pas horaire).

## Planification efficace

### Ordre de grandeur des coûts

| Type de cron | Coût par run | Coût / mois (horaire) |
|-------------|-------------|----------------------|
| no_agent (script) | **0$** | **0$** |
| Ollama local | **0$** | **0$** |
| DeepSeek / Gemini | ~0.001-0.01$ | ~7-70$ |

**Règle LEO :** Tout cron récurrent (toutes les heures/jours) doit être `no_agent`
ou tourner sur Ollama. DeepSeek est réservé aux interactions directes.

### Ordonnancement décalé (staggered)

Quand plusieurs crons tournent à la même fréquence, décalez les minutes pour
éviter l'embouteillage :

```text
H:00 → machines-kpi   (collecte métriques)
H:05 → budget-check   (solde API)
H:10 → dashboard-KPI  (génération HTML)
H:15 → dashboard-machines
H:20 → monitoring-crons
```

Chaque cron a `~5 min` de fenêtre exclusive.

## Configuration d'un cron

### Syntaxe de planification

| Expression | Signification | Usage |
|------------|--------------|-------|
| `0 * * * *` | Toutes les heures à :00 | Collecte métriques |
| `5 * * * *` | Toutes les heures à :05 | Budget |
| `10 * * * *` | Toutes les heures à :10 | Dashboard KPI |
| `0 6 * * *` | Tous les jours à 06:00 | Backup quotidien |
| `0 8 * * 1` | Tous les lundis à 08:00 | Rapport hebdo |
| `0 18 * * *` | Tous les jours à 18:00 | Sync externe |
| `30m` | Toutes les 30 minutes | Monitoring rapide |

### Exemple concret : backup quotidien

```bash
hermes cron create "0 6 * * *" "Backup quotidien" --script run-backup.sh
```

### Exemple concret : dashboard horaire

```bash
hermes cron create "10 * * * *" "Générer le dashboard" --script run-dashboard.sh
```

## Gestion des crons

```bash
# Lister les crons
hermes cron list

# Modifier un cron
hermes cron edit <id> --schedule "every 4h"

# Mettre en pause
hermes cron pause <id>

# Reprendre
hermes cron resume <id>

# Supprimer
hermes cron remove <id>

# Forcer l'exécution immédiate
hermes cron run <id>

# Voir le statut du scheduler
hermes cron status
```

## Surveillance

Hermes Agent enregistre chaque exécution de cron avec :
- Son statut (ok/error)
- Sa sortie (stdout)
- Horodatage

Ces informations sont consultables :

```bash
# Voir les logs d'un cron
cat ~/.hermes/cron/output/<id>/*.md
```

**Astuce LEO :** Créez un **dashboard de monitoring** des crons pour avoir un œil sur l'état de tous vos crons en un coup d'œil. Ce dashboard peut lui-même être mis à jour par un cron horaire.

### 🔍 dashboard-watch — surveillance automatique

Un cron `dashboard-watch` (toutes les 2h) vérifie que tous les dashboards sont à jour :

- **HTTP 200** — chaque dashboard répond
- **Âge < 2h** — données fraîches
- **Budget cohérent** — valeur affichée du budget ≈ `budget.json` (écart max 1$)
- **Redeploiement auto** — si stale ou 404, le script relance le déploiement

Le script est dans `scripts/dashboard-watch.py` et son état est sauvegardé dans `metrics/dashboard-watch-state.json`.

### 🛡️ Auto-Heal — cicatrisation automatique (cron agent, H:45)

Depuis le 21/06/2026, un cron **agent-driven** (pas no_agent) tourne toutes les heures à H:45 pour détecter et corriger automatiquement les problèmes connus :

- **Crons en erreur** → détection via `cronjob list`, diagnostic (PATH `gh`, script cassé, import manquant) et correction auto + execution forcée
- **Dashboard HTTP non-200** → redéploiement immédiat
- **budget-webhook down** → redémarrage automatique
- **Disque plein** → alerte

**Patterns auto-réparables :**
| Pattern | Détection | Correction |
|---------|-----------|------------|
| `gh` introuvable | Stderr "gh: command not found" | Patch avec chemin absolu `~/Projets_Dev/home/.local/bin/gh` |
| Dashboard 404 | HTTP != 200 | Relance le script de déploiement |
| budget-webhook down | Process manquant | Relance via watchdog |
| Import Python cassé | Traceback d'import | pip install dans le venv |

**Rapport :** livré en local (plus sur Telegram). Consultez le **🌍 Global Dashboard** à
http://localhost:8765/dashboard pour tout voir en un coup d'œil.

## Pièges à éviter

### 🔴 Ne pas mettre de LLM sur une tâche purement script

Un cron de collecte de métriques (Python pur) **n'a pas besoin** d'un LLM.
Le LLM dirait juste "j'ai exécuté le script, voici le résultat" — gaspillage
de tokens et d'argent.

### 🔴 Gérer l'identité et le token Git

Si votre cron push sur GitHub, l'environnement cron peut ne pas avoir accès
aux credentials GitHub. Deux solutions :

**Solution 1 — Chemin absolu vers gh :**
```python
import subprocess, os
gh_path = "~/Projets_Dev/home/.local/bin/gh"
tok = os.environ.get("GH_TOKEN")
if not tok:
    tok = subprocess.run([gh_path, "auth", "token"],
        capture_output=True, text=True).stdout.strip()
remote = f"https://user:{tok}@github.com/user/repo.git"
subprocess.run(["git", "remote", "set-url", "origin", remote])
subprocess.run(["git", "push", "origin", "main"])
```

**Solution 2 — Variable d'environnement :**
Définir `GH_TOKEN` dans le script ou l'environnement du cron.

### 🔴 Attention aux chemins dans l'environnement cron

L'environnement d'exécution d'un cron no_agent est minimal. Utilisez des
**chemins absolus** dans vos scripts. Exemple : `/opt/hermes/.venv/bin/python3`
plutôt que `python3`.

### 🔴 Cross-device move

Dans un script cron, ne pas utiliser `Path.rename()` entre `/tmp/` et
`~/Projets_Dev/` — ces répertoires sont souvent sur des filesystems différents.
Utilisez `shutil.move()`.

```python
# ❌ Ne fait pas
tmp.rename(local_path)

# ✅ Fait
import shutil
shutil.move(str(tmp), str(local_path))
```

### 🔴 Vérifier les sorties

Un cron no_agent qui exit 0 mais ne fait rien est silencieux. Pour les
tâches critiques, faites en sorte qu'il produise une sortie utile pour
confirmer que le travail a été fait.

### Pour aller plus loin

- Voir `03-utilisation/dashboards.md` pour le monitoring
- Voir `exemples/LEO.md` pour l'architecture cron complète

---

# Crons horaires : métriques, KPI, dashboards

Les crons horaires sont la cheville ouvrière de LEO. Ils tournent 24h/24 et maintiennent les dashboards à jour sans intervention humaine.

## Principe

Un cron horaire = un script no_agent = **0 € par exécution**.

```bash
hermes cron create \
  --name "Dashboard Machines" \
  --schedule "0 * * * *" \
  --script ~/.hermes/profiles/leo-copilot/scripts/update_machines_kpi.py \
  --no-agent
```

Le flag `--no-agent` est essentiel : sans LLM, l'exécution est gratuite.

## Les crons horaires de LEO

```yaml
Toutes les heures (minute 0):
  - Dashboard LEO KPI      → collecte sessions, tokens, budget
  - Dashboard Machines     → CPU, RAM, disque 3 machines
  - Dashboard Crons        → statut 39 crons
  - Dashboard GitHub       → activité repos
  - Dashboard BAVI LEO     → KPIs voyages

Toutes les 30 minutes (minute 30):
  - Auto-heal              → vérification santé système
  - Classifieur Gmail      → nouveaux emails (aussi toutes les 15 min)

Toutes les 15 minutes:
  - Classifieur Gmail      → scan boîte de réception
```

## Staggering (évitement de conflit)

Quand plusieurs crons tournent à la même minute, ils peuvent entrer en conflit (API rate limit, CPU saturé). La solution : **staggering**.

```yaml
# Au lieu de tout lancer à H:00
H:00 → Dashboard LEO KPI
H:05 → Dashboard Machines
H:10 → Dashboard Crons
H:15 → Dashboard GitHub
H:20 → Dashboard BAVI LEO
H:25 → Dashboard n8n
H:30 → Auto-heal
```

Chaque cron démarre 5 minutes après le précédent. Les pics de charge sont lissés.

## Script typique

```python
#!/usr/bin/env python3
# update_machines_kpi.py
import json, subprocess

# Collecte
result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
disk_usage = result.stdout.split("\n")[1].split()[4]

result = subprocess.run(["free", "-h"], capture_output=True, text=True)
ram_usage = result.stdout.split("\n")[1].split()[2]

# Génération HTML
html = f"""<!DOCTYPE html>
<html>
<head><title>Machines</title></head>
<body>
  <h1>🖥️ Machines</h1>
  <p>Disque: {disk_usage} | RAM: {ram_usage}</p>
</body>
</html>"""

# Sauvegarde
with open("/tmp/dashboard-machines.html", "w") as f:
    f.write(html)
```

## Vérification

```bash
# Voir les logs du cron
tail -20 ~/.hermes/profiles/leo-copilot/logs/agent.log

# Vérifier le dashboard en ligne
curl -s https://user.github.io/leo-metrics/ | head -5
```

---

# Crons quotidiens : backup, veille IA, sync

Les crons quotidiens sont les tâches lourdes qui s'exécutent une fois par jour. Backup, veille IA, synchronisation — le ménage automatisé.

## Les crons quotidiens de LEO

```yaml
04:00 — Backup → GDrive
  Action: Archive tous les profils + config → Google Drive
  Rétention: 7 jours
  Coût: 0 € (no_agent)
  Script: ~/.hermes/profiles/leo-copilot/scripts/hermes-backup.py

07:00 — Veille IA
  Action: Collecte 15 sources RSS → analyse DeepSeek → email
  Coût: ~0,05 €/jour (agent LLM)
  Durée: ~2 minutes

09:00 — Hermes Update Check
  Action: Vérifie si une nouvelle version d'Hermes est disponible
  Coût: 0 € (no_agent)

18:00 — Sync Drive → GitHub
  Action: Miroir bidirectionnel Google Drive ↔ GitHub
  Coût: 0 € (no_agent)

23:00 — Budget Snapshot
  Action: Sauvegarde du budget quotidien dans l'historique
  Coût: 0 € (no_agent)
```

## Backup quotidien

```yaml
Ce qui est sauvegardé:
  - profiles/default/       → config, SOUL, .env
  - profiles/leo-copilot/   → config, crons, mémoire, skills
  - profiles/bavi-leo/      → config, mémoire, roadbooks
  - profiles/emile/         → config, SOUL, .env
  - memories/               → MEMORY.md, USER.md (partagés)
  - scripts/                → tous les scripts customs
  - sessions/               → historique des conversations
  - .env                    → tokens et clés API
  - config.yaml             → configuration globale
  - credentials_vault.json  → coffre-fort des credentials

Destination:
  - Local: ~/.hermes/backups/
  - Cloud: Google Drive (Hermes_Christophe/backups/)
  
Rétention: 7 jours
Taille moyenne: ~40-70 MB
```

## Veille IA quotidienne

```yaml
Processus:
  1. Collecte RSS (15 sources, ~50 articles)
  2. DeepSeek V4 Flash analyse chaque article
  3. Sélection des 15 plus pertinents
  4. Rédaction du rapport formaté
  5. Envoi par email à christophe.danhier@gmail.com

Coût: ~0,05 €/jour = ~1,50 €/mois
Tags: ALERTE, NOUVEAU, À SUIVRE, CONFORMITÉ, TENDANCE
```

## Synchronisation Drive → GitHub

```yaml
Fonctionnement:
  - Scanne les dossiers Google Drive partagés
  - Détecte les nouveaux fichiers .docx ou .md
  - Convertit les .docx en .md
  - Commit + push sur le wiki GitHub correspondant

Wikis synchronisés:
  - BAVI_LEO ↔ Drive (docs bureaux)
  - voyages-wiki ↔ Drive (roadbooks)
  - emile-wiki ↔ Drive (brouillons mémoire)
```

## Planification avec cron

```yaml
# Format: minute heure jour mois jour_semaine
0 4 * * *   → Tous les jours à 04:00
0 7 * * *   → Tous les jours à 07:00
0 9 * * *   → Tous les jours à 09:00
0 18 * * *  → Tous les jours à 18:00
0 23 * * *  → Tous les jours à 23:00
```

---

# Watchdogs et alertes

Les watchdogs sont des scripts qui surveillent en continu l'état des services et alertent en cas de problème. C'est le système immunitaire de LEO.

## Principe

Un watchdog = un script qui tourne régulièrement et vérifie qu'un service répond.

```bash
# Watchdog typique
#!/bin/bash
# Vérifie que n8n répond
if ! curl -s http://localhost:5678/healthz > /dev/null; then
    echo "❌ n8n ne répond pas"
    # Tentative de redémarrage
    docker restart n8n
    # Notification
    hermes memory add "n8n relancé le $(date)" --target memory
fi
```

## Les watchdogs de LEO

```yaml
Toutes les 30 minutes:
  - 🩺 Auto-heal complet       → crons, Ollama, Docker, disque, tokens (n8n retiré)
  - 📧 Classifieur Gmail       → nouveaux emails à classer

Toutes les 2 heures:
  - 📊 Dashboard Watch         → vérifie que le dashboard répond
  - 🔄 Dashboard redeploy      → redéploie si un dashboard est obsolète

Toutes les 6 heures:
  - 🔭 Drive Watch             → détecte les changements dans Google Drive

Tous les jours:
  - 🤖 Hermes Update Check     → nouvelle version disponible ?
  - 💰 Budget Check            → solde suffisant ?
```

## Auto-heal : le watchdog principal

```yaml
Vérifications:
  ✅ Crons:        44/44 OK ?
  ✅ Ollama:       qwen2.5:7b responsive ?
  ✅ n8n:          healthz 200 ?
  ✅ Docker:       3/3 conteneurs UP ?
  ✅ Disque:       < 80% utilisé ?
  ✅ Token LEO:    Google API OK ?
  ❌ Token Christophe: invalid_grant (à ré-autoriser manuellement)

En cas d'échec:
  1. Tentative de correction automatique
  2. Si réussi → log + continue
  3. Si échec → issue GitHub (label auto-heal)
```

## Dashboard Watch

Le Dashboard Watch vérifie que le dashboard LEO est en ligne et à jour :

```bash
# Vérification unique
curl -s -o /dev/null -w "%{http_code}" http://localhost:8765/dashboard
# → 200
```

## Notifications

```yaml
Canaux de notification:
  - Telegram DM      → alertes critiques (disque, budget, panne)
  - GitHub Issues    → problèmes non critiques (auto-heal, watchdogs)
  - Dashboard        → tous les statuts en temps réel
  
Règles:
  - Une alerte = une issue GitHub
  - Label "auto-heal" si corrigé automatiquement
  - Pas de spam : pas de notification pour les succès
```

---

# Drive ↔ GitHub sync

La synchronisation entre Google Drive et GitHub est le pont qui relie les documents collaboratifs à la documentation publiée.

## Pourquoi synchroniser ?

```yaml
Google Drive:
  - Écriture collaborative (Google Docs)
  - Accessible depuis n'importe quel appareil
  - Versionnage basique

GitHub Pages:
  - Publication publique et élégante
  - Versionnage professionnel (git)
  - Déploiement automatique (MkDocs)

Le sync = le meilleur des deux mondes
```

## Fonctionnement

```text
Google Docs
     │
     ▼
Drive Watch (toutes les 6h)
     │
     ▼
Conversion .docx → .md
     │
     ▼
Git add + commit + push
     │
     ▼
GitHub Pages (déploiement automatique)
     │
     ▼
Wiki en ligne 🌐
```

## Script de synchronisation

```bash
#!/bin/bash
# drive-sync.sh

# 1. Scanne les dossiers Drive partagés
python3 ~/.hermes/profiles/leo-copilot/scripts/drive-sync.py --scan

# 2. Détecte les nouveaux fichiers
python3 ~/.hermes/profiles/leo-copilot/scripts/drive-sync.py --diff

# 3. Convertit les .docx en .md
python3 ~/.hermes/profiles/leo-copilot/scripts/drive-sync.py --convert

# 4. Commit + push
cd ~/Projets_Dev/BAVI_LEO && git add -A && git commit -m "sync Drive $(date +%Y-%m-%d)" && git push
cd ~/Projets_Dev/voyages-wiki && git add -A && git commit -m "sync Drive $(date +%Y-%m-%d)" && git push
cd ~/Projets_Dev/emile-wiki && git add -A && git commit -m "sync Drive $(date +%Y-%m-%d)" && git push
```

## Wikis synchronisés

| Wiki | Dossier Drive | Usage |
|:-----|:--------------|:------|
| **BAVI_LEO** | `Hermes_Christophe/BAVI/` | Documentation bureaux |
| **voyages-wiki** | `Hermes_Christophe/Voyages/` | Roadbooks camping-car |
| **emile-wiki** | `bavi/bureau-emile/` | Mémoire universitaire |

## Résolution de conflits

```yaml
Règle: GitHub gagne en cas de conflit.
  - Drive est la source des nouveaux documents
  - GitHub est la source de vérité pour les modifications existantes
  - En cas de modification simultanée : version GitHub prioritaire
```

## Voir aussi

- **Ch.12** : Bureau Sylvia (publication des roadbooks)
- **Ch.13** : Bureau Émile (sync des brouillons)
- **Ch.17** : Skills productivité

---

> *Parties V et VI terminées — Prochaine étape : [Partie VII — La Partie des Dix](06-partie-des-dix.md)*

---

*Document mis à jour le 18/07/2026 à 13:00 — Léo 🦁 | v5.0*

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)

