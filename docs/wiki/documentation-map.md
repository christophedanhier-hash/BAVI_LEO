# 🗺️ Carte Documentaire — BAVI LEO

> **Usage** : quand une analyse ou documentation système impacte BAVI, cette carte indique **quelles pages** doivent être mises à jour.
> **Règle** : toute modification d'un bureau ou de l'infrastructure → mettre à jour cette carte ET les pages impactées dans le même mouvement.

## 📄 Pages du portail

| # | Page | Contenu | Pages liées | Statut |
|:-:|:-----|:--------|:-----------:|:------:|
| 1 | `index.md` | Portail BAVI, présentation des 8 bureaux, architecture | Toutes | ✅ |
| 2 | `skills.md` | Catalogue des 125 skills LEO — *section AUTO* | 1, guide | ✅ |
| 3 | `guide-utilisation.md` | Guide d'utilisation BAVI, navigation inter-wikis | 1 | ✅ |
| 4 | `wiki/crons.md` | 37 crons automatisés — *section AUTO* | bureau-michel | ✅ |

## 🧠 Bureaux Agent Pro — 8 bureaux, ~46 pages

### Bureau Léo — Hermes Agent

| Page | Contenu | Pages liées | Statut |
|:-----|:--------|:-----------:|:------:|
| `bureau-leo/index.md` | Présentation bureau Léo (accueil) | Tous bureaux | ✅ |
| `bureau-leo/guide-hermes-complet.md` | Guide Hermes complet v3.2 — 6 414 lignes | 1, skills | ✅ |
| `bureau-leo/dossiers/dossier-skoda-enyaq.md` | Dossier leasing Skoda Enyaq | bureau-michel | ✅ |
| `bureau-leo/etude-marche-quad-biplace.md` | Étude marché quad biplace | — | ✅ |
| `bureau-leo/archive/analyse-bot-leo-hub.md` | Analyse bot LEO Hub (archive) | — | 📦 |

### Bureau Gérard — OCA Astronomie (T600)

| Page | Contenu | Pages liées | Statut |
|:-----|:--------|:-----------:|:------:|
| `bureau-gerard/index.md` | Présentation bureau Gérard | — | ✅ |
| `bureau-gerard/t600/document-reference-t600.md` | Documentation technique T600 — 1 135 lignes | formation, risques | ✅ |
| `bureau-gerard/t600/formation-operateur-t600.md` | Formation opérateur T600 — 774 lignes | document-ref | ✅ |
| `bureau-gerard/t600/analyse-risques-t600.md` | Analyse risques T600 — 917 lignes | document-ref | ✅ |

### Bureau Michel — Infrastructure Hermes

| Page | Contenu | Pages liées | Statut |
|:-----|:--------|:-----------:|:------:|
| `bureau-michel/index.md` | Présentation bureau Michel | Toutes infra | ✅ |
| `bureau-michel/analyse-acces-credentials-20260630.md` | Audit accès/credentials | pra-recovery | ✅ |
| `bureau-michel/analyse-bureau-memoire-20260625.md` | Analyse mémoire partagée | — | ✅ |
| `bureau-michel/analyse-processus-bpmn-20260701.md` | Analyse processus BPMN | — | ✅ |
| `bureau-michel/audit-penguin-2026-06-28.md` | Audit machine Penguin | — | ✅ |
| `bureau-michel/pra-leo-recovery-20260629.md` | Plan reprise activité LEO | credentials | ✅ |
| `bureau-michel/prompt-kilo-code-tofdan.md` | Prompt Kilo Code | — | ✅ |
| `bureau-michel/rapport-audit-leo-2026-07-05.md` | Rapport audit LEO juillet | — | ✅ |
| `bureau-michel/n8n/ping-workflow.md` | Workflow n8n Ping | — | ✅ |
| `bureau-michel/n8n/rapport-n8n-leo-20260619.md` | Rapport n8n LEO | — | ✅ |
| `bureau-michel/archive/` (10 fichiers) | Anciennes analyses pré-crash | — | 📦 |

### Bureau Robert — Stratégie

| Page | Contenu | Pages liées | Statut |
|:-----|:--------|:-----------:|:------:|
| `bureau-robert/index.md` | Présentation bureau Robert | — | ✅ |

### Bureau Sophie — Finance

| Page | Contenu | Pages liées | Statut |
|:-----|:--------|:-----------:|:------:|
| `bureau-sophie/index.md` | Présentation bureau Sophie | — | ✅ |

### Bureau Sylvia — Voyages

| Page | Contenu | Pages liées | Statut |
|:-----|:--------|:-----------:|:------:|
| `bureau-sylvia/index.md` | Présentation bureau Sylvia (Voyages) | — | ✅ |
| `bureau-sylvia/analyse-bot-voyage-sylvia.md` | Analyse bot voyage Sylvia | — | ✅ |
| ~~`bureau-sylvie/index.md`~~ | **SUPPRIMER** — doublon de bureau-sylvia | — | ❌ |
| ~~`bureau-sylvie/README.md`~~ | **SUPPRIMER** — doublon de bureau-sylvia | — | ❌ |

### Bureau Émile — Mémoire

| Page | Contenu | Pages liées | Statut |
|:-----|:--------|:-----------:|:------:|
| `bureau-emile/index.md` | Présentation bureau Émile (Mémoire) | — | ✅ |
| `bureau-emile/analyse-bot-emile.md` | Analyse bot Émile assistant pédagogique | — | ✅ |

### Bureau Virginie — Médical

| Page | Contenu | Pages liées | Statut |
|:-----|:--------|:-----------:|:------:|
| `bureau-virginie/index.md` | Présentation bureau Virginie (Médical) | — | ✅ |
| `bureau-virginie/consultation-sylvie-michaux.md` | Consultation médicale Sylvie Michaux | — | ✅ |

## 🔗 Graphe de dépendances

```
index.md (portail)
  → skills.md              ← Catalogue skills, section AUTO
  → guide-utilisation.md   ← Guide utilisateur
  → wiki/crons.md          ← Crons, section AUTO
  → Tous les index bureaux ← Liens vers chaque bureau

wiki/crons.md
  → bureau-michel/         ← Monitoring infra, watchdogs
  → bureau-leo/index.md    ← Architecture LEO

skills.md
  → bureau-leo/guide-hermes-complet.md  ← Référence skills
  → guide-utilisation.md               ← Utilisation

bureau-michel/analyse-acces-credentials.md
  → bureau-michel/pra-leo-recovery.md  ← PRA dépends des credentials

bureau-gerard/t600/document-reference-t600.md
  → bureau-gerard/t600/formation-operateur-t600.md
  → bureau-gerard/t600/analyse-risques-t600.md
```

## 📋 Checklist — Quand tu modifies...

| Tu changes... | Pages à vérifier |
|:--------------|:-----------------|
| **Ajout/suppression d'un bureau** | `index.md`, `wiki/agent-pro/index.md` |
| **Nouveau cron** | `wiki/crons.md`, `bureau-michel/` |
| **Nouveau skill** | `skills.md`, `bureau-leo/guide-hermes-complet.md` |
| **Modification guide** | `bureau-leo/guide-hermes-complet.md`, `guide-utilisation.md` |
| **Analyse infrastructure** | `bureau-michel/` (créer page dans le bon dossier) |
| **Document T600** | `bureau-gerard/t600/` (document-ref + formation + risques) |

## 🧹 Pages orphelines / à nettoyer

| Page | Problème |
|:-----|:---------|
| `bureau-sylvie/index.md` | Doublon de `bureau-sylvia/index.md` — à supprimer |
| `bureau-sylvie/README.md` | Doublon de `bureau-sylvia/` — à supprimer |

---

*Document créé le 07/07/2026 — Léo 🦁*
