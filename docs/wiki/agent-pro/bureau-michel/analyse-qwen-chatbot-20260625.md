---
date: 2026-06-25
bureau: bureau-michel
version: v2.1
modele: deepseek-v4-pro
tags: [ollama, qwen, chatbot, telegram, gemini, analyse, modele]
statut: analyse
type: analyse
---

# Analyse — Bot Telegram : Gemini + qwen2.5:7b (fallback)

**Bureau :** Michel — Infra_Hermes 🔧 | **Version :** v2.1
**Date :** 25/06/2026 | **Type :** Analyse (①→③→⑤→⑥→⑦)

---

## 💳 Coût du service BAVI LEO

| Métrique | Valeur |
|:---------|------:|
| Sessions LEO | 1 |
| Tokens consommés | ~15K IN · ~5K OUT |
| Coût DeepSeek réel | **~0,01 €** |
| Frais de service BAVI LEO | 1,00 € |
| **Total facturé** | **1,01 €** |

---

## ① CADRAGE

**Question :** Un bot Telegram utilisant Gemini 2.0 Flash en primaire et qwen2.5:7b (Ollama local) en fallback est-il viable techniquement et économiquement ?

**Contexte :**
- Ollama qwen2.5:7b sur LEO (100.92.102.28:11434), CPU, 41 tok/s
- Gemini API key disponible
- Objectif : bot fiable, gratuit, avec filet de sécurité local

**Type de livrable :** Analyse (①→③→⑤→⑥→⑦)

---

## ③ PRODUCTION

### Gemini 2.0 Flash — Specifications

| Critère | Valeur |
|---|---|
| **Modèle** | Gemini 2.0 Flash (Google) |
| **Qualité français** | 9/10 |
| **Raisonnement** | 8/10 |
| **Contexte max** | 1M tokens |
| **Vision** | ✅ |
| **Fonction calling** | ✅ |
| **Vitesse** | ~80 tok/s (API) |

### Gemini — Tiers gratuit (Google AI Studio)

| Limite | Valeur | Impact bot |
|---|---|---|
| **RPM** (Requests Per Minute) | 15 req/min | Si >15 msg/min → erreur 429 |
| **TPM** (Tokens Per Minute) | 1M tok/min | Large pour du chat |
| **RPD** (Requests Per Day) | 1 500 req/jour | ~50 msg/heure, usage perso OK |
| **Coût** | 0€ dans ces limites | Gratuit |

### qwen2.5:7b — Specifications

| Critère | Valeur |
|---|---|
| **Modèle** | qwen2.5:7b (Alibaba) |
| **Paramètres / RAM** | 7.6B / Q4_K_M (~4.7 Go) |
| **Contexte max** | 32K tokens |
| **Vitesse** | 41 tok/s (CPU) |
| **Coût** | 0€ (local) |

### Matrice Forces/Faiblesses

| ✅ Forces | ❌ Faiblesses |
|---|---|
| Gemini : fiable, 9/10 français, 1M contexte | Gemini : limité à 15 RPM / 1 500 RPD |
| qwen2.5 : 24/7 local, pas de rate limit | qwen2.5 : switch chinois, hallucinations |
| Architecture redondante : jamais down | Double maintenance (2 APIs) |
| Coût total : 0€ | Latence fallback : +2-3s si bascule |

### Architecture corrigée

```
┌─────────────────────────────────────────┐
│          Bot Telegram (nouveau)          │
└─────────────────┬───────────────────────┘
                  │
                  ▼
        ┌─────────────────┐
        │ Gemini 2.0 Flash │  ← PRIMAIRE
        │   (API Google)   │     Fiable, qualitatif
        │     Gratuit*      │     80% des requêtes
        └────────┬─────────┘
                 │
                 │  Si 429 (rate limit)
                 │  OU timeout (>10s)
                 │  OU erreur API
                 ▼
        ┌─────────────────┐
        │   qwen2.5:7b     │  ← FALLBACK
        │  (Ollama local)  │     Filet de sécurité
        │      0€          │     ~20% des requêtes
        └─────────────────┘

* Gratuit dans les limites : 15 RPM, 1M TPM, 1500 RPD
```

---

## ⑤ SYNTHÈSE

**Verdict :** 🟢 Go

Architecture robuste et gratuite :
- **Gemini primary** : propriétaire de la conversation, qualité garantie pour 80%+ des requêtes
- **qwen2.5 fallback** : filet de sécurité local, absorbe les dépassements de rate limit
- **Coût total** : 0€ (dans les limites du tiers gratuit Gemini)
- **Risque** : faible — le fallback local assure la continuité même si l'API Google est down

---

## ⑥ LIVRABLE

| # | Recommandation | Priorité | Effort |
|---|---------------|:--------:|:------:|
| 1 | Créer un nouveau profil Hermes ou webhook Telegram | 🔴 Haute | 1h |
| 2 | Implémenter le script de bascule : 429/timeout → qwen | 🔴 Haute | 1h |
| 3 | Compteur RPM local pour anticiper les limites | 🟡 Moyenne | 30min |
| 4 | Watchdog + cron healthcheck (les 2 endpoints) | 🟡 Moyenne | 30min |
| 5 | Dashboard monitoring (requêtes, bascules, coûts) | 🟢 Basse | 2h |

---

## ⑦ ARCHIVAGE

- **Fichier source :** `/opt/data/hermes-christophe/BAVI/AGENT-PRO/bureau-michel/analyse-qwen-chatbot-20260625.md`
- **Wiki :** BAVI LEO → Agent Pro → Bureau Michel — Infra_Hermes

---

*Analyse produite par BAVI LEO — Bureau Michel — Infra_Hermes 🔧 — 25/06/2026*
