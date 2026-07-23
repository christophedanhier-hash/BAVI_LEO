---
date: 2026-06-27
bureau: bureau-robert
auteur: LEO + Robert
version: v1
modele: deepseek-v4-flash
tags: [robert, leo, analyse, business, bpmn, data-flow, architecture, gouvernance]
statut: finalise
type: analyse
---

# 🤖 Analyse Business & Fonctionnelle — LEO (Bureau Central)

> **Bureau :** 🏛️ Robert — Conseil Stratégique IT | **Date :** 27/06/2026
> **Sujet :** Analyse du bot LEO Hermes, hub central BAVI, gouvernance des bureaux

---

## 1. 🎯 Présentation

### 1.1 Contexte

**LEO** est l'ensemble des profils agentiques centraux de l'écosystème BAVI (Bureaux Agentiques Virtuels). Il est le point d'entrée unique de **Christophe** pour tous les sujets : documentation, analyses, emails, classification, et gouvernance des bureaux.

Contrairement aux autres bots (Sylvia pour les voyages, Michel pour l'infra, Emile pour les études), LEO est **polyvalent** et **orchestrateur** — il ne fait pas un métier, il les coordonne tous.

### 1.2 Objectifs

| Objectif | Description |
|:---------|:------------|
| 🧠 **Orchestrer** les 10 bureaux BAVI (dispatch conditionnel) |
| 📝 **Produire** des analyses, rapports, notes et dossiers |
| 📧 **Gérer** les emails (envoi LEO, lecture Christophe) |
| 📋 **Classifier** les 3240 emails de la boîte Christophe (Ollama) |
| 🏗️ **Gouverner** les skills (source de vérité, sync copilot) |
| 📚 **Documenter** dans les wikis (BAVI, Hermes, OCA) |

### 1.3 Public cible

| Utilisateur | Interaction | Fréquence |
|:------------|:------------|:---------:|
| 🧑‍✈️ **Christophe** (propriétaire) | DM Telegram quotidien | 🔴 Quotidienne |
| 🤖 **leo-copilot** (bot orchestrateur) | Sync skills + mémoire (continu) | 🔴 Quotidienne |
| 🤖 **default** (bot par défaut) | Sync skills (30 min) | 🟡 Continue |
| 🤖 **bureau-robert** (bot conseil) | Sync skills (30 min) | 🟢 Continue |
| 🤖 **bavi-leo** (bot backup) | Sync skills (30 min) | 🟢 Continue |
| 🤖 **emile** (bot études) | Sync skills (30 min) | 🟢 Continue |

### 1.4 Chiffres clés

| Indicateur | Valeur |
|:-----------|:------:|
| Sessions totales | 431 |
| Messages échangés | 13 089 |
| Bureaux gérés | 10 |
| Skills installés | 112 |
| Crons automatisés | 39 |
| Emails classifiés | 3 240 |
| Modèle | DeepSeek Flash, Qwen 2.5 7B, Gemini 3.5 Flash |

---

## 2. 🏗️ Architecture technique

### 2.1 Diagramme d'architecture

```mermaid
graph TB
    subgraph "📱 Point d entree"
        TG[Telegram<br/>DM Christophe]
    end

    subgraph "🤖 LEO Hermes"
        L[Agent LEO<br/>Profil default<br/>DeepSeek Flash]
        SK[Skills BAVI<br/>10 bureaux]
        MB[Memoire<br/>431 sessions]
        CR[Crons<br/>39 automatismes]
    end

    subgraph "🧠 Bureaux dispatches"
        R[🏛️ Robert<br/>Conseil IT]
        S[💰 Sophie<br/>Finance]
        AO[🛡️ AO<br/>Assurance]
        G[📝 Gerard<br/>T600]
        SY[🧭 Sylvia<br/>Voyages]
        M[🔧 Michel<br/>Infra]
        V[🩺 Virginie<br/>Medical]
        E[🎓 Emile<br/>Etudes]
    end

    subgraph "🔄 Sync profils"
        LC[Michel<br/>Infra]
        BV[Bot Voyage<br/>Sylvia]
        BE[Bot Emile<br/>Etudes]
    end

    TG -->|messages| L
    L -->|dispatch| R
    L -->|dispatch| S
    L -->|dispatch| AO
    L -->|dispatch| G
    L -->|dispatch| SY
    L -->|dispatch| M
    L -->|dispatch| V
    L -->|dispatch| E
    L --> SK
    L --> MB
    L --> CR
    
    SK -->|sync 30min| LC
    SK -->|sync 30min| BV
    SK -->|sync 30min| BE
```

### 2.2 Stack technique

| Composant | Technologie | Rôle |
|:----------|:------------|:-----|
| **Agent** | Hermes Agent (profil `default`) | Exécution centrale |
| **Modèle** | DeepSeek V4 Flash | Inférence quotidienne |
| **Fallback** | Gemini 3.5 Flash | Si DeepSeek indisponible |
| **Modèle local** | Ollama qwen2.5:7b | Classification emails (gratuit) |
| **Transport** | Telegram API | Interface Christophe |
| **Documentation** | GitHub Pages (BAVI_LEO, voyages-wiki, wiki-oca) | Wikis déployés |
| **Source de vérité** | hermes-christophe (GitHub + Drive) | AGENT-PRO, LEO |
| **Email** | Gmail API (2 comptes) | Envoi LEO, lecture Christophe |
| **Skills** | `/opt/data/skills/` + sync vers profils | 112 skills |

---

## 3. 🔄 Flux fonctionnels

### 3.1 Processus de travail — BPMN

```mermaid
flowchart TD
    U[👤 Christophe] -->|message Telegram| L[🤖 LEO]
    
    L -->|① Cadrage| Q{Type de demande?}
    
    Q -->|Analyse IT| R[🏛️ Active Robert]
    Q -->|Budget/Finance| S[💰 Active Sophie]
    Q -->|Voyage| SY[🧭 Redirige vers Sylvia]
    Q -->|Infra/Cron| M[🔧 Redirige vers Michel]
    Q -->|Medical| V[🩺 Active Virginie]
    Q -->|Documentation| G[📝 Active Gerard]
    Q -->|Email| EM[📧 Envoi email]
    Q -->|Classification| CL[📋 Classifie boite]
    
    R --> PROD[③ Production]
    S --> PROD
    V --> PROD
    G --> PROD
    EM --> SEND[✅ Email envoye]
    CL --> OLLAMA[🧠 Ollama<br/>gratuit]
    
    PROD --> DEL[⑥ Livrable]
    DEL --> ARCH[⑦ Archivage<br/>Wiki + Commit]
    OLLAMA --> ARCH
    
    style U fill:#e3f2fd,stroke:#1976d2
    style L fill:#fff3e0,stroke:#f57c00
    style Q fill:#fff3e0,stroke:#f57c00
    style SEND fill:#c8e6c9,stroke:#388e3c
    style OLLAMA fill:#c8e6c9,stroke:#388e3c
    style ARCH fill:#f3e5f5,stroke:#7b1fa2
```

### 3.2 Flux de données

```mermaid
flowchart LR
    subgraph "📥 Entrees"
        I1[👤 Messages Telegram]
        I2[📧 Emails Christophe<br/>Gmail API]
        I3[📁 Drive Google<br/>BAVI, LEO]
        I4[🔧 Demandes infra<br/>via Christophe]
    end

    subgraph "⚙️ Traitement LEO"
        T1[🧠 Compréhension<br/>DeepSeek Flash]
        T2[🏷️ Dispatch bureau<br/>Conditionnel]
        T3[📝 Production document<br/>Analyse/Rapport/Note]
        T4[🤖 Classification<br/>Ollama qwen2.5]
        T5[📧 Envoi email<br/>Gmail send]
        T6[🔄 Sync skills<br/>30 min]
    end

    subgraph "📤 Sorties"
        O1[💬 Reponse Telegram]
        O2[📄 Document .md<br/>AGENT-PRO]
        O3[📧 Email LEO<br/>leodanhieria]
        O4[🏷️ Labels Gmail<br/>9 categories]
        O5[📚 Wiki mis a jour<br/>GH Pages]
        O6[🔄 Skills propages<br/>Autres profils]
    end

    I1 --> T1
    I2 --> T4
    I3 --> T1
    I4 --> T1

    T1 --> T2
    T2 --> T3
    T1 --> T5
    T4 --> O4

    T3 --> O2
    T3 --> O1
    T2 --> O1
    T5 --> O3
    O2 --> O5
    T6 --> O6

    style I1 fill:#e3f2fd
    style I2 fill:#e3f2fd
    style O1 fill:#c8e6c9
    style O2 fill:#c8e6c9
    style O4 fill:#c8e6c9
    style O5 fill:#c8e6c9
    style O6 fill:#c8e6c9
```

### 3.3 Cycle de vie d'une analyse

```mermaid
flowchart TD
    START([Demande]) --> CADR[① Cadrage]
    CADR --> DISP{② Dispatch<br/>Quel bureau?}
    
    DISP -->|Expert identifie| PROD[③ Production<br/>Analyse directe]
    DISP -->|Multi-experts| DP[Parallele<br/>Delegation]
    
    PROD --> CROIS{④ Croisement<br/>Necessaire?}
    DP --> CROIS
    
    CROIS -->|Oui| CROSS[Confronter analyses]
    CROIS -->|Non| SYNTH[⑤ Synthese]
    CROSS --> SYNTH
    
    SYNTH --> LIVR[⑥ Livrable<br/>Format selon type]
    LIVR --> ARCH[⑦ Archivage<br/>AGENT-PRO + Wiki + Commit]
    ARCH --> PUSH[✅ Git Push]
    PUSH --> ENDE([Fin])
```

### 3.4 Workflow par type de livrable (LEO)

```mermaid
flowchart LR
    subgraph "📄 Analyse"
        A1[① Cadrage] --> A3[③ Production]
        A3 --> A5[⑤ Synthese]
        A5 --> A6[⑥ Livrable]
        A6 --> A7[⑦ Archivage]
    end
    
    subgraph "📋 Rapport"
        R1[①] --> R2[② Dispatch]
        R2 --> R3[③ Production]
        R3 --> R4[④ Croisement]
        R4 --> R5[⑤ Synthese]
        R5 --> R6[⑥ Livrable]
        R6 --> R7[⑦ Archivage]
    end
    
    subgraph "📝 Note"
        N1[① Cadrage] --> N3[③ Production]
        N3 --> N6[⑥ Livrable]
    end
```

---

## 4. 💳 Modèle économique

### 4.1 Coûts de fonctionnement

| Poste | Coût | Fréquence |
|:------|:----:|:---------|
| **DeepSeek V4 Flash** (inférence) | ~0,05 €/jour | Quotidien |
| **Ollama qwen2.5:7b** (classification) | **0 €** (local) | Continue |
| **GitHub Pages** (wikis) | **0 €** | Continue |
| **Gmail API** (emails) | **0 €** (quotas gratuits) | Quotidien |
| **Drive** (stockage) | **0 €** (15 Go gratuits) | Continue |
| **Total mensuel** | **~1,50 €** | |

### 4.2 Répartition du coût DeepSeek

```mermaid
pie title Repartition cout DeepSeek mensuel
    "Veille IA" : 45
    "Analyses LEO" : 30
    "Classification" : 0
    "Crons agents" : 25
```

### 4.3 Facturation (via LEO)

| Service | Tarif | Payé par |
|:--------|:-----:|:---------|
| Analyses LEO pour Christophe | Tokens IN/OUT uniquement | Christophe |
| Travaux via Robert (Conseil IT) | 2,50 € forfait | Christophe |
| Travaux via Sophie (Finance) | 2,50 € forfait | Christophe |
| Veille IA quotidienne | ~0,05 €/jour | Christophe |
| Classification emails | **0 €** (Ollama) | Christophe |

---

## 5. 🚫 Périmètre fonctionnel

### 5.1 Ce que LEO fait

| Fonction | Statut | Bureau utilisé |
|:---------|:------:|:---------------|
| Analyse stratégique IT | ✅ Actif | 🏛️ Robert |
| Analyse financière/TCO | ✅ Actif | 💰 Sophie |
| Consultation médicale | ✅ Actif | 🩺 Virginie |
| Documentation T600 | ✅ Actif | 📝 Gérard |
| Envoi emails (LEO) | ✅ Actif | Direct |
| Classification emails | ✅ Actif | Ollama + Gmail |
| Roadbooks voyage | ⏭️ Redirige | 🧭 Sylvia |
| Infrastructure/crons | ⏭️ Redirige | 🔧 Michel |
| Études/mémoire | ⏭️ Redirige | 🎓 Emile |

### 5.2 Ce que LEO ne fait pas

| Fonction | Raison | Qui le fait |
|:---------|:-------|:------------|
| Infrastructure Hermes | Spécialisation | 🔧 Michel |
| Roadbooks camping-car | Spécialisation | 🧭 Sylvia |
| Assistance mémoire | Spécialisation | 🎓 Emile |
| Maintenance Hermes | Spécialisation | 🔧 Michel |
| Bot voyage autonome | Profil dédié | 🤖 @bavi_leo_voyages_bot |

---

## 6. 📊 Indicateurs clés

| KPI | Valeur | Objectif |
|:----|:------:|:--------:|
| Sessions / mois | ~130 | >100 |
| Taux de réponse < 5s | >95 % | >90 % |
| Documents produits | 15+ | 10/mois |
| Emails classifiés | 3 240/3 240 | 100 % |
| Crons actifs | 30/30 | 100 % verts |
| Skills (source de vérité) | 112 | À jour |
| Bureaux fonctionnels | 10 | 10 |
| Temps indisponibilité | 0 (depuis v0.17.0) | <1h/mois |

---

## 7. 🔗 Relations avec les autres bots

```mermaid
flowchart LR
    L[🤖 LEO<br/>Central] -->|sync skills| LC[🔧 Michel<br/>Infra]
    L -->|sync skills| BV[🧭 Sylvia<br/>Voyage]
    L -->|redirige voyage| BV
    L -->|redirige infra| LC
    L -->|source de vérité| ALL[📚 Tous les skills]
    
    LC -->|besoin doc| L
    BV -->|besoin analyse| L
```

---

## 8. 📈 Évolutions possibles

| Évolution | Impact | Complexité |
|:----------|:------:|:----------:|
| 🤖 Agent vocal (reconnaissance vocale) | Fort | Élevée |
| 📊 Dashboard temps réel LEO | Moyen | Moyenne |
| 🌍 Support anglais | Moyen | Faible |
| 🔌 Plugin calendrier (Google Calendar) | Moyen | Moyenne |
| 🧠 Fine-tuning du modèle | Fort | Élevée |

---

## Versions

| Version | Date | Auteur | Description |
|:--------|:-----|:-------|:------------|
| v1 | 27/06/2026 | LEO + Robert | Version initiale — analyse business LEO bot central |

---

*Analyse produite par 🏛️ Bureau Robert — BAVI LEO*

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)

