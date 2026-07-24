---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v5.0
modele: deepseek-v4-flash
tags: [hermes, guide, demarrage, debutant, troubleshooting, installation]
statut: ✅ À jour
type: extraction-source
hide:
  - toc
---

> **Dernière mise à jour rédactionnelle :** 18/07/2026 à 12:30 — Léo 🦁
> **Source :** Hermès pour les Nuls — Annexe B + Problèmes courants

# Guide de démarrage rapide 🚀

> *Installer Hermès et parler à son premier agent en 60 secondes*

---

## Installation

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

## Premier chat

```bash
hermes chat -q "Bonjour, que peux-tu faire ?"
```

## Connexion Telegram

```bash
# 1. Créez un bot avec @BotFather sur Telegram
# 2. Récupérez le token
# 3. Configurez Hermes
hermes gateway setup
```

## Commandes essentielles

| Commande | Action |
|:---------|:-------|
| `hermes` | Lancer en mode interactif |
| `hermes doctor` | Diagnostic complet |
| `hermes model` | Changer de modèle/provider |
| `hermes tools list` | Voir les outils disponibles |
| `hermes skills list` | Voir les skills installés |
| `hermes cron list` | Voir les crons actifs |
| `hermes gateway status` | Voir le statut du gateway |
| `hermes profile list` | Voir les profils |

## Slash commands utiles

En session interactive :

| Commande | Effet |
|:---------|:-------|
| `/new` | Nouvelle session |
| `/retry` | Renvoyer la dernière requête |
| `/undo` | Annuler le dernier échange |
| `/title mon-sujet` | Nommer la session |
| `/skill nom` | Charger un skill |
| `/platforms` | Statut des plateformes |
| `/help` | Liste complète |

## Syntaxe cron rapide

```text
0 6 * * *      → Tous les jours à 6h
30m            → Toutes les 30 min
every 2h       → Toutes les 2h
every monday 9am → Tous les lundis 9h
```

> 🔗 **Documentation complète :** [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)

---

# Problèmes courants et solutions 🔧

## Installation

### `pip install` échoue (installation manuelle)

```text
ERROR: Could not find a version that satisfies the requirement...
```

**Causes possibles :**
- Python < 3.11
- Venv non activé
- Pip obsolète

**Note :** La méthode recommandée est le script d'installation officiel :
```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Solutions (installation manuelle) :**
```bash
# Vérifier la version Python
python3 --version  # Doit être 3.11+

# Mettre à jour pip
python3 -m pip install --upgrade pip

# Réinstaller dans le venv
source .venv/bin/activate
pip install -e .
```

### `hermes doctor` signale des erreurs

```text
✗ Gateway telegram: bot token not configured
✗ Profile default: provider unreachable
```

**Solutions :** Suivez les indications de `hermes doctor` — il diagnostique précisément ce qui manque.

## Communication

### L'assistant ne répond pas sur Telegram

1. Vérifiez que le gateway tourne : `hermes gateway status`
2. Redémarrez le gateway : `hermes gateway restart`
3. Vérifiez le token bot Telegram (dans config.yaml)
4. Vérifiez que votre user ID est dans `allowed_users`

### Perte de session

Si votre assistant perd sa session (contexte précédent), c'est normal :
- Chaque nouvelle conversation est une session fraîche
- Les informations durables doivent être stockées dans les **skills** ou la **mémoire**
- Utilisez `hermes sessions list` ou `hermes sessions browse` pour voir les sessions récentes

## Crons

### Un cron en no_agent échoue sans raison

**Cause la plus fréquente :** l'environnement minimal du cron.

**Solutions :**
- Utilisez des chemins **absolus** dans vos scripts
- Utilisez un wrapper shell qui appelle le bon interpréteur
- Testez le script manuellement depuis le même environnement

### Un cron LLM-driven est lent

**Causes :**
- Le modèle choisi est trop lourd pour la tâche
- Le prompt est trop long (contexte volumineux)

**Solutions :**
- Utilisez un modèle plus petit (qwen2.5:7b au lieu de qwen2.5:32b)
- Allumez le GPU si disponible
- Passez en no_agent si la tâche n'a pas vraiment besoin de LLM

### Cron jamais exécuté (last_run_at = null)

**Causes :**
- Le cron a été créé mais n'a pas encore atteint son premier déclenchement
- Le cron est en pause
- Le scheduler Hermes ne tourne pas

**Vérifier :** `hermes cron list` montre tous les crons avec leur prochain run.

## Google Sheets / Drive

### Erreur 403 "The caller does not have permission"

**Cause :** Le compte OAuth utilisé n'a pas accès au document.

**Solution :** Partagez le document (sheet ou dossier) avec l'adresse email associée au token OAuth de votre assistant.

### Token OAuth expiré

Si le refresh_token ne fonctionne plus :
1. Obtenez un nouveau token via le flow OAuth
2. Mettez à jour le fichier token de votre assistant
3. (Alternative) Utilisez un compte de service Google

## GitHub Pages

### "Your current plan does not support GitHub Pages"

GitHub Pages gratuit ne fonctionne que sur les dépôts **publics**.

**Solution :** Rendez le dépôt public (les dashboards ne contiennent pas de données sensibles). Si le dépôt doit rester privé, trouvez une autre solution d'hébergement.

### "Author identity unknown" sur git commit

L'environnement minimal du cron ne connaît pas l'identité Git.

**Solution :** Configurez explicitement dans votre script ou wrapper :

```bash
git -C /tmp/repo config user.name "MonAssistant"
git -C /tmp/repo config user.email "assistant@exemple.com"
```

### "Could not read Username" sur git push

Pas de TTY pour l'authentification dans un cron.

**Solution :** Passez le token GitHub directement dans l'URL du remote.

## Ollama

### Ollama ne répond pas

```bash
curl: (7) Failed to connect to localhost port 11434: Connection refused
```

**Solutions :**
1. Vérifiez qu'Ollama tourne : `systemctl status ollama` ou `ollama serve`
2. Vérifiez le port : `ss -tlnp | grep 11434`
3. Démarrez Ollama : `ollama serve` (ou `sudo systemctl start ollama`)

### Modèle introuvable sur Ollama (qwen2.5:7b)

```bash
curl http://localhost:11434/api/tags  # Liste les modèles disponibles
ollama pull qwen2.5:7b               # Télécharger le modèle
```

Les noms exacts des modèles sont importants — utilisez ceux listés par `ollama list` ou l'API tags.

## Divers

### Message "Broken pipe" dans un cron

Un `Broken pipe` (Errno 32) se produit quand la sortie du processus est trop volumineuse pour le pipeline.

**Solutions :**
- Réduisez la sortie de votre script
- Passez en no_agent (script direct)
- Si le script produit une sortie utile, écrivez-la dans un fichier plutôt que stdout

### "Stop" non respecté

Si vous dites "stop" à votre assistant et qu'il continue, rappelez-lui la règle : "stop" est définitif. Si le problème persiste, une nouvelle session (`/reset`) peut être nécessaire.

## Contribuer à ce guide

Vous avez rencontré un problème non listé ? Ouvrez une issue sur le [dépôt GitHub](https://github.com/christophedanhier-hash/hermes-guide) — ce guide est vivant.

---

*Document mis à jour le 18/07/2026 à 12:30 — Léo 🦁 | v5.0*

> 🤖 Dernier audit : 24/07/2026 à 11:28 (UTC+2)
