# Analyse OpenRouter — Modèles, Prix & Recommandations

*Générée le 24/07/2026 depuis l'API OpenRouter (343 modèles analysés)*

---

## 1. Modèles gratuits (:free) — actuellement utilisés par Michel

| Modèle | Contexte | Usage |
|--------|:--------:|-------|
| `nvidia/nemotron-3-ultra-550b-a55b:free` | 1M | Audit rédactionnel (⚠ rate-limité) |
| `google/gemma-4-31b-it:free` | 262K | Journaux Quotidiens (⚠ rate-limité) |
| `openai/gpt-oss-20b:free` | 131K | Unified Collector (⚠ rate-limité) |
| `nvidia/nemotron-3-super-120b-a12b:free` | 262K | bon mais rate-limité |
| `inclusionai/ling-3.0-flash:free` | 262K | nouveau prometteur |

⚠ Les modèles `:free` sont bridés (HTTP 429 en cron). Inutilisables pour des jobs automatisés.

---

## 2. Modèles payants — prix OpenRouter

### Entrée de gamme (< $0.50/M output)

| Modèle | Contexte | Input/1M | Output/1M | Ratio Q/P |
|--------|:--------:|:--------:|:---------:|:---------:|
| **DeepSeek V4 Flash** (Léo actuel) | **1M** | $0.098 | **$0.196** | ⭐⭐⭐⭐⭐ |
| **Qwen 3.5 Flash** | **1M** | $0.065 | $0.26 | ⭐⭐⭐⭐⭐ |
| **Llama 4 Scout** | **1.3M** | $0.10 | $0.30 | ⭐⭐⭐⭐⭐ |
| **Gemini 2.5 Flash Lite** (fallback Michel) | **1M** | $0.10 | $0.40 | ⭐⭐⭐⭐ |
| **Nemotron 3 Super 120B** | **1M** | $0.08 | $0.45 | ⭐⭐⭐⭐ |
| DeepSeek V4 Pro (Michel actuel) | **1M** | $0.44 | $0.87 | ⭐⭐⭐⭐ |
| Mistral Small 3.1 | 32K | $0.05 | $0.08 | ⭐⭐⭐ |
| GPT-OSS-20B | 131K | $0.03 | $0.14 | ⭐⭐⭐ |
| Llama 4 Maverick | **1M** | $0.20 | $0.80 | ⭐⭐⭐⭐ |
| GPT-4.1 Mini | **1M** | $0.40 | $1.60 | ⭐⭐⭐ |

### Gamme intermédiaire ($0.50-2.50/M output)

| Modèle | Contexte | Input/1M | Output/1M | Usage |
|--------|:--------:|:--------:|:---------:|-------|
| Gemini 2.5 Flash | **1M** | $0.30 | $2.50 | vision, web search |
| Qwen 3.5 Plus | **1M** | $0.26 | $1.56 | généraliste haut de gamme |
| Mistral Large | 262K | $0.50 | $1.50 | analyse |
| Nemotron 3 Ultra 550B | 512K | $0.50 | $2.20 | raisonnement |
| DeepSeek R1-0528 | 163K | $0.50 | $2.15 | raisonnement profond |
| Qwen3-32B | 131K | $0.08 | $0.28 | bon marché, solide |

### Premium ($2.50+/M output)

| Modèle | Contexte | Input/1M | Output/1M |
|--------|:--------:|:--------:|:---------:|
| Grok 4.20 | **2M** | $1.25 | $2.50 |
| Gemini 3.5 Flash | **1M** | $1.50 | $9.00 |
| GPT-4.1 | **1M** | $2.00 | $8.00 |
| Claude Sonnet 4 | **1M** | $3.00 | $15.00 |
| GPT-5.6 Luna | **1M** | $1.00 | $6.00 |

---

## 3. Meilleurs ratios Contexte / Prix

| Contexte | Modèle | Output/1M | Idéal pour |
|:--------:|--------|:---------:|------------|
| **2M** | Grok 4.20 | $2.50 | très longs documents |
| **1.3M** | **Llama 4 Scout** | **$0.30** | 🏆 meilleur rapport |
| **1M** | DeepSeek V4 Flash | **$0.196** | 🏆 meilleur global |
| **1M** | Gemini 2.5 Flash Lite | $0.40 | vision + texte |
| **1M** | Qwen 3.5 Flash | **$0.26** | 🏆 meilleur prix long ctx |
| **1M** | Nemotron 3 Super 120B | $0.45 | analyse technique |
| **1M** | Llama 4 Maverick | $0.80 | bon équilibre |
| **1M** | DeepSeek V4 Pro | $0.87 | raisonnement |

---

## 4. Recommandations par profil

| Profil | Modèle recommandé | Contexte | Prix/1M out | Fallback |
|--------|-------------------|:--------:|:----------:|----------|
| **Léo** (dialogue, rédactions) | DeepSeek V4 Flash | 1M | $0.196 | Gemini 2.5 Flash Lite |
| **Michel** (crons) | Qwen 3.5 Flash | 1M | $0.26 | Llama 4 Scout |
| **Robert** (stratégique) | DeepSeek V4 Pro | 1M | $0.87 | Qwen 3.5 Plus |
| **Émile** (éducation) | Gemini 2.5 Flash Lite | 1M | $0.40 | Qwen 3.5 Flash |
| **Sylvia** (voyages) | Gemini 2.5 Flash Lite | 1M | $0.40 | DeepSeek V4 Flash |

---

## 5. Budget avec 10$ OpenRouter

| Usage | Modèle | Coût/1M out | Appels estimés |
|-------|--------|:----------:|:--------------:|
| Audit rédactionnel (3x/jour) | Llama 4 Scout | $0.30 | ~2 000 audits |
| Journaux Quotidiens | Qwen 3.5 Flash | $0.26 | ~2 300 runs |
| Unified Collector | DeepSeek V4 Flash | $0.20 | ~3 000 collectes |
| Fallback Léo | Gemini 2.5 Flash Lite | $0.40 | ~1 500 utilisations |

Les 10$ de crédits OpenRouter + le compte DeepSeek direct → capacité quasi illimitée pour l'usage actuel.

---

*Données récupérées depuis api.openrouter.ai le 24/07/2026*
