---
date: 2026-06-25
bureau: bureau-michel
version: v2.0
modele: deepseek-v4-pro
tags: [ollama, qwen, chatbot, telegram, gemini, analyse, modele]
statut: analyse
type: analyse
---

# Analyse — Ollama qwen2.5:7b comme Chatbot Telegram

**Bureau :** Michel — Infra_Hermes 🔧 | **Version :** v2.0
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

**Question :** qwen2.5:7b (Ollama local, CPU) est-il viable comme chatbot Telegram autonome, avec Gemini en fallback ?

**Contexte :**
- Ollama sur LEO (100.92.102.28:11434), CPU uniquement
- Modèle déjà en production : classifieur email 2 comptes
- Gemini API key disponible (free tier : 15 RPM, 1500 RPD)
- Objectif : bot Telegram gratuit avec fallback fiable

**Type de livrable :** Analyse → workflow simplifié ①→③→⑤→⑥→⑦

---

## ③ PRODUCTION

### Spécifications du modèle

| Critère | Valeur |
|---|---|
| **Modèle** | qwen2.5:7b (Alibaba, juin 2025) |
| **Paramètres** | 7.6 milliards |
| **Quantization** | Q4_K_M (~4.7 Go RAM) |
| **Contexte max** | 32 768 tokens |
| **Vitesse mesurée** | 41 tok/s (CPU LEO) |
| **Capacités** | completion, tools (pas de vision) |
| **Positionnement** | Équivalent Llama 3.1 8B / Mistral 7B v0.3 |

### Benchmarks réels

| Test | Résultat | Score |
|---|---|---|
| Code (reverse linked list Python) | ✅ Syntaxe parfaite | ⭐⭐⭐⭐ |
| Créatif (idées open source IA) | ✅ Pertinent, structuré | ⭐⭐⭐⭐ |
| Technique (embedding vectoriel) | ⚠️ Correct mais switch chinois | ⭐⭐⭐ |
| Classification (9 catégories, 90%+) | ✅ Fiable en production | ⭐⭐⭐⭐ |

### Matrice Forces/Faiblesses

| ✅ Forces | ❌ Faiblesses |
|---|---|
| Gratuit — 0€, local, pas de rate limit | Switch occasionnel en chinois |
| Rapide (41 tok/s) | Raisonnement multi-étapes limité |
| Bon en français | Pas de vision / multimodal |
| Code propre et concis | Hallucine sur sujets pointus |
| Classification fiable (90%+) | Contexte 32K (Gemini = 1M) |

### Comparaison avec Gemini 2.0 Flash

| Critère | qwen2.5:7b | Gemini 2.0 Flash | Vainqueur |
|---|---|---|---|
| **Coût** | 0€ (local) | Gratuit (15 RPM) | qwen2.5 |
| **Qualité français** | 7/10 | 9/10 | Gemini |
| **Raisonnement** | 6/10 | 8/10 | Gemini |
| **Vitesse** | 41 tok/s | ~80 tok/s (API) | Gemini |
| **Fiabilité** | ⚠️ switch CN | ✅ stable | Gemini |
| **Contexte** | 32K | 1M | Gemini |
| **Vision** | ❌ | ✅ | Gemini |
| **Disponibilité** | 24/7 local | Dépendance Google | qwen2.5 |
| **Fonction calling** | ✅ tools | ✅ function calling | Égalité |

### Architecture proposée

```
┌─────────────────────────────────────────┐
│          Bot Telegram (nouveau)          │
└─────────────────┬───────────────────────┘
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
┌───────────────┐   ┌───────────────┐
│  qwen2.5:7b   │   │ Gemini Flash  │
│  (primaire)   │   │  (fallback)   │
│  Ollama local │   │  API Google   │
│     0€        │   │  Gratuit      │
└───────────────┘   └───────────────┘

Règles de bascule :
• Réponse < 20 tokens → Gemini
• Idéogrammes chinois → Gemini
• Requête contexte > 16K → Gemini
• User insatisfait → Gemini
```

---

## ⑤ SYNTHÈSE

**Verdict :** 🟡 Go conditionnel

- qwen2.5:7b **seul** → ❌ Pas assez fiable (switch chinois, hallucinations)
- qwen2.5:7b **+ Gemini fallback** → ✅ Architecture robuste, gratuite, complémentaire

**Distribution estimée :** 80% requêtes → qwen2.5, 20% → Gemini.

Les deux modèles sont complémentaires : qwen2.5 apporte la disponibilité 24/7 et le coût zéro, Gemini garantit la qualité et la fiabilité pour les requêtes complexes.

---

## ⑥ LIVRABLE

| # | Recommandation | Priorité | Effort |
|---|---------------|:--------:|:------:|
| 1 | Créer un nouveau profil Hermes ou webhook Telegram | 🔴 Haute | 1h |
| 2 | Implémenter le script de bascule qwen2.5 → Gemini | 🔴 Haute | 2h |
| 3 | Tests de non-régression (switch chinois) | 🔴 Haute | 1h |
| 4 | Ajouter watchdog + cron healthcheck | 🟡 Moyenne | 30min |
| 5 | Dashboard monitoring (requêtes, bascules) | 🟢 Basse | 2h |

---

## ⑦ ARCHIVAGE

- **Fichier source :** `/opt/data/hermes-christophe/BAVI/AGENT-PRO/bureau-michel/analyse-qwen-chatbot-20260625.md`
- **Wiki :** BAVI LEO → Agent Pro → Bureau Michel — Infra_Hermes
- **Index :** Régénéré via `agent-pro-index.py`

---

*Analyse produite par BAVI LEO — Bureau Michel — Infra_Hermes 🔧 — 25/06/2026*
