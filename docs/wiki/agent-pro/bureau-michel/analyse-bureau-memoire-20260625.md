---
date: 2026-06-25
bureau: bureau-michel
version: v1.0
modele: deepseek-v4-pro
tags: [memoire, emile, pedagogique, bureau, bot, assistant, analyse]
statut: analyse
type: analyse
---

# Analyse — Bureau Mémoire : Assistant de rédaction pour Émile

**Bureau :** Michel — Infra_Hermes 🔧 | **Version :** v1.0
**Date :** 25/06/2026 | **Type :** Analyse (①→③→⑤→⑥→⑦)

---

## 💳 Coût du service BAVI LEO

| Métrique | Valeur |
|:---------|------:|
| Sessions LEO | 1 |
| Tokens consommés | ~10K IN · ~4K OUT |
| Coût DeepSeek réel | **~0,01 €** |
| Frais de service BAVI LEO | 1,00 € |
| **Total facturé** | **1,01 €** |

---

## ① CADRAGE

**Demande :** Créer un bureau BAVI dédié à l'assistance à la rédaction du mémoire de fin d'études d'Émile, sur des aspects pédagogiques. Le bot doit fonctionner comme le « bot voyage » de Sylvie : un assistant spécialisé avec personnalité, contexte persistant et instructions système dédiées.

**Utilisatrice :** Émile (fille de Christophe), étudiante
**Domaine :** Pédagogie / Sciences de l'éducation
**Livrable :** Mémoire de fin d'études (50-150 pages)

**Type de livrable :** Analyse (①→③→⑤→⑥→⑦)

---

## ③ PRODUCTION

### Concept du Bureau Mémoire

| Élément | Description |
|---|---|
| **Nom proposé** | Bureau Émile — Assistant Pédagogique 🎓 |
| **Type** | Bureau spécialisé mono-utilisateur |
| **Modèle** | DeepSeek v4 Flash (via API LEO) |
| **Fallback** | Gemini 3.5 Flash (contexte 1M) |
| **Pattern** | Inspiré du « bot voyage » (Bureau Sylvie) |

### Différences avec le bot voyage

| Aspect | Bot Voyage (Sylvie) | Bot Mémoire (Émile) |
|---|---|---|
| **Domaine** | Camping-car, itinéraires, réservations | Pédagogie, recherche, rédaction académique |
| **Personnalité** | Conseiller voyage pratique | Tuteur académique rigoureux et encourageant |
| **Contexte** | Roadbook par voyage | Plan de mémoire, chapitres, bibliographie |
| **Tâches** | Trouver campings, calculer étapes | Structurer plan, rédiger, relire, citer |
| **Session** | 1 roadbook = 1 conversation | 1 chapitre = 1 session (ou session continue) |
| **Livrable final** | Roadbook PDF | Mémoire complet |

### Système prompt — Assistant Mémoire

```markdown
Tu es un assistant pédagogique spécialisé dans l'accompagnement 
à la rédaction de mémoires de fin d'études. Ton interlocutrice 
est Émile, une étudiante en sciences de l'éducation.

TON RÔLE :
- Aider à structurer le plan du mémoire
- Proposer des axes de recherche et des problématiques
- Relire et améliorer des passages rédigés (clarté, rigueur)
- Suggérer des formulations académiques
- Vérifier la cohérence des arguments
- Aider à la mise en forme des citations et de la bibliographie

TON COMPORTEMENT :
- Encourageant mais exigeant — tu vises l'excellence académique
- Pédagogue : tu expliques POURQUOI une formulation est meilleure
- Rigoureux : tu signales les imprécisions, les affirmations non étayées
- Concis : tu vas à l'essentiel, pas de blabla
- Respectueux du travail d'Émile : tu suggères, tu n'imposes pas

LIMITES :
- Tu ne rédiges PAS le mémoire à sa place
- Tu ne fais PAS de recherche documentaire externe (pas de web)
- Tu ne cites PAS d'auteurs sans vérification
- Tu travailles avec le contenu qu'Émile te fournit
```

### Sessions types

| Session | Contenu fourni par Émile | Rôle du bot |
|---|---|---|
| **Structuration** | Thème, idées générales | Aider à bâtir le plan, formuler la problématique |
| **Rédaction** | Brouillon de chapitre | Relire, améliorer, suggérer des reformulations |
| **Argumentation** | Idée/thèse à défendre | Aider à structurer l'argumentation, trouver des failles |
| **Relecture finale** | Chapitre complet | Vérifier cohérence, orthographe, style académique |
| **Bibliographie** | Liste de sources | Aider au formatage (APA, etc.) |

### Infra technique

| Élément | Solution |
|---|---|
| **Interface** | Bot Telegram (nouveau ou profil existant) |
| **Primaire** | DeepSeek v4 Flash (128K, suffisant pour un chapitre) |
| **Fallback** | Gemini 3.5 Flash (1M, si chapitre > 128K) |
| **Contexte** | Envoyer le plan + le chapitre en cours à chaque session |
| **Stockage** | Les brouillons restent chez Émile (Google Docs, Drive) |

---

## ⑤ SYNTHÈSE

🟢 **Go — Bureau viable et utile**

**Forces du concept :**
- Pattern éprouvé (bot voyage) — simple à adapter
- DeepSeek v4 Flash suffisant pour du texte académique (128K = ~100 pages)
- Coût quasi nul pour l'étudiante (< 0,50€/session)
- Système prompt dédié = personnalité cohérente, pas de dérive
- Émile garde le contrôle : le bot suggère, elle écrit

**Points d'attention :**
- Le bot ne remplace pas un directeur de mémoire — c'est un assistant
- Pas de recherche web externe = limite assumée (évite les hallucinations)
- Si le mémoire dépasse 100 pages, Gemini 3.5 Flash prend le relais (1M)

---

## ⑥ LIVRABLE

| # | Action | Priorité | Effort |
|---|--------|:--------:|:------:|
| 1 | Rédiger et tester le système prompt « Assistant Mémoire » | 🔴 Haute | 2h |
| 2 | Configurer le profil Hermes ou le bot Telegram | 🔴 Haute | 1h |
| 3 | Créer la structure Bureau Émile dans BAVI | 🟡 Moyenne | 30min |
| 4 | Test réel avec Émile sur un extrait de son mémoire | 🔴 Haute | 1h |
| 5 | Ajuster le prompt après feedback | 🟡 Moyenne | 1h |
| 6 | Ajouter le bureau à la nav BAVI_LEO | 🟢 Basse | 15min |

---

## ⑦ ARCHIVAGE

- **Fichier :** `/opt/data/hermes-christophe/BAVI/AGENT-PRO/bureau-michel/analyse-bureau-memoire-20260625.md`
- **Bureau proposé :** Bureau Émile — Assistant Pédagogique 🎓
- **Prochaine étape :** Rédaction du système prompt + test avec Émile

---

*Analyse produite par BAVI LEO — Bureau Michel — Infra_Hermes 🔧 — 25/06/2026*
