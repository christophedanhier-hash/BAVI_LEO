---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v5.0
modele: deepseek-v4-flash
tags: [hermes, guide, documentation, dix-erreurs, commandes, extensions, ressources, bavi]
statut: ✅ À jour
type: guide
hide:
  - toc
---

> **Dernière mise à jour rédactionnelle :** 18/07/2026 à 12:30 — Léo 🦁
> **Dernier commit :** `f6da9c7` — 18/07/2026 à 12:18

# Partie VII : La partie des Dix 🎯

> **10 erreurs évitées, 10 commandes essentielles, 10 façons d'étendre Hermès, 10 ressources pour aller plus loin.**

---

## 10 erreurs à ne pas faire

Les pièges les plus courants rencontrés avec Hermes Agent — et comment les éviter.

### 1. `hermes` n'est pas dans le PATH

```bash
# ❌ Ça ne marche pas
hermes chat

# ✅ Ça marche
/opt/hermes/.venv/bin/hermes chat

# ✅ Solution : créer un alias
alias hermes='/opt/hermes/.venv/bin/hermes'
```

### 2. Les tokens .env sont fragiles

Le moindre caractère spécial (`$`, `!`, `&`) dans un fichier `.env` peut casser le gateway. Toujours utiliser des guillemets :

```bash
# ❌ Problème si le token contient $ ou !
TELEGRAM_BOT_TOKEN=abc$def

# ✅ Sécurisé
TELEGRAM_BOT_TOKEN="abc$def"
```

### 3. s6-svstat DOWN ne veut pas dire mort

```bash
# ❌ s6 dit DOWN mais le processus tourne
s6-svstat /run/service/gateway-default
# → down (faux négatif)

# ✅ Vérifier les processus
ps aux | grep hermes.*gateway
```

`s6-svstat` peut retourner `down` même quand le processus est actif. Toujours vérifier avec `ps`.

### 4. Le contexte DeepSeek est limité à 128K tokens

Si votre conversation ou document dépasse 128K tokens, DeepSeek plante.

```yaml
# Solution : fallback Gemini (1M tokens, gratuit)
fallback_providers: '[{"provider": "gemini", "model": "gemini-3.5-flash"}]'
```

Gemini a un contexte 8 fois plus grand — parfait pour les longs documents.

### 5. Ne jamais réappliquer les labels Gmail

```python
# ❌ DANGER : réappliquer les labels en masse
# → Des milliers d'emails re-classifiés, pagaille assurée

# ✅ Règle d'or
if email.already_labeled:
    pass  # Ne pas toucher
```

Les labels Gmail sont appliqués une seule fois. Passé ce cap, on n'y touche plus.

### 6. Budget DeepSeek : mesurer le delta, pas les logs

Les logs DeepSeek ne reflètent pas toujours le coût réel. Utilisez le **delta de balance** :

```python
# ✅ Fiable
vrai_coût = solde_avant - solde_après

# ❌ Pas fiable
cout_logs = somme(prix_token * tokens)
```

### 7. Les symlinks dans scripts/ sont refusés

Hermes v0.17.0 refuse les liens symboliques dans le dossier `scripts/`.

```bash
# ❌ Symlink refusé
ln -s ~/.hermes/profiles/leo-copilot/scripts/backup.py ~/.hermes/profiles/leo-copilot/scripts/backup.py

# ✅ Copie réelle
cp ~/.hermes/profiles/leo-copilot/scripts/backup.py ~/.hermes/profiles/leo-copilot/scripts/backup.py
```

### 8. Toujours vérifier avant de livrer

```bash
# Règle absolue : vérifier AVANT de dire "c'est fait"
curl -s -o /dev/null -w "%{http_code}" https://mon-site.com
# → 200 ✅

grep "version: 2.0" ~/Projets_Dev/config.yaml
# → trouvé ✅
```

Ne jamais faire confiance à "ça devrait marcher". Vérifiez.

### 9. Un backup qui n'est pas testé n'existe pas

```bash
# Vérifier le contenu du backup
tar -tzf ~/.hermes/backups/leo-backup-*.tar.gz | head -20

# Simuler une restauration
tar -xzf ~/.hermes/backups/leo-backup-*.tar.gz -C /tmp/test-restore
```

Testez vos backups. Le jour où vous en avez besoin, il est trop tard pour découvrir qu'ils sont vides.

### 10. Documentez vos pièges

Quand vous passez 2 heures à résoudre un problème, **notez-le dans un skill**. La prochaine fois, ce sera 5 minutes.

```markdown
## Pièges
- Le port 5678 de n8n n'est accessible que via Tailscale
- Après un kill du gateway, attendre 30s avant de relancer
- La clé API DeepSeek est dans le .env du profil, pas le global
```

La documentation, c'est comme l'humour : c'est mieux avec un peu d'avance.

---

## 10 commandes à connaître absolument

Les commandes essentielles pour utiliser Hermes au quotidien.

### 1. Lancer le gateway

```bash
hermes gateway run --replace
```

Démarre le gateway Telegram. Le flag `--replace` tue l'ancienne instance avant de lancer la nouvelle.

### 2. Créer un profil

```bash
hermes profile create mon-profil
```

Crée un profil Hermes isolé, avec son propre bot Telegram, sa mémoire, ses skills et ses crons.

### 3. Utiliser un profil spécifique

```bash
hermes -p mon-profil chat
```

Lance une session chat avec le profil `mon-profil`. Utile pour basculer entre Léo, Michel, Sylvia ou Émile.

### 4. Lister les crons

```bash
hermes cron list
```

Affiche toutes les tâches planifiées, leur état, leur prochaine exécution.

### 5. Créer un cron no_agent (gratuit)

```bash
hermes cron create \
  --name "Vérification disque" \
  --schedule "0 8 * * *" \
  --script ~/.hermes/profiles/leo-copilot/scripts/check-disk.sh \
  --no-agent
```

Le flag `--no-agent` = pas de LLM = **0€ par exécution**.

### 6. Voir les logs du gateway

```bash
tail -f ~/Projets_Dev/logs/gateway.log
```

Indispensable pour comprendre pourquoi le bot ne répond pas, ou debugger une connexion Telegram.

### 7. Modifier la configuration

```bash
hermes config set model.default deepseek-v4-pro
hermes config set display.language fr
```

Modifie le `config.yaml` du profil courant sans éditer le fichier à la main.

### 8. Sauvegarder un fait en mémoire

```bash
hermes memory add "Le serveur est à Bruxelles" --target memory
hermes memory add "Christophe préfère le style concis" --target user
```

`--target memory` = pour le système. `--target user` = pour le profil utilisateur.

### 9. Lister les skills

```bash
hermes skills list
```

Affiche tous les skills disponibles. Vous pouvez charger le détail avec `hermes skills show <nom>`.

### 10. Forcer une exécution de cron

```bash
hermes cron run <id-du-cron>
```

Exécute immédiatement une tâche planifiée, sans attendre son horaire. Utile pour tester un nouveau cron.

### Bonus : la commande magique

```bash
# Tout reconstruire après un crash
# 1. Restaurer le backup GDrive
# 2. Lancer les gateways
hermes gateway run --replace                    # Léo
hermes -p leo-copilot gateway run --replace     # Michel
hermes -p bavi-leo gateway run --replace        # Sylvia
hermes -p emile gateway run --replace           # Émile
```

---

## 10 façons d'étendre son Hermès

Hermes Agent est conçu pour être extensible. Voici 10 pistes pour aller plus loin.

### 1. Ajouter un LLM local (Ollama)

```yaml
# Économisez 100% sur les tâches simples
model:
  default: ollama
  provider: ollama
  base_url: http://localhost:11434
```

Ollama + Qwen2.5-7B = classification d'emails gratuite, prototypage rapide, confidentialité totale.

### 2. Créer un bot spécialisé

Un bot par domaine : voyage, finances, documentation, pédagogie. Chacun avec son propre profil, son propre token Telegram, sa propre mémoire.

```bash
hermes profile create bot-voyages
hermes -p bot-voyages config set model.default deepseek-v4-flash
hermes -p bot-voyages gateway run --replace
```

### 3. Connecter Discord

```yaml
# config.yaml
discord:
  enabled: true
  token: VOTRE_TOKEN_DISCORD
```

Hermes peut répondre dans vos serveurs Discord. Utile pour les équipes.

### 4. Automatiser avec n8n (⚠️ Historique / Obsolète)

> **Note :** n8n est désormais déprécié dans l'écosystème LEO depuis la v5.0. Les workflows n8n ont été migrés vers des crons Hermes natifs et des scripts Python autonomes. Cette section est conservée à titre historique.

n8n connectait Hermes à 400+ services : email, calendrier, CRM, bases de données, webhooks.

```bash
# Workflow exemple (historique)
Trigger: Réception email → Action: Classifier avec Hermes → Sortie: Label Gmail
```

**Alternatives actuelles :** crons Hermes (`--no-agent` pour le gratuit), scripts Python, webhooks natifs.

### 5. Dashboard temps réel

Des dashboards HTML statiques déployés sur GitHub Pages, mis à jour par des crons :

```bash
python3 ~/.hermes/profiles/leo-copilot/scripts/update_mon_dashboard.py
cd mon-dashboard && git push
# → En ligne en 30 secondes
```

### 6. Synchronisation Drive ↔ GitHub

```bash
# Cron toutes les 6h
python3 ~/.hermes/profiles/leo-copilot/scripts/drive-sync.sh
# Google Docs → Markdown → Wiki GitHub Pages
```

Les documents Google sont automatiquement convertis en pages de wiki.

### 7. Skills personnalisés

```bash
mkdir -p ~/.hermes/skills/mes-skills/mon-automatisation/
```

Écrivez vos propres skills en Markdown. Voir le Ch.21 pour le guide complet.

### 8. Partage de mémoire entre profils

```bash
ln -s ~/.hermes/memories/MEMORY.md ~/.hermes/profiles/mon-profil/memories/MEMORY.md
```

Tous vos bots partagent la même mémoire. Ce que l'un apprend, les autres le savent.

### 9. Multi-modèles (routage intelligent)

```yaml
fallback_providers: '[{"provider": "gemini", "model": "gemini-3.5-flash"}]'
```

DeepSeek pour le quotidien, Gemini pour les longs contextes (1M tokens), Ollama pour le gratuit. Le meilleur des trois mondes.

### 10. Ajouter une plateforme de messagerie

Hermes supporte : **Telegram**, **Discord**, **WhatsApp**, **Slack**, **Signal**, **Microsoft Teams**, **Google Chat**.

```yaml
# Exemple : activer WhatsApp
whatsapp:
  access_token: VOTRE_TOKEN
  phone_number_id: "..."
```

Chaque plateforme peut avoir son propre ensemble de commandes et de permissions.

---

## 10 ressources pour aller plus loin

Pour continuer votre voyage avec Hermes Agent.

### 1. La documentation officielle

🌐 **hermes-agent.nousresearch.com/docs**

La documentation officielle d'Hermes Agent. Toutes les configs, tous les providers, toutes les options. La référence absolue.

### 2. Le dépôt GitHub

📦 **github.com/nousresearch/hermes-agent**

Le code source, les issues, les discussions. Idéal pour suivre les évolutions, signaler des bugs, ou contribuer.

### 3. Le wiki BAVI LEO

🌐 **christophedanhier-hash.github.io/BAVI_LEO**

La documentation complète de l'écosystème LEO : 10 bureaux, 117 skills, 39 crons, 1 dashboard central. La preuve que Hermes peut gérer un assistant IA complet.

### 4. Le guide Hermès pour les Nuls

🌐 **christophedanhier-hash.github.io/hermes-guide**

Le livre que vous êtes en train de lire. Mis à jour régulièrement avec les nouvelles parties et les retours d'expérience de LEO.

### 5. GitHub Pages

🌐 **pages.github.com**

Hébergement gratuit pour wikis, dashboards, sites statiques. Utilisé par LEO pour ses 5 wikis et son dashboard central. Zéro backend, zéro coût.

### 6. DeepSeek API

🌐 **platform.deepseek.com**

Le provider principal de LEO. Excellent rapport qualité/prix. Compte gratuit avec crédits de démarrage.

### 7. Ollama

🌐 **ollama.com**

LLM local, gratuit, open-source. Parfait pour la classification, le prototypage, les tâches privées. Utilisé par LEO pour le classifieur Gmail (0€/mois).

### 8. n8n (⚠️ Historique / Obsolète)

🌐 **n8n.io** (self-hosted)

> **Note :** n8n a été déprécié dans l'écosystème LEO depuis la v5.0. Cette référence est conservée à titre historique.

Automatisation low-code, 400+ intégrations. Alternative open-source à Zapier. Hébergé sur LEO pour les workflows de notification, sync et vérification. **Désormais remplacé par des crons Hermes natifs et scripts Python.**

### 9. MkDocs

🌐 **mkdocs.org**

Générateur de documentation statique. Transforme du Markdown en site web élégant. Utilisé par tous les wikis LEO.

### 10. Chart.js

🌐 **chartjs.org**

Bibliothèque de graphiques JavaScript. Légère, flexible, gratuite. Utilisée par tous les dashboards LEO.

### Bonus : la communauté

🌐 **Discord Nous Research** (lien sur le repo GitHub)

Le meilleur endroit pour poser des questions, partager vos réalisations, et rencontrer d'autres utilisateurs d'Hermes Agent.

---

*Fin de la Partie VII — La partie des Dix.*

---

*Document mis à jour le 18/07/2026 à 13:00 — Léo 🦁 | v5.0*

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)

