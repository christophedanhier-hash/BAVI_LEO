---
date: 2026-06-25
bureau: bureau-michel
version: v2.2
modele: deepseek-v4-pro
tags: [ollama, qwen, chatbot, telegram, gemini, analyse, modele, memoire, pedagogique, emile]
statut: analyse
type: analyse
---

# Analyse — Bot Telegram : Gemini + qwen2.5 (fallback) + Scope Mémoire Pédagogique

**Bureau :** Michel — Infra_Hermes 🔧 | **Version :** v2.2
**Date :** 25/06/2026 | **Type :** Analyse (①→③→⑤→⑥→⑦)

---

## 💳 Coût du service BAVI LEO

| Métrique | Valeur |
|:---------|------:|
| Sessions LEO | 1 |
| Tokens consommés | ~18K IN · ~6K OUT |
| Coût DeepSeek réel | **~0,02 €** |
| Frais de service BAVI LEO | 1,00 € |
| **Total facturé** | **1,02 €** |

---

## ① CADRAGE

### Scopes

| Scope | Description | Contrainte clé |
|---|---|---|
| **Scope 1 — Chatbot général** | Bot Telegram fiable, gratuit, pour usage quotidien | Fiabilité, coût 0€ |
| **Scope 2 — Mémoire Émile** 🆕 | Assistant de rédaction pour le mémoire de fin d'études d'Émile, sur des aspects pédagogiques | Long contexte, qualité rédactionnelle, rigueur académique |

### Contexte technique
- Ollama qwen2.5:7b sur LEO (CPU, 41 tok/s, 32K contexte)
- Gemini 2.0 Flash : API disponible, 1M contexte, 15 RPM gratuit
- Référence : le « bot voyage » (Sylvie) suit un pattern similaire — assistant spécialisé avec instructions système dédiées

### Contraintes spécifiques Scope 2 (Mémoire)
- **Contexte long indispensable** : un mémoire fait 50-150 pages. Le modèle doit pouvoir ingérer des chapitres entiers pour fournir des retours cohérents
- **Qualité rédactionnelle** : français académique, structuration, citations
- **Rigueur** : pas d'hallucinations sur des faits, dates, auteurs
- **Pattern « bot voyage »** : système prompt dédié, personnalité adaptée, contexte persistant

**Type de livrable :** Analyse (①→③→⑤→⑥→⑦)

---

## ③ PRODUCTION

### Gemini 2.0 Flash — Specifications

| Critère | Valeur |
|---|---|
| **Modèle** | Gemini 2.0 Flash (Google) |
| **Qualité français** | 9/10 |
| **Raisonnement** | 8/10 |
| **Contexte max** | 1M tokens (~700 pages) |
| **Vision** | ✅ |
| **Fonction calling** | ✅ |
| **Vitesse** | ~80 tok/s (API) |

### Gemini — Tiers gratuit (Google AI Studio)

| Limite | Valeur | Impact Scope 1 | Impact Scope 2 |
|---|---|---|---|
| **RPM** | 15 req/min | Léger | Léger (usage solo) |
| **TPM** | 1M tok/min | Large | OK même avec gros prompts |
| **RPD** | 1 500 req/jour | ~50 msg/h | Large pour 1 utilisateur |
| **Coût** | 0€ | Gratuit | Gratuit |

### qwen2.5:7b — Specifications

| Critère | Valeur | Compatible Scope 2 ? |
|---|---|---|
| **Modèle** | qwen2.5:7b | ⚠️ Limité |
| **Contexte max** | 32K tokens (~25 pages) | ❌ Insuffisant pour un mémoire |
| **Vitesse** | 41 tok/s (CPU) | ✅ |
| **Coût** | 0€ (local) | ✅ |

### Impact du Scope 2 sur l'architecture

| Exigence Mémoire | Gemini 2.0 Flash | qwen2.5:7b |
|---|---|---|
| Contexte > 100 pages | ✅ 1M tokens | ❌ 32K max |
| Français académique | ✅ 9/10 | ⚠️ 7/10 + risque chinois |
| Structuration (plan, chapitres) | ✅ | ⚠️ |
| Citations, références | ✅ | ⚠️ Hallucinations |
| Relecture orthographique | ✅ | ✅ |
| Recherche documentaire | ✅ | ⚠️ |

**Constats :** Pour le Scope 2 (mémoire), Gemini est le seul viable. qwen2.5 ne peut pas ingérer un mémoire et sa qualité rédactionnelle est insuffisante pour de l'académique. Pour le Scope 1 (chat général), l'architecture hybride fonctionne.

### Architecture

```
┌──────────────────────────────────────────────────────────┐
│                   Bot Telegram (profil unique)            │
│                                                          │
│  ┌─────────────────────┐    ┌──────────────────────────┐ │
│  │   Scope 1 : Chat     │    │  Scope 2 : Mémoire Émile  │ │
│  │   (usage quotidien)  │    │  (session dédiée)         │ │
│  └──────────┬──────────┘    └──────────┬───────────────┘ │
│             │                          │                  │
│             ▼                          ▼                  │
│  ┌───────────────────┐    ┌──────────────────────────┐   │
│  │ Gemini 2.0 Flash  │    │   Gemini 2.0 Flash ONLY   │   │
│  │    (primaire)     │    │   (pas de fallback qwen)  │   │
│  └────────┬──────────┘    │   Système prompt dédié :  │   │
│           │               │   « Assistant pédagogique │   │
│           │ 429/timeout   │    pour mémoire de fin     │   │
│           ▼               │    d'études »             │   │
│  ┌───────────────────┐    └──────────────────────────┘   │
│  │   qwen2.5:7b      │                                    │
│  │   (fallback)      │                                    │
│  │   Usage général    │                                    │
│  │   seulement        │                                    │
│  └───────────────────┘                                    │
└──────────────────────────────────────────────────────────┘

Règle : Scope 2 (Mémoire) → Gemini uniquement. Pas de fallback qwen
        car 32K insuffisant + qualité académique non garantie.
```

### Pattern « bot voyage » appliqué au Scope 2

| Élément | Bot Voyage (Sylvie) | Bot Mémoire (Émile) |
|---|---|---|
| **Système prompt** | Assistant voyage, campings, itinéraires | Assistant pédagogique, mémoire, recherche |
| **Personnalité** | Conseiller voyage pratique | Tuteur académique rigoureux |
| **Contexte** | Roadbook, étapes, réservations | Plan de mémoire, chapitres, bibliographie |
| **Session** | Persistante par roadbook | Persistante par chapitre/thématique |
| **Modèle** | DeepSeek Pro | Gemini 2.0 Flash |

---

## ⑤ SYNTHÈSE

### Scope 1 — Chat général
🟢 Go — Gemini primary, qwen2.5 fallback. Architecture robuste, 0€.

### Scope 2 — Mémoire Émile
🟡 Go conditionnel — Gemini uniquement, sans fallback.

- ✅ Gemini 2.0 Flash est **techniquement suffisant** pour l'assistance à la rédaction de mémoire
- ✅ Le **contexte 1M tokens** permet d'ingérer des chapitres entiers
- ✅ Le **tiers gratuit** (1 500 RPD) est large pour un usage solo étudiant
- ⚠️ **Pas de fallback qwen** : 32K insuffisant + switch chinois = risque pour un mémoire
- ⚠️ Si rate limit Gemini atteint → l'étudiante doit attendre (pas de plan B local)

### Recommandation

| Scope | Architecture | Coût |
|---|---|---|
| Scope 1 (Général) | Gemini primary → qwen fallback | 0€ |
| Scope 2 (Mémoire) | Gemini uniquement | 0€ |

---

## ⑥ LIVRABLE

| # | Action | Scope | Priorité | Effort |
|---|--------|:-----:|:--------:|:------:|
| 1 | Créer le profil Hermes/webhook Telegram | 1+2 | 🔴 Haute | 1h |
| 2 | Implémenter bascule 429 → qwen (Scope 1) | 1 | 🔴 Haute | 1h |
| 3 | Rédiger le système prompt « Assistant Mémoire » | 2 | 🔴 Haute | 2h |
| 4 | Blinder Scope 2 : pas de fallback, message clair si rate limit | 2 | 🔴 Haute | 30min |
| 5 | Tests avec un extrait de mémoire réel | 2 | 🟡 Moyenne | 1h |
| 6 | Watchdog + cron healthcheck | 1+2 | 🟡 Moyenne | 30min |
| 7 | Dashboard monitoring (requêtes, bascules, coûts) | 1+2 | 🟢 Basse | 2h |

---

## ⑦ ARCHIVAGE

- **Fichier source :** `/opt/data/hermes-christophe/BAVI/AGENT-PRO/bureau-michel/analyse-qwen-chatbot-20260625.md`
- **Wiki :** BAVI LEO → Agent Pro → Bureau Michel — Infra_Hermes

---

*Analyse produite par BAVI LEO — Bureau Michel — Infra_Hermes 🔧 — 25/06/2026*
