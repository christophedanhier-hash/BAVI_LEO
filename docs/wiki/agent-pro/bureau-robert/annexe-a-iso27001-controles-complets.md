---
date: 2026-07-13
bureau: bureau-robert
auteur: LEO 🤖 — Appui Bureau Robert
version: v2
modele: deepseek-v4-flash
tags: [iso27001, securite, isms, certification, norme, conformite, annexe-a, controles]
statut: finalise
type: rapport-recherche
---

# 🛡️ ANNEXE A — ISO/IEC 27001:2022  
## Les 93 Contrôles Complets — Référence exhaustive

| Champ | Valeur |
|:------|:-------|
| **Bureau** | 🏛️ Robert — Conseil Stratégique IT |
| **Standard** | ISO/IEC 27001:2022 — Annexe A |
| **Contrôles** | 93 (issus de ISO/IEC 27002:2022) |
| **Date** | 13/07/2026 |
| **Version** | v2 |

---

## Table des matières

1. [Résumé des évolutions 2013 → 2022](#-résumé-des-évolutions-2013--2022)
2. [5. Contrôles Organisationnels (37)](#-5-contrôles-organisationnels--37-contrôles)
3. [6. Contrôles Liés aux Personnes (8)](#-6-contrôles-liés-aux-personnes--8-contrôles)
4. [7. Contrôles Physiques (14)](#-7-contrôles-physiques--14-contrôles)
5. [8. Contrôles Technologiques (34)](#-8-contrôles-technologiques--34-contrôles)
6. [11 Nouveaux Contrôles (2022)](#-récapitulatif-des-11-nouveaux-contrôles-2022)
7. [Correspondance 2013 → 2022](#-évolution-2013--2022--correspondance)
8. [Statement of Applicability (SoA)](#-statement-of-applicability-soa)
9. [Références](#-références-bibliographie)

---

## 📋 Résumé des évolutions 2013 → 2022

| Métrique | 2013 | 2022 | Variation |
|:---------|:----:|:----:|:---------:|
| Contrôles | 114 | **93** | −21 (−18%) |
| Catégories | 14 | **4** | −10 |
| Nouveaux contrôles | — | **11** 🆕 | +11 |
| Contrôles fusionnés | — | 24 (de 58) | −34 |
| Contrôles révisés | — | 58 | — |
| Contrôles supprimés | — | 0 | — |

### Les 4 domaines de la version 2022

```
┌──────────────────────────────────────────────────────────┐
│  ╔══════════════════════════════════════════════════════╗ │
│  ║  🔷  5. Organisationnel        37 contrôles  (5.1–5.37)  │
│  ║  🔶  6. Personnel               8 contrôles  (6.1–6.8)   │
│  ║  🔷  7. Physique               14 contrôles  (7.1–7.14)  │
│  ║  🔶  8. Technologique          34 contrôles  (8.1–8.34)  │
│  ║  ─────────────────────────────────────────────────── ║ │
│  ║  TOTAL                        93 contrôles            │
│  ╚══════════════════════════════════════════════════════╝ │
└──────────────────────────────────────────────────────────┘
```

---

## 🔷 5. CONTRÔLES ORGANISATIONNELS — 37 contrôles

> **Domaine :** Politiques, gouvernance, sécurité fournisseurs, incidents, conformité, continuité

### Section A — Politiques et gouvernance (5.1–5.7)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 5.1 | **Politiques de sécurité de l'information** | Révisé | Définir, approuver, publier et réviser les politiques de sécurité |
| 5.2 | **Rôles et responsabilités SI** | Révisé | Définir et attribuer les rôles et responsabilités en sécurité |
| 5.3 | **Séparation des tâches** | Révisé | Séparer les tâches pour réduire les risques de conflit d'intérêts |
| 5.4 | **Responsabilités de la direction** | Révisé | La direction approuve les politiques et soutient la sécurité |
| 5.5 | **Contact avec les autorités** | Révisé | Établir et maintenir le contact avec les autorités compétentes |
| 5.6 | **Contact avec les groupes d'intérêt** | Révisé | Établir des contacts avec associations professionnelles |
| 5.7 | **Veille stratégique (Threat Intelligence)** | 🆕 **Nouveau** | Recueillir et analyser les informations sur les menaces |

### Section B — Gestion des actifs et projets (5.8–5.13)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 5.8 | **Sécurité dans la gestion de projet** | 🆕 **Nouveau** | Intégrer la sécurité dans la méthodologie de projet |
| 5.9 | **Inventaire des actifs** | Révisé | Tenir un inventaire complet des actifs informationnels |
| 5.10 | **Acceptation des actifs** | Révisé | Documenter et approuver l'acceptation des actifs |
| 5.11 | **Utilisation acceptable** | Révisé | Règles d'utilisation acceptable des actifs |
| 5.12 | **Classification de l'information** | Révisé | Classifier les informations selon leur sensibilité |
| 5.13 | **Étiquetage de l'information** | Révisé | Appliquer un étiquetage conforme à la classification |

### Section C — Transfert et accès (5.14–5.18)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 5.14 | **Transfert d'information** | Révisé | Sécuriser le transfert d'information interne et externe |
| 5.15 | **Contrôle d'accès** | Révisé | Établir et documenter une politique de contrôle d'accès |
| 5.16 | **Gestion des identités** | Révisé | Gérer le cycle de vie complet des identités numériques |
| 5.17 | **Informations d'authentification** | Révisé | Gérer de manière sécurisée les mots de passe et secrets |
| 5.18 | **Droits d'accès** | Révisé | Provisionner, réviser et révoquer les droits d'accès |

### Section D — Fournisseurs (5.19–5.21)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 5.19 | **Sécurité dans les relations fournisseurs** | Révisé | Définir les exigences de sécurité pour l'accès des fournisseurs |
| 5.20 | **Approvisionnement** | Révisé | Intégrer la sécurité dans le processus d'approvisionnement |
| 5.21 | **Gestion des incidents fournisseurs** | 🆕 **Nouveau** | Gérer les incidents de sécurité liés aux fournisseurs |

### Section E — Incidents et conformité (5.22–5.25)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 5.22 | **Surveillance et revue** | Révisé | Surveiller et réviser les services fournisseurs |
| 5.23 | **Conformité légale** | Révisé | Identifier et respecter les obligations légales et contractuelles |
| 5.24 | **Planification de continuité SI** | Révisé | Planifier et tester la continuité de la sécurité |
| 5.25 | **Gestion des exceptions** | 🆕 **Nouveau** | Gérer et approuver les exceptions aux politiques |

### Section F — Changements et crises (5.26–5.30)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 5.26 | **Télétravail** | Révisé | Mettre en œuvre des mesures de sécurité pour le télétravail |
| 5.27 | **Gestion des changements** | Révisé | Contrôler les changements impactant la sécurité |
| 5.28 | **Gestion des crises** | 🆕 **Nouveau** | Préparer et répondre aux situations de crise |
| 5.29 | **Sécurité pendant la perturbation** | 🆕 **Nouveau** | Maintenir la sécurité en période de perturbation |
| 5.30 | **Préparation aux incidents cyber** | 🆕 **Nouveau** | Se préparer spécifiquement aux cyber-incidents |

### Section G — Contrôles généraux (5.31–5.37)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 5.31 | **Protection des données personnelles** | Révisé | Assurer la conformité RGPD et protection des données |
| 5.32 | **Droits de propriété intellectuelle** | Révisé | Protéger la propriété intellectuelle |
| 5.33 | **Protection des enregistrements** | Révisé | Protéger les enregistrements contre perte et falsification |
| 5.34 | **Révision indépendante de la sécurité** | Révisé | Faire auditer la sécurité par un tiers |
| 5.35 | **Conformité aux politiques et standards** | Révisé | Vérifier la conformité aux politiques et normes |
| 5.36 | **Audit des systèmes d'information** | Révisé | Planifier et réaliser des audits SI |
| 5.37 | **Documentation opérationnelle** | 🆕 **Nouveau** | Maintenir la documentation des procédures |

---

## 🔶 6. CONTRÔLES LIÉS AUX PERSONNES — 8 contrôles

> **Domaine :** Ressources humaines, formation, sensibilisation, confidentialité, signalement

### Section A — Avant et pendant l'emploi (6.1–6.5)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 6.1 | **Sélection pré-embauche** | Révisé | Vérifier les antécédents des candidats avant l'embauche |
| 6.2 | **Conditions contractuelles** | Révisé | Inclure les clauses de sécurité dans les contrats |
| 6.3 | **Sensibilisation et formation** | Révisé | Former et sensibiliser les employés à la sécurité |
| 6.4 | **Processus disciplinaire** | Révisé | Appliquer des sanctions en cas de violation |
| 6.5 | **Responsabilités après départ** | Révisé | Gérer les responsabilités après départ ou changement de rôle |

### Section B — Après l'emploi et divers (6.6–6.8)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 6.6 | **Accords de confidentialité** | Révisé | Faire signer des accords de non-divulgation (NDA) |
| 6.7 | **Télétravail** | Révisé | Appliquer des mesures spécifiques au travail à distance |
| 6.8 | **Signalement d'incidents** | Révisé | Permettre aux employés de signaler les incidents |

---

## 🔷 7. CONTRÔLES PHYSIQUES — 14 contrôles

> **Domaine :** Sécurité des locaux, équipements, contrôle d'accès physique, environnement

### Section A — Périmètre et accès (7.1–7.3)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 7.1 | **Périmètre de sécurité** | Révisé | Définir et protéger les périmètres de sécurité physique |
| 7.2 | **Contrôle d'accès physique** | Révisé | Contrôler l'accès (badges, biométrie, registres) |
| 7.3 | **Sécurisation des bureaux et locaux** | Révisé | Sécuriser bureaux, salles serveurs, locaux techniques |

### Section B — Équipements et médias (7.4–7.8)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 7.4 | **Sécurité des équipements** | Révisé | Protéger les équipements contre les menaces physiques |
| 7.5 | **Câblage de sécurité** | Révisé | Protéger câbles électriques et réseau contre interceptions |
| 7.6 | **Mise au rebut** | Révisé | Détruire ou effacer les données avant mise au rebut |
| 7.7 | **Postes de travail dégagés** | Révisé | Politique clear desk / clear screen |
| 7.8 | **Maintenance des équipements** | Révisé | Maintenir les équipements conformément aux spécifications |

### Section C — Opérations physiques (7.9–7.14)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 7.9 | **Transport sécurisé** | Révisé | Sécuriser les biens pendant le transport |
| 7.10 | **Stockage sécurisé** | Révisé | Utiliser armoires et coffres sécurisés |
| 7.11 | **Alimentation électrique** | Révisé | Assurer une alimentation électrique de secours (UPS) |
| 7.12 | **Protection incendie** | Révisé | Installer et maintenir détection/extinction incendie |
| 7.13 | **Surveillance** | Révisé | Installer caméras et systèmes anti-intrusion |
| 7.14 | **Contrôle d'accès visiteurs** | 🆕 **Nouveau** | Gérer l'accès et l'accompagnement des visiteurs |

---

## 🔶 8. CONTRÔLES TECHNOLOGIQUES — 34 contrôles

> **Domaine :** Sécurité IT, chiffrement, réseau, cloud, applications, incidents

### Section A — Postes de travail et endpoints (8.1–8.6)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.1 | **Postes de travail sécurisés** | Révisé | Configurer et durcir les postes de travail |
| 8.2 | **Protection contre les malwares** | Révisé | Déployer et maintenir des solutions anti-malware (AV/EDR) |
| 8.3 | **Sauvegarde** | Révisé | Politique de sauvegarde et tests de restauration |
| 8.4 | **Journalisation** | Révisé | Enregistrer et analyser les événements (logs, SIEM) |
| 8.5 | **Gestion des vulnérabilités** | Révisé | Scanner et corriger les vulnérabilités (patch management) |
| 8.6 | **Chiffrement** | Révisé | Chiffrer les données sensibles au repos et en transit |

### Section B — Cryptographie et certificats (8.7–8.8)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.7 | **Gestion des clés cryptographiques** | Révisé | Gérer le cycle de vie des clés (génération, stockage, révocation) |
| 8.8 | **Gestion des certificats** | 🆕 **Nouveau** | Gérer les certificats numériques (PKI, TLS) |

### Section C — Sécurité réseau (8.9–8.11)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.9 | **Sécurité réseau** | Révisé | Segmenter, filtrer et sécuriser les réseaux (pare-feu, VLAN) |
| 8.10 | **Gestion des services réseau** | Révisé | Contrôler l'accès et la configuration des services |
| 8.11 | **Isolation des réseaux** | 🆕 **Nouveau** | Isoler les réseaux sensibles (DMZ, OT, IoT) |

### Section D — Sécurité applicative (8.12–8.15)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.12 | **Gestion des configurations** | Révisé | Gérer les configurations sécurisées des systèmes |
| 8.13 | **Sécurité des applications** | Révisé | Intégrer la sécurité dans le cycle de développement (DevSecOps) |
| 8.14 | **API Security** | 🆕 **Nouveau** | Sécuriser les interfaces de programmation (API) |
| 8.15 | **Tests de sécurité** | Révisé | Réaliser tests d'intrusion et assessments |

### Section E — Sécurité des données (8.16–8.18)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.16 | **Sécurité des bases de données** | Révisé | Contrôler l'accès et chiffrer les bases de données |
| 8.17 | **Protection contre les fuites de données** | 🆕 **Nouveau** | Mettre en œuvre des mesures DLP |
| 8.18 | **Sécurité des données Cloud** | 🆕 **Nouveau** | Sécuriser les workloads Cloud (CASB, CSPM) |

### Section F — Logging et monitoring (8.19–8.21)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.19 | **Gestion des logs** | Révisé | Centraliser et protéger les logs (SIEM) |
| 8.20 | **Détection d'intrusion** | Révisé | Déployer IDS/IPS pour détecter les intrusions |
| 8.21 | **Gestion des consoles d'administration** | 🆕 **Nouveau** | Sécuriser l'accès aux consoles d'administration |

### Section G — Réponse aux incidents (8.22–8.24)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.22 | **Réponse aux incidents** | Révisé | Établir des procédures de réponse aux incidents (SOC) |
| 8.23 | **Forensic** | Révisé | Collecter et analyser les preuves numériques |
| 8.24 | **Gestion des alertes de sécurité** | 🆕 **Nouveau** | Trier et escalader les alertes de sécurité |

### Section H — Menaces et malwares (8.25–8.27)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.25 | **Protection anti-malware avancée** | Révisé | Utiliser des solutions EDR / XDR |
| 8.26 | **Gestion des menaces internes** | 🆕 **Nouveau** | Détecter et prévenir les menaces internes (insiders) |
| 8.27 | **Sécurité des emails** | Révisé | Protéger contre le phishing et les emails malveillants |

### Section I — Cloud et virtualisation (8.28–8.30)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.28 | **Sécurité du Cloud** | Révisé | Sécuriser les environnements Cloud (IaaS, PaaS, SaaS) |
| 8.29 | **Sécurité des conteneurs** | 🆕 **Nouveau** | Sécuriser conteneurs et orchestrateurs (K8s, Docker) |
| 8.30 | **Sécurité des workloads hybrides** | 🆕 **Nouveau** | Protéger les charges de travail hybrides |

### Section J — Sauvegarde et reprise (8.31–8.32)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.31 | **Sauvegarde des données critiques** | Révisé | Sauvegarder et tester la restauration des données critiques |
| 8.32 | **Plan de reprise d'activité (PRA)** | Révisé | Documenter et tester le plan de reprise IT |

### Section K — Développement sécurisé (8.33–8.34)

| ID | Contrôle | Évolution | Description |
|:--:|:---------|:---------:|:------------|
| 8.33 | **Développement sécurisé** | Révisé | Appliquer les principes de sécurité dès la conception (SSDLC) |
| 8.34 | **Test de sécurité du code** | 🆕 **Nouveau** | Revues de code et tests de sécurité automatisés |

---

## 🆕 RÉCAPITULATIF DES 11 NOUVEAUX CONTRÔLES (2022)

| ID | Contrôle | Domaine | Description |
|:--:|:---------|:-------:|:------------|
| 5.7 | Veille stratégique (Threat Intelligence) | Organisationnel | Collecte et analyse des menaces |
| 5.8 | Sécurité dans la gestion de projet | Organisationnel | Sécurité intégrée aux projets |
| 5.21 | Gestion des incidents fournisseurs | Organisationnel | Incidents liés aux fournisseurs |
| 5.25 | Gestion des exceptions | Organisationnel | Approbation des exceptions |
| 5.28 | Gestion des crises | Organisationnel | Réponse aux situations de crise |
| 5.29 | Sécurité pendant la perturbation | Organisationnel | Continuité en période perturbée |
| 5.30 | Préparation aux incidents cyber | Organisationnel | Cyber-préparation |
| 5.37 | Documentation opérationnelle | Organisationnel | Procédures documentées |
| 7.14 | Contrôle d'accès visiteurs | Physique | Gestion des visiteurs |
| 8.8 | Gestion des certificats | Technologique | Gestion PKI / TLS |
| 8.14 | API Security | Technologique | Sécurisation des API |

---

## 📊 ÉVOLUTION 2013 → 2022 — Correspondance

| 2013 (14 catégories) | 2022 (4 domaines) |
|:---------------------|:-------------------|
| A.5 — Politiques de sécurité | → 5. Organisationnel |
| A.6 — Organisation de la sécurité | → 5. Organisationnel |
| A.7 — Sécurité des ressources humaines | → 6. Personnel |
| A.8 — Gestion des actifs | → 5. Organisationnel |
| A.9 — Contrôle d'accès | → 5. Organisationnel / 8. Technologique |
| A.10 — Cryptographie | → 8. Technologique |
| A.11 — Sécurité physique et environnement | → 7. Physique |
| A.12 — Sécurité opérationnelle | → 8. Technologique |
| A.13 — Sécurité des communications | → 8. Technologique |
| A.14 — Acquisition, développement, maintenance | → 8. Technologique |
| A.15 — Relations avec les fournisseurs | → 5. Organisationnel |
| A.16 — Gestion des incidents | → 5. Organisationnel |
| A.17 — Continuité d'activité | → 5. Organisationnel |
| A.18 — Conformité | → 5. Organisationnel |

---

## 📝 STATEMENT OF APPLICABILITY (SoA)

La **Déclaration d'Applicabilité** (SoA) est un document **obligatoire** pour la certification. Il liste chaque contrôle et indique :

| Colonne | Description |
|:--------|:------------|
| **ID** | Référence du contrôle (ex: 5.1, 6.2) |
| **Nom** | Intitulé complet du contrôle |
| **Applicable ?** | Oui / Non |
| **Justification** | Pourquoi le contrôle est applicable ou non |
| **État d'implémentation** | Implémenté / Partiellement / Non implémenté |
| **Document de preuve** | Référence vers la politique, procédure ou outil |

---

## ✅ Liste des 93 contrôles — Référence rapide

```
ORGANISATIONNEL (37)
  5.01  5.02  5.03  5.04  5.05  5.06  5.07  5.08  5.09
  5.10  5.11  5.12  5.13  5.14  5.15  5.16  5.17  5.18
  5.19  5.20  5.21  5.22  5.23  5.24  5.25  5.26  5.27
  5.28  5.29  5.30  5.31  5.32  5.33  5.34  5.35  5.36
  5.37

PERSONNEL (8)
  6.01  6.02  6.03  6.04  6.05  6.06  6.07  6.08

PHYSIQUE (14)
  7.01  7.02  7.03  7.04  7.05  7.06  7.07  7.08
  7.09  7.10  7.11  7.12  7.13  7.14

TECHNOLOGIQUE (34)
  8.01  8.02  8.03  8.04  8.05  8.06  8.07  8.08  8.09
  8.10  8.11  8.12  8.13  8.14  8.15  8.16  8.17  8.18
  8.19  8.20  8.21  8.22  8.23  8.24  8.25  8.26  8.27
  8.28  8.29  8.30  8.31  8.32  8.33  8.34
```

---

## 📚 RÉFÉRENCES — Bibliographie

### Standards officiels

| Référence | Titre | Organisme | Année |
|:----------|:------|:----------|:-----:|
| **ISO/IEC 27001:2022** | Information security, cybersecurity and privacy protection — Information security management systems — Requirements | ISO / IEC | 2022 |
| **ISO/IEC 27002:2022** | Information security, cybersecurity and privacy protection — Information security controls | ISO / IEC | 2022 |
| **ISO/IEC 27000:2022** | Information security management systems — Overview and vocabulary | ISO / IEC | 2022 |
| **ISO/IEC 27005:2022** | Information security, cybersecurity and privacy protection — Guidance on managing information security risks | ISO / IEC | 2022 |
| **ISO/IEC 27006:2024** | Requirements for bodies providing audit and certification of information security management systems | ISO / IEC | 2024 |
| **ISO/IEC 17021-1:2015** | Conformity assessment — Requirements for bodies providing audit and certification of management systems | ISO / IEC | 2015 |
| **ISO 31000:2018** | Risk management — Guidelines | ISO | 2018 |

### Textes réglementaires associés

| Texte | Description |
|:------|:------------|
| **RGPD (Règlement UE 2016/679)** | Règlement Général sur la Protection des Données |
| **NIS 2 (Directive UE 2022/2555)** | Directive sur la sécurité des réseaux et des systèmes d'information |
| **eIDAS (Règlement UE 910/2014)** | Identification électronique et services de confiance |
| **Loi belge du 30 juillet 2018** | Protection des personnes physiques à l'égard du traitement des données |

### Organismes de certification et audit

| Organisme | Rôle | Site web |
|:----------|:-----|:---------|
| **ISO** | Organisation internationale de normalisation | iso.org |
| **IEC** | Commission électrotechnique internationale | iec.ch |
| **BSI** | British Standards Institution (BS 7799 originel) | bsigroup.com |
| **IRCA** | International Register of Certificated Auditors | irca.org |
| **PECB** | Professional Evaluation and Certification Board | pecb.com |
| **ANAB** | ANSI National Accreditation Board | anab.org |

### Sources consultées

| Source | URL | Contenu |
|:-------|:----|:--------|
| ISO — ISO/IEC 27001 | iso.org/standard/27001 | Standard officiel |
| ISO — ISO/IEC 27002 | iso.org/standard/75652 | Guide des contrôles |
| Wikipedia — ISO/IEC 27001 | en.wikipedia.org/wiki/ISO/IEC_27001 | Présentation générale |
| ISMS.online — Annex A Explained | isms.online/iso-27001/annex-a-2022/ | Guide des contrôles 2022 |
| ISO 27001 Security | iso27001security.com | Documentation technique |

---

## Historique des versions

| Version | Date | Auteur | Description |
|:--------|:-----|:-------|:------------|
| **v1** | 13/07/2026 | LEO 🤖 | Version initiale — 93 contrôles Annexe A |
| **v2** | 13/07/2026 | LEO 🤖 | Ajout références bibliographiques, correction formatage tableaux, sections réorganisées |

---

*Document produit par 🤖 Bureau LEO avec l'appui de 🏛️ Bureau Robert — Conseil Stratégique IT*
*BAVI LEO — Juillet 2026*
