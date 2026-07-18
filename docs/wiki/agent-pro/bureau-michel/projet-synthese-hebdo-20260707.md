---
date: 2026-07-07
bureau: bureau-michel
version: v1
modele: qwen2.5:7b
tags: [synthese, hebdomadaire, veille, budget, monitoring, gemma, agentic]
statut: concept
type: analyse
---

# 📊 Projet : Synthèse Hebdomadaire LEO

> **Bureau :** Michel 🔧
> **Modèle cible :** qwen2.5:7b (local, Ollama)
> **Date :** 07/07/2026
> **Statut :** Concept validé, à implémenter

---

## 🎯 Objectif

Produire un rapport de synthèse hebdomadaire automatique qui croise :
- **Veille IA** (articles marquants de la semaine)
- **Budget DeepSeek** (coûts API, tendances)
- **Métriques machines** (CPU, VRAM, uptime, incidents LEO/Yoga/Penguin)
- **État des crons** (échecs, alertes)

→ Via **qwen2.5:7b** en local (Ollama), gratuit, privé.

---

## 📋 Architecture proposée

```
[Sources de données]          [Agent LEO]              [Livraison]
     ┌─────────┐          ┌────────────────┐        ┌──────────┐
     │ Veille  │          │  Collecte →    │        │ Telegram │
     │ Budget  │ ──────→ │  Prompt →      │ ─────→ │ (ou DM)  │
     │ Metrics │          │  qwen2.5:7b │        │          │
     │ Crons   │          │  → Synthèse    │        └──────────┘
     └─────────┘          └────────────────┘
```

### Fréquence
- **Hebdomadaire** (dimanche 20h)
- Cron Hermes, profil `default` ou `leo-copilot`

### Sources exactes à définir
- Veille : `/opt/data/metrics/veille/raw-*.json` (7 derniers jours)
- Budget : dashboard KPI budget
- Métriques : à définir (base SQLite du dashboard ?)
- Crons : logs d'erreur des 7 derniers jours

### Livraison
- Message Telegram structuré (Markdown)
- À Christophe uniquement (pas de CC)

---

## 📝 Plan d'implémentation (à venir)

| Phase | Action | Dépendances |
|:-----:|--------|:-----------:|
| ① | Définir les sources exactes + format extraction | — |
| ② | Écrire script collecte (récupère les 4 sources) | Phase ① |
| ③ | Écrire prompt qwen2.5:7b pour la synthèse | Phase ② |
| ④ | Créer le cron Hermes (domingo 20h) | Phase ③ |
| ⑤ | Tester et ajuster le prompt | Phase ④ |

---

## 💰 Coût estimé

- **Gemma-agentic :** 0 €/mois (local, GPU)
- **Tok/s attendu :** ~20 tok/s
- **Temps de génération :** ~30-60 secondes
- **Électricité GPU :** ~0.05 €/semaine (négligeable)

---

## 📎 Références

- Analyse initiale : `analyse-fable-leo-20260707.md`
- Modèle : qwen2.5:7b (Ollama, 6.1 GB, ~20 tok/s)
- API Ollama : `http://100.92.102.28:11434/v1`
