---
date: 2026-06-25
bureau: bureau-michel
version: v2.0
modele: deepseek-v4-pro
tags: [memoire, emile, pedagogique, bureau, bot, assistant, wiki, mermaid, analyse]
statut: analyse
type: analyse
---

# Analyse — Bureau Émile : Assistant Pédagogique + Wiki + Sources

**Bureau :** Michel — Infra_Hermes 🔧 | **Version :** v2.0
**Date :** 25/06/2026 | **Type :** Analyse (①→③→⑤→⑥→⑦)

---

## 💳 Coût du service BAVI LEO

| Métrique | Valeur |
|:---------|------:|
| Sessions LEO | 1 |
| Tokens consommés | ~15K IN · ~6K OUT |
| Coût DeepSeek réel | **~0,02 €** |
| Frais de service BAVI LEO | 1,00 € |
| **Total facturé** | **1,02 €** |

---

## ① CADRAGE

**Demande complète :**
Mettre à jour le document avec les nouvelles informations sur les profils/bots et la technologie utilisée.

**Utilisatrice :** Émile, étudiante en sciences de l'éducation
**Livrable final :** Mémoire de fin d'études (50-150 pages)

---

## ③ PRODUCTION

### Ajouter les détails spécifiés en réalité à l'architecture globale.

```mermaid
flowchart TB
    subgraph Utilisatrice["👩‍🎓 Émile"]
        TG[Bot Telegram]
        WK[Wiki Émile]
    end

    subgraph Sources["📚 Sources de contexte"]
        PLAN[Plan de mémoire]
        BROU[Brouillons chapitres]
        BIBLIO[Bibliographie]
        NOTES[Notes de recherche]
        PROF[Retours directeur]
    end

    subgraph LEO["🖥️ LEO - Infra Hermes"]
        BOT[Bot Hermes - Profil Émile]
        DS[DeepSeek v4 Flash]
        GM[Gemini 3.5 Flash]
        WIKI[Wiki MkDocs - Mémoire Émile]
        GH[GitHub Pages]
    end

    TG <-->|chat| BOT
    WK -->|lecture docs| WIKI
    BOT -->|primaire| DS
    BOT -->|fallback >128K| GM
    WIKI --> GH
    BOT -->|lit| WIKI
    
    PLAN -->|alimente| BOT
    BROU -->|alimente| BOT
    BIBLIO -->|alimente| BOT
    NOTES -->|alimente| BOT
    PROF -->|alimente| BOT
    PLAN -->|publié sur| WIKI
    BROU -->|publié sur| WIKI
```

### Le Bot Telegram — Fonctionnement

```mermaid
sequenceDiagram
    participant E as 👩‍🎓 Émile
    participant BOT as 🤖 Bot Mémoire
    participant DS as 🧠 DeepSeek Flash
    participant GM as 🌐 Gemini 3.5
    participant WIKI as 📖 Wiki Émile

    E->>BOT: "Peux-tu relire mon chapitre 2 ?"
    BOT->>WIKI: Charger plan + chapitre 2
    WIKI-->>BOT: Plan.md + Chapitre2.md
    BOT->>DS: [Système prompt + plan + chapitre]
    
    alt Chapitre < 128K tokens
        DS-->>BOT: Analyse, suggestions
    else Chapitre > 128K tokens
        BOT->>GM: [Même contexte]
        GM-->>BOT: Analyse, suggestions
    end
    
    BOT-->>E: "Voici mes suggestions : ..."
    E->>E: Modifie son brouillon
    E->>WIKI: Met à jour Chapitre2.md
```

### Session type — Cycle complet

```mermaid
flowchart LR
    A[📝 Émile écrit un brouillon] --> B[💾 Sauve sur Drive/PC]
    B --> C[📤 Demande au bot de relire]
    C --> D{⚠️ Besoin mise à jour wiki ?}
    D -->|Oui| E[🔄 Sync Drive → Wiki GitHub]
    D -->|Non| F[🤖 Bot charge le contexte]
    E --> F
    F --> G{📏 Contexte > 128K ?}
    G -->|Non| H[🧠 DeepSeek analyse]
    G -->|Oui| I[🌐 Gemini analyse]
    H --> J[💬 Suggestions envoyées à Émile]
    I --> J
    J --> K[✏️ Émile applique les corrections]
    K --> A
```

### Le Wiki Émile — Structure

Un wiki MkDocs dédié, hébergé sur GitHub Pages, accessible 24/7. Même pattern que les autres wikis BAVI (voyages, OCA, hermes-wiki).

```
emile-wiki/                      → Nouveau dépôt GitHub
├── docs/
│   ├── index.md                 → Accueil : présentation, mode d'emploi
│   ├── plan.md                  → Plan du mémoire (problématique, axes)
│   ├── chapitres/
│   │   ├── chapitre1.md         → Introduction
│   │   ├── chapitre2.md         → Cadre théorique
│   │   ├── chapitre3.md         → Méthodologie
│   │   ├── chapitre4.md         → Résultats
│   │   └── chapitre5.md         → Discussion
│   ├── bibliographie.md         → Références (format APA)
│   ├── notes.md                 → Notes de recherche, idées
│   └── retours-directeur.md     → Commentaires du directeur de mémoire
├── mkdocs.yml                   → Configuration MkDocs Material
└── .github/workflows/deploy.yml → Déploiement auto sur GitHub Pages
```

**URL :** `https://christophedanhier-hash.github.io/emile-wiki/`

```mermaid
flowchart TB
    subgraph Drive["Google Drive (Émile)"]
        D1[Chapitre2.docx]
        D2[Notes de recherche]
    end

    subgraph GitHub["emile-wiki"]
        G1[chapitres/chapitre2.md]
        G2[notes.md]
    end

    subgraph Wiki["🌐 emile-wiki GitHub Pages"]
        W1[Chapitre 2 en HTML]
        W2[Notes en HTML]
    end

    subgraph Bot["🤖 Bot Mémoire"]
        BT[Contexte chargé]
    end

    D1 -->|sync Drive→GitHub| G1
    D2 -->|sync Drive→GitHub| G2
    G1 -->|MkDocs build| W1
    G2 -->|MkDocs build| W2
    W1 -->|bot lit le wiki| BT
    W2 -->|bot lit le wiki| BT
```

### Sources et alimentation du contexte

Le bot a besoin de contexte pour être pertinent. Trois mécanismes :

```mermaid
flowchart TB
    subgraph M1["① Contexte direct (chat)"]
        C1[Émile copie-colle un extrait]
        C2[Bot lit le message]
        C1 --> C2
    end

    subgraph M2["② Contexte wiki (automatique)"]
        W1[Émile mentionne un chapitre]
        W2[Bot fetch le .md depuis emile-wiki]
        W3[Contexte ajouté au prompt]
        W1 --> W2 --> W3
    end

    subgraph M3["③ Contexte Drive sync (automatique)"]
        D1[Émile sauve dans Drive]
        D2[Cron Drive→GitHub sync]
        D3[Wiki mis à jour]
        D4[Bot lit la dernière version]
        D1 --> D2 --> D3 --> D4
    end

    M1 --> BT[Prompt final envoyé au modèle]
    M2 --> BT
    M3 --> BT
```

| Mécanisme | Quand | Avantage | Inconvénient |
|---|---|---|---|
| ① Direct | Questions rapides, petits extraits | Immédiat | Limité en taille, manuel |
| ② Wiki | Relecture de chapitre complet | Automatique, versionné | Nécessite wiki à jour |
| ③ Drive sync | Émile travaille hors ligne, synchro ensuite | Transparent pour Émile | Latence (cron) |

### Règle de bascule DeepSeek → Gemini

```mermaid
flowchart TD
    REQ[Requête d'Émile] --> COUNT{Taille contexte}
    COUNT -->|< 128K tokens| DS[🧠 DeepSeek v4 Flash]
    COUNT -->|> 128K tokens| GM[🌐 Gemini 3.5 Flash]
    DS --> OK{Succès ?}
    OK -->|✅| REP[💬 Réponse à Émile]
    OK -->|❌ erreur| GM
    GM --> REP
```

---

## ⑤ SYNTHÈSE

🟢 **Go — Écosystème complet prêt à déployer**

L'architecture couvre tout le cycle :
1. **Émile écrit** → ses brouillons (Word, Google Docs)
2. **Sync automatique** → Drive → GitHub → wiki MkDocs
3. **Bot Telegram** → lit le wiki, charge le contexte, assiste via DeepSeek
4. **Fallback Gemini** → si chapitre > 128K tokens (~100 pages)
5. **Émile corrige** → cycle recommence

**Points forts :**
- Wiki dédié accessible 24/7 (GitHub Pages, gratuit)
- Bot toujours à jour (lit le wiki, pas de copier-coller)
- Pattern éprouvé (bot voyage Sylvie + sync Drive existante)
- Émile garde le contrôle total de son contenu

---

## ⑥ LIVRABLE — Plan d'implémentation

| # | Action | Priorité | Effort |
|---|--------|:--------:|:------:|
| 1 | Créer le dépôt `emile-wiki` sur GitHub | 🔴 Haute | 15min |
| 2 | Créer la structure MkDocs + template | 🔴 Haute | 30min |
| 3 | Déployer GitHub Pages | 🔴 Haute | 10min |
| 4 | Créer le profil Hermes « Émile » + système prompt | 🔴 Haute | 2h |
| 5 | Connecter le bot au wiki (lecture .md) | 🔴 Haute | 1h |
| 6 | Ajouter la sync Drive → emile-wiki (cron/n8n) | 🟡 Moyenne | 1h |
| 7 | Configurer fallback Gemini 3.5 (>128K) | 🟡 Moyenne | 30min |
| 8 | Test réel avec Émile — session relecture | 🔴 Haute | 1h |
| 9 | Ajouter emile-wiki à la nav BAVI LEO | 🟢 Basse | 15min |

---

## ⑦ ARCHIVAGE

- **Fichier :** `~/Projets_Dev/hermes-christophe/BAVI/AGENT-PRO/bureau-michel/analyse-bureau-memoire-20260625.md`
- **Wiki BAVI :** Agent Pro → Bureau Michel — Infra_Hermes
- **Dépôt à créer :** `emile-wiki` → ✅ [Créé](https://github.com/christophedanhier-hash/emile-wiki) le 26/06/2026
- **Dossier Drive :** `bavi/bureau-emilie` → ✅ Créé et partagé avec Émile le 26/06/2026 — elle y dépose ses documents (brouillons, notes, sources)
- **Profil Hermes à créer :** `emile` (ou intégré au bot existant)

---

## 📋 Avancement final (26/06/2026) — ✅ IMPLÉMENTÉ

| # | Action | Statut |
|---|--------|:------:|
| 0 | Dossier Drive `bavi/bureau-emilie` partagé avec Émile | ✅ |
| 1 | Dépôt `emile-wiki` + structure MkDocs (12 fichiers) | ✅ |
| 2 | GitHub Pages déployé | ✅ |
| 3 | Profil Hermes `emile` + SOUL.md + fallback Gemini | ✅ |
| 4 | Skill `bureau-emile` | ✅ |
| 5 | Nav BAVI LEO + page wiki bureau | ✅ |
| 6 | Bot Telegram `@Bureau_ia_emilie_bot` | ✅ |
| 7 | Gateway s6-supervisé + polling Telegram | ✅ |
| 8 | Cron Drive sync → emile-wiki (placeholder) | ✅ |
| 9 | Test réel — Christophe travaille avec le bot | ✅ En cours |

**URLs actives :**
- 🤖 Bot : [@Bureau_ia_emilie_bot](https://t.me/Bureau_ia_emilie_bot)
- 📖 Wiki : https://christophedanhier-hash.github.io/emile-wiki/ (HTTP 200)
- 🧠 Profil : `~/.hermes/profiles/emile/` (DeepSeek Flash + Gemini fallback, s6-supervisé)
- 📁 Drive : `bavi/bureau-emilie` (partagé avec Émilie Danhier)
- 🏛️ BAVI LEO : nav `🎓 Bureau Émile — Mémoire`

**Profil technique :**
- Modèle : DeepSeek v4 Flash (primaire) → Gemini 3.5 Flash (fallback >128K)
- Gateway : s6-supervisé (`/run/service/gateway-emile`)
- Token : stocké dans `~/.hermes/profiles/emile/.env`
- Logs : `~/Projets_Dev/logs/gateways/emile/`

*Analyse produite par BAVI LEO — Bureau Michel — Infra_Hermes 🔧 — 25/06/2026, implémenté et documenté 26/06/2026*

> 🤖 Dernier audit : 24/07/2026 à 11:45 (UTC+2)
