# ⚙️ LEO Admin — Infrastructure Hermes

**Version :** 1.0 | **Catégorie :** PRIVÉ Infrastructure | **Orchestrateur :** LEO (natif)

---

## Rôle

LEO Admin est le bureau **d'infrastructure et d'administration** de l'écosystème Hermes. Contrairement aux autres bureaux qui sont des skills Hermes activés à la demande, LEO Admin fonctionne **en permanence** via des crons, scripts et dashboards.

---

## Sous-skills Hermes

| Skill | Rôle | Type |
|-------|------|------|
| `budget-tracking` | Suivi du budget DeepSeek, arbitrage Ollama/Gemini | Cron H:35 |
| `machine-metrics` | Collecte CPU/RAM/Disk sur LEO, Yoga, Penguin | Cron H:00 |
| `dashboard-kpi` | Dashboard KPI Hermes (sessions, tokens, coûts) | Cron H:35 |
| `system-management` | Gestion centralisée des machines via Tailscale | Cron |
| `leo-email-assistant` | Envoi d'emails via Gmail OAuth2 | À la demande |
| `dashboard-deployment` | Déploiement HTML sur GitHub Pages | Cron toutes les 4h |

---

## Workflow

Contrairement aux bureaux PRO et PRIVÉ interactifs, LEO Admin suit un **modèle cron-driven** :

```
Collecte → Traitement → Dashboard → Livraison
```

| Flux | Source | Destination | Fréquence |
|------|--------|-------------|-----------|
| 📊 Métriques machines | LEO local + Penguin SSH | GitHub Pages | H:00 |
| 💰 Budget DeepSeek | API DeepSeek + state.db | Dashboard LEO | H:35 |
| ⏰ État des crons | Hermes state | Crons Dashboard | H:00 |
| 🔄 Sync Drive ↔ GitHub | Drive API | Repos wikis | 18h quotidien |
| 📧 Email | Gmail OAuth2 | Destinataires | À la demande |

---

## Dashboards actifs

| Dashboard | URL | Met à jour |
|-----------|-----|------------|
|| BAVI LEO KPIs | bavi-leo-dashboard | Toutes les heures |
|| Hermes KPI | dashboard-leo | Toutes les heures |
| Machines | leo-metrics | Toutes les heures |
| Crons | crons-dashboard | Toutes les heures |
| GitHub | github-dashboard | Toutes les 4h |

---

## Machines supervisées

| Machine | IP | Statut | Collecte |
|---------|----|--------|----------|
| **LEO** (Hermes) | 100.92.102.28 | ✅ Actif | Locale |
| **Penguin** (NAS) | 100.113.110.40 | ✅ Actif | SSH |
| **Yoga** (Chromebook) | 100.88.78.6 | ❌ Timeout | Hors ligne |
| **Pixel** (téléphone) | — | ❌ Refusé | Non monitoré |

---

## Règles

- Zéro gaspillage de tokens DeepSeek : priorité Ollama local, fallback Gemini, dernier recours DeepSeek
- Budget : alerte si solde < $20
- Anti-régression : pas de répétition, pas de réessai sans accord

---

## Différence avec les autres bureaux

| Critère | Bureaux PRO / PRIVÉ | LEO Admin |
|---------|--------------------|-----------|
| Activation | À la demande (Telegram) | **Automatique (cron)** |
| Orchestrateur | Skill Hermes | **LEO natif** |
| Sous-agents | Experts virtuels | **Skills Hermes réels** |
| Interaction | Conversationnelle | **Silencieuse (dashboards)** |
| Tokens | DeepSeek (coûteux) | **Ollama local (gratuit)** |
