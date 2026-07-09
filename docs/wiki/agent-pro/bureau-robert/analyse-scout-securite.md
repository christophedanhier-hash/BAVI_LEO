---
date: 2026-07-09
bureau: bureau-robert
version: v1
modele: deepseek-chat
tags: [analyse, scout, microsoft, securite, rgpd, nis2, donnees-sante, mutualite, solidaris, pro]
statut: finalise
type: analyse-securite
---

# Analyse Sécurité — Microsoft SCOUT en contexte Solidaris (Mutualité, Assurance Obligatoire)

**Destinataires :** RSSI, DPO, Direction Sécurité  
**Rédacteur :** Bureau Robert — Expert Sécurité (Expert #2)  
**Date :** 9 juillet 2026  
**Classification :** CONFIDENTIEL — Usage interne Solidaris

---

## 1. Résumé Exécutif

Microsoft SCOUT est un agent IA desktop profondément intégré à Windows (PowerShell, Python, navigateur, exécution de code local, installation de packages). Pour une mutualité comme Solidaris, qui traite des **données de santé relevant de l'article 9 RGPD** (catégories particulières), SCOUT présente des **risques graves et multiples** que les garde-fous techniques actuels (Intune, permissions granulaires) ne couvrent pas complètement.

**Jugement global : NON acceptable en l'état** pour un déploiement généralisé sur le périmètre mutualiste. Un déploiement sandbox très restreint (pilote technique, pas de données réelles) est le seul scénario envisageable à court terme.

---

## 2. Matrice des Risques

| # | Risque | Gravité | Probabilité | Criticité | Description |
|---|--------|---------|-------------|-----------|-------------|
| R1 | Exfiltration données de santé vers modèles tiers (Gemini, Opus via Copilot) | **Critique (5)** | **Élevée (4)** | **20 — CRITIQUE** | Le consentement utilisateur ne couvre pas les données de santé (art. 9 RGPD). Les données Solidaris (INAMI, BCSS, eHealth) peuvent transiter par GitHub Copilot configuré sur des modèles externes. |
| R2 | Exécution de code arbitraire local (PowerShell, Python) | **Critique (5)** | **Élevée (4)** | **20 — CRITIQUE** | SCOUT exécute du code avec les droits de l'utilisateur. En cas de compromission du prompt ou d'une skill malveillante, escalade de privilèges possible. |
| R3 | Supply chain — installation de packages npm, Python non vérifiés | **Élevée (4)** | **Élevée (4)** | **16 — ÉLEVÉ** | SCOUT peut installer des dépendances depuis des registres publics. Risque de dependency confusion, package malveillant, ou version vulnérable. |
| R4 | Interaction non supervisée avec le navigateur | **Élevée (4)** | **Moyenne (3)** | **12 — ÉLEVÉ** | SCOUT peut lire et manipuler le contenu du navigateur. Exfiltration de sessions web, accès à eHealth/BCSS, modification de formulaires. |
| R5 | Non-respect de la minimisation des données | **Élevée (4)** | **Élevée (4)** | **16 — ÉLEVÉ** | L'architecture de SCOUT nécessite d'envoyer le contexte (prompt, code, fichiers) à des LLMs. Pas de garantie de minimisation. |
| R6 | Absence de traçabilité complète des actions IA | **Moyenne (3)** | **Élevée (4)** | **12 — ÉLEVÉ** | Les logs SCOUT sont immatures. Impossible de garantir une piste d'audit complète pour les autorités de contrôle (APD, INAMI). |
| R7 | Violation du principe d'intégrité des traitements mutualistes | **Élevée (4)** | **Moyenne (3)** | **12 — ÉLEVÉ** | Un agent IA modifiant des fichiers ou exécutant des scripts peut altérer des traitements réglementés (statistiques INAMI, remboursements). |
| R8 | Non-conformité NIS2 — Sécurité des réseaux et SI | **Élevée (4)** | **Moyenne (3)** | **12 — ÉLEVÉ** | SCOUT crée des canaux de communication non maîtrisés (LLM cloud, registres packages) qui contournent les contrôles réseau traditionnels. |
| R9 | Consentement insuffisant au sens RGPD | **Critique (5)** | **Très élevée (5)** | **25 — CRITIQUE** | Le formulaire de consentement SCOUT ne distingue pas les données de santé. Le consentement n'est pas une base légale valide pour le traitement de données de santé par un responsable de traitement mutualiste. |
| R10 | Dépendance à GitHub Copilot comme unique backend LLM | **Moyenne (3)** | **Faible (2)** | **6 — MOYEN** | Si Copilot est bridé aux modèles Microsoft (GPT-4o), le risque est moindre. Mais la configuration "modèles externes" est un risque immédiat. |

### Carte thermique

```mermaid
quadrantChart
    title Carte thermique des risques SCOUT
    x-axis "Faible" --> "Critique"
    y-axis "Faible" --> "Critique"
    quadrant-1 "Risques critiques (action immédiate)"
    quadrant-2 "Risques élevés (surveillance renforcée)"
    quadrant-3 "Risques moyens (à surveiller)"
    quadrant-4 "Risques faibles (acceptables)"
    R1: [0.85, 0.90]
    R2: [0.90, 0.85]
    R9: [0.95, 0.95]
    R3: [0.80, 0.70]
    R4: [0.65, 0.80]
    R5: [0.75, 0.75]
    R6: [0.60, 0.70]
    R7: [0.55, 0.75]
    R8: [0.60, 0.65]
    R10: [0.30, 0.40]
```

---

## 3. Analyse RGPD Approfondie

### 3.1 Licéité du traitement (Art. 6 + Art. 9)

**Arbre de décision des bases légales :**

```mermaid
flowchart TD
    A["Données de santé<br/>transférées via SCOUT"] --> B{"Base légale<br/>identifiée ?"}
    
    B -->|Non| C["❌ Aucune base légale<br/>= Traitement illicite"]
    B -->|Oui| D{Quelle base ?}
    
    D -->|Consentement<br/>explicite art.9.2.a| E["Rapport asymétrique<br/>employeur/mutualité"]
    E --> F["❌ Consentement non valable<br/>pour responsable de traitement"]
    
    D -->|Intérêt public / santé<br/>art.9.2.h,i| G["SCOUT est un agent<br/>généraliste, pas médical"]
    G --> H[❌ Pas applicable]
    
    D -->|Obligation légale<br/>art.9.2.b| I["Aucune loi n'impose<br/>l'usage d'un agent IA"]
    I --> J[❌ Pas applicable]
    
    D -->|Exécution contrat<br/>art.6.1.b| K["L'agent n'est pas<br/>nécessaire aux soins"]
    K --> L[❌ Pas applicable]
    
    C --> M[🛑 TRAITEMENT NON CONFORME]
    F --> M
    H --> M
    J --> M
    L --> M
    
    style M fill:#ff4444,color:#fff,stroke:#cc0000
    style C fill:#ff8888,color:#000
    style A fill:#ffdddd,color:#000,stroke:#cc0000
```

Solidaris traite des **catégories particulières de données** (art. 9 RGPD) :
- Données de santé des affiliés
- Données INAMI (remboursements, statuts)
- Données BCSS (mutualité, affiliation)
- Données eHealth (DMG, dossier médical global)

**Problème fondamental :** SCOUT, par conception, envoie le contexte de la requête à un LLM distant (via GitHub Copilot). La base légale pour ce transfert est :
- ❌ **Consentement explicite** (art. 9(2)(a)) — Pas valable pour un responsable de traitement mutualiste dans le cadre de ses missions, rapport asymétrique
- ❌ **Intérêt public / santé** (art. 9(2)(h,i)) — Non applicable à un agent généraliste
- ❌ **Obligation légale** (art. 9(2)(b)) — Non
- ❌ **Nécessité contractuelle** (art. 6(1)(b)) — L'agent n'est pas nécessaire à l'exécution des soins

**Conclusion : Aucune base légale identifiée pour le transfert de données de santé vers des LLMs cloud via SCOUT.**

### 3.2 Minimisation (Art. 5(1)(c))

SCOUT transmet tout le contexte nécessaire à l'exécution de la tâche. Dans un environnement mutualiste, ce contexte inclut quasi-systématiquement des données à caractère personnel (nom, NISS, numéro d'affiliation, code INAMI). La **minimisation est structurellement impossible**.

### 3.3 DPO et Registre (Art. 30, 35, 37)

- **AIPD obligatoire** (Art. 35) : Un déploiement SCOUT nécessite une Analyse d'Impact relative à la Protection des Données. Le risque pour les droits et libertés est manifestement élevé.
- **Registre** : Chaque interaction SCOUT génère un traitement qui doit figurer au registre — impraticable à l'échelle.

### 3.4 Transferts hors UE (Art. 44-49)

Si GitHub Copilot ou les modèles externes sont hébergés hors EEE :
- **Data Privacy Framework** (US) : Insuffisant pour des données de santé
- **Clauses Contractuelles Types** : À vérifier avec Microsoft — ne couvrent pas les modèles tiers
- **Décision d'adéquation** : Aucune pour les données de santé vers les US

**Diagramme de flux de données SCOUT :**

```mermaid
flowchart LR
    subgraph Poste["🖥️ Poste Solidaris"]
        U[Utilisateur] -->|Prompt + contexte| S[SCOUT Agent]
        S -->|Exécute| PS[PowerShell / Python]
        S -->|Lit| FS[Fichiers locaux]
        S -->|Interagit| NAV[Navigateur]
    end
    
    subgraph Cloud["☁️ Cloud Microsoft"]
        GH[GitHub Copilot] -->|Prompt enrichi| LLM{Modèle LLM}
        LLM --> GPT["GPT-4o<br/>Microsoft Azure"]
        LLM --> EXT["Modèles externes<br/>Gemini, Opus, Claude<br/>⚠️ SELON CONFIG"]
    end
    
    subgraph Tiers["🌐 Services tiers non maîtrisés"]
        NPM[npm Registry]
        PYPI[PyPI]
        PSG[PowerShell Gallery]
    end
    
    subgraph Données["🔴 Données à risque"]
        SANTE["Données de santé<br/>Art.9 RGPD"]
        INAMI[INAMI / BCSS / eHealth]
        NISS[NISS affiliés]
    end
    
    S -->|Commande packages| NPM
    S -->|Commande packages| PYPI
    S -->|Commande packages| PSG
    
    S -->|Contexte complet<br/>via API HTTPS| GH
    
    Données -.-> FS
    Données -.->|Transférées sans<br/>minimisation| S
    
    EXT -.->|❌ Pas de DLP<br/>sur ces canaux| S
    
    style Données fill:#ff4444,color:#fff,stroke:#cc0000
    style EXT fill:#ffaa00,color:#000
    style S fill:#d0e0ff,color:#000,stroke:#0066cc
    style GH fill:#e0e0e0,color:#000
```

### 3.5 Droit des personnes (Art. 12-23)

- **Droit à l'information** : Comment expliquer à un affilié Solidaris que ses données transitent par un LLM non déterminé ?
- **Droit d'opposition / effacement** : Impossible si les données ont été utilisées pour l'entraînement d'un modèle (bien que OpenAI/Microsoft affirment le contraire, l'auditabilité est nulle)

---

## 4. Analyse NIS2

Solidaris, comme mutualité d'assurance obligatoire, est probablement une **entité essentielle** au sens de NIS2 (secteur santé, seuil > 50 employés ou CA > 10M€).

### 4.1 Exigences impactées par SCOUT

| Exigence NIS2 | Impact | Analyse |
|--------------|--------|---------|
| **Art. 21(2)(c) — Sécurité des RH** | **Rouge** | Les utilisateurs peuvent consentir à des traitements qu'ils ne maîtrisent pas, hors politique de sécurité |
| **Art. 21(2)(d) — Sécurité des accès** | **Orange** | SCOUT contourne les contrôles GPO classiques par son modèle "Allow/Deny" géré par l'utilisateur |
| **Art. 21(2)(g) — Cryptographie** | **Vert** | Chiffrement natif Microsoft, mais les données sont déchiffrées avant envoi au LLM |
| **Art. 21(2)(i) — Gestion des incidents** | **Rouge** | Un incident SCOUT (exfiltration) est indétectable par les EDR classiques |
| **Art. 23 — Reporting incidents** | **Rouge** | Impossible de qualifier un incident dans les délais NIS2 (24h pour les entités essentielles) |
| **Art. 21(2)(j) — Tests de sécurité** | **Orange** | SCOUT nécessite une nouvelle surface d'attaque à tester, non couverte par les pentests classiques |
| **Art. 24 — Usage de technologies certifiées** | **Orange** | Aucune certification cybersécurité (EUCS, SOC 2) spécifique pour SCOUT connu à ce jour |

### 4.2 Risque de sanction

- Entité essentielle : amende jusqu'à 10M€ ou 2% du chiffre d'affaires annuel mondial
- Rupture d'obligation de notification d'incident : risque de sanction majoré

---

## 5. Analyse ISO 27001

| Contrôle | Statut SCOUT | Risque |
|---------|-------------|--------|
| A.5.14 — Transfert d'information | Non conforme | Toutes les données partent vers le LLM |
| A.6.7 — Télétravail | Étendu | SCOUT aggrave les risques en mobilité |
| A.8.10 — Suppression d'information | Non garanti | Données potentiellement persistées dans les logs LLM |
| A.8.12 — Prévention de fuite de données | Non conforme | Aucun DLP n'intercepte les appels API vers Copilot |
| A.8.16 — Activités de surveillance | Insuffisant | Logs SCOUT limités vs exigences d'audit |
| A.10.2 — Dépendances fournisseur | Critique | Dépendance à GitHub Copilot + modèles externes |
| A.14.2 — Sécurité du développement | Hors scope | SCOUT installe des packages non audités |

---

## 6. Comparaison avec l'Existant (Poste Verrouillé + GPO + EDR)

| Critère | Situation Actuelle (Solidaris) | Avec SCOUT | Évolution du risque |
|---------|-------------------------------|------------|-------------------|
| **Surface d'attaque** | Poste verrouillé, GPO restrictives, exécution restreinte | Exécution illimitée Python/PowerShell + installations packages | ⬆️ **CRITIQUE** |
| **DLP / Exfiltration** | Proxy, DLP réseau, blocage USB/applications cloud | Canal HTTPS direct vers GitHub Copilot + modèles tiers | ⬆️ **CRITIQUE** |
| **Audit / Logs** | Logs Windows, EDR (Defender/ Sentinel) | Logs SCOUT propriétaires, non intégrés au SIEM central | ⬆️ **ÉLEVÉ** |
| **Contrôle des permissions** | GPO + AD + RBAC strictes | Permissions SCOUT gérées par Intune + consentement utilisateur | ⬆️ **ÉLEVÉ** |
| **Supply chain** | Catalogue approuvé (SCCM/Intune) | npm, PyPI, PowerShell Gallery — aucun contrôle | ⬆️ **CRITIQUE** |
| **Sécurité navigateur** | Proxy + GPO Chrome/Edge restreint | SCOUT peut interagir avec le navigateur | ⬆️ **ÉLEVÉ** |
| **Gestion des identités** | PIV/SSO, MFA obligatoire | SCOUT ne gère PAS les mots de passe — bon point | ➡️ **NEUTRE** |
| **Mobilité** | VPN + device compliance | SCOUT mobile non contrôlé | ⬆️ **ÉLEVÉ** |

---

## 7. Analyse des Garde-Fous Proposés (Intune, Permissions Granulaires)

### 7.1 Politique Intune obligatoire

✅ **Points positifs :**
- Impose une configuration minimale de sécurité
- Peut bloquer SCOUT sur les devices non conformes
- Permet le déploiement sélectif (groupes de test)

❌ **Limites :**
- Intune ne contrôle pas ce que fait SCOUT, seulement la configuration du device
- Aucun contrôle sur le contenu envoyé au LLM
- BYOD/MDM partiel = trou dans la raquette
- Les politiques Intune sont contournables si le device est compromis

### 7.2 Permissions granulaires (Allow/Deny/Allow always)

✅ **Points positifs :**
- Chaque action sensible déclenche une demande explicite
- L'admin IT peut centraliser les permissions par automation
- Permet un blocage fin des actions à risque (ex: installer un package, écrire dans le système)

❌ **Limites :**
- **Fatigue de consentement :** L'utilisateur finit par cliquer "Allow always" par habitude
- **Pas de distinction données de santé :** Le modèle Allow/Deny ne sait pas si le fichier ouvert contient des données de santé
- **Pas de contexte réglementaire :** SCOUT ne peut pas décider de ce qui est RGPD-compatible
- **L'utilisateur peut autoriser une action dangereuse** en toute bonne foi

### 7.3 Formulaire de consentement "Données hors safe bubble Microsoft"

❌ **Problème critique :**
- Le consentement utilisateur ne couvre pas les données de santé (art. 9 RGPD)
- L'utilisateur d'une mutualité n'est pas habilité à consentir pour le compte de l'organisation ni des affiliés
- Le formulaire crée une **fausse sécurité juridique**

### 7.4 Contrôle des endpoints via Intune + Defender for Endpoint

✅ **Potentiel :**
- Blocage des exécutables non signés
- ASR rules (Attack Surface Reduction) pour bloquer les comportements suspects
- File Indicator pour bloquer les packages non approuvés

❌ **Limites :**
- Les scripts PowerShell signés par Microsoft peuvent être autorisés par défaut
- Les packages npm/Python sont rarement signés — difficile à bloquer sans casser le workflow
- Defender n'inspecte pas le contenu envoyé au LLM

---

## 8. Scénarios de Déploiement

**Arbre de décision :**

```mermaid
flowchart TD
    START["Déploiement SCOUT<br/>en mutualité ?"] --> COND1{"Toutes les barrières<br/>levées ?"}
    
    COND1 -->|Non| COND2{"Aucune donnée réelle<br/>+ réseau isolé<br/>+ durée limitée ?"}
    COND1 -->|Oui| C["Déploiement Contrôlé<br/>Progressif"]
    
    COND2 -->|Non| A["Refus Pur et Simple<br/>⚠️ RECOMMANDÉ"]
    COND2 -->|Oui| B["Sandbox Technique Isolée<br/>Pilote restreint"]
    
    A --> A1["Surveiller évolution<br/>du produit SCOUT"]
    A --> A2["Préparer stratégie<br/>Agent IA souveraine"]
    
    B --> B1[Données synthétiques]
    B --> B2[VLAN dédié]
    B --> B3[5-10 postes IT]
    B --> B4[3 mois max]
    B --> B5[Logs intensifs]
    
    C --> C1{"Barrières requises<br/>avant déploiement"}
    C1 --> C2["☐ Contrat Microsoft<br/>safe bubble exclusif"]
    C1 --> C3[☐ AIPD validée APD]
    C1 --> C4[☐ Certification HDS]
    C1 --> C5[☐ DLP inspection API]
    C1 --> C6[☐ Logs SIEM temps réel]
    C1 --> C7[☐ Formation utilisateurs]
    C1 --> C8[☐ Politique sécurité RSSI/DPO]
    
    style A fill:#ff4444,color:#fff,stroke:#cc0000
    style B fill:#ffaa00,color:#000
    style C fill:#88cc88,color:#000
    style START fill:#d0e0ff,color:#000,stroke:#0066cc
```

### Scénario A : Refus Pur et Simple ⚠️ RECOMMANDÉ

| Critère | Évaluation |
|---------|-----------|
| **Risque global** | Acceptable (risque évité) |
| **Conformité** | Garantie |
| **Cohérence avec l'existant** | Parfaite |
| **Coût** | Aucun |
| **Innovation** | Perdue |

**Arguments :**
- Les risques critiques (R1, R2, R9) ne peuvent pas être atténués techniquement
- Aucune base légale RGPD pour le transfert de données de santé
- NIS2 non compatible
- **Recommandation :** Refuser le déploiement. Surveiller l'évolution de SCOUT (notamment un éventuel modèle privé on-premise).

### Scénario B : Sandbox Technique Isolée ⚠️ PILOTE RESTREINT

| Critère | Évaluation |
|---------|-----------|
| **Risque global** | Acceptable avec contrôles stricts |
| **Conformité** | Sous condition (pas de données réelles) |
| **Cohérence avec l'existant** | Silotée |
| **Coût** | Moyen (infra + supervision) |
| **Innovation** | Partielle (test technique sans valeur métier) |

**Conditions strictes :**
1. **Aucune donnée réelle** — données synthétiques uniquement
2. **Mise en réseau isolée** (VLAN dédié, pas d'accès aux applicatifs métier, proxy bloqué vers les domaines métier)
3. **Comptes de test dédiés** (pas de comptes réels Solidaris)
4. **GitHub Copilot bridé aux modèles Microsoft uniquement** (vérification contractuelle)
5. **Journalisation intensive** (network logs + process logs + SCOUT logs)
6. **Durée limitée** (3 mois, revue avant extension)
7. **Périmètre** : 5-10 postes, service IT uniquement (pas de métier)

**Objectif du pilote :**
- Tester la maturité des logs SCOUT
- Valider ou infirmer les capacités de blocage Intune
- Cartographier les canaux d'exfiltration réels
- Évaluer le comportement des utilisateurs face à Allow/Deny

### Scénario C : Déploiement Contrôlé Progressif ⚠️ NON RECOMMANDÉ À CE STADE

| Critère | Évaluation |
|---------|-----------|
| **Risque global** | Élevé |
| **Conformité** | Non garantie |
| **Cohérence avec l'existant** | Difficile |
| **Coût** | Élevé (Intune + formation + audit + DPO) |
| **Innovation** | Maximale |

**Barrières avant d'envisager ce scénario :**
☐ Négociation contractuelle Microsoft pour garantir le **traitement exclusif dans le safe bubble Azure** (pas de modèles tiers)
☐ **AIPD validée** par l'APD (délais 6-12 mois)
☐ **Certification** SOC 2 + HDS pour SCOUT + GitHub Copilot
☐ **Chiffrement de bout en bout** des données envoyées au LLM (homomorphique ou à défaut TLS + clé client)
☐ **DLP** capable d'inspecter les appels API Copilot
☐ **Logs SCOUT intégrés au SIEM** avec alertes en temps réel
☐ **Formation obligatoire** de tous les utilisateurs (avec test de non-régression)
☐ **Politique de sécurité SCOUT** validée par le RSSI, le DPO et la Direction
☐ **Garantie contractuelle** d'absence de réutilisation des données pour l'entraînement

Tant que ces barrières ne sont pas toutes levées → **Scénario A ou B uniquement.**

---

## 9. Recommandations au RSSI

**Calendrier de mise en œuvre :**

```mermaid
gantt
    title Planning recommandations SCOUT
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y
    
    section Court terme (0-3 mois)
    Refuser déploiement SCOUT           :done, a1, 2026-07-09, 7d
    Notifier le DPO                     :a2, after a1, 5d
    Contacter Microsoft (contrat, certif) :a3, after a2, 30d
    Préparer position de négociation    :a4, after a3, 20d
    
    section Moyen terme (3-12 mois)
    Monter pilote sandbox (Scénario B)  :b1, 2026-10-01, 90d
    Réaliser AIPD complète              :b2, 2026-09-01, 120d
    Analyser alternatives souveraines   :b3, 2026-10-01, 90d
    
    section Long terme (12+ mois)
    Définir politique Agent IA mutualiste :c1, 2027-07-01, 120d
    Participer travaux sectoriels       :c2, 2027-07-01, 180d
    Porter sujet eHealth / SPF Santé    :c3, 2027-09-01, 90d
```

### Court terme (0-3 mois)

1. **Refuser le déploiement** de SCOUT sur le périmètre mutualiste dans sa forme actuelle
2. **Notifier le DPO** pour ouverture d'une fiche d'analyse préliminaire
3. **Contacter Microsoft** pour obtenir :
   - Le contrat spécifique Solidaris (indicateurs de sécurité, SLA, engagement de non-réutilisation)
   - La confirmation écrite que GitHub Copilot peut être bridé aux modèles Microsoft uniquement
   - Les certifications en vigueur pour SCOUT (SOC 2, HDS, EUCS)
4. **Préparer une position de négociation** : refus sauf garanties contractuelles fermes sur :
   - Safe bubble exclusif (Azure OpenAI, pas de modèle tiers)
   - Absence de réutilisation des données
   - Auditabilités des logs
   - Clause résolutoire en cas de non-conformité

### Moyen terme (3-12 mois)

5. **Monter un pilote sandbox** (Scénario B) si les conditions de sécurité sont réunies
6. **Réaliser une AIPD** complète en vue d'un éventuel déploiement futur
7. **Analyser les alternatives** :
   - Modèle on-premise (GPT-Next, Mistral Large auto-hébergé)
   - Agents IA open-source avec données locales (Hermes Agent, LangChain)
   - Partenariat avec un éditeur HDS (Health Data Hosting français)

### Long terme (12+ mois)

8. **Définir une politique « Agent IA pour mutualiste »** intégrant :
   - Classification des données autorisées / interdites pour les agents
   - Principe de minimisation automatique (anonymisation avant envoi LLM)
   - Traçabilité obligatoire (logs, preuves de non-rétention)
   - Procédure de réponse à incident spécifique aux agents IA
9. **Participer aux travaux sectoriels** (Mutualité chrétienne, UNMS, UCM) pour une position commune
10. **Porter le sujet au niveau eHealth / SPF Santé** : les agents IA dans les mutualités sont un enjeu sectoriel

---

## 11. Mise à jour — Microsoft Build 2026

*Date de mise à jour : 9 juillet 2026*

Lors de la conférence Microsoft Build 2026 (mai 2026), Microsoft a présenté un ensemble de nouvelles fonctionnalités et annonces liées à la sécurité des agents IA qui impactent directement l'analyse de SCOUT en contexte Solidaris.

### 11.1 Microsoft Agent Platform (MAP) — Gouvernance unifiée

Microsoft a annoncé **Microsoft Agent Platform (MAP)** , une plateforme open source unifiée pour gouverner les agents. Pour Solidaris, cela représente une évolution potentiellement positive :

- **Standardisation** : un cadre unique pour la sécurité des agents, au lieu de solutions propriétaires disparates
- **Ouverture** : plateforme open source, permettant l'audit par la communauté et les RSSI
- **Orchestration** : possibilité de centraliser les politiques de sécurité applicables à tous les agents Microsoft

**Analyse Solidaris :** MAP est une avancée architecturale, mais elle n'adresse pas le problème fondamental du transfert de données de santé vers le cloud Microsoft. Une plateforme de gouvernance ne rend pas un traitement illicite soudainement licite.

### 11.2 Identité gérée pour chaque agent (Entra ID)

Microsoft introduit la notion d'**identité gérée** pour chaque agent, avec :

- Un **compte Entra ID dédié** par agent → auditabilité comparable à celle d'un utilisateur humain
- Application automatique de **Conditional Access** (MFA, device compliance, localisation)
- **DLP/Purview** appliqué automatiquement sur les flux de l'agent
- Traçabilité complète dans les logs Entra ID (sign-ins, actions, accès aux ressources)

**Analyse Solidaris :** C'est un progrès significatif en matière d'auditabilité. Pouvoir tracer chaque action d'un agent comme on trace un utilisateur (via Entra ID) répond partiellement au risque R6 (traçabilité). Cependant, cela ne résout PAS le problème RGPD du transfert de données de santé :

- L'identité gérée améliore l'auditabilité mais ne résout PAS le problème RGPD du transfert de données de santé — les données partent toujours vers le cloud Microsoft
- L'application de DLP/Purview sur les flux agents est positive, mais le DLP Microsoft n'est pas calibré pour les catégories particulières de données (art. 9 RGPD) dans un contexte d'agent IA
- Conditional Access ne peut pas distinguer une interaction légitime d'une exfiltration via prompt engineering

### 11.3 Agent 365 — Plan de contrôle sécurité unifié

**Agent 365** est un nouveau service de sécurité qui unifie **Entra ID + Defender + Purview** pour :

- Sécuriser, gouverner et gérer le cycle de vie des agents
- Détection des comportements anormaux des agents (UEBA adapté aux agents)
- Rapports de sécurité centralisés dans le portail Defender

**Analyse Solidaris :** Agent 365 est une brique manquante dans l'écosystème Microsoft. Elle adresse le risque de shadow IT des agents (un agent non autorisé qui s'exécute). Cependant, le service est nouveau et immature — aucun retour d'expérience sectoriel (santé, mutualité) disponible.

### 11.4 Agent Registry — Découverte des agents fantômes

Microsoft a présenté **Agent Registry**, un agent dédié à la découverte des **agents fantômes** (agents non autorisés publiant des endpoints sur les postes de travail).

**Analyse Solidaris :** Utile dans un environnement mutualiste où le shadow IT est un risque réel (agents non approuvés installés par des utilisateurs). Cela comble partiellement le risque R7 (intégrité des traitements mutualistes).

### 11.5 Code MD — 100 agents collaboratifs pour la sécurité offensive

**Code MD** est une initiative de Microsoft utilisant **100 agents collaboratifs** pour :

- Trouver des failles de sécurité en mode red team automatisé
- Générer des rapports directement dans le portail Defender
- Tester en continu la surface d'attaque

**Analyse Solidaris :** Peut-être pertinent pour les équipes Sécurité de Solidaris dans le cadre de tests d'intrusion continus, mais hors scope pour l'analyse de SCOUT comme outil utilisateur.

### 11.6 DLP natif sur les flux agents (Purview)

Microsoft renforce **Purview** avec un DLP natif capable d'inspecter les flux agents :

- Bloquer l'envoi de données sensibles (patterns PII, IBAN, NISS) via les API agents
- Appliquer des politiques DLP automatiquement sur les canaux agent → LLM
- Alertes en temps réel dans le portail Purview

**Analyse Solidaris :**
✅ **Points positifs :**
- Possibilité de détecter l'envoi de NISS, numéros INAMI, données BCSS vers le LLM
- Blocage en temps réel des flux non conformes
- Intégration avec l'existant Purview Solidaris (si déployé)

❌ **Limites :**
- Le DLP Purview inspecte le trafic vers le LLM mais ne peut pas bloquer l'exfiltration via des canaux indirects (agent qui écrit dans un fichier, puis upload manuel)
- La configuration des patterns DLP pour les données de santé mutualistes (NISS, INAMI, codes eHealth) nécessite un travail important et une maintenance continue
- Faux positifs potentiellement élevés dans un environnement qui manipule massivement ces données
- Le DLP ne résout pas le problème de base légale — même avec DLP, le transfert reste juridiquement non fondé

### 11.7 Hosted Agents en sandbox sécurisée (GA juillet 2026)

Microsoft annonce la **disponibilité générale** (GA juillet 2026) des **Hosted Agents** :

- Exécution en sandbox sécurisée avec compute/mémoire/filesystem partagés
- Isolation des agents par tenant
- Pas d'accès direct au poste utilisateur
- Facturation à l'usage

**Analyse Solidaris :** Pour Solidaris, les Hosted Agents sont potentiellement **plus sécurisés** que SCOUT (agent desktop). Une architecture où l'agent s'exécute dans une sandbox cloud et ne peut pas accéder directement au poste limite le risque R2 (exécution de code arbitraire local). Cela pourrait être une alternative à SCOUT desktop pour certains cas d'usage, mais les données de santé transiteraient toujours vers le cloud Microsoft.

### 11.8 Modèles MAI — 9 modèles maison Microsoft sous licence commerciale

Microsoft présente **MAI (Microsoft AI)** , une famille de **9 modèles maison** :

- Entraînés par Microsoft, disponibles sous licence commerciale
- **Sans distillation** de modèles concurrents (OpenAI, Google, Meta)
- Les **données restent dans le tenant Microsoft** — réduction du risque d'exfiltration vers LLMs tiers
- Modèles spécialisés : code, raisonnement, vision, analyse de documents

**Analyse Solidaris :**
✅ **Points positifs :**
- Les données ne quittent pas le tenant Microsoft → réduction du périmètre d'exfiltration
- Licence commerciale → couverture juridique (indemnisations, limitations de responsabilité)
- 9 modèles spécialisés permettent de choisir le modèle adapté à la tâche sans sur-exposition

❌ **Limites :**
- Les données restent dans le tenant Microsoft, ce qui ne résout pas le transfert hors EEE si le tenant est hébergé aux US
- Aucune garantie que les modèles spécialisés ne seront pas entraînés/réentraînés avec les données du tenant
- La « réduction du risque d'exfiltration vers LLMs tiers » est un argument commercial — le risque principal reste le transfert vers Microsoft lui-même

### 11.9 « Sécurité intégrée, pas ajoutée » — Message officiel Microsoft

Microsoft communique sur le principe de **sécurité intégrée dès la conception** pour ses agents.

**Analyse Solidaris :** Un message politique attendu. Dans les faits, SCOUT reste un agent desktop avec exécution de code local, packages externes, et transfert vers le cloud. Les annonces Build 2026 améliorent le **périmètre de sécurité** mais ne changent pas l'**architecture fondamentale** qui pose problème pour les données de santé mutualistes.

### Synthèse — Impact des annonces Build 2026 sur l'analyse SCOUT

| Risque | Impact Build 2026 | Appréciation |
|--------|-------------------|-------------|
| **R1** — Exfiltration vers modèles tiers | ⚠️ Réduit avec MAI (modèles maison), mais pas éliminé | Amélioration partielle |
| **R2** — Exécution de code arbitraire local | ➡️ Peu d'impact direct (Hosted Agents limitent mais c'est une alternative, pas un patch) | Stable |
| **R3** — Supply chain packages | ➡️ Non adressé par les annonces | Stable |
| **R4** — Interaction navigateur | ➡️ Non adressé | Stable |
| **R5** — Minimisation des données | ➡️ Non adressé (DLP aide à détecter, pas à minimiser) | Stable |
| **R6** — Traçabilité | ✅ Amélioration significative (identité gérée Entra ID + logs) | Positif |
| **R7** — Intégrité traitements | ⚠️ Agent Registry aide contre les agents fantômes, mais pas contre SCOUT lui-même | Légère amélioration |
| **R8** — NIS2 sécurité réseau | ⚠️ DLP Purview sur flux agents = progrès, mais contournable | Amélioration partielle |
| **R9** — Consentement/base légale | ➡️ **Non adressé** — aucune annonce ne résout le problème de base légale RGPD | **Aucun impact** |
| **R10** — Dépendance Copilot | ⚠️ MAP + MAI réduisent la dépendance à GitHub Copilot | Amélioration partielle |

**Conclusion Build 2026 :** Les annonces de Microsoft Build 2026 apportent des améliorations notables en matière de gouvernance (MAP), d'auditabilité (identité gérée Entra ID), de détection (Agent Registry, DLP Purview) et de sécurisation des modèles (MAI). Cependant, **le problème fondamental identifié dans cette analyse persiste** : l'absence de base légale RGPD pour le transfert de données de santé vers le cloud Microsoft, quel que soit le niveau de sécurité technique. L'identité gérée améliore l'auditabilité mais ne résout PAS le problème RGPD du transfert de données de santé.

**Recommandation mise à jour :** Les annonces Build 2026 ne changent pas la recommandation de refus de déploiement de SCOUT sur le périmètre mutualiste. Elles renforcent l'intérêt de :
- Surveiller l'évolution de MAP (gouvernance ouverte) qui pourrait, à terme, permettre une architecture agent compatible avec les exigences mutualistes
- Tester les Hosted Agents en sandbox cloud plutôt que SCOUT desktop (risque R2 réduit)
- Négocier avec Microsoft un contrat incluant les modèles MAI exclusivement (pas de modèles tiers) + garantie contractuelle de non-réutilisation des données
- Préparer une AIPD intégrant ces nouvelles capacités techniques dans l'évaluation du risque

---

## 12. Synthèse Décisionnelle

| Décision | Faisabilité technique | Conformité RGPD | Conformité NIS2 | Sécurité | Coût | Recommandation |
|----------|----------------------|-----------------|-----------------|----------|------|---------------|
| **Refus** | Immédiate | ✅ Garantie | ✅ Garantie | ✅ Maximale | Aucun | 🥇 **PRIVILÉGIÉE** |
| **Sandbox test** | 2-4 semaines | ⚠️ Sous conditions (données synthétiques) | ⚠️ Acceptable | ⚠️ Acceptable | €€ | 🥈 Acceptable |
| **Déploiement contrôlé** | 6-12 mois | ❌ Non garantie | ❌ Non conforme | ❌ Élevé | €€€€ | 🥉 NON |

**Conclusion :** Microsoft SCOUT, dans son architecture actuelle (modèle cloud, exécution de code, packages externes, consentement utilisateur), n'est pas compatible avec les exigences réglementaires et de sécurité d'une mutualité d'assurance obligatoire traitant des données de santé. **Recommandation ferme : refuser le déploiement, surveiller l'évolution du produit, et préparer une stratégie « Agent IA mutualiste » souveraine.**

---

## Annexes

### Annexe A — Références

- RGPD : Règlement (UE) 2016/679, articles 5, 6, 9, 30, 35, 44-49
- NIS2 : Directive (UE) 2022/2555, articles 21, 23, 24
- ISO 27001:2022 — Annexes A.5, A.6, A.8, A.10, A.14
- Loi belge du 30 juillet 2018 relative à la protection des personnes physiques
- Loi coordonnée du 14 juillet 1994 relative à l'assurance obligatoire soins de santé
- Avis CNIL / APD belge sur les agents IA et données de santé

### Annexe B — Glossaire

| Terme | Définition |
|-------|-----------|
| BCSS | Banque Carrefour de la Sécurité Sociale |
| eHealth | Plateforme belge d'échange de données de santé |
| INAMI | Institut National d'Assurance Maladie-Invalidité |
| DMG | Dossier Médical Global |
| HDS | Hébergeur de Données de Santé (agrément français) |
| EUCS | European Union Cybersecurity Certification Scheme |
| Safe bubble | Périmètre de confiance Microsoft (Azure + Microsoft 365) |
| NISS | Numéro d'Identification de la Sécurité Sociale |
| APD | Autorité de Protection des Données (belge) |


---

## 10. Mise à jour — Microsoft Build 2026 (juin 2026)

Les annonces de Build 2026 apportent des évolutions notables en matière de sécurité des agents :

### 10.1 Identité gérée pour les agents

Chaque agent autonome a désormais **sa propre identité Entra ID** :
- Auditable comme un utilisateur (logs, traces)
- Gouvernance via Conditional Access et MFA
- DLP/Purview appliqué automatiquement sur les flux de l'agent
- Agent Registry détecte les agents fantômes publiant des endpoints sur les postes

**🔴 Impact RGPD :** L'identité gérée améliore l'auditabilité et la traçabilité, ce qui répond à une partie des exigences RGPD (piste d'audit). Mais elle ne résout PAS le problème fondamental du transfert de données de santé vers des LLMs. L'AIPD reste obligatoire.

### 10.2 Agent 365 — Plan de contrôle sécurité unifié

Agent 365 étend Entra + Defender + Purview dans une vue unique pour :
- Sécuriser, gouverner et gérer le cycle de vie des agents (cloud et locaux)
- Appliquer des politiques DLP sur les flux agents
- Détecter les anomalies de comportement via Defender

### 10.3 Modèles MAI souverains

Les 9 nouveaux modèles MAI (Microsoft AI) sont entraînés sur données sous licence commerciale, sans distillation :
- **Réduction du risque d'exfiltration :** les données restent dans le tenant Microsoft
- **Alternative aux modèles tiers :** plus besoin d'envoyer des données à OpenAI, Google ou Anthropic
- **Mais vigilance :** selon la configuration GitHub Copilot, les modèles externes restent accessibles

### 10.4 Implications pour Solidaris

| Avancée sécurité | Impact |
|:-----------------|:-------|
| Identité gérée Entra ID | ✅ Améliore traçabilité — pas de RGPD bouclé |
| Modèles MAI souverains | ✅ Réduit exfiltration vers tiers |
| Agent Registry | ✅ Détecte agents non autorisés |
| DLP natif agents | ✅ Complément à l'EDR existant |
| **Verdict sécurité** | **🔴 Reste NON acceptable pour données de santé sans AIPD + DPA** |

> **Recommandation :** Ces avancées rendent un **POC technique (données synthétiques)** plus réaliste. Mais le déploiement sur données réelles reste bloqué par l'absence de base légale RGPD.

