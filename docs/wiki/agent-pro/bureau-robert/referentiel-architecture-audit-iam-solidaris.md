---
date: 2026-07-21
bureau: bureau-robert
projet: AUDIT-IAM-ET-ETL-SOLIDARIS
version: v1
tags: [architecture, referentiel, iam, audit, etl, solidaris, dev]
statut: finalise
type: referentiel-architecture
---

# 🏗️ Référentiel Architecture — AUDIT IAM ETL SOLIDARIS

> **Projet :** Audit IAM — Identity & Access Management Solidaris
> **Dépôt :** `christophedanhier-hash/AUDIT-IAM-ET-ETL-SOLIDARIS`
> **Stack :** Python 3.12 · Pandas · Streamlit · PyInstaller · ReportLab · NetworkX · Matplotlib
> **Date :** 21/07/2026 | **Version :** v1

---

## 1. Architecture globale du système

```mermaid
flowchart TB
    subgraph SOURCES["📡 Sources de données"]
        AD[Active Directory<br/>Solidaris]
        CICS[Système CICS<br/>Transactions]
        RACF[Fichier TXT RACF<br/>Extraction brute]
    end

    subgraph ETL["⚙️ Pipeline ETL"]
        E1[ETL-IAM<br/>Convertir TXT → Excel]
        E2[ETL-IAM<br/>Fusion AD + CICS]
        E3[ETL-IAM<br/>Enrichissement final]
        E1 --> E2 --> E3
    end

    subgraph ENGINE["🧠 Moteur d'analyse"]
        MQ[Audit qualité<br/>data_quality.py]
        AN[Détection anomalies<br/>anomalies.py]
        SC[Scoring de risque<br/>scoring.py]
        SD[Contrôle SoD<br/>sod.py]
        CL[Clustering<br/>clustering.py]
        CO[Co-occurrences<br/>cooc.py]
        PR[Profiling métier<br/>profiling.py]
    end

    subgraph OUTPUT["📊 Livrables"]
        DASH[Dashboard HTML<br/>dashboard.py]
        PDF[Rapport PDF<br/>report_pdf.py]
        VIS[Graphiques<br/>visuals.py]
    end

    subgraph CADASTRE["📋 ETL Cadastre"]
        MAJ_AD[MAJ Cadastre<br/>depuis AD]
        MAJ_UO[MAJ étiquettes UO]
        CTL[Contrôle post-MAJ]
    end

    subgraph APP["🖥️ Application"]
        ST[Streamlit App<br/>app_consultation_acces.py]
        PACK[Package PyInstaller<br/>launcher_streamlit.py]
    end

    AD --> E2
    RACF --> E1
    CICS --> E2
    E3 --> ENGINE
    ENGINE --> OUTPUT
    AD --> CADASTRE
    E3 --> APP
```

---

## 2. Chaîne de traitement des données

```mermaid
flowchart LR
    subgraph STEP0["Step 0 — Conversion"]
        TXT[Fichier TXT RACF<br/>Extraction brute] --> XLSX[Fichier Excel<br/>Convertir_TXT_en_Excel_1.py]
    end

    subgraph STEP1["Step 1 — Fusion"]
        XLSX --> MERGE1[FULL_MERGE_B_PUIS_A_TRIE.parquet<br/>Merge_A_et_B_Step_1.py]
        AD[Export AD] --> MERGE1
    end

    subgraph STEP2["Step 2 — Enrichissement"]
        MERGE1 --> MERGE2[FULL_MERGE_STEP_2.xlsx<br/>Merge_Step_2.py]
    end

    subgraph AUDIT["Audit & Analyse"]
        MERGE2 --> PREPROCESS[Preprocessing<br/>preprocessing.py]
        PREPROCESS --> QUALITY[Data Quality<br/>data_quality.py]
        PREPROCESS --> ENGINE[Moteur d'analyse<br/>15 modules src/]
    end

    subgraph OUTPUT2["Livrables"]
        ENGINE --> HTML[Dashboard HTML]
        ENGINE --> PDF[Rapport PDF]
        ENGINE --> VISU[Graphiques PNG]
    end
```

---

## 3. Architecture des modules `src/` (moteur d'analyse)

```mermaid
flowchart TD
    subgraph CONFIG["Configuration"]
        CFG[config.py]:::config
    end

    subgraph PREPROCESSING["Prétraitement"]
        PRE[preprocessing.py]:::pre
        DQ[data_quality.py]:::pre
    end

    subgraph ORCHESTREUR["Orchestration"]
        PIP[pipeline.py]:::core
        MAIN[main.py<br/>Point d'entrée CLI]:::core
    end

    subgraph ANALYSE["Modules d'analyse"]
        EDA[eda.py<br/>Analyse exploratoire]:::analyse
        EXT[extraction.py<br/>Codes rares]:::analyse
        ANO[anomalies.py<br/>Détection anomalies]:::analyse
        SCO[scoring.py<br/>Scoring risque]:::analyse
        SOD[sod.py<br/>SoD]:::analyse
        CLU[clustering.py<br/>K-Means]:::analyse
        COO[cooc.py<br/>Co-occurrences]:::analyse
        PRO[profiling.py<br/>Profils métier]:::analyse
    end

    subgraph LIVRABLES["Livrables"]
        VIS[visuals.py<br/>Graphiques]:::output
        RPT[report_pdf.py<br/>PDF]:::output
        DSH[dashboard.py<br/>Dashboard HTML]:::output
    end

    MAIN --> PIP
    CFG --> PIP
    CFG --> MAIN
    PRE --> PIP
    DQ --> PIP
    PIP --> EDA --> PRO
    PIP --> EXT
    PIP --> ANO
    PIP --> SCO
    PIP --> SOD
    PIP --> CLU
    PIP --> COO
    EDA --> VIS
    ANO --> VIS
    SCO --> VIS
    CLU --> VIS
    COO --> VIS
    PRO --> VIS
    ANO --> RPT
    SCO --> RPT
    PIP --> DSH

    classDef config fill:#f9f,stroke:#333,stroke-width:1px
    classDef pre fill:#bbf,stroke:#333,stroke-width:1px
    classDef core fill:#bfb,stroke:#333,stroke-width:1px
    classDef analyse fill:#ffd,stroke:#333,stroke-width:1px
    classDef output fill:#fdd,stroke:#333,stroke-width:1px
```

---

## 4. Flux d'exécution — Application Streamlit

```mermaid
flowchart TB
    START[Démarrage] --> LOAD{Chargement données}
    LOAD -->|Parquet trouvé| CACHE[Cache local<br/>copie + signature]
    LOAD -->|Fichier distant| DOWNLOAD[Téléchargement<br/>depuis source distante]
    DOWNLOAD --> CACHE
    CACHE --> UI[Interface Streamlit]

    subgraph UI["🧩 Interface Utilisateur"]
        SR[🔍 Recherche<br/>par identifiant]
        FI[📋 Filtres<br/>UO / Hors UO / Actif]
        DE[📄 Détail utilisateur<br/>droits, transactions]
        ST[📊 Statistiques<br/>volumes, répartition]
    end

    SR --> RES[Affichage résultats]
    FI --> RES
    DE --> RES
    ST --> RES

    subgraph BUILD["Build & Packaging"]
        PS[build_app_consultation.ps1] --> PI[PyInstaller<br/>onedir]
        PI --> BIN[AppConsultationAcces.exe<br/>dist_build/]
        BIN --> VER[N versions conservées]
    end
```

---

## 5. Pipeline ETL Cadastre

```mermaid
flowchart LR
    subgraph EXTRACTION["Extraction AD"]
        AD[Active Directory<br/>Export LDAP] --> FILTRE[Filtres d'exclusion<br/>types comptes, attributs, company]
    end

    subgraph MAJ["Mise à jour"]
        FILTRE --> BACKUP[Backup automatique<br/>avant écriture]
        BACKUP --> INSERT[INSERT<br/>Nouveaux comptes]
        BACKUP --> UPDATE[UPDATE<br/>Comptes existants]
        BACKUP --> DELETE[DELETE<br/>Comptes sortis]
    end

    subgraph CONTROLE["Contrôle"]
        INSERT --> RAPPORT[Rapport post-MàJ<br/>Controle_Cadastre.py]
        UPDATE --> RAPPORT
        DELETE --> RAPPORT
    end
```

---

## 6. Déploiement et environnement

```mermaid
flowchart TD
    subgraph ENV["Environnement"]
        PY[Python 3.12.10] --> VENV[.venv]
        VENV --> REQ[requirements.txt<br/>9 dépendances]
    end

    subgraph DEV["Développement"]
        VS[VS Code] --> GIT[GitHub<br/>christophedanhier-hash]
        GIT --> LOCAL[Clone local<br/>Projets_Dev/]
    end

    subgraph EXEC["Exécution"]
        MODE1[Mode CLI<br/>python main.py -m all]
        MODE2[Mode Streamlit<br/>streamlit run app_consultation_acces.py]
        MODE3[Mode Package<br/>AppConsultationAcces.exe]
    end

    LOCAL --> MODE1
    LOCAL --> MODE2
    LOCAL --> MODE3
```

---

## 7. Index des modules

| Module | Rôle | Lignes | Dépendances clés |
|:-------|:-----|:------:|:-----------------|
| `main.py` | Point d'entrée CLI | ~49 | src.* |
| `app_consultation_acces.py` | Application Streamlit | ~1 199 | pandas, streamlit |
| `src/config.py` | Configuration centralisée | ~100 | os, json |
| `src/preprocessing.py` | Chargement & nettoyage | ~300 | pandas, config |
| `src/data_quality.py` | Audit qualité données | ~200 | pandas, config |
| `src/pipeline.py` | Orchestrateur principal | ~135 | 15 modules src |
| `src/eda.py` | Analyse exploratoire | ~400 | pandas, matplotlib |
| `src/extraction.py` | Extraction codes rares | ~150 | pandas |
| `src/anomalies.py` | Détection d'anomalies | ~250 | pandas, numpy |
| `src/scoring.py` | Score de risque combiné | ~200 | pandas, numpy |
| `src/sod.py` | Séparation des tâches | ~300 | pandas, json |
| `src/clustering.py` | K-Means + optimisation | ~350 | sklearn, pandas |
| `src/cooc.py` | Co-occurrences + graphe | ~250 | pandas, networkx |
| `src/profiling.py` | Profils génériques + gap | ~400 | pandas, config |
| `src/visuals.py` | Visualisations | ~350 | matplotlib, seaborn |
| `src/report_pdf.py` | Génération PDF | ~300 | reportlab |
| `src/dashboard.py` | Dashboard HTML | ~250 | pandas |

---

## 8. Métriques clés

| Indicateur | Valeur |
|:-----------|:------:|
| Fichiers Python | 37 |
| Lignes de code | ~5 300 |
| Modules src/ | 15 |
| Scripts ETL | 6 (3 IAM + 3 Cadastre) |
| Tests | 12 fichiers (~480 lignes) |
| Couverture de tests | ~9 % |
| Dépendances | 9 (requirements.txt) |
| Données | ~428 Mo (gitignorées) |
| Commits Git | 5 |

---

*Document produit par Robert 🏛️ — Pool Développement (D1 Architecte + D2 Rédacteur Technique)*
*Projet : AUDIT-IAM-ET-ETL-SOLIDARIS — Juillet 2026*
