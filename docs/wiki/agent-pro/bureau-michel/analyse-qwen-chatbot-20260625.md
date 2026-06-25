---
date: 2026-06-25
bureau: bureau-michel
version: v2.0
modele: deepseek-v4-pro
tags: [ollama, qwen, chatbot, telegram, gemini, analyse]
statut: analyse
---

# Rapport Technique — Ollama qwen2.5:7b comme Chatbot Telegram

**Bureau :** Michel — Infra_Hermes 🔧 | **Version :** v2.0
**Date :** 25/06/2026 | **Experts :** SysAdmin, Scripteur
**Statut :** ✅ Analyse livrée — attente Go

---

## 💳 Coût du service BAVI LEO

| Métrique | Valeur |
|:---------|------:|
| Sessions LEO | 1 |
| Tokens consommés | ~12K IN · ~4K OUT |
| Coût DeepSeek réel | **~0,01 €** |
| Frais de service BAVI LEO | 1,00 € |
| **Total facturé** | **1,01 €** |

---

## ① CADRAGE

**Demande :** Évaluer si qwen2.5:7b (Ollama local sur LEO) est viable comme chatbot Telegram autonome, avec Gemini en fallback.

**Contexte :**
- Modèle déjà en production : classifieur email multi-comptes
- Ollama sur LEO (100.92.102.28:11434)
- Pas de GPU — CPU uniquement
- Gemini API key disponible (free tier : 15 RPM, 1500 RPD)

---

## ② DISPATCH

| Expert | Activé | Justification |
|--------|:------:|---------------|
| SysAdmin | ✅ | Évaluer le modèle, specs, benchmarks |
| Scripteur | ✅ | Architecture bot, intégration Telegram |
| DataDoc | ❌ | Pas d'audit système demandé |
| Networker | ❌ | Réseau déjà validé |

---

## ③ PRODUCTION

### SysAdmin — Spécifications du modèle

| Critère | Valeur |
|---|---|
| Modèle | qwen2.5:7b (Alibaba) |
| Paramètres | 7.6 milliards |
| Quantization | Q4_K_M (~4.7 Go RAM) |
| Contexte max | 32K tokens |
| Vitesse mesurée | 41 tok/s (CPU) |
| Capacités | completion, tools |

**Positionnement :** Équivalent à Llama 3.1 8B / Mistral 7B v0.3.

### SysAdmin — Benchmarks

| Test | Résultat | Score |
|---|---|---|
| Code Python (reverse linked list) | ✅ Propre, syntaxe parfaite | ⭐⭐⭐⭐ |
| Créatif (idées open source IA) | ✅ Pertinent, structuré | ⭐⭐⭐⭐ |
| Technique (embedding vectoriel) | ⚠️ Correct mais switch chinois | ⭐⭐⭐ |
| Classification email (9 catégories) | ✅ 90%+ fiable | ⭐⭐⭐⭐ |

### SysAdmin — Matrice Forces/Faiblesses

| ✅ Forces | ❌ Faiblesses |
|---|---|
| Gratuit — 0€, local, pas de rate limit | Switch occasionnel en chinois |
| Rapide (41 tok/s) | Raisonnement multi-étapes limité |
| Bon en français (pas parfait) | Pas de vision / multimodal |
| Code propre et concis | Hallucine sur sujets pointus |
| Classification fiable | Contexte 32K (Gemini = 1M) |

### Scripteur — Architecture proposée

```
┌─────────────────────────────────────────┐
│          Bot Telegram (nouveau)          │
│         Profil Hermes dédié OU           │
│      Webhook direct → Ollama API         │
└─────────────────┬───────────────────────┘
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
┌───────────────┐   ┌───────────────┐
│  qwen2.5:7b   │   │ Gemini Flash  │
│  (primaire)   │   │  (fallback)   │
│  Ollama local │   │  API Google   │
│     0€        │   │  Gratuit 15rpm│
└───────┬───────┘   └───────┬───────┘
        │                   │
        └───────┬───────────┘
                ▼
        Règles de bascule :
        • Réponse < 20 tokens → Gemini
        • Idéogrammes chinois → Gemini
        • Question complexe → Gemini
        • User frustré (2è tentative) → Gemini
```

---

## ④ CROISEMENT — qwen2.5 vs Gemini

| Critère | qwen2.5:7b | Gemini 2.0 Flash | Vainqueur |
|---|---|---|---|
| Coût | 0€ | Gratuit (15 RPM) | qwen2.5 |
| Qualité français | 7/10 | 9/10 | Gemini |
| Raisonnement | 6/10 | 8/10 | Gemini |
| Vitesse | 41 tok/s | ~80 tok/s | Gemini |
| Fiabilité | ⚠️ switch CN | ✅ stable | Gemini |
| Contexte | 32K | 1M | Gemini |
| Vision | ❌ | ✅ | Gemini |
| Disponibilité | 24/7 local | Dépendance Google | qwen2.5 |

---

## ⑤ SYNTHÈSE

**Verdict :** 🟡 Go conditionnel

qwen2.5:7b seul n'est pas assez fiable pour un chatbot autonome (switch chinois, hallucinations). L'architecture hybride **qwen2.5 primaire + Gemini fallback** est la solution recommandée : robuste, gratuite, et tire parti des forces de chaque modèle.

---

## ⑥ LIVRABLE — Recommandations

| # | Action | Priorité |
|---|--------|:--------:|
| 1 | Créer un nouveau profil Hermes dédié au bot | Haute |
| 2 | Implémenter la règle de bascule qwen2.5 → Gemini | Haute |
| 3 | Tests de non-régression (éviter le switch chinois) | Haute |
| 4 | Ajouter un watchdog + cron de healthcheck | Moyenne |
| 5 | Dashboard de monitoring (requêtes, bascules, coûts) | Basse |

---

## ⑦ ARCHIVAGE

- **Fichier :** `/opt/data/hermes-christophe/BAVI/AGENT-PRO/bureau-michel/analyse-qwen-chatbot-20260625.md`
- **Projet lié :** `bot-qwen-telegram` (à créer si Go)

---

*Analyse produite par BAVI LEO — Bureau Michel — Infra_Hermes 🔧 — 25/06/2026*
