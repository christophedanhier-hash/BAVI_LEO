---
date: 2026-06-25
bureau: bureau-michel
version: v3.0
modele: deepseek-v4-pro
tags: [deepseek, gemini, chatbot, telegram, memoire, emile, analyse]
statut: analyse
type: analyse
---

# Analyse — Bot Telegram : DeepSeek v4 Flash + Gemini 3.5 Flash (fallback)

**Bureau :** Michel — Infra_Hermes 🔧 | **Version :** v3.0
**Date :** 25/06/2026 | **Type :** Analyse (①→③→⑤→⑥→⑦)

---

## 💳 Coût du service BAVI LEO

| Métrique | Valeur |
|:---------|------:|
| Sessions LEO | 1 |
| Tokens consommés | ~20K IN · ~8K OUT |
| Coût DeepSeek réel | **~0,02 €** |
| Frais de service BAVI LEO | 1,00 € |
| **Total facturé** | **1,02 €** |

---

## ① CADRAGE

### Scopes

| Scope | Description | Contrainte clé |
|---|---|---|
| **Scope 1 — Chat général** | Bot Telegram quotidien | Fiabilité, coût maîtrisé |
| **Scope 2 — Mémoire Émile** | Assistant de rédaction pour mémoire de fin d'études (aspects pédagogiques) | Qualité rédactionnelle, contexte long, rigueur |

### Décision finale

Après évaluation de qwen2.5:7b (❌ switch chinois, 32K contexte insuffisant) et des modèles Gemini Pro (💸 coût élevé dû aux *thinking tokens*), l'architecture retenue est :

- **Primaire : DeepSeek v4 Flash** — fiable, économique, déjà en production (LEO Hermes)
- **Fallback : Gemini 3.5 Flash** — 1M contexte, dernière génération (mai 2026)

**Type de livrable :** Analyse (①→③→⑤→⑥→⑦)

---

## ③ PRODUCTION

### DeepSeek v4 Flash — Primaire

| Critère | Valeur |
|---|---|
| **Modèle** | deepseek-v4-flash |
| **Fournisseur** | DeepSeek (Chine) |
| **Contexte max** | 128K tokens (~100 pages) |
| **Qualité français** | 8/10 |
| **Coût input** | ~0,15 $ / 1M tokens |
| **Coût output** | ~0,60 $ / 1M tokens |
| **Fiabilité** | ✅ Stable, pas de switch langue |
| **Expérience LEO** | ✅ En production (LEO Hermes, classifieur) |

### Gemini 3.5 Flash — Fallback

| Critère | Valeur |
|---|---|
| **Modèle** | gemini-3.5-flash |
| **Sortie** | Mai 2026 (dernière génération) |
| **Contexte max** | 1M tokens (~700 pages) |
| **Qualité français** | 9/10 |
| **Coût** | Billing Google (pay-per-use) |
| **Activation** | Seulement si 128K insuffisant ou erreur DeepSeek |

### Modèles écartés

| Modèle | Raison |
|---|---|
| qwen2.5:7b | ❌ Switch chinois, 32K contexte, hallucinations |
| Gemini 2.5 Pro | ❌ Thinking tokens coûteux (96% de la sortie = pensée) |
| Gemini 3.1 Pro | ❌ Idem — Pro models trop chers pour usage étudiant |
| Gemini 2.0 Flash | ❌ Retiré par Google |

### Architecture finale

```
┌──────────────────────────────────────────────────────┐
│               Bot Telegram (profil unique)            │
│                                                      │
│  ┌──────────────────┐   ┌──────────────────────────┐ │
│  │ Scope 1 : Chat    │   │ Scope 2 : Mémoire Émile   │ │
│  │ (quotidien)       │   │ (pédagogique)             │ │
│  └────────┬─────────┘   └──────────┬───────────────┘ │
│           │                        │                  │
│           ▼                        ▼                  │
│  ┌─────────────────────────────────────────────────┐ │
│  │           DeepSeek v4 Flash (PRIMAIRE)           │ │
│  │   • 128K contexte                               │ │
│  │   • Fiable, économique, éprouvé LEO              │ │
│  │   • Système prompt dédié par scope              │ │
│  └────────────────────┬────────────────────────────┘ │
│                       │                               │
│                       │ Si erreur OU besoin >128K     │
│                       ▼                               │
│  ┌─────────────────────────────────────────────────┐ │
│  │          Gemini 3.5 Flash (FALLBACK)             │ │
│  │   • 1M contexte                                 │ │
│  │   • Dernière génération (mai 2026)               │ │
│  │   • Activé uniquement si nécessaire              │ │
│  └─────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘

Règle : Gemini 3.5 n'est appelé que si DeepSeek échoue
        OU si le contexte dépasse 128K (chapitre complet de mémoire).
        90%+ des requêtes → DeepSeek seul.
```

### Pattern « bot voyage » appliqué

| Élément | Bot Voyage (Sylvie) | Bot Mémoire (Émile) |
|---|---|---|
| **Système prompt** | Assistant voyage | Assistant pédagogique — mémoire de fin d'études |
| **Personnalité** | Conseiller pratique | Tuteur académique rigoureux |
| **Contexte** | Roadbook, itinéraires | Plan de mémoire, chapitres, bibliographie |
| **Modèle primaire** | DeepSeek Pro | DeepSeek v4 Flash |
| **Modèle fallback** | Aucun | Gemini 3.5 Flash (1M contexte) |

---

## ⑤ SYNTHÈSE

🟢 **Go pour implémentation**

- **DeepSeek v4 Flash primaire** : fiable, économique, déjà maîtrisé par LEO
- **Gemini 3.5 Flash fallback** : filet de sécurité pour longs contextes (1M) et pannes DeepSeek
- **qwen2.5 retiré** de l'architecture — plus utile
- **Coût estimé** : < 1€/jour pour usage étudiant normal
- **Scope Mémoire** prêt : système prompt à rédiger, pattern bot voyage à adapter

---

## ⑥ LIVRABLE — Plan d'implémentation

| # | Action | Scope | Priorité | Effort |
|---|--------|:-----:|:--------:|:------:|
| 1 | Créer profil Hermes/webhook Telegram | 1+2 | 🔴 Haute | 1h |
| 2 | Configurer DeepSeek v4 Flash comme primaire | 1+2 | 🔴 Haute | 30min |
| 3 | Configurer Gemini 3.5 Flash comme fallback (128K+ ou erreur) | 1+2 | 🔴 Haute | 30min |
| 4 | Rédiger système prompt « Assistant Mémoire » pour Scope 2 | 2 | 🔴 Haute | 2h |
| 5 | Test avec extrait de mémoire réel | 2 | 🟡 Moyenne | 1h |
| 6 | Watchdog + cron healthcheck | 1+2 | 🟡 Moyenne | 30min |

---

## ⑦ ARCHIVAGE

- **Fichier source :** `/opt/data/hermes-christophe/BAVI/AGENT-PRO/bureau-michel/analyse-qwen-chatbot-20260625.md`
- **Wiki :** BAVI LEO → Agent Pro → Bureau Michel — Infra_Hermes
- **Prochaine étape :** Implémentation — session planifiée demain

---

*Analyse produite par BAVI LEO — Bureau Michel — Infra_Hermes 🔧 — 25/06/2026*
