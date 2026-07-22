---
date: 2026-06-27
bureau: bureau-robert
auteur: LEO + Robert
version: v1
modele: deepseek-v4-flash
tags: [robert, emile, analyse, business, bpmn, data-flow, architecture, education]
statut: finalise
type: analyse
---

# 🎓 Analyse Business & Fonctionnelle — Bot Emile (Assistant Pédagogique)

> **Bureau :** 🏛️ Robert — Conseil Stratégique IT | **Date :** 27/06/2026
> **Sujet :** Analyse du bot Émile, assistant pédagogique pour mémoire de fin d'études

---

## 1. 🎯 Présentation

### 1.1 Contexte

**Émile** est un assistant pédagogique dédié à l'accompagnement d'Émilie (emidanhier@gmail.com) pour son **mémoire de fin d'études en sciences de l'éducation**. Accessible via un profil Hermes dédié (`emile`), il combine un wiki MkDocs, un Drive partagé et un bot Telegram pour offrir un environnement de travail complet.

### 1.2 Objectifs

| Objectif | Description |
|:---------|:------------|
| 📚 **Assister** la rédaction du mémoire de fin d'études |
| 📝 **Relire** et améliorer les chapitres (relecture critique) |
| 🔗 **Syncer** les brouillons Drive → Wiki (cron horaire) |
| 📖 **Publier** le wiki MkDocs sur GitHub Pages |
| 💬 **Répondre** aux questions sur le contenu, la méthodologie |

### 1.3 Public cible

| Utilisateur | Rôle | Accès |
|:------------|:-----|:------|
| 🧑‍🎓 **Émilie** (étudiante) | Rédactrice du mémoire | Bot Telegram + Drive partagé |
| 🧑‍✈️ **Christophe** | Superviseur, propriétaire | Bot Telegram + Drive owner |
| 🔧 **Michel** | Infrastructure (cron, sync) | Skill Emile + scripts |

### 1.4 Chiffres clés

| Indicateur | Valeur |
|:-----------|:------:|
| Modèle | DeepSeek V4 Flash |
| Fallback | Gemini 3.5 |
| Wiki | https://christophedanhier-hash.github.io/emile-wiki/ |
| Drive partagé | bavi/bureau-emile |
| Sync cron | Horaire (Drive → Wiki) |
| Utilisateur actif | 1 (Émilie) |
| Référent technique | Michel (Infra_Hermes) |

---

## 2. 🏗️ Architecture technique

### 2.1 Diagramme d'architecture

```mermaid
graph TB
    subgraph "👤 Utilisateur"
        E[🧑‍🎓 Emilie<br/>Etudiante]
        D[📱 Drive partage<br/>emidanhier@gmail.com]
    end

    subgraph "🤖 Bot Emile"
        BE[Agent Emile<br/>Profil emile<br/>DeepSeek Flash]
        SK[Skill bureau-emile<br/>Assistant pedagogique]
    end

    subgraph "🔄 Infrastructure"
        CS[Cron sync<br/>Drive → Wiki<br/>Toutes les heures]
        LC[🔧 Michel<br/>Maintenance infra]
    end

    subgraph "📚 Contenu"
        DRV[Drive Google<br/>bavi/bureau-emile]
        GH[GitHub<br/>emile-wiki]
        WP[Wiki GH Pages<br/>emile-wiki/]
    end

    E -->|questions| BE
    E -->|brouillons Word| D
    D --> DRV
    DRV -->|cron horaire| CS
    CS -->|conversion .docx → .md| GH
    GH -->|deploiement| WP
    BE -->|lit contexte| WP
    LC -->|maintenance| CS
    LC -->|gère infra| BE

    style E fill:#e3f2fd,stroke:#1976d2
    style BE fill:#fff3e0,stroke:#f57c00
    style DRV fill:#f3e5f5,stroke:#7b1fa2
    style WP fill:#c8e6c9,stroke:#388e3c
    style LC fill:#e8f5e9,stroke:#388e3c
```

### 2.2 Stack technique

| Composant | Technologie | Rôle |
|:----------|:------------|:-----|
| **Agent** | Hermes Agent (profil `emile`) | Exécution du bot |
| **Modèle** | DeepSeek V4 Flash ($0,15/$0,60 M) | Inférence |
| **Fallback** | Gemini 3.5 | Si DeepSeek indisponible |
| **Transport** | Telegram API | Interface Émilie |
| **Wiki** | GitHub Pages (`emile-wiki`) | Publication du mémoire |
| **Stockage** | Google Drive (`bavi/bureau-emile`) | Brouillons, sources |
| **Sync** | Hermes cron (horaire) | Conversion Drive → Wiki |
| **Infra** | Michel (profil leo-copilot) | Maintenance, déploiement |

---

## 3. 🔄 Flux fonctionnels

### 3.1 Processus de travail — BPMN

```mermaid
flowchart TD
    E[🧑‍🎓 Emilie] -->|ecrit brouillon Word| DRV[📁 Drive bureau-emile]
    DRV -->|cron horaire| CONV[🔄 Conversion .docx → .md]
    CONV --> GH[📦 GitHub emile-wiki]
    GH -->|deploiement| WP[🌐 Wiki en ligne]
    
    E -->|pose question| BE[🤖 Bot Emile]
    BE -->|① Cadrage| Q{Type de demande?}
    
    Q -->|Relire chapitre| READ[📖 Charge .md du wiki]
    READ --> ANALYSE[🧠 Analyse critique]
    ANALYSE --> REPONSE[💬 Retour structure, forme, fond]
    REPONSE --> WIKI[📝 Mise a jour wiki si besoin]
    
    Q -->|Methodologie| METH[📋 Conseil methodologique]
    METH --> REPONSE
    
    Q -->|Correction orthographe| CORR[✏️ Correction]
    CORR --> REPONSE
    
    WIKI --> FIN([Fin])
    REPONSE --> FIN
    
    style E fill:#e3f2fd,stroke:#1976d2
    style BE fill:#fff3e0,stroke:#f57c00
    style WP fill:#c8e6c9,stroke:#388e3c
    style DRV fill:#f3e5f5,stroke:#7b1fa2
    style CONV fill:#e8f5e9,stroke:#388e3c
```

### 3.2 Flux de données

```mermaid
flowchart LR
    subgraph "📥 Entrees"
        I1[📄 Brouillon .docx<br/>Drive Emilie]
        I2[💬 Question Telegram<br/>Relecture, methode]
        I3[📚 Sources academiques<br/>Web, PDF]
    end

    subgraph "⚙️ Traitement Emile"
        T1[🔁 Conversion<br/>.docx → .md]
        T2[🧠 Analyse chapitre<br/>DeepSeek Flash]
        T3[📋 Relecture critique<br/>Fond, forme, structure]
        T4[📝 Correction<br/>Orthographe, style]
    end

    subgraph "📤 Sorties"
        O1[🌐 Wiki mis a jour<br/>emile-wiki/]
        O2[💬 Retour dans chat<br/>Telegram]
        O3[📄 Chapitre corrige<br/>.md dans wiki]
    end

    I1 --> T1
    T1 --> O1
    I2 --> T2
    I2 --> T4
    I3 --> T3
    
    T2 --> O2
    T3 --> O2
    T4 --> O3
    O3 --> O1

    style I1 fill:#e3f2fd
    style I2 fill:#e3f2fd
    style O1 fill:#c8e6c9
    style O2 fill:#c8e6c9
```

### 3.3 Cycle de vie d'un chapitre

```mermaid
flowchart TD
    DEBUT([Brouillon Emilie]) --> DRV[📁 Drive<br/>brouillon.docx]
    DRV --> CRON[⏰ Sync horaire]
    CRON --> CONV[🔄 Conversion]
    CONV --> WIKI[🌐 Wiki .md]
    WIKI --> DEMANDE{Emilie demande<br/>relecture?}
    DEMANDE -->|Oui| ANALYSE[🧠 Analyse Emile]
    ANALYSE --> RETOUR[💬 Retour chat]
    RETOUR --> MODIF[✏️ Emilie modifie]
    MODIF --> DRV
    DEMANDE -->|Non| OK[✅ Pret]
```

---

## 4. 💳 Modèle économique

### 4.1 Coûts de fonctionnement

| Poste | Coût | Fréquence |
|:------|:----:|:---------|
| **DeepSeek Flash** (inférence) | ~0,02 €/session | Hebdomadaire |
| **Gemini 3.5** (fallback) | **0 €** | Rare |
| **GitHub Pages** (wiki) | **0 €** | Continue |
| **Drive** (stockage) | **0 €** | Continue |
| **Sync cron** (conversion) | **0 €** | Horaire |
| **Total mensuel** | **~0,10 €** | |

### 4.2 Facturation

| Service | Tarif | Payé par |
|:--------|:-----:|:---------|
| Accès bot + wiki | **0 €** (accompagnement) | Émilie |
| Relecture chapitre | Inclus | Émilie |
| Infrastructure (sync, cron, hébergement) | **0 €** | Christophe (infra) |

> Le bot Emile est un service gratuit dans l'écosystème BAVI — l'infrastructure est mutualisée avec les autres bots.

---

## 5. 🚫 Périmètre fonctionnel

### 5.1 Ce que Emile fait

| Fonction | Statut | Détail |
|:---------|:------:|:-------|
| Relecture critique chapitres | ✅ Actif | Fond, forme, structure |
| Correction orthographe/style | ✅ Actif | Grammaire, syntaxe |
| Conseil méthodologique | ✅ Actif | Méthodologie mémoire |
| Sync Drive → Wiki | ✅ Actif | Cron horaire |
| Wiki à jour | ✅ Actif | GitHub Pages |

### 5.2 Ce que Emile ne fait pas

| Fonction | Raison | Qui le fait |
|:---------|:-------|:------------|
| Roadbooks voyage | Hors scope | 🧭 Sylvia |
| Analyse infra | Hors scope | 🔧 Michel |
| Conseil IT stratégique | Hors scope | 🏛️ Robert |
| Envoi emails | Hors scope | 🤖 LEO |

---

## 6. 📊 Indicateurs clés

| KPI | Valeur | Objectif |
|:----|:------:|:--------:|
| Chapitres relus | 0 | 5+ |
| Sync Drive → Wiki OK | ✅ Actif | 100 % |
| Temps de réponse | <5s | <10s |
| Uptime bot | ✅ Actif | >99 % |
| Wiki déployé | ✅ emile-wiki/ | Accessible |

---

## 7. 🔗 Relations avec les autres bots

```mermaid
flowchart LR
    E[🎓 Emile<br/>Etudes] -->|lit contexte| W[🌐 emile-wiki]
    E -->|depend infra| LC[🔧 Michel<br/>Infra]
    LC -->|gère sync cron| E
    L[🤖 LEO<br/>Central] -->|source de verite| SK[📋 Skill Emile]
```

---

## 8. 📈 Évolutions possibles

| Évolution | Impact | Complexité |
|:----------|:------:|:----------:|
| 🤖 Relecture automatique à chaque sync | Fort | Moyenne |
| 📊 Suivi d'avancement (chapitres relus) | Moyen | Faible |
| 🔍 Détection de plagiat (API externe) | Moyen | Élevée |
| 📝 Génération de bibliographie automatique | Moyen | Faible |
| 🗓️ Planning de rédaction | Faible | Faible |

---

## Versions

| Version | Date | Auteur | Description |
|:--------|:-----|:-------|:------------|
| v1 | 27/06/2026 | LEO + Robert | Version initiale — analyse business bot Emile |

---

*Analyse produite par 🏛️ Bureau Robert — BAVI LEO*

> 🤖 Dernier audit : 22 July 2026 à 07:40 (UTC+2)

