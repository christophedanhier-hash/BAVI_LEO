---
date: 2026-07-16
bureau: bureau-robert
version: v1
tags: [notebooklm, source, fusion, strategie, cowork, amodei, gouvernance, solidaris, ao, pro]
statut: finalise
type: source-notebooklm
---

# 📦 Sources NotebookLM — Bureau Robert
## Dossier stratégique Copilot Cowork + Note Amodei + Référentiel Robert

> **Document unique** destiné à être importé dans NotebookLM pour générer une présentation.
> Fusion des 3 sources : Cowork, Amodei, Référentiel Robert.

---

# PARTIE 1 — DOSSIER STRATÉGIQUE COPILOT COWORK

---

## Contexte

Microsoft a publié en juillet 2026 son guide « Copilot Credits Guide » détaillant un nouveau modèle de facturation à l'usage pour les capacités IA avancées de son écosystème, notamment Copilot Cowork.

La Direction AO de Solidaris doit comprendre ce nouveau modèle pour :
- Anticiper les coûts potentiels d'une adoption
- Comparer avec les alternatives open source et autres fournisseurs
- Prendre une décision éclairée sur l'opportunité de déployer Cowork
- Budgétiser correctement les années à venir

---

## Qu'est-ce que Copilot Cowork ?

Copilot Cowork est un système agentique qui planifie, exécute et livre du travail réel de manière autonome dans l'environnement Microsoft 365. Décrivez le résultat que vous voulez, Cowork fait le travail.

Capacités :
- Email : rédiger, envoyer, classer, répondre automatiquement
- Calendrier : planifier des réunions, gérer les conflits
- Documents : créer, éditer des fichiers Word, Excel, PowerPoint
- Teams : poster dans les canaux, répondre aux messages
- Fichiers : organiser, déplacer, partager dans OneDrive/SharePoint

Prérequis : licence Microsoft 365 Copilot obligatoire. Cowork est facturé en supplément à l'usage (aucun crédit inclus dans l'abonnement).

---

## Architecture du modèle de coûts — Copilot Credits

Les Copilot Credits sont la monnaie commune pour tous les usages IA payants : Copilot Cowork, Work IQ APIs, Copilot Studio, Dynamics 365.

Les crédits sont mutualisés au niveau du tenant. La consommation totale est la somme des usages de tous les services.

---

## Les 4 buckets de coûts

Chaque tâche Cowork consomme des crédits selon 4 facteurs :

1. **Models** — Modèles IA : sélection automatique selon la tâche (léger, standard, haute qualité)
2. **Runtime** — Orchestration cloud : planification, exécution, suivi des agents, long-running
3. **Context** — Contexte : emails, fichiers, calendrier, personnes, Teams
4. **Tools** — Outils : chaque action concrète coûte 0,1 crédit (email, réunion, document, etc.)

---

## Grille tarifaire indicative

Taux de conversion : 100 crédits = 1 USD (prix catalogue Microsoft, juillet 2026)

- **Light** : 125 crédits (~1,25$) — contexte étroit, modèle léger, 0-1 outils
- **Medium** : 500 crédits (~5,00$) — contexte riche, modèle capable, plusieurs outils
- **Heavy** : 1 200 crédits (~12,00$) — agrégation large, modèle haute qualité

---

## Méthodologie d'estimation en 4 étapes

**Étape 1** — Définir les personas : Corporate Knowledge Worker, Customer-Facing, Technical Worker, Manager & Senior Leader

**Étape 2** — Estimer les prompts par persona et par mois :
- Corporate Knowledge Worker : 22 light, 11 medium, 5 heavy
- Customer-Facing : 17 light, 13 medium, 5 heavy
- Technical Worker : 12 light, 9 medium, 14 heavy
- Manager & Senior Leader : 13 light, 6 medium, 3 heavy

**Étape 3** — Appliquer le coût par prompt : (Light × 1,25$) + (Medium × 5,00$) + (Heavy × 12,00$)

**Étape 4** — Calculer le budget mensuel total : somme des coûts individuels × 12 pour l'annuel

---

## Scénarios budgétaires pour Solidaris

### Scénario A — Pilote Direction AO (50 utilisateurs)
- Agents AO : 30 × 147$/mois
- Managers AO : 10 × 86$/mois
- Tech/Support : 10 × 235$/mois
- Total Cowork : ~7 620$/mois
- Licence M365 Copilot : ~30$/user/mois
- **Total annuel : ~109 000 $**

### Scénario B — Déploiement partiel (200 utilisateurs)
- Total Cowork : ~28 990$/mois
- Licence M365 Copilot : ~30$/user/mois
- **Total annuel : ~420 000 $**

### Scénario C — Généralisation (1 000 utilisateurs)
- Total Cowork : ~145 000$/mois
- Licence M365 Copilot : ~30$/user/mois
- **Total annuel : ~2 100 000 $**

---

## Comparaison Cowork vs API directe

| Critère | Cowork | API directe (via Robert) |
|---------|--------|--------------------------|
| Intégration M365 | Native | Aucune (développement) |
| Sécurité données | Héritée M365 | À configurer (proxy) |
| Coût prompt heavy | ~12$ | ~0,05-0,50$ |
| Personnalisation | Limitée | Totale (RAG, fine-tuning) |
| Agentique | Intégré | À construire |
| Vendor lock-in | Élevé | Modéré |

---

## Points d'attention Solidaris

- **RGPD** : vérifier le DPA Azure pour les données de santé
- **AI Act** : classification du système, transparence requise
- **NIS2** : Solidaris probablement dans le périmètre (santé)
- **Licence M365 Copilot** : ~30$/user/mois, obligatoire
- **Vendor lock-in** : garder une architecture hybride comme alternative

---

## Recommandations

**Court terme (T3-T4 2026) :**
1. Demander un devis partenaire Microsoft CSP
2. Vérifier le DPA Azure pour les données santé
3. Comparer Cowork vs API directe sur un cas d'usage AO précis
4. Lancer un POC 5 utilisateurs Cowork (1 mois)

**Moyen terme (2027) :**
5. Décider entre Cowork, API directe, ou hybride
6. Négocier contrat pluriannuel
7. Former les équipes

---

# PARTIE 2 — NOTE STRATÉGIQUE PRÉDICTIONS AMODEI

---

## Contexte

Dario Amodei, CEO d'Anthropic (créateur de Claude), a partagé ses prédictions sur l'évolution de l'IA. Analyse traduite en opportunités et risques concrets pour la Direction AO de Solidaris.

---

## Les 4 prédictions clés

### Prédiction 1 — L'IA égalera ou dépassera les humains dans la plupart des tâches cognitives (2026-2028)

Pour Solidaris : agents AO assistés sur tâches complexes (remboursements, contentieux), réduction du temps de traitement, mais validation humaine obligatoire (AI Act).

### Prédiction 2 — Accélération médicale : 100 ans de progrès en 5-10 ans (2026-2030)

Pour Solidaris : nouveaux protocoles de soins, nouvelles nomenclatures INAMI, adaptation réglementaire massive, formation continue.

### Prédiction 3 — L'IA comme copilote permanent, pas un outil ponctuel (dès maintenant)

Pour Solidaris : chaque agent AO pourrait avoir son assistant IA dédié, productivité +30-50%, transformation profonde des métiers.

### Prédiction 4 — Chute des coûts de l'IA, accès quasi gratuit (2025-2027)

Pour Solidaris : plus d'excuse pour ne pas expérimenter, le risque n'est plus financier mais organisationnel et culturel.

---

## Analyse SWOT pour la Direction AO

**Forces :** Direction déjà sensibilisée à l'IA (via Robert), infrastructure en place, budget POC accessible
**Faiblesses :** Culture numérique hétérogène, données dispersées, pas de référent IA métier
**Opportunités :** Assistant IA pour chaque agent, automatisation tâches répétitives, analyse prédictive
**Menaces :** Résistance au changement, dépendance fournisseurs, conformité AI Act, fuite de données

---

## Recommandations

**Court terme (T3-T4 2026) :** POC Assistant IA AO, acculturation des équipes, cartographie processus automatisables, audit données disponibles

**Moyen terme (2027) :** Déploiement assistant IA (10-20 pilotes), mise en conformité AI Act, formation continue

**Long terme (2028+) :** IA généralisée 100% des agents, automatisation décisions courantes, intégration INAMI/BCSS

---

## Budget estimatif POC

- Infra cloud (Azure OpenAI) : 2 000 - 5 000 $/mois
- Data engineering : 10 000 - 20 000 $
- Développement POC : 15 000 - 30 000 $
- Acculturation et formation : 5 000 - 10 000 $
- **Total POC : 32 000 - 65 000 $**

---

## Conclusion — « Personne n'est prêt, mais Solidaris peut l'être »

La Direction AO a déjà une longueur d'avance : infrastructure stratégique (Robert et ses experts), vision claire, experts dédiés prêts à agir.

---

# PARTIE 3 — RÉFÉRENTIEL BUREAU ROBERT

---

## Qu'est-ce que le Bureau Robert ?

Robert est l'orchestrateur du Conseil Stratégique IT & Business pour la Direction AO de Solidaris. Il reçoit une demande, analyse le besoin, dispatche aux 16 sous-agents (9 IT + 7 Business) + 1 experte transverse (Sophie), croise leurs analyses et synthétise.

Canal actif : Telegram.

---

## Architecture des experts

### Pool IT (9 experts)
1. Vision Stratégique — marché, tendances, benchmarking
2. Architecture SI — APIs, cloud, intégration
3. Sécurité & RGPD — risques, AIPD, NIS2, AI Act (obligatoire données santé)
4. Projet & Programme — planning, jalons, TCO, ROI
5. Budget & TCO — coûts, licensing, scénarios financiers
6. Interopérabilité — eHealth, BCSS, MyCareNet
7. Data Engineering & IA Ops — pipelines, MLOps, RAG (systématique POC IA)
8. Infrastructure & Cloud IA — GPU, vector DB, déploiement
9. API & Intégration IA — proxy, caching, tokens, gateway IA

### Pool Business (7 experts)
10. Expert Métier AO — INAMI/BCSS, réglementation (obligatoire métier AO)
11. Architecture Processus Métier — BPMN, goulots, optimisation
12. R&D & Innovation IA — veille, POC, prototypage (systématique nouveau concept)
13. Gestion du Changement — impact, adoption, accompagnement
14. Juridique & Conformité — AI Act, RGPD santé (obligatoire données réelles)
15. Acculturation & Formation — supports, ateliers, vulgarisation
16. Data & Analyse — qualité données, KPIs, data governance

### Expert transverse
17. Sophie — Analyse Financière (business case, TCO, ROI, scénarios)

---

## Règles de dispatch impératives

- Données de santé → Sécurité (3) + Juridique (14)
- Impact agents AO → Changement (13) + Processus (11) + Expert AO (10)
- Nouveau concept IA → R&D (12) + Data Eng (7) + Expert AO (10)
- Projet IA concret (POC) → Data Eng (7) + Cloud IA (8) + API IA (9) + Sécurité (3) + Expert AO (10) + R&D (12)
- Budget simple → Budget (5)
- Analyse financière approfondie → Sophie (17)
- Christophe dit « Sophie, … » → détecter, lancer Sophie, relayer

---

## Modes de saisine

- Quick scan : 2-3 experts, chat, avis rapide
- Note d'analyse : 4-5 experts, 1 session, note structurée
- Dossier stratégique : 6-9 experts, 2-3 sessions, dossier complet
- Projet déploiement IA : 8-12 experts, 3+ sessions, CDC + roadmap

---

## Canaux de communication

- Telegram : actif, Christophe ↔ Robert
- Teams : évolution future (Direction AO)
- Email : évolution future

---

## Règles de production

1. Frontmatter YAML obligatoire sur tout document
2. Schémas Mermaid uniquement
3. Commit + push immédiat après chaque modification
4. Mémoire persistante active
5. Délégation aux sous-agents via delegate_task

---

## Ce que Robert ne fait pas

- Ne décide pas — aide à décider
- N'implémente pas — pas de code, config, déploiement
- Ne modifie pas l'infrastructure (c'est Michel)
- Ne stocke pas d'analyses personnelles

---

## Stockage

Toutes les analyses produites par Robert sont stockées dans :
BAVI_LEO/docs/wiki/agent-pro/bureau-robert/

Index auto-généré par agent-pro-index.py

---

## Bureau de la Connaissance

Bureau dédié à la capitalisation et à la mémoire organisationnelle. Alimenté automatiquement par Robert à chaque analyse produite (ajout d'une fiche dans la bibliothèque de cas).

URL : https://christophedanhier-hash.github.io/BAVI_LEO/wiki/agent-pro/bureau-connaissance/

---

*Document fusionné par Robert 🏛️ — Juillet 2026*
*Sources : dossier-strategique-copilot-cowork, note-strategique-amodei, referentiel-robert*
