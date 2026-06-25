---
date: 2026-06-25
bureau: bureau-michel
version: v2.0
modele: deepseek-v4-pro
tags: [ollama, qwen, chatbot, telegram, gemini, analyse, modele]
statut: analyse
---

# Rapport Technique — Ollama qwen2.5:7b comme Chatbot Telegram

**Bureau :** Michel — Infra_Hermes 🔧 | **Version :** v2.0
**Date :** 25/06/2026 | **Experts :** SysAdmin, Scripteur
**Modèle :** DeepSeek Pro

---

## 💳 Coût du service BAVI LEO

| Métrique | Valeur |
|:---------|------:|
| Sessions LEO | 1 |
| Tokens consommés | ~15K IN · ~5K OUT |
| Coût DeepSeek réel | **~0,01 €** |
| Frais de service BAVI LEO | 1,00 € forfait |
| **Total facturé** | **1,01 €** |

---

## ① CADRAGE

**Demande :** Évaluer si qwen2.5:7b (Ollama local, CPU) est viable comme chatbot Telegram autonome, avec Gemini en fallback.

**Contexte technique :**
- Ollama sur LEO (100.92.102.28:11434), CPU uniquement
- Modèle déjà en production : classifieur email 2 comptes
- Gemini API key disponible (free tier)
- Objectif : bot Telegram gratuit avec fallback fiable

---

## ② DISPATCH

| Expert | Activé | Justification |
|--------|:------:|---------------|
| **SysAdmin** | ✅ | Spécifications matérielles, benchmarks, performance modèle |
| **Scripteur** | ✅ | Architecture bot, intégration Telegram + Ollama |
| DataDoc | ❌ | Pas d'audit système requis |
| Networker | ❌ | Connectivité déjà validée (Ollama et Gemini OK) |

---

## ③ PRODUCTION

### SysAdmin — Spécifications du modèle

| Critère | Valeur |
|---|---|
| **Modèle** | qwen2.5:7b (Alibaba, juin 2025) |
| **Paramètres** | 7.6 milliards |
| **Quantization** | Q4_K_M (~4.7 Go RAM) |
| **Contexte max** | 32 768 tokens |
| **Vitesse mesurée** | 41 tok/s (CPU LEO) |
| **Capacités** | completion, tools (pas de vision) |
| **Positionnement** | Équivalent Llama 3.1 8B / Mistral 7B v0.3 |

### SysAdmin — Benchmarks réels

| Test | Prompt | Résultat | Score |
|---|---|---|---|
| Code | Reverse linked list (Python) | ✅ Syntaxe parfaite, classe + méthode | ⭐⭐⭐⭐ |
| Créatif | Idées projet open source IA | ✅ Pertinent, structuré, 3 idées | ⭐⭐⭐⭐ |
| Technique | Expliquer embedding vectoriel | ⚠️ Correct mais switch partiel chinois | ⭐⭐⭐ |
| Classification | 9 catégories email (90%+) | ✅ Fiable en production | ⭐⭐⭐⭐ |

### SysAdmin — Matrice Forces/Faiblesses

| ✅ Forces | ❌ Faiblesses |
|---|---|
| Gratuit — 0€, local, pas de rate limit | Switch occasionnel en chinois |
| Rapide (41 tok/s) | Raisonnement multi-étapes limité |
| Bon en français (pas parfait) | Pas de vision / multimodal |
| Code propre et concis | Hallucine sur sujets pointus |
| Classification fiable (90%+) | Contexte 32K (Gemini = 1M) |
| Disponible 24/7 (local) | 7.6B limité vs modèles 70B+ |

### Scripteur — Architecture proposée

```
┌─────────────────────────────────────────┐
│          Bot Telegram (nouveau)          │
│    Profil Hermes dédié ou webhook        │
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
        Règles de bascule automatique :
        • Réponse < 20 tokens → Gemini
        • Idéogrammes chinois détectés → Gemini
        • Requête avec contexte > 16K → Gemini
        • User insatisfait (2è tentative) → Gemini
```

**Points d'attention techniques :**
- Pas besoin de GPU — CPU LEO suffit pour 41 tok/s
- Pas de nouveau conteneur — Ollama déjà en service
- Script de bascule à écrire (~50 lignes Python)
- Monitoring : watchdog + cron healthcheck recommandé

---

## ④ CROISEMENT

Comparaison systématique qwen2.5:7b vs Gemini 2.0 Flash :

| Critère | qwen2.5:7b | Gemini 2.0 Flash | Vainqueur |
|---|---|---|---|
| **Coût** | 0€ (local) | Gratuit (15 RPM, 1500 RPD) | qwen2.5 |
| **Qualité français** | 7/10 | 9/10 | Gemini |
| **Raisonnement** | 6/10 | 8/10 | Gemini |
| **Vitesse** | 41 tok/s (CPU) | ~80 tok/s (API) | Gemini |
| **Fiabilité** | ⚠️ switch chinois | ✅ stable | Gemini |
| **Contexte max** | 32K | 1M | Gemini |
| **Vision** | ❌ | ✅ | Gemini |
| **Disponibilité** | 24/7 local | Dépendance Google | qwen2.5 |
| **Fonction calling** | ✅ tools | ✅ function calling | Égalité |

**Analyse croisée :** Les deux modèles sont complémentaires. qwen2.5 excelle en disponibilité et coût nul. Gemini domine en qualité, fiabilité et capacités. L'architecture hybride tire parti des deux.

---

## ⑤ SYNTHÈSE

**Verdict technique :** 🟡 Go conditionnel

- qwen2.5:7b **seul** → ❌ Pas assez fiable pour un chatbot autonome (switch chinois, hallucinations)
- qwen2.5:7b **+ Gemini fallback** → ✅ Architecture robuste, gratuite, complémentaire

**Distribution estimée :**
- 80% requêtes → qwen2.5 (conversation simple, questions générales, code basique)
- 20% requêtes → Gemini (raisonnement complexe, contexte long, fiabilité critique)

---

## ⑥ LIVRABLE

| # | Recommandation | Priorité | Effort |
|---|---------------|:--------:|:------:|
| 1 | Créer un nouveau profil Hermes ou webhook Telegram | 🔴 Haute | 1h |
| 2 | Implémenter le script de bascule qwen2.5 → Gemini | 🔴 Haute | 2h |
| 3 | Tests de non-régression (éviter le switch chinois) | 🔴 Haute | 1h |
| 4 | Ajouter un watchdog + cron healthcheck | 🟡 Moyenne | 30min |
| 5 | Dashboard monitoring (requêtes, bascules, coûts) | 🟢 Basse | 2h |

---

## ⑦ ARCHIVAGE

- **Fichier source :** `/opt/data/hermes-christophe/BAVI/AGENT-PRO/bureau-michel/analyse-qwen-chatbot-20260625.md`
- **Wiki :** BAVI LEO → Agent Pro → Bureau Michel — Infra_Hermes
- **Index :** Régénéré via `agent-pro-index.py`

---

*Analyse produite par BAVI LEO — Bureau Michel — Infra_Hermes 🔧 — 25/06/2026*
