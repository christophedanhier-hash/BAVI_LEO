---
date: 2026-06-28
bureau: bureau-robert
auteur: LEO + Robert
version: v2
modele: deepseek-v4-flash
tags: [robert, michel, infra-hermes, analyse, business, bpmn, data-flow, architecture, systeme]
statut: finalise
type: analyse
---

# 🔧 Analyse Business & Fonctionnelle — Michel (Infra_Hermes)

> **Bureau :** 🏛️ Robert — Conseil Stratégique IT | **Date :** 27/06/2026
> **Sujet :** Analyse du bot Michel, infrastructure Hermes, maintenance système

---

## 1. 🎯 Présentation

### 1.1 Contexte

**Michel** (profil `leo-copilot`) est le bot **infrastructure** de l'écosystème BAVI. Il porte le bureau **Michel — Infra_Hermes** et gère tout ce qui touche au fonctionnement technique de la plateforme Hermes Agent : crons, dashboards, Google APIs, Git, skills, budget, machines, réseau.

|Contrairement à LEO (polyvalent/documentation) et Sylvia (voyage), Michel a un scope **purement technique** — il ne fait ni analyses business, ni roadbooks, ni consultations. Michel utilise plusieurs modèles d'IA (DeepSeek, OpenAI, Gemini, Grok, Anthropic) et un modèle local Ollama qwen2.5:7b, selon les besoins.

> 🔑 **Changement majeur (v2)** : Michel dispose désormais de l'**accès root complet** sur la machine LEO (`sudo` sans restriction). Il est devenu le **padron de la machine** et peut tout faire : installation système, configuration Nginx, pare-feu (UFW), DNS, certificats SSL, tunnels Cloudflare, ports réseau — sans dépendre de CodeWhale. L'ère CodeWhale est révolue pour LEO.

### 1.2 Objectifs

| Objectif | Description |
|:---------|:------------|
| 🏗️ **Installer & maintenir** les services système (Nginx, Cloudflare, DNS, SSL, UFW) | CodeWhale remplacé ✅ |
| ⚙️ **Maintenir** l'infrastructure Hermes (39 crons, 8 dashboards) |
| 🛠️ **Dépanner** les services (gateways, conteneurs, SSH, tunnels) |
| 📊 **Surveiller** les machines (LEO, Yoga, Penguin — CPU, RAM, disque) |
| 💰 **Suivre** le budget DeepSeek ($19,46 solde, suivi horaire) |
| 🤖 **Gérer** les bots Telegram (gateways, profils) |
| 🔄 **Synchroniser** les skills et la mémoire entre profils |
| 📋 **Orchestrer** n8n (6 workflows, API REST) |

### 1.3 Public cible

| Utilisateur | Interaction | Fréquence |
|:------------|:------------|:---------:|
| 🧑‍✈️ **Christophe** | Demandes via DM Telegram | Hebdomadaire |
| 🤖 **LEO** (bot central) | Sync skills (30 min) | Continue |
| 🧭 **Sylvia** (bot voyage) | Sync skills (30 min) | Continue |
| 🎓 **Emile** (bot études) | Sync skills (30 min) | Continue |

### 1.4 Chiffres clés

| Indicateur | Valeur |
|:-----------|:------:|
| Modèle | DeepSeek V4 Pro ($2/$8 M tokens) |
| Fallback | Gemini 2.5 Flash |
| Crons gérés | 30 (tous verts) |
| Dashboards | 8 temps réel |
| Machines surveillées | 3 (LEO, Yoga, Penguin) |
| Accès système | `sudo` root complet 🔑 |
| Services système | Nginx, Cloudflare, UFW, SSL, DNS |
| n8n workflows | 6 |
| Skills BAVI | 4 (Michel, Emile, governance, versioning) |
| Budget DeepSeek | $19,46 (dashboard) |

---

## 2. 🏗️ Architecture technique

### 2.1 Diagramme d'architecture

```mermaid
graph TB
    subgraph "📱 Point d entree"
        TG[Telegram<br/>DM Christophe]
    end

    subgraph "🔧 Michel"
        LC[Agent Michel<br/>Profil leo-copilot<br/>DeepSeek V4 Pro]
        SK[Skills<br/>Michel + Emile + governance]
        MB[Memoire sessions]
    end

    subgraph "⚙️ Infrastructure gérée"
        CR[Crons<br/>30 automatismes]
        DB[Dashboards<br/>8 tableaux de bord]
        N8N[n8n<br/>6 workflows]
        GW[Gateways<br/>3 profils Hermes]
    end

    subgraph "🔌 Services système (root access)"
        NG[Nginx<br/>Sites, configs]
        CF[Cloudflare Tunnel<br/>DNS, ingress]
        UF[UFW<br/>Pare-feu ports]
        SS[SSL/Certbot<br/>Certificats TLS]
        PORT[Ports<br/>80, 443, 8081]
    end

    subgraph "🖥️ Machines"
        L[LEO server<br/>457 Go, 20% disque]
        Y[Yoga<br/>Monitoring CPU/RAM]
        P[Penguin<br/>Monitoring CPU/RAM]
    end

    subgraph "🔌 Services"
        OL[Ollama<br/>qwen2.5:7b local]
        CS[Code-server<br/>VS Code web]
        SSH[Tunnels SSH<br/>Conteneur → Host]
        TL[Tailscale<br/>Réseau prive]
    end

    subgraph "🔄 Sync"
        MEM[Sync mémoire<br/>30 min]
        SKL[Sync skills<br/>30 min]
        GA[Google APIs<br/>Gmail, Drive, Sheets]
    end

    TG --> LC
    LC --> CR
    LC --> DB
    LC --> N8N
    LC --> GW
    LC --> NG
    LC --> CF
    LC --> UF
    LC --> SS
    LC --> PORT
    LC --> L
    LC --> Y
    LC --> P
    LC --> OL
    LC --> CS
    LC --> SSH
    LC --> TL
    LC --> MEM
    LC --> SKL
    LC --> GA
```

### 2.2 Stack technique

| Composant | Technologie | Rôle |
|:----------|:------------|:-----|
| **Agent** | Hermes Agent (profil `leo-copilot`) | Exécution infra |
| **Modèle** | DeepSeek V4 Pro ($2/M IN, $8/M OUT) | Inférence complexe |
| **Fallback** | Gemini 2.5 Flash | Si DeepSeek rate-limit |
| **Modèle local** | Ollama qwen2.5:7b | Classification emails (gratuit) |
| **Transport** | Telegram API (bot `@hermes_leo_copilot_bot`) | Interface Christophe |
| **n8n** | API REST locale | Workflows notification |
| **Code** | Code-Server (VS Code web, port 8081) | Développement distant |
| **Réseau** | Tailscale (100.92.102.28) | Accès privé machines |
| **Budget** | Dashboard Hermes (port 9119) | Suivi temps réel |
| **Accès système** | `sudo` root complet | Padron machine — remplace CodeWhale ✅ |
| **Skills source** | Sync depuis LEO (profil default) | 30 min |

---

## 3. 🔄 Flux fonctionnels

### 3.1 Processus de travail — BPMN

```mermaid
flowchart TD
    U[👤 Christophe] -->|message Telegram| LC[🔧 Michel]
    
    LC -->|① Cadrage| Q{Type de demande?}
    
    Q -->|Panne/Incident| DIAG[🔍 Diagnostic]
    DIAG -->|Root cause| FIX[🛠️ Correction]
    FIX --> TEST[✅ Verification]
    TEST --> ARCH
    
    Q -->|Nouveau service| SETUP[📦 Installation/Config]
    SETUP --> TEST
    
    Q -->|Dashboard| DASH[📊 Mise a jour dashboard]
    DASH --> TEST
    
    Q -->|Cron| CRON[⏰ Creation/Modification cron]
    CRON --> TEST
    
    Q -->|Audit| AUDIT[📋 Audit systeme]
    AUDIT --> DOC
    
    Q -->|Sync| SYNC[🔄 Sync memoire/skills]
    SYNC --> FIN
    
    TEST --> ARCH[⑦ Archivage<br/>Analyse .md + commit]
    DOC --> ARCH
    ARCH --> FIN([Fin])
    
    style U fill:#e3f2fd,stroke:#1976d2
    style LC fill:#fff3e0,stroke:#f57c00
    style Q fill:#fff3e0,stroke:#f57c00
    style TEST fill:#c8e6c9,stroke:#388e3c
    style ARCH fill:#f3e5f5,stroke:#7b1fa2
```

### 3.2 Flux de données

```mermaid
flowchart LR
    subgraph "📥 Entrees"
        I1[👤 Messages Telegram<br/>Christophe]
        I2[📊 Metriques machines<br/>CPU, RAM, disque]
        I3[🔔 Alertes crons<br/>Erreurs, timeouts]
        I4[📧 Google API<br/>Tokens, scopes]
    end

    subgraph "⚙️ Traitement Michel"
        T1[🧠 Analyse<br/>DeepSeek V4 Pro]
        T2[🛠️ Correction<br/>Scripts, configs]
        T3[📊 Dashboard gen<br/>Chart.js + HTML]
        T4[💰 Budget tracking<br/>CSV + dashboard]
        T5[🔄 Sync cron<br/>Memoire + skills]
    end

    subgraph "📤 Sorties"
        O1[💬 Reponse Telegram]
        O2[📄 Analyse infra<br/>.md archive]
        O3[📊 Dashboard mis a jour<br/>GH Pages]
        O4[⚙️ Services corriges<br/>Crons, gateways]
        O5[🔄 Profils synchronises<br/>Memoire, skills]
    end

    I1 --> T1
    I2 --> T3
    I3 --> T2
    I4 --> T1

    T1 --> O1
    T1 --> O2
    T2 --> O4
    T3 --> O3
    T4 --> O3
    T5 --> O5

    style I1 fill:#e3f2fd
    style I2 fill:#e3f2fd
    style O1 fill:#c8e6c9
    style O2 fill:#c8e6c9
    style O3 fill:#c8e6c9
    style O4 fill:#c8e6c9
    style O5 fill:#c8e6c9
```

### 3.3 Workflow par type de livrable

```mermaid
flowchart TD
    subgraph "📄 Analyse infra"
        A1[① Cadrage] --> A3[③ Production]
        A3 --> A5[⑤ Synthese]
        A5 --> A6[⑥ Livrable]
        A6 --> A7[⑦ Archive .md]
    end
    
    subgraph "📊 Dashboard"
        C1[Collecte metriques] --> T1[Traitement Python]
        T1 --> P1[Publication GH Pages]
    end
    
    subgraph "🛠️ Correction"
        D1[Diagnostic] --> D2[Script correction]
        D2 --> D3[Verification]
        D3 --> D4[Documentation]
    end
```

---

## 4. 💳 Modèle économique

### 4.1 Coûts de fonctionnement

| Poste | Coût | Fréquence |
|:------|:----:|:---------|
| **DeepSeek V4 Pro** (inférence) | ~0,10 €/tâche complexe | Hebdomadaire |
| **Gemini Flash** (fallback) | **0 €** (cap 100 €/mois offert) | Rare |
| **Ollama** (classification) | **0 €** (local) | Continue |
| **n8n** (workflows) | **0 €** (self-hosted) | Continue |
| **Code-Server** (VS Code) | **0 €** (local) | Continue |
| **Total mensuel** | **~2-5 €** | |

### 4.2 Répartition du coût DeepSeek Pro

```mermaid
pie title Repartition cout DeepSeek Pro
    "Analyses infra complexes" : 40
    "Corrections systeme" : 30
    "Audits" : 20
    "Divers" : 10
```

### 4.3 Facturation

| Service | Tarif | Note |
|:--------|:-----:|:-----|
| Correction infra (panne, cron, gateway) | Inclus | Maintenance courante |
| Audit système complet | 5,00 € | Forfait BAVI |
| Mise à jour dashboard | Inclus | Maintenance courante |
| Ajout nouveau service | 5,00 € | Installation + config |
| Sync memory/skills | **0 €** | Automatisé (cron) |

---

## 5. 🚫 Périmètre fonctionnel

### 5.1 Ce que Michel fait

| Fonction | Statut | Détail |
|:---------|:------:|:-------|
| **🚀 Services système** | ✅ Nouveau (v2) | Installation Nginx, Cloudflare Tunnel, DNS, UFW, SSL — remplace CodeWhale |
| Maintenance crons (30) | ✅ Actif | Création, debug, staggering |
| Dashboards temps réel | ✅ Actif | 8 dashboards Chart.js |
| n8n workflows | ✅ Actif | 6 workflows, API REST |
| Google APIs | ✅ Actif | Gmail, Drive, Sheets, tokens |
| Git repos (10) | ✅ Actif | Clean trees, sync, push |
| Hermes config | ✅ Actif | Profils, version, gateways |
| Sync mémoire/skills | ✅ Actif | Cross-profil (30 min) |
| Budget tracking | ✅ Actif | DeepSeek credits |
| Machines monitoring | ✅ Actif | CPU, RAM, disque (3 machines) |
| Ollama local | ✅ Actif | qwen2.5:7b classification |
| Code-Server | ✅ Actif | VS Code web, port 8081 |
| Tunnels SSH | ✅ Actif | Conteneur → Host |
| Réseau Tailscale | ✅ Actif | Connectivité privée |

### 5.2 Ce que Michel ne fait pas

| Fonction | Raison | Qui le fait |
|:---------|:-------|:------------|
| Rédaction documents voyage | Hors scope | 🧭 Sylvia |
| Analyses stratégiques IT | Hors scope | 🏛️ Robert/LEO |
| Consultations médicales | Hors scope | 🩺 Virginie |
| Documentation T600 | Hors scope | 📝 Gérard |
| Envoi emails personnels | Hors scope | 🤖 LEO |
| Mise à jour documentation wiki | Hors scope | 🤖 LEO |

---

## 6. 📊 Indicateurs clés

| KPI | Valeur | Objectif |
|:----|:------:|:--------:|
| Crons verts | 30/30 | 100 % |
| Dashboards répondant | 8/8 | 100 % |
| Temps moyen correction incident | <30 min | <1h |
| Uptime gateways | 100 % (depuis v0.17.0) | >99,5 % |
| Sync skills OK | 4/4 | 100 % |
| Budget DeepSeek | $19,46 | >$10 toujours |
| Disque LEO | 83 Go/457 Go (20%) | <80 % |
| Tunnels SSH actifs | 1 | 1 |

---

## 7. 🔗 Relations avec les autres bots

```mermaid
flowchart LR
    LC[🔧 Michel<br/>Infra] -->|depend| HERMES[Hermes Agent<br/>Plateforme]
    LC -->|sync skills| L[🤖 LEO<br/>Source de verite]
    LC -->|gère infra| BV[🧭 Sylvia<br/>Bot voyage]
    LC -->|gère infra| BE[🎓 Emile<br/>Bot etudes]
    L -->|source skills| LC
    BV -->|besoin infra| LC
    BE -->|besoin infra| LC
```

---

## 8. 📈 Évolutions possibles

| Évolution | Impact | Complexité |
|:----------|:------:|:----------:|
| 🔔 Système d'alertes temps réel (webhook) | Fort | Moyenne |
| 📊 Dashboard unique consolidé | Moyen | Faible |
| 🤖 Auto-heal des crons (déjà partiel) | Fort | Élevée |
| 🐳 Gestion complète des services système (Nginx, Cloudflare, UFW) | ✅ **Fait (v2)** | Remplace CodeWhale |
| 🌐 API status publique | Moyen | Faible |
| 📱 App mobile monitoring | Faible | Élevée |

---

## Versions

| Version | Date | Auteur | Description |
|:--------|:-----|:-------|:------------|
| v1 | 27/06/2026 | LEO + Robert | Version initiale — analyse business Michel |
| v2 | 28/06/2026 | LEO + Robert | 🚀 Michel devient padron machine — accès root complet, plus de dépendance CodeWhale |

---

*Analyse produite par 🏛️ Bureau Robert — BAVI LEO*

> 🤖 Dernier audit : 20 July 2026 à 09:15 (UTC+2)

