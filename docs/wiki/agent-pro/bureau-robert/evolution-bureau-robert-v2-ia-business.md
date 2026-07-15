---
date: 2026-07-14
bureau: bureau-robert
auteur: LEO
version: brouillon-v2
modele: deepseek-v4-flash
tags: [evolution, ia, business, solidaris, ao, strategie, innovation, robert-v2]
statut: brouillon
type: analyse-evolution
---

# 🏛️ Bureau Robert v2 — Évolution Stratégique IA  
## Analyse : Architecture multi-experts IT & Business pour l'intégration de l'IA

> **Document de réflexion — pas encore implémenté**
> **Date :** 14/07/2026 | **Version :** brouillon v2

---

## 1. Principe fondateur : Robert reste un orchestrateur

Robert ne change pas de nature. Il reste celui qui **orchestre** — il reçoit la demande, analyse le besoin, **dispatche** aux bons sous-agents, croise leurs analyses et produit la synthèse.

La différence : il dispose désormais de **deux pools d'experts** au lieu d'un.

```mermaid
flowchart TD
    A[📨 Demande - Direction AO] --> B[🏛️ Robert - Orchestrateur]
    B --> C{Analyse & Dispatch}
    C --> D[Pool IT - 9 experts]
    C --> E[Pool Business - 7 experts]
    D --> F[Synthèse croisée]
    E --> F
    F --> G[📄 Recommandation finale]
```

---

## 2. Architecture des sous-agents

### 2.1 Pool IT — Renforcé (9 experts)

| # | Sous-agent | Rôle | Expertise clé |
|:-:|:-----------|:-----|:--------------|
| 1 | 🏛️ **Vision Stratégique** | Analyse du marché, tendances, positionnement | Veille technologique, benchmarks |
| 2 | 🏗️ **Architecture SI** | Intégration technique, patterns, dépendances | APIs, cloud, SI Solidaris |
| 3 | 🛡️ **Sécurité & RGPD** | Risques, conformité, AIPD | Données santé, NIS2, AI Act |
| 4 | 📋 **Projet & Programme** | Planning, coûts, TCO, jalons | Gestion de projet IT |
| 5 | 💰 **Budget & TCO** | Modélisation financière, ROI | Coûts IT, scénarios |
| 6 | 🔄 **Interopérabilité** | eHealth, BCSS, MyCareNet, connecteurs | Standards mutualistes belges |

**Nouveaux experts IT (pour répondre au Business IA) :**

| # | Sous-agent | Rôle | Expertise clé | Pourquoi |
|:-:|:-----------|:-----|:--------------|:---------|
| 7 | 🧪 **Data Engineering & IA Ops** | Pipelines de données, préparation datasets, feature engineering, MLOps | Python, bases vectorielles, embeddings, RAG | Le Business va demander des PoC IA → quelqu'un doit les construire |
| 8 | ☁️ **Infrastructure & Cloud IA** | GPU, vecteur DB, déploiement modèles, scaling | Azure OpenAI, AWS Bedrock, huggingface | Les modèles LLM ne tournent pas sur un serveur classique |
| 9 | 🔗 **API & Intégration IA** | Sécurisation des appels API IA, proxy, caching, rate limiting, monitoring tokens | OpenAI API, gestion coûts tokens, gateway IA | Connecter les modèles externes au SI Solidaris sans fuite de données |

### 2.2 Pool Business — Nouveaux (7 experts)

| # | Sous-agent | Rôle | Expertise clé | Quand l'activer |
|:-:|:-----------|:-----|:--------------|:----------------|
| 10 | ⚖️ **Expert Métier AO** | Connaissance des processus INAMI/BCSS, réglementation mutualiste Solidaris | Contexte métier AO, circuits de remboursement | Tout projet touchant au métier AO |
| 11 | 🏢 **Architecture des Processus Métier** | Cartographier les processus AO, identifier les goulots et points d'entrée IA | BPMN, flux métier, analyse de valeur | Dès qu'un processus métier est concerné |
| 12 | 🧪 **R&D & Innovation IA** | Veille cas d'usage mutualistes, POC, prototypage | IA générative, RPA, OCR, NLP, agents | Pour tout sujet IA concret |
| 13 | 🔄 **Gestion du Changement** | Impact organisationnel, adoption, accompagnement des équipes | Conduite du changement, formation | Projets impactant les agents AO |
| 14 | ⚖️ **Juridique & Conformité Métier** | AI Act, RGPD santé, droit mutualiste, responsabilité | Droit social, assurances, données santé | Obligatoire pour tout projet avec données réelles |
| 15 | 🎓 **Acculturation & Formation** | Création de supports, ateliers, vulgarisation IA | Pédagogie, cas d'usage concrets | En amont ou parallèle au déploiement |
| 16 | 📊 **Data & Analyse** | Données disponibles, qualité, préparation, indicateurs | Data governance, analytics, KPI | Pour tout projet data-driven |

---

## 3. Fonctionnement — Comment Robert orchestre

### 3.1 Exemple : Mission "Chatbot agent AO"

```mermaid
flowchart TB
    Q["Peut-on mettre un chatbot<br>pour aider les agents AO ?"]

    Q --> R[🏛️ Robert analyse]
    R -->|Contexte: données santé,<br>agents AO, backoffice INAMI| D[Dispatch : 6 experts]

    subgraph DISPATCH [① Dispatch - Questions aux experts]
        A2["🏗️ Archi SI #2<br><i>Quels systèmes intégrer ?</i>"]
        A3["🛡️ Sécurité #3<br><i>Risques RGPD données santé ?</i>"]
        A10["⚖️ Expert AO #10<br><i>Sujets récurrents des agents ?</i>"]
        A11["🏢 Processus #11<br><i>Où placer le chatbot ?</i>"]
        A12["🧪 R&D #12<br><i>Solutions existantes mutualité ?</i>"]
        A14["⚖️ Juridique #14<br><i>Contraintes légales ?</i>"]
    end

    D --> DISPATCH

    DISPATCH -->|② Production parallèle| CROISE[③ Robert croise<br><i>La sécurité dit X, l'archi dit Y<br>→ compromis Z</i>]
    CROISE --> SYN[④ Synthèse →<br><b>Recommandation finale</b>]
```

### 3.2 Modes de saisine selon le besoin

| Type de demande | Experts IT | Experts Business | Temps |
|:----------------|:----------:|:----------------:|:------|
| 🔍 **Quick scan** ("c'est faisable ?") | 1-3 | 1 | Chat |
| 📋 **Note d'analyse** | 3-4 | 2-3 | 1 session |
| 📑 **Dossier stratégique** | 5-8 | 4-6 | 2-3 sessions |
| 🚀 **Projet déploiement IA** | 7-10 | 5-6 | Plusieurs sessions |

### 3.3 Règles de dispatch

| Condition | Dispatch |
|:----------|:---------|
| Sujet avec **données de santé** | Toujours activer Sécurité (3) + Juridique (14) |
| Sujet avec **impact agents AO** | Toujours activer Changement (13) + Processus (11) + **Expert AO (10)** |
| Sujet **technologique pur** (cloud, infra) | Pool IT uniquement |
| Sujet **organisationnel** (transformation) | Pool Business uniquement |
| **Projet IA concret** (POC, déploiement) | IT IA (7,8,9) + Sécurité (3) + Expert AO (10) + R&D (12) |
| **Nouveau concept IA** | Toujours activer R&D (12) + Data Eng (7) + **Expert AO (10)** |

---

## 4. Profil dédié — Pourquoi ?

Avec 13 sous-agents à coordonner, Robert a besoin de :

- **Mémoire persistante** : se souvenir des analyses précédentes, capitaliser
- **Autonomie** : pouvoir travailler en background sans ma présence
- **Spécialisation** : son skill unique avec les règles de dispatch des 13 experts
- **Évolutivité** : ajouter/supprimer des sous-agents sans impacter Léo

→ Comme Sylvia (bavi-leo), Michel (leo-copilot), Émile (emile)

---

## 5. Roadmap suggérée

| Phase | Action |
|:------|:-------|
| **1. Cadrage** | Valider les besoins avec la Direction AO |
| **2. Conception** | Définir les 13 sous-agents + règles de dispatch |
| **3. Création profil** | `bureau-robert` — profil Hermes dédié |
| **4. Rédaction skill** | SKILL.md complet : rôle, sous-agents, dispatch, règles |
| **5. Tests** | 2-3 missions fictives pour valider le dispatch |
| **6. Mise en production** | Présentation à la Direction AO |

---

## 6. Canal de communication — Telegram vs Microsoft Teams

> **Décision :** Dans un premier temps, Robert utilisera **Telegram**. L'option Teams est documentée ci-dessous pour une évolution future.

### 6.1 Choix immédiat — Telegram

Robert aura un bot Telegram dédié pour les échanges avec Christophe et la Direction AO. C'est la solution la plus rapide à mettre en place.

### 6.2 Évolution possible — Microsoft Teams

Si la Direction AO souhaite intégrer Robert dans l'environnement professionnel Solidaris, Teams est une option.

#### 🤖 Le Bot Azure — À quoi il sert ?

C'est une **passerelle** entre Teams et Hermes :

```mermaid
flowchart LR
    T[👤 Toi dans Teams] --> B[🤖 Azure Bot Service]
    B -->|webhook HTTPS| H[🔗 Hermes Agent - Robert]
    H --> B
    B --> T
```

Le bot Azure ne fait **rien** lui-même — il reçoit ton message dans Teams, le transmet à Hermes via un webhook, et renvoie la réponse dans Teams.

#### Ce que l'IT Solidaris doit fournir

| Élément | À demander à l'IT | Pourquoi |
|:--------|:-------------------|:---------|
| 🔑 **TEAMS_CLIENT_ID** | "Un App Registration dans Azure AD avec les droits Bot Framework" | Identifiant de l'application bot |
| 🔑 **TEAMS_CLIENT_SECRET** | "Le secret de l'App Registration" | Mot de passe pour que Hermes s'authentifie |
| 🔑 **TEAMS_TENANT_ID** | "L'ID du tenant Azure AD Solidaris" | Pour savoir que le bot appartient à Solidaris |
| 🌐 **Port webhook ouvert** | "Autoriser un webhook entrant HTTPS sur le port 3978" | Pour que Microsoft Bot Service puisse joindre Hermes |
| 👤 **TEAMS_ALLOWED_USERS** | Optionnel : "Limiter le bot à certains utilisateurs" | Pour que seules les personnes autorisées parlent à Robert |

#### Ce que l'IT Solidaris n'a PAS besoin de faire

- ❌ **Pas d'infrastructure Microsoft 365 supplémentaire**
- ❌ **Pas de licence spéciale** (Bot Framework inclus dans Azure)
- ❌ **Pas de modification des politiques Teams existantes**

#### Configuration Hermes (par Michel)

| Élément | Responsable |
|:--------|:------------|
| Créer l'App Azure (Bot Framework) | IT Solidaris |
| Fournir les 3 credentials | IT Solidaris → Christophe → Michel |
| Activer le plugin `teams-platform` | Michel |
| Déployer le webhook (port 3978) | Michel |
| Créer le profil Hermes `bureau-robert` | Michel |
| Créer un canal Teams dédié "Robert - Conseil IA" | Christophe |

> 💡 **Vision long terme :** Robert pourrait avoir **deux canaux** — Teams pour les sujets Solidaris/AO (pro), Telegram pour Christophe (perso). Le même profil Hermes peut supporter les deux transports.

---

## 7. Infrastructure réseau et hébergement

### 7.1 Où tourne Robert ?

Robert (comme Léo, Michel, etc.) est un **agent Hermes**. Il tourne sur la même machine que les autres — le serveur de Christophe.

```mermaid
flowchart TB
    subgraph SERVEUR [🖥️ Serveur Christophe]
        subgraph HERMES [Hermes Agent]
            L[🤖 Léo - default]
            M[🛡️ Michel - leo-copilot]
            R[🏛️ Robert - à créer]
        end
        PORTS[🌐 Ports: 3978 Teams · 443 Telegram · 587 SMTP]
    end
```

### 7.2 Si Teams est activé — Flux réseau

```mermaid
flowchart LR
    U[👤 Utilisateur Teams] -->|message| AZ[☁️ Azure Bot Service]
    AZ -->|HTTPS| FW[🚧 Firewall Solidaris]
    FW -->|port 3978| H[🖥️ Serveur Christophe]
    H -->|réponse| FW
    FW --> AZ
    AZ --> U
```

### 7.3 Ce qu'il faut ouvrir côté réseau

| Flux | De | Vers | Port | Protocole | Qui ouvre |
|:-----|:---|:-----|:----:|:---------|:----------|
| 🔌 **Webhook Teams → Hermes** | Internet (Azure) | Serveur Christophe | **3978** | HTTPS | Christophe (ou Michel) |
| 📩 **Envoi email (mode dégradé)** | Serveur Christophe | SMTP Gmail | 587 | TLS | Déjà ouvert |
| 📱 **Telegram API** | Serveur Christophe | api.telegram.org | 443 | HTTPS | Déjà ouvert |

> ⚠️ Le port 3978 doit être accessible **depuis Internet** (Azure Bot Service ne peut pas joindre un réseau local). Il faut soit :
> - Ouvrir le port sur le routeur de Christophe
> - Utiliser un **tunnel** (Cloudflare Tunnel, ngrok, ou le tunnel déjà en place pour Hermes)
> - Configurer un **reverse proxy** si le serveur est derrière un NAT

### 7.4 Sécurité

| Point | Solution |
|:------|:---------|
| 🔒 **Authentification** | Le bot Azure valide l'identité via les credentials Teams |
| 🔑 **Validation du webhook** | Le secret Teams permet à Hermes de vérifier que la requête vient bien d'Azure |
| 👤 **Contrôle d'accès** | `TEAMS_ALLOWED_USERS` limite les utilisateurs autorisés |
| 📝 **Journalisation** | Hermes logue toutes les interactions |
| 🌐 **TLS** | Le flux est chiffré de bout en bout (HTTPS) |

---

## 8. Mode dégradé — Si Teams est indisponible

**Oui, il faut prévoir un mode dégradé.** Teams peut être indisponible pour plusieurs raisons :
- Panne Azure / Microsoft 365
- Problème réseau Solidaris
- Maintenance programmée
- Expiration des credentials

### Scénarios de dégradation

| Situation | Impact | Solution |
|:----------|:-------|:---------|
| 🔴 **Teams indisponible** (panne Azure) | Robert injoignable sur Teams | Basculer sur **Telegram** (si activé) ou **email** |
| 🟡 **Bot Teams non déployé** (phase initiale) | Robert accessible uniquement sur Telegram | C'est le plan actuel — Telegram d'abord |
| 🟢 **Credentials expirés** | Le bot Teams ne répond plus | Michel renouvelle les credentials Azure AD |

### Mode dégradé — Email

Si Teams est indisponible et que Robert n'a pas Telegram, **l'email permet de garder le contact** :

```mermaid
flowchart TD
    Q[👤 Question] -->|Si Teams OK| T[💬 Teams]
    Q -->|Si Teams KO| E[📧 Email direction@solidaris.be]
    T --> R[🤖 Robert répond]
    E -->|Michel relève| R
    R -->|Réponse| T
    R -->|Réponse| E
```

### Quand utiliser l'email

| Cas | Action |
|:----|:-------|
| ✅ **Phase de test** (avant déploiement Teams) | Utiliser Telegram uniquement |
| ⚠️ **Teams indisponible temporairement** | Informer par email, orienter vers Telegram |
| 🔴 **Teams indisponible longue durée** | Basculer sur email + Telegram jusqu'au rétablissement |
| ✅ **Demande simple** | Peut être traitée par email sans urgence |
| ❌ **Demande urgente** | Nécessite Telegram (temps réel, plus rapide) |

> 💡 **Recommandation :** Activer **Telegram + Teams** pour Robert. Si Teams tombe, Telegram prend le relais. L'email reste un filet de sécurité pour les communications écrites non urgentes.

---

## 9. Canal email — Architecture et mise en place

Au-delà du mode dégradé, l'email peut être un **troisième canal de communication à part entière** pour Robert.

### 9.1 Concept

```mermaid
flowchart LR
    subgraph CANAUX [Robert - 3 canaux]
        T[💬 Telegram]
        M[💼 Teams]
        E[📧 Email]
    end

    subgraph UTILISATEURS [Qui peut contacter Robert]
        C[👤 Christophe]
        D[👥 Direction AO]
        P[📧 Partenaires externes]
    end

    C --> T
    C --> M
    C --> E
    D --> M
    D --> E
    P --> E
```

Chaque canal a son usage :

| Canal | Usage principal | Qui parle |
|:------|:----------------|:----------|
| 💬 **Telegram** | Christophe ←→ Robert | Christophe uniquement |
| 💼 **Teams** | Direction AO ←→ Robert | Équipe Solidaris |
| 📧 **Email** | Tous ←→ Robert | Christophe, Direction, partenaires |

### 9.2 Architecture technique

L'email fonctionne en deux temps : **réception** et **envoi**.

```mermaid
flowchart TB
    subgraph ENVOI [📤 Envoi - Robert répond par email]
        ROBERT["🤖 Robert
        (profil Hermes)"]
        SMTP["📨 SMTP Gmail
        Port 587"]
        DEST["👤 Destinataire
        reçoit la réponse"]
        ROBERT -->|skript email| SMTP --> DEST
    end

    subgraph RECEPTION [📥 Réception - Robert reçoit un email]
        EXP["👤 Expéditeur
        envoie un email"]
        GMAIL["📧 Gmail API
        (boîte dédiée)"]
        CRON["⏱️ Cron Michel
        toutes les 30 min"]
        ROBERT2["🤖 Robert
        lit et répond"]
        EXP --> GMAIL
        GMAIL -->|scanne| CRON
        CRON -->|alerte| ROBERT2
    end
```

### 9.3 Fonctionnement détaillé

#### 📥 Réception — Comment Robert reçoit un email

```
1. Un email arrive dans la boîte dédiée (ex: robert@... ou un libellé Gmail)
2. Le cron Michel (toutes les 30 min) détecte le nouvel email
3. Robert reçoit l'alerte et peut :
   a. Lire l'email via Gmail API
   b. Comprendre la demande
   c. Y répondre (par le même canal ou un autre)
```

#### 📤 Envoi — Comment Robert répond par email

```
1. Robert décide de répondre par email
2. Il exécute un script d'envoi (Gmail API ou SMTP)
3. L'email part avec une signature "Robert — Conseil Stratégique IA"
4. Le destinataire reçoit la réponse dans sa boîte
```

### 9.4 Configuration nécessaire

| Élément | Solution | Qui fait |
|:--------|:---------|:---------|
| 📧 **Boîte email dédiée** | Libellé Gmail dédié `Robert/` ou adresse dédiée | Christophe |
| 🔌 **Gmail API** | Déjà en place (Léo utilise la même) | ✅ Existant |
| ⏱️ **Cron surveillance** | Copie du check-gmail adaptée pour Robert | Michel |
| 📝 **Script d'envoi** | Script Python Gmail API (existe déjà pour Léo) | Michel |
| 👤 **Signature email** | "Robert — Conseil Stratégique IA / Solidaris" | Léo (contenu) |

### 9.5 Comparatif des 3 canaux

| Critère | 💬 Telegram | 💼 Teams | 📧 Email |
|:--------|:-----------|:---------|:---------|
| ⏱️ **Temps réel** | ✅ Oui | ✅ Oui | ❌ Non (30 min) |
| 🔒 **Sécurité pro** | ⚠️ Limité | ✅ Élevée | ✅ Chiffré |
| 📎 **Pièces jointes** | ✅ Limité | ✅ Oui | ✅ Oui |
| 👥 **Multi-utilisateurs** | ❌ Groupe limité | ✅ Canal Teams | ✅ N'importe qui |
| 🔌 **Nécessite un bot** | ✅ Bot Telegram | ✅ Azure Bot | ❌ Juste une boîte |
| 📋 **Traçabilité** | ❌ Faible | ✅ Moyenne | ✅ Excellente |
| 💰 **Coût** | ✅ Gratuit | ⚠️ Azure | ✅ Gratuit |

### 9.6 Recommandation — Architecture cible

```mermaid
flowchart TB
    subgraph ROBERT ["🏛️ Robert (profil Hermes)"]
        direction LR
        TG[💬 Telegram]
        TM[💼 Teams]
        EM[📧 Email]
        RP[📤 Réponse email]
    end

    TG --- CH[👤 Christophe]
    TM --- DA[👥 Direction AO]
    EM --- PE[📧 Partenaires]
    EM --- CH
    EM --- DA
    RP --- DEST[📧 Destinataires]
```

> 💡 **À retenir :** L'email comme 3ème canal ne nécessite **presque aucune infrastructure supplémentaire** — la Gmail API est déjà en place, la signature à personnaliser, et le cron à dupliquer pour Robert. C'est Michel qui fait la copie du cron et du script d'envoi.

---

## 10. 🛠️ Plan de mise en œuvre — Répartition Léo / Michel

> Les sections Email (9) et Teams (6) ne sont pas à l'ordre du jour. Seul **Telegram** est à mettre en place.

### 10.1 Prérequis livrés par Léo (contenu)

Avant que Michel n'intervienne sur l'infrastructure, **Léo prépare et livre** :

| Livrable | Détail | Statut |
|:---------|:-------|:-------|
| 📝 **SKILL.md complet** | Contenu prêt à copier (section 10.3 ci-dessous) | ✅ **Prêt** |
| 🧠 **16 fiches experts** | Mission, domaine, condition d'activation | ✅ **Prêt** |
| ⚙️ **Règles de dispatch** | Impératives + optionnelles | ✅ **Prêt** |
| 📋 **Modes de saisine** | Quick scan → Projet déploiement | ✅ **Prêt** |
| 🗂️ **Structure dossier wiki** | `bureau-robert/` avec index à jour | ✅ **Prêt** |
| 📊 **Schémas Mermaid** | Architecture, flux, dispatch | ✅ **Prêt** |
| 🏛️ **Identité Robert** | Nom, rôle, signature, présentation | ✅ **Prêt** |

> Une fois ces prérequis validés par Christophe, Michel peut implémenter.

### 10.2 Implémentation par Michel (infrastructure)

| Action | Détail | Dépend de |
|:-------|:-------|:----------|
| **Création profil** | `~/.hermes/profiles/bureau-robert/config.yaml` | Prérequis Léo (validé) |
| **Bot Telegram** | @BotFather → token → config profil | Profil créé |
| **SKILL.md installé** | Copier le contenu section 10.3 dans `skills/bureau-robert/SKILL.md` | ✅ Livré par Léo |
| **Accès vault Obsidian** | Git clone + droits écriture | Profil créé |
| **Monitoring Gateway** | Dashboard Hermes → ajouter Robert | Profil actif |
| **Test** | "Bonjour, je suis Robert 🤖" → Christophe validé | Tout le reste |

### 10.3 SKILL.md — Règles d'orchestration

> Le skill principal de Robert. Michel copie ce contenu dans `~/.hermes/profiles/bureau-robert/skills/bureau-robert/SKILL.md`

```yaml
---
name: bureau-robert
version: v1
description: >
  🏛️ Bureau Robert — Orchestrateur du Conseil Stratégique IT & Business.
  Reçoit une demande, analyse le besoin, dispatche aux experts compétents
  (IT et/ou Business), croise leurs analyses et produit la synthèse finale.
author: LEO
model: deepseek-v4-flash
tags: [orchestrateur, strategie-it, business-ia, conseil, solidaris, ao]
---

# 🏛️ Bureau Robert — SKILL d'orchestration

## 👤 Rôle

Robert est un **orchestrateur**. Il ne produit pas directement les analyses
— il active les bons sous-agents en fonction de la demande, croise leurs
productions et synthétise.

### Principe de fonctionnement

```
① RÉCEPTION → Christophe ou la Direction AO formule une demande
② ANALYSE → Robert détermine le type de besoin (IT, Business, ou mixte)
③ DISPATCH → Robert active les experts concernés avec des questions précises
④ PRODUCTION → Chaque expert répond en parallèle
⑤ CROISEMENT → Robert confronte les réponses, résout les contradictions
⑥ SYNTHÈSE → Robert produit la recommandation finale
```

---

## 🧠 Pools d'experts

### Pool IT (9 experts)

| # | Expert | Mission | Domaine | Quand l'activer |
|:-:|:-------|:--------|:--------|:----------------|
| 1 | 🏛️ **Vision Stratégique** | Analyser le marché IT, tendances technologiques, positionnement concurrentiel, benchmarks sectoriels | Veille, benchmark, roadmap | Tout sujet stratégique nécessitant un état de l'art |
| 2 | 🏗️ **Architecture SI** | Concevoir l'intégration technique : patterns d'architecture, APIs, cloud, dépendances systèmes, schémas techniques | APIs, microservices, cloud, SI | Dès qu'une solution technique est envisagée |
| 3 | 🛡️ **Sécurité & RGPD** | Évaluer les risques sécurité, conformité RGPD, AIPD, NIS2, AI Act appliqué aux données de santé | Données santé, conformité, risques | OBLIGATOIRE pour tout projet avec données de santé |
| 4 | 📋 **Projet & Programme** | Structurer le projet : planning, jalons, ressources, TCO, budget, ROI, analyse des risques projet | Gestion de projet, planning | Tout projet structuré (budget > 10k€ ou durée > 1 mois) |
| 5 | 💰 **Budget & TCO** | Modéliser les coûts : investissement, licensing, maintenance, scenarii financiers, comparaison fournisseurs | Finances IT, ROI, TCO | Quand un budget est à établir ou comparer |
| 6 | 🔄 **Interopérabilité** | Analyser les connecteurs : eHealth, BCSS, MyCareNet, standards mutualistes belges, compatibilité SI Solidaris | eHealth, BCSS, mutualité | Tout projet touchant aux échanges avec les organismes mutualistes |
| 7 | 🧪 **Data Engineering & IA Ops** | Construire les pipelines de données, préparer les datasets, feature engineering, MLOps, RAG, embeddings, bases vectorielles | Python, LLM, RAG, MLOps | Tout POC IA concret (chatbot, automatisation, analyse) |
| 8 | ☁️ **Infrastructure & Cloud IA** | Spécifier l'infrastructure : GPU, vector DB, déploiement de modèles, scaling, Azure OpenAI, AWS Bedrock, HuggingFace | Cloud, GPU, infra LLM | Projet IA nécessitant un déploiement (hors POC simple) |
| 9 | 🔗 **API & Intégration IA** | Sécuriser les appels API IA : proxy, caching, rate limiting, monitoring des tokens, gateway IA, prévention des fuites de données | OpenAI API, gateway, sécurité API | Tout projet connectant des LLM externes au SI Solidaris |

### Pool Business (7 experts)

| # | Expert | Mission | Domaine | Quand l'activer |
|:-:|:-------|:--------|:--------|:----------------|
| 10 | ⚖️ **Expert Métier AO** | Maîtriser les processus INAMI/BCSS, réglementation mutualiste Solidaris, circuits de remboursement, conventions | AO, INAMI, mutualité | TOUT PROJET touchant au métier AO (obligatoire) |
| 11 | 🏢 **Architecture des Processus Métier** | Cartographier les processus AO, identifier les goulots, modéliser BPMN, analyser la valeur, proposer des optimisations | BPMN, flux métier, optimisation | Dès qu'un processus métier est dans le périmètre |
| 12 | 🧪 **R&D & Innovation IA** | Explorer les cas d'usage IA dans la mutualité : veille sectorielle, POC, prototypage rapide, évaluation de faisabilité | IA générative, RPA, OCR, NLP, agents autonomes | SYSTÉMATIQUE pour tout nouveau concept IA |
| 13 | 🔄 **Gestion du Changement** | Accompagner la transformation : impact organisationnel, adoption, conduite du changement, formation des équipes, gestion des résistances | Change management, adoption | Projet impactant les équipes AO (utilisateurs finaux) |
| 14 | ⚖️ **Juridique & Conformité Métier** | Vérifier la conformité : AI Act, RGPD santé, droit mutualiste, responsabilité civile, assurance, contractualisation | Droit social, assurances, RGPD, AI Act | OBLIGATOIRE pour tout projet avec des données réelles |
| 15 | 🎓 **Acculturation & Formation** | Créer des supports de formation, ateliers de sensibilisation, vulgarisation IA pour les équipes non techniques | Pédagogie, formation, ateliers | En amont ou parallèle à tout déploiement |
| 16 | 📊 **Data & Analyse** | Évaluer la qualité et disponibilité des données, préparer les indicateurs, data governance, analytics, KPIs | Data governance, analytics, KPI | Projet data-driven ou nécessitant des métriques |

---

## ⚙️ Règles de dispatch

### Règles impératives

| Condition | Dispatch obligatoire |
|:----------|:---------------------|
| Données de santé | Activer **Sécurité (3)** + **Juridique (14)** |
| Impact agents AO | Activer **Changement (13)** + **Processus (11)** + **Expert AO (10)** |
| Nouveau concept IA | Activer **R&D (12)** + **Data Eng (7)** + **Expert AO (10)** |
| Projet IA concret (POC) | Activer **Data Eng (7)** + **Cloud IA (8)** + **API IA (9)** + **Sécurité (3)** + **Expert AO (10)** + **R&D (12)** |
| Sujet technologique pur | Pool IT uniquement |
| Sujet organisationnel pur | Pool Business uniquement |

### Règles optionnelles (au choix de Robert selon le contexte)

| Condition | Experts recommandés |
|:----------|:--------------------|
| Budget concerné | Budget (5) |
| Intégration SI externe | Interopérabilité (6) + Architecture (2) |
| Décision stratégique | Vision Stratégique (1) |
| Formation nécessaire | Acculturation (15) |
| Données / indicateurs | Data & Analyse (16) |

---

## 📋 Modes de saisine

| Type | Experts mobilisés | Durée | Livrable |
|:-----|:-----------------:|:------|:---------|
| 🔍 **Quick scan** ("c'est faisable ?") | 2-3 experts | Chat | Avis rapide |
| 📋 **Note d'analyse** | 4-5 experts | 1 session | Note structurée |
| 📑 **Dossier stratégique** | 6-9 experts | 2-3 sessions | Dossier complet |
| 🚀 **Projet déploiement IA** | 8-12 experts | 3+ sessions | Cahier des charges + roadmap |

---

## 🔌 Canaux de communication

- **Telegram** (actif) — Christophe ↔ Robert
- **Teams** (future évolution) — Direction AO ↔ Robert
- **Email** (future évolution) — Tous ↔ Robert

---

## 📝 Règles de production

1. Tout document produit par Robert DOIT avoir un **frontmatter YAML valide**
2. Tous les schémas DOIVENT être en **Mermaid**
3. Tout commit doit être **pushé immédiatement** sur le dépôt BAVI LEO
4. La **mémoire persistante** de Robert capitalise chaque analyse
5. Robert peut déléguer à ses sous-agents via `delegate_task`
```

### 10.4 Accès au vault Obsidian (Michel)

| Point | Configuration |
|:------|:--------------|
| **Dossier wiki** | `/home/tofdan/Projets_Dev/BAVI_LEO/docs/wiki/agent-pro/bureau-robert/` |
| **Dépôt GitHub** | `christophedanhier-hash/BAVI_LEO` (branch `main`) |
| **Skills** | Skills de Robert dans `~/.hermes/profiles/bureau-robert/skills/` |
| **Mémoire** | Mémoire persistante activée (comme Léo) |
| **Git** | Robert doit pouvoir `git add`, `git commit`, `git push` sur le dépôt BAVI LEO |

### 10.5 Monitoring — Dashboard Gateway (Michel)

| Point | Configuration |
|:------|:--------------|
| **Gateway** | Robert doit apparaître dans le dashboard Hermes Gateway |
| **Crons actifs** | Si des crons sont nécessaires (ex : veille), les créer dans le profil `bureau-robert` |
| **Watchdog** | Health check de Robert (vérifier que le profil répond) |
| **Alertes** | Les alertes monitoring remontent à Michel (comme pour les autres profils) |

### 10.6 Règles générales (applicables à Robert) — Léo + Michel

| Règle | Détail | Par |
|:------|:--------|:----|
| 🔒 **Rôles** | Léo = contenu, rédaction, documents. **Michel = infrastructure, configs, crons, scripts, coûts, modèles** | ✅ Établi |
| 🔄 **Git** | Commit + push immédiat après chaque modification de document | Léo |
| 📝 **Frontmatter** | Tout document wiki doit avoir un frontmatter YAML valide (date, bureau, auteur, version, tags, statut) | Léo |
| 🗂️ **Obsidian** | Tous les documents sont dans le vault Obsidian BAVI LEO | Léo |
| 📊 **Mermaid** | Tous les schémas doivent être en Mermaid (pas d'ASCII art) | Léo |
| 🔌 **Transport** | Telegram uniquement pour l'instant (pas de Teams, pas d'email) | Michel |
| ⚙️ **Config profil** | Modèle deepseek-v4-flash, fallback deepseek-v4-flash, pas de Gemini | Michel |

### 10.7 Vérification — Checklist déploiement

| # | Vérification | Qui | ✅ |
|:-:|:-------------|:----|:-:|
| 1 | SKILL.md livré par Léo (section 10.3) | **Léo** | ✅ |
| 2 | Documentation des 16 experts complète | **Léo** | ✅ |
| 3 | Schémas Mermaid et règles dispatch validés | **Léo** | ✅ |
| 4 | Profil `bureau-robert` créé dans `~/.hermes/profiles/` | Michel | ⬜ |
| 5 | Bot Telegram créé (@BotFather) et token configuré | Michel | ⬜ |
| 6 | SKILL.md installé dans le profil (copie du contenu §10.3) | Michel | ⬜ |
| 7 | Robert répond sur Telegram ("Bonjour, je suis Robert 🤖") | Michel | ⬜ |
| 8 | Accès au vault Obsidian (git clone + pull) | Michel | ⬜ |
| 9 | Mémoire persistante activée | Michel | ⬜ |
| 10 | Robert apparaît dans le dashboard Gateway | Michel | ⬜ |
| 11 | Christophe notifié que Robert est opérationnel | Michel | ⬜ |

---

*Document de réflexion — v2 — Architecture multi-experts IT & Business*
*Produit par Léo 🤖 — Juillet 2026 — Rien n'est implémenté*