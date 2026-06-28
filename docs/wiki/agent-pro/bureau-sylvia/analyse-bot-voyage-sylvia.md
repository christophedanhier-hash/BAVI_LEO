---
date: 2026-06-27
bureau: bureau-sylvia
auteur: LEO + Robert
version: v1
modele: deepseek-v4-flash
tags: [robert, sylvia, voyage, analyse, business, bpmn, data-flow, architecture]
statut: finalise
type: analyse
---

# 🧭 Analyse Business & Fonctionnelle — Bot Carnet de Voyages (Sylvia)

> **Bureau :** 🏛️ Robert — Conseil Stratégique IT | **Date :** 27/06/2026
> **Sujet :** Analyse du bot voyage BAVI LEO, modèle économique, flux fonctionnels et architecture

---

## 1. 🎯 Présentation du projet

### 1.1 Contexte

**Sylvia** est un assistant de voyage intelligent, déployé comme bot Telegram `@bavi_leo_voyages_bot`. Elle est le fruit d'une évolution : partie d'un simple assistant roadbook camping-car, elle est aujourd'hui une **agence de voyage complète** capable de gérer tous modes de transport et hébergements.

### 1.2 Objectifs

| Objectif | Description |
|:---------|:------------|
| 🎯 **Assister** la planification de voyages pour Christophe et ses amis |
| 📋 **Produire** des roadbooks structurés et des notes PDF |
| 🗺️ **Générer** des cartes interactives OSM |
| 💰 **Facturer** de manière transparente (abonnement + forfait) |
| 📚 **Archiver** chaque document dans un wiki versionné |

### 1.3 Public cible

| Profil | Rôle | Accès | Facturation |
|:-------|:-----|:------|:------------|
| 🧑‍✈️ **Christophe** | Propriétaire, admin système | DM + groupe Telegram | Tokens IN/OUT uniquement |
| 👥 **Amis** (Pascal…) | Utilisateurs du bot voyage | Groupe Telegram | Abonnement **12 €/an** + forfait document |
| 🧑 **Invités** | Consultation ponctuelle | Groupe Telegram (limité) | Abonnement ou accès libre selon décision |

---

## 2. 🏗️ Architecture technique

### 2.1 Diagramme d'architecture générale

```mermaid
graph TB
    subgraph "📱 Utilisateurs"
        T[Telegram]
    end

    subgraph "🧠 Hermes Agent"
        BP[Profil bavi-leo<br/>DeepSeek Flash]
        SK[Skill bureau-sylvia<br/>555 lignes]
        MB[Mémoire & Sessions]
    end

    subgraph "🗄️ Stockage"
        DRV[Drive Google<br/>bavi/bureau-sylvia]
        GH[GitHub<br/>voyages-wiki]
        WP[Wiki GH Pages<br/>voyages-wiki/]
    end

    subgraph "📧 Communication"
        GM[Gmail API<br/>leodanhieria]
    end

    T <-->|chat Telegram| BP
    BP -->|charge| SK
    BP -->|sauvegarde| MB
    SK -->|documents| DRV
    SK -->|commit+push| GH
    GH -->|déploiement| WP
    SK -->|email réservation| GM
    GM -->|copier-coller texte| T
```

### 2.2 Stack technique

| Composant | Technologie | Rôle |
|:----------|:------------|:-----|
| **Agent** | Hermes Agent (profil `bavi-leo`) | Exécution du skill Sylvia |
| **Modèle** | DeepSeek V4 Flash ($0,15/M IN, $0,60/M OUT) | Inférence chat + production documents |
| **Transport** | Telegram API (bot `@bavi_leo_voyages_bot`) | Interface utilisateur |
| **Stockage docs** | Google Drive (dossier `bavi/bureau-sylvia`) | Brouillons, sources |
| **Versioning** | GitHub (`christophedanhier-hash/voyages-wiki`) | Wiki, historique des commits |
| **Hébergement** | GitHub Pages | Site web public du wiki |
| **Email** | Gmail API (compte `leodanhieria@gmail.com`) | Envoi confirmations |
| **Sync cron** | Hermes cron (`wiki-sync`) | Synchronisation Drive → Wiki |

---

## 3. 🔄 Flux fonctionnels

### 3.1 Processus complet — BPMN (Business Process)

```mermaid
flowchart TD
    %% Acteurs
    U[👤 Utilisateur] -->|message Telegram| S[🧭 Sylvia]
    
    %% Phase ①
    S -->|① Cadrage| Q{Type de demande?}
    Q -->|Question rapide| CHAT[💬 Chat simple]
    Q -->|Note/PDF| NOTE[📝 Note analyse]
    Q -->|Roadbook| RB[🗺️ Roadbook]
    
    %% Chat - gratuit
    CHAT -->|Abonnement| REP[✅ Réponse directe]
    REP -->|pas de document| FIN[Fin]
    
    %% Note - 2.50€
    NOTE -->|② Dispatch| PROD_N[③ Production]
    PROD_N -->|recherche web| SYN_N[⑤ Synthèse]
    SYN_N -->|⑥ Livrable| PDF[📄 Génération PDF]
    PDF -->|⑦ Archivage| WIKI_N[📁 Wiki + Commit]
    WIKI_N -->|2,50 € facturé| FIN
    
    %% Roadbook - 2.50€
    RB -->|② Dispatch| PROD_R[③ Production<br/>🌤️ Météo<br/>🏕️ Campings<br/>🗺️ Cartes<br/>🚐 Itinéraire]
    PROD_R -->|④ Croisement| CROSS[Confrontation données]
    CROSS -->|⑤ Synthèse| SYN_R[📋 Synthèse itinéraire]
    SYN_R -->|⑥ Livrable| CARTE[🗺️ Carte folium]
    CARTE -->|⑦ Archivage| WIKI_R[📁 Wiki + Commit + Push]
    WIKI_R -->|2,50 € facturé| FIN

    %% Styles
    style U fill:#e3f2fd,stroke:#1976d2
    style S fill:#fff3e0,stroke:#f57c00
    style CHAT fill:#e8f5e9,stroke:#388e3c
    style NOTE fill:#e8f5e9,stroke:#388e3c
    style RB fill:#e8f5e9,stroke:#388e3c
    style PDF fill:#fce4ec,stroke:#c62828
    style CARTE fill:#fce4ec,stroke:#c62828
    style FIN fill:#f5f5f5,stroke:#9e9e9e
```

### 3.2 Flux de données

```mermaid
flowchart LR
    subgraph "📥 Données entrantes"
        D1[👤 Message utilisateur<br/>texte libre]
        D2[🌐 Recherche web<br/>campings, horaires]
        D3[📍 Coordonnées GPS<br/>Park4Night, OSM]
        D4[📧 Email réservation<br/>Gmail API]
    end

    subgraph "⚙️ Traitement Sylvia"
        T1[🧠 Compréhension<br/>LLM Flash]
        T2[🗃️ Structuration<br/>.md + métadonnées]
        T3[🗺️ Génération carte<br/>folium/leaflet]
        T4[📊 Calcul budget<br/>tokens + forfait]
    end

    subgraph "📤 Données sortantes"
        S1[💬 Réponse chat<br/>Telegram]
        S2[📄 Document .md<br/>wiki]
        S3[🗺️ Carte interactive<br/>.html]
        S4[📧 Email confirmation<br/>Gmail]
        S5[📊 Facture<br/>tableau pricing]
    end

    D1 --> T1
    D2 --> T1
    D3 --> T3
    D4 --> T1

    T1 --> T2
    T2 --> T3
    T1 --> T4

    T1 --> S1
    T2 --> S2
    T3 --> S3
    T1 --> S4
    T4 --> S5

    style D1 fill:#e3f2fd
    style D2 fill:#e3f2fd
    style D3 fill:#e3f2fd
    style D4 fill:#e3f2fd
    style S1 fill:#c8e6c9
    style S2 fill:#c8e6c9
    style S3 fill:#c8e6c9
    style S4 fill:#c8e6c9
    style S5 fill:#c8e6c9
```

### 3.3 Cycle de vie d'un document

```mermaid
flowchart TD
    START([Question]) --> CHAT{Chat ou Document?}
    
    CHAT -->|Info rapide| SIMPLE[💬 Réponse chat<br/>✅ gratuit - abonnement]
    SIMPLE --> ENDE([Fin])
    
    CHAT -->|Note/PDF| NOTE[📝 Production note<br/>💳 2,50 euro]
    CHAT -->|Roadbook| RB[🗺️ Production roadbook<br/>💳 2,50 euro]
    
    NOTE --> VAL[Validation]
    RB --> VAL
    
    VAL -->|Modifications| RETOUR[Retour en production]
    RETOUR --> NOTE
    RETOUR --> RB
    
    VAL -->|Valide| WIKI[📁 Wiki + Commit + Push]
    WIKI --> PUB[🌐 Déploiement GH Pages]
    PUB --> ENDE
```

---

## 4. 💳 Modèle économique

### 4.1 Structure de revenus

```mermaid
pie title Repartition du chiffre d affaires
    "Abonnements" : 12
    "Forfaits document" : 8
    "Tokens DeepSeek" : 0
```

### 4.2 Tarifs

| Poste | Tarif | Bénéficiaire |
|:------|:-----:|:-------------|
| 🎫 **Abonnement annuel** | **12 €/an** par ami | Chat illimité |
| 📝 **Forfait note/PDF** | **2,50 €** | Document dans le wiki |
| 🗺️ **Forfait roadbook** | **2,50 €** | Fichier + carte + wiki |
| 💰 **Tokens DeepSeek** | Coût réel ($0,15/0,60M) | Christophe : tokens only, Amis : inclus dans forfait |

### 4.3 Projection annuelle (estimation)

| Poste | Quantité | Prix unitaire | Total/an |
|:------|:--------:|:-------------:|:--------:|
| Abonnements | 1 abonné (Pascal) | 12 € | **12 €** |
| Roadbooks | 4 / an | 2,50 € | **10 €** |
| Notes/PDF | 6 / an | 2,50 € | **15 €** |
| Tokens DeepSeek | ~500K IN/mois | $0,15/M | **~0,90 $/an** |
| **Total estimé** | | | **~37 €/an** |

---

## 5. 🚫 Périmètre fonctionnel

| Fonction | Statut | Priorité |
|:---------|:------:|:--------:|
| Roadbooks camping-car | ✅ Actif | Haute |
| Roadbooks voiture/train/avion | ✅ Actif | Haute |
| Recherche hébergements (tous types) | ✅ Actif | Haute |
| Cartes interactives OSM | ✅ Actif | Haute |
| Notes PDF | ✅ Actif | Moyenne |
| Location vélo/moto/voiture | ✅ Actif | Basse |
| Multi-utilisateurs (groupe) | ✅ Actif | Haute |
| Copier-coller email pour amis | ✅ Actif | Basse |
| Réservation en ligne directe | ❌ Futur | — |
| Paiement intégré | ❌ Futur | — |

---

## 6. 📈 Évolutions possibles

| Évolution | Impact | Complexité |
|:----------|:------:|:----------:|
| 📱 Application mobile dédiée | Fort | Élevée |
| 💳 Paiement Stripe intégré | Fort | Moyenne |
| 🤝 Partenariats hôteliers/campings | Moyen | Faible |
| 🌍 Support multilingue | Faible | Faible |
| 📊 Dashboard admin pour Christophe | Moyen | Moyenne |
| 🗓️ Calendrier de réservation | Moyen | Moyenne |

---

## 7. 📊 Indicateurs clés (KPI)

| Indicateur | Valeur | Objectif |
|:-----------|:------:|:--------:|
| Utilisateurs actifs | 2 (Christophe + Pascal) | +1/an |
| Documents produits | 4 roadbooks | 8/an |
| Taux de rétention (J+30) | 100 % | >80 % |
| Coût moyen par document | 0,09 € (tokens) | <0,50 € |
| Temps moyen de réponse chat | <5s | <10s |
| Satisfaction utilisateur | ✅ Aucun retour négatif | >4/5 |

---

## 8. 🔗 Annexes

- [🌐 Wiki voyage](https://christophedanhier-hash.github.io/voyages-wiki/)
- [📖 Guide utilisateur](https://christophedanhier-hash.github.io/voyages-wiki/guide-utilisateur/)
- [🤖 Bot Telegram](https://t.me/bavi_leo_voyages_bot)
- [📋 Suivi projet](https://github.com/christophedanhier-hash/leo-tracker/issues)
- [🧠 Skill Sylvia (source de vérité)](https://github.com/christophedanhier-hash/hermes-christophe)

---

## Versions

| Version | Date | Auteur | Description |
|:--------|:-----|:-------|:------------|
| v1 | 27/06/2026 | LEO + Robert | Version initiale — analyse business BPMN + flux données |

---

*Analyse produite par 🏛️ Bureau Robert — BAVI LEO*
