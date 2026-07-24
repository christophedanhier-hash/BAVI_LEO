# Analyse OpenRouter — Plateforme LEO

> **Date** : 23 juillet 2026  
> **Auteur** : Michel (LEO Infrastructure)  
> **Clé API** : `sk-or-v1-...3846` (free tier, $10 crédits offerts)

---

## 1. Qu'est-ce qu'OpenRouter ?

OpenRouter est un **routeur API unifié** qui donne accès à **342 modèles** de tous les fournisseurs majeurs (DeepSeek, OpenAI, Anthropic, Google, Meta, NVIDIA, etc.) via une seule clé API, une seule facturation, un seul format d'appel (OpenAI-compatible).

**Avantage clé** : une seule intégration → tous les modèles. Plus besoin de gérer 5 clés API différentes.

---

## 2. Modèles disponibles (aperçu)

### 🆓 Gratuits (15 modèles) — utilisés actuellement

| Modèle | Contexte | Usage LEO |
|--------|----------|-----------|
| `openai/gpt-oss-20b:free` | 131k | Collector v2 (15 min) |
| `google/gemma-4-31b-it:free` | 262k | Journaux quotidiens (23h) |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | 1000k | Audit rédactionnel (06h) |

### 🦈 DeepSeek via OpenRouter (11 modèles)

| Modèle | Prix/1M tokens (prompt/compl) | Vs Direct DeepSeek |
|--------|------------------------------|-------------------|
| `deepseek-chat` (V3) | $0.20 / $0.80 | **-25% / -27%** moins cher ! |
| `deepseek-v4-pro` | $0.44 / $0.87 | -20% moins cher |
| `deepseek-v4-flash` | $0.10 / $0.20 | -28% moins cher |
| `deepseek-r1-0528` | $0.50 / $2.15 | Raisonnement |

### 🤖 Autres modèles majeurs

| Fournisseur | Modèle flagship | Prix/1M tokens |
|-------------|----------------|---------------|
| Google | `gemini-3.6-flash` | $1.50 / $7.50 |
| Anthropic | `claude-sonnet-5` | $2.00 / $10.00 |
| OpenAI | `gpt-5.6-luna-pro` | $1.00 / $6.00 |
| NVIDIA | `nemotron-3-ultra-550b` | **Gratuit** |

---

## 3. Pourquoi utiliser DeepSeek via OpenRouter plutôt qu'en direct ?

### 💰 Économique
- **DeepSeek-chat via OpenRouter est 25% moins cher** qu'en direct ($0.20 vs $0.27/M input)
- Une seule facture, pas de surprise
- Possibilité de mixer gratuit + payant selon la tâche

### 🔄 Résilience
- **Fallback automatique** : si DeepSeek down → bascule sur un modèle gratuit (Gemma, Nemotron)
- Pas de SPOF sur un seul fournisseur

### 🎯 Flexibilité
- Routing intelligent : tâches simples → gratuit, complexes → DeepSeek Pro
- Test A/B entre modèles sans changer de code

---

## 4. Architecture recommandée pour LEO

```
┌─────────────────────────────────────────────────────┐
│                    Hermes Gateway                     │
│                                                      │
│  Primaire: deepseek (direct) — sessions utilisateur  │
│  Fallback: custom:openrouter → gemma-4-31b (gratuit) │
│                                                      │
│  Crons LLM:                                           │
│    ├─ Collector v2    → openai/gpt-oss-20b (gratuit) │
│    ├─ Journaux        → google/gemma-4-31b (gratuit) │
│    ├─ Audit           → nvidia/nemotron-550b (gratuit)│
│    └─ Point Contact   → no_agent (script bash)       │
│                                                      │
│  Option futur:                                        │
│    └─ deepseek via OpenRouter (moins cher que direct)│
└─────────────────────────────────────────────────────┘
```

---

## 5. Endpoints API utiles

| Endpoint | Description |
|----------|-------------|
| `GET /api/v1/models` | Liste tous les modèles (342) |
| `GET /api/v1/auth/key` | Statut clé, limits, usage |
| `GET /api/v1/credits` | Crédits restants/utilisés |
| `POST /api/v1/chat/completions` | Appel LLM (format OpenAI) |

---

## 6. Paramètres de configuration

### Hermes (config.yaml)
```yaml
providers:
  custom:
    openrouter:
      base_url: https://openrouter.ai/api/v1
      api_key: sk-or-v1-...

# Fallback DeepSeek → OpenRouter gratuit
profiles:
  michel:
    provider: deepseek
    model: deepseek-v4-pro
    fallback:
      - provider: custom:openrouter
        model: google/gemma-4-31b-it:free
```

### Cron (spécifique par modèle)
```yaml
# Cron utilisant OpenRouter gratuit
model:
  provider: custom:openrouter
  model: openai/gpt-oss-20b:free
```

### Appels directs
```python
# Format compatible OpenAI
requests.post("https://openrouter.ai/api/v1/chat/completions",
  headers={"Authorization": "Bearer $KEY"},
  json={
    "model": "deepseek/deepseek-chat",
    "messages": [{"role": "user", "content": "..."}],
    "temperature": 0.7,
    "max_tokens": 1000
  }
)
```

---

## 7. Dashboard LEO

Le dashboard affiche les stats OpenRouter en direct :
- **Crédits** : 10 offerts, 0 utilisés
- **Usage** : daily/weekly/monthly (0 pour l'instant)
- **Modèles actifs** : GPT-OSS 20B, Gemma 4 31B, Nemotron 550B
- **Coût** : $0.00/mois (100% gratuit)

Endpoint : `/api/openrouter?token=leo-panel-2026` (cache 5 min)

---

## 8. Prochaines étapes possibles

| Priorité | Action | Gain |
|----------|--------|------|
| 🔴 P1 | Migrer DeepSeek-chat → OpenRouter | -25% coût, fallback natif |
| 🟡 P2 | Test A/B : gemma-4-31b vs deepseek-chat pour Synthèse Hebdo | Gratuit vs payant |
| 🟢 P3 | Routing intelligent : tâche simple → gratuit, complexe → pro | Optimisation coûts |
| 🟢 P3 | Ajouter Claude/GPT via OpenRouter pour tâches critiques | Meilleure qualité |

---

## 9. Limites du free tier

- **Rate limit** : 20 requêtes/minute (modèles gratuits)
- **Pas de SLA** : les modèles gratuits peuvent être lents ou indisponibles
- **Pas de fine-tuning** 
- **Clé standard** (pas management key) → pas d'accès à `/activity`

---

*Document généré automatiquement par Michel — BAVI_LEO*

> 🤖 Dernier audit : 24/07/2026 à 07:57 (UTC+2)
