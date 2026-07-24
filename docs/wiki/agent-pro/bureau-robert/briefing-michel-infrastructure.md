---
date: 2026-07-15
bureau: bureau-robert
auteur: Robert (Bureau Robert)
destination: Michel (infrastructure Hermes)
version: v1
type: briefing-infrastructure
statut: finalise
tags: [michel, infrastructure, crons, deploiement, contexte, pro]
---

# 🔧 Briefing Infrastructure — Michel
## Ce que Robert a déjà fait · Ce qu'il reste à implémenter

> **De :** Robert 🏛️
> **À :** Michel 🛡️
> **Objet :** Tout ce que tu dois savoir pour intervenir sur le Bureau Robert sans casser ce qui existe ou refaire ce qui est fait.

---

## 1. Contexte général

Mettre à jour le contexte général pour refléter les profils réels utilisés.

| Élément | Valeur |
|:--------|:-------|
| **Profil** | `~/.hermes/profiles/bureau-robert/` |
| **Canal actif** | Telegram (session en cours avec Christophe) |
| **Modèle** | deepseek-v4-flash (provider deepseek) |
| **Dépôt** | `christophedanhier-hash/BAVI_LEO` |
| **Clone local** | `/home/tofdan/Projets_Dev/BAVI_LEO/` |
| **Wiki** | `https://christophedanhier-hash.github.io/BAVI_LEO/wiki/agent-pro/bureau-robert/` |

---

## 2. ✅ Ce que Robert a déjà fait — Ne pas refaire

| Élément | Détail | Où ça se trouve |
|:--------|:-------|:----------------|
| **Profil Hermes** | `bureau-robert` créé, config YAML avec modèle deepseek-v4-flash | `~/.hermes/profiles/bureau-robert/config.yaml` |
| **SOUL.md** | Règles d'orchestration du Bureau Robert | `~/.hermes/profiles/bureau-robert/SOUL.md` |
| **SKILL.md** | v2.4 — 16 experts IT/Business + Sophie #17 + règles dispatch | `~/.hermes/profiles/bureau-robert/skills/bureau-robert/SKILL.md` |
| **Bot Telegram** | Canal actif — Robert répond déjà | Config profil |
| **Mémoire persistante** | Active — capitalise chaque analyse | Profil Hermes |
| **Accès git BAVI LEO** | Clone local avec droits d'écriture, token GitHub configuré | `/home/tofdan/Projets_Dev/BAVI_LEO/` |
| **16 fiches expert** | Prompts personae complets (experts 01 à 16) | `docs/wiki/agent-pro/bureau-robert/expert-XX-xxx.md` |
| **Référentiel v4** | Document complet avec historique v1→v4 | `docs/wiki/agent-pro/bureau-robert/evolution-bureau-robert-v2-ia-business.md` |
| **Intégration Sophie #17** | Dispatch transverse, 5 situations, fallback | SKILL.md + référentiel |
| **Bureau Connaissance** | Nouveau bureau créé (structure + référentiel) | `docs/wiki/agent-pro/bureau-connaissance/` |
| **Référence dépôt** | Procédure vérification accès BAVI LEO | `skills/bureau-robert/references/bavi-leo-repository.md` |

> **Règle :** Si c'est dans cette liste, **ne le touche pas sans me demander** — c'est mon périmètre.

---

## 3. 🔧 Ce que Michel doit implémenter

### 3.1 Monitoring — Dashboard Gateway

| Action | Détail | Priorité |
|:-------|:-------|:---------|
| Ajouter Robert au dashboard Gateway | Robert doit apparaître dans la liste des profils Hermes surveillés | 🟡 Moyenne |
| Health check | Vérifier que le profil `bureau-robert` répond | 🟡 Moyenne |
| Alertes | Les alertes monitoring doivent remonter à Michel (comme les autres profils) | 🟡 Moyenne |

### 3.2 Cron — Veille hebdomadaire (Bureau Connaissance)

| Paramètre | Valeur |
|:----------|:-------|
| **Fréquence** | Hebdomadaire (lundi matin 8h) |
| **Action** | Scanner les nouveaux documents dans `docs/wiki/agent-pro/bureau-robert/`, extraire les frontmatter, produire une synthèse |
| **Destination** | `docs/wiki/agent-pro/bureau-connaissance/synthese-mensuelle-YYYY-MM-DD.md` |
| **Script** | À créer — Python, utilise le clone local BAVI LEO |
| **Comportement silence** | Si rien de nouveau → ne pas produire de rapport |
| **Notification** | En cas d'erreur → alerte à Michel |

### 3.3 Cron — Détection de patterns

| Paramètre | Valeur |
|:----------|:-------|
| **Fréquence** | Mensuelle (1er du mois) |
| **Action** | Analyser les tags des 30 derniers jours, détecter les sujets apparaissant 3× ou plus |
| **Destination** | `docs/wiki/agent-pro/bureau-connaissance/patterns-recurrents.md` |
| **Script** | À créer — Python |
| **Notification** | Si pattern détecté → Robert peut en informer Christophe |

### 3.4 Évolutions futures (pas urgent)

| Élément | Quand | Qui |
|:--------|:------|:----|
| Canal Teams | Si la Direction AO le demande | Michel (Azure Bot) |
| Canal Email | Si Christophe le décide | Michel (copie crons Gmail existants) |

---

## 4. 🚫 Ce que Michel ne doit PAS faire

| Action | Raison |
|:-------|:-------|
| ❌ Modifier le SKILL.md | C'est mon périmètre — contenu et experts |
| ❌ Modifier les fiches expert | C'est mon périmètre — contenu des prompts |
| ❌ Modifier le SOUL.md | C'est mon périmètre — règles orchestration |
| ❌ Modifier les documents du wiki | C'est mon périmètre — analyses |
| ❌ Créer/supprimer des experts dans le SKILL | C'est mon périmètre — architecture pools |
| ❌ Modifier les règles de dispatch | C'est mon périmètre — conditions activation |
| ❌ Créer un bot Telegram supplémentaire | Un seul bot, déjà actif |
| ❌ Ajouter des profils Hermes pour sous-agents | Les experts vivent dans mes delegate_task |

---

## 5. ⚠️ Points sensibles

| Point | Explication |
|:------|:------------|
| **Profil dédié** | Robert a SON profil (`bureau-robert`). Ne pas appliquer la config du profil `default` sans vérifier. |
| **Auteur git** | Commits signés `LEO (Christophe's Hermes)`. Ne pas changer. |
| **Token GitHub** | Déjà configuré (url.insteadof). Ne pas recréer. |
| **Port 3978** | Réservé pour Teams (si activé un jour). Pas avant. |

---

## 6. 📋 Checklist Michel

| # | Tâche | 🔧 |
|:-:|:------|:-:|
| 1 | Dashboard Gateway — ajouter Robert | ⬜ |
| 2 | Health check — Robert répond ? | ⬜ |
| 3 | Alertes monitoring → Michel | ⬜ |
| 4 | Cron veille hebdomadaire (script Python) | ⬜ |
| 5 | Cron détection patterns (script Python) | ⬜ |
| 6 | (Futur) Canal Teams si demandé | ⬜ |
| 7 | (Futur) Canal Email si demandé | ⬜ |

---

*Document produit par Robert 🏛️ à destination de Michel 🛡️*
*Juillet 2026*

> 🤖 Dernier audit : 24/07/2026 à 11:47 (UTC+2)
