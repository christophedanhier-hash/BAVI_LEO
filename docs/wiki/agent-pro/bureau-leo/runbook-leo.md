# 🛡️ LEO Runbook — Procédures d'urgence
> Dernière mise à jour : 2026-07-11
> Accessible sur GDrive : Hermes_Christophe/runbook/

---

## 🚨 EN CAS DE PANNE GÉNÉRALE

Si tout est down, suis ces étapes dans l'ordre :

### 1. Vérifier si la machine est UP
```bash
ping 100.92.102.28
ssh tofdan@100.92.102.28
```

### 2. Vérifier l'état général
```bash
cd /home/tofdan/.hermes
python3 profiles/leo-copilot/scripts/leo-health-check.py
```

---

## 🔄 REDÉMARRER LES GATEWAYS

### Léo Hermès (default) — profil principal
```bash
cd /home/tofdan/.hermes
python -m hermes_cli.main gateway run &
```

### Michel — chef infra
```bash
cd /home/tofdan/.hermes
hermes -p leo-copilot gateway run --replace &
```

### BAVI Léo / Sylvia — voyages
```bash
cd /home/tofdan/.hermes
hermes -p bavi-leo gateway run --replace &
```

### Émile — mémoire/pédagogie
```bash
cd /home/tofdan/.hermes
hermes -p emile gateway run --replace &
```

---

## 📊 REDÉMARRER LE DASHBOARD

```bash
cd /home/tofdan/Projets_Dev/BAVI_LEO
pkill -f "uvicorn server:app"
/home/tofdan/.hermes/venv/bin/uvicorn server:app --host 0.0.0.0 --port 8765 &
```

URL : `http://100.92.102.28:8765/dashboard?token=leo-panel-2026`

---

## 🔧 REDÉMARRER N8N

```bash
docker restart n8n
# ou
docker start n8n
```

---

## 🌐 PROBLÈMES RÉSEAU

### Vérifier Tailscale
```bash
tailscale status
```

### Relancer Tailscale si down
```bash
sudo tailscale up
```

---

## 💾 RESTAURATION COMPLÈTE DEPUIS BACKUP

### Étape 1 : Récupérer le backup depuis GDrive
Le backup quotidien est dans `Hermes_Christophe/backups/leo-full-backup-AAAA-MM-JJ.tar.gz`

### Étape 2 : Restaurer
```bash
cd /tmp
# Télécharger le backup depuis GDrive (via rclone ou manuellement)
tar -xzf leo-full-backup-2026-07-XX.tar.gz
cp -r profiles/ /home/tofdan/.hermes/
cp -r vault-*/ /home/tofdan/.hermes/
cp -r memories/ /home/tofdan/.hermes/
cp .env config.yaml credentials_vault.json /home/tofdan/.hermes/
cp -r skills/ scripts/ metrics/ /home/tofdan/.hermes/
cp state.db /home/tofdan/.hermes/
```

### Étape 3 : Redémarrer les gateways (voir section ci-dessus)

---

## 📋 VÉRIFICATIONS RAPIDES

```bash
# Gateways UP ?
ps aux | grep -E "gateway run" | grep -v grep

# Dashboard répond ?
curl -s -o /dev/null -w "%{http_code}" http://localhost:8765/

# n8n répond ?
curl -s http://localhost:5678/healthz

# Crons OK ?
cd /home/tofdan/.hermes
hermes -p leo-copilot cron list | grep -c "ok"

# Espace disque
df -h /
```

---

## 📁 FICHIERS CRITIQUES

| Fichier | Emplacement |
|---------|-------------|
| .env (tokens) | `/home/tofdan/.hermes/.env` |
| Config Hermes | `/home/tofdan/.hermes/config.yaml` |
| Credentials vault | `/home/tofdan/.hermes/credentials_vault.json` |
| Health state | `/home/tofdan/.hermes/metrics/health-state.json` |
| Cron jobs | `/home/tofdan/.hermes/profiles/leo-copilot/cron/jobs.json` |
| Dashboard builder | `/home/tofdan/Projets_Dev/BAVI_LEO/dashboard_builder.py` |
| Dashboard server | `/home/tofdan/Projets_Dev/BAVI_LEO/server.py` |
| Vaults Obsidian | `/home/tofdan/.hermes/vault-leo/` (×4) |

---

## 🩺 WATCHDOGS ACTIFS (vérification auto)

| Watchdog | Fréquence | Action |
|----------|-----------|--------|
| Dashboard Server | 2 min | Redémarre si down |
| BAVI Server | 5 min | Redémarre si down |
| GitHub Actions | 15 min | Alerte si erreur |
| Cron Health | 15 min | Alerte si cron down |
| Cron Ownership | 15 min | Alerte si orphelin |
| LEO Health Check | 15 min | Alerte si gateway down |

---

## 📞 EN DERNIER RECOURS

Si rien ne répond et que les procédures ci-dessus échouent :
1. Redémarrer la machine LEO : `sudo reboot`
2. Vérifier que Docker et les conteneurs redémarrent
3. Relancer les gateways manuellement
4. Vérifier le dashboard

**Contact Christophe** : Telegram @Tofdan
