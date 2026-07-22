---
date: 2026-07-15
bureau: bureau-connaissance
version: v1
tags: [connaissance, memoire, capitalisation, referentiel, v1, pro]
statut: finalise
type: referentiel
---

# 📚 Bureau de la Connaissance — Référentiel
## Capitalisation & Mémoire Organisationnelle

> **Bureau créé par :** 🏛️ Robert
> **Date :** 15/07/2026 | **Version :** v1
> **Mission :** Capitaliser, structurer et réutiliser toute la connaissance produite par les analyses des bureaux Robert, Sophie et associés.

---

## 1. Pourquoi ce bureau ?

Les 16 experts de Robert + Sophie produisent des analyses, mais **personne n'en fait la synthèse transverse**. Résultat :
- Les décisions passées sont difficiles à retrouver
- Les patterns récurrents ne sont pas détectés
- Chaque nouvelle analyse repart souvent de zéro
- La connaissance est dans les fichiers mais pas dans la mémoire collective

Le **Bureau de la Connaissance** comble ce vide.

---

## 2. Architecture — 4 sous-agents

| # | Expert | Mission | Livrable |
|:-:|:-------|:--------|:---------|
| 1 | 📖 **Mémorialiste** | Synthèses périodiques, mémoire organisationnelle | Synthèse hebdo/mensuelle |
| 2 | 📊 **Analyste transverse** | Tableaux de bord, KPIs d'activité, tendances | Dashboard d'activité |
| 3 | 🧩 **Bibliothécaire** | Indexation, recherche transverse, bibliothèque de cas | Bibliothèque de cas |
| 4 | 🔍 **Détecteur de patterns** | Sujets récurrents, questions standardisables | Rapport de patterns |

---

## 3. Déclencheurs

| Type | Déclencheur | Action | Fréquence | Qui |
|:-----|:------------|:-------|:----------|:----|
| ⏱️ **Programmé** | Cron hebdo | Scanner les nouveaux documents, produire la synthèse | Hebdomadaire | **Michel** 🔧 |
| 💬 **Sur demande** | Christophe dit « Robert, synthétise… » | Lancer le Mémorialiste + Analyste | Manuel | Robert |
| 💬 **Recherche** | Christophe dit « qu'avait-on dit sur X ? » | Lancer le Bibliothécaire | Immédiat | Robert |
| ⚡ **Seuil** | Même sujet 3× en 30 jours | Alerte : « pattern détecté » | Automatique | **Michel** 🔧 |

> **Note infrastructure :** Les crons programmés et l'automatisation par seuil sont gérés par **leo-copilot** (responsable infrastructure). Voir section 6.

---

## 4. Structure des documents

```
BAVI_LEO/docs/wiki/agent-pro/bureau-connaissance/
├── index.md                               ← Page d'accueil (auto-générée)
├── referentiel-bureau-connaissance.md     ← Ce document
├── synthese-mensuelle-YYYY-MM.md          ← Synthèses périodiques
├── tableau-de-bord-robert.md              ← KPIs du Bureau Robert
├── bibliotheque-cas-ia.md                 ← Cas d'usage IA documentés
├── patterns-recurrents.md                 ← Sujets & questions qui reviennent
└── repertoire-expertises.md               ← Qui sait quoi (annuaire des compétences)
```

---

## 5. Ce que le Bureau Connaissance produit

### Synthèse mensuelle

```
# Synthèse Mensuelle — Juillet 2026
## Bureau Robert 🏛️

📊 Activité : 7 analyses produites (4 finalisées, 2 archivées, 1 brouillon)
🧠 Experts sollicités : Vision, Archi, Sécurité, Projet, Budget
📂 Dossiers traités : SCOUT, ISO 27001, Assurance Obligatoire
🔍 Pattern détecté : 3 demandes sur la sécurité des données → standardiser ?
📎 Cas réutilisable : SCOUT V2 (architecture déploiement agent autonome)
```

### Tableau de bord

| Métrique | Juillet | Tendance |
|:---------|:------:|:---------|
| Analyses produites | 7 | 📈 |
| Experts sollicités | 5/16 | 🟡 |
| Projets IA identifiés | 2 | 📈 |
| Patterns détectés | 1 | 🆕 |
| Temps moyen de réponse | < 2h | ✅ |

### Bibliothèque de cas

| Cas | Problème | Solution | Statut | Lien |
|:----|:---------|:---------|:------:|:-----|
| Agent autonome SCOUT | Automatisation poste Windows | Autopilot Microsoft | ✅ Archivé | [lien] |
| ISO 27001 | Certification sécurité | Mise en conformité ISMS | ✅ Archivé | [lien] |

---

## 6. Infrastructure — Rôle de Michel

| Tâche | Qui | Description |
|:------|:----|:------------|
| 🏗️ Structure dossier + index | **Robert** ✅ | Création du répertoire et des documents |
| 📝 Contenu des documents | **Robert** ✅ | Rédaction des synthèses et analyses |
| ⏱️ **Cron veille hebdomadaire** | **Michel** 🔧 | Script qui scanne `bureau-robert/` et produit la synthèse |
| ⚡ **Cron détection patterns** | **Michel** 🔧 | Script qui repère les sujets récurrents |
| 🔄 **Mise à jour index** | **Robert** | Après chaque nouveau document |
| 📊 **Dashboard gateway** | **Michel** 🔧 | Ajouter le bureau au monitoring |

---

## 7. Exemple d'utilisation

```
Christophe : « Robert, qu'avait-on dit sur l'ISO 27001 ? »

Robert → active le Bibliothécaire →
  « 2 documents trouvés dans bureau-robert/ :
   1. Rapport ISO/IEC 27001:2022 (13/07/2026) ✅ Finalisé
   2. ANNEXE A — ISO/IEC 27001:2022 (13/07/2026) ✅ Finalisé
   Tags : securite, isms, certification, conformite
   Lien : [url]
   Résumé : Structure du standard, 93 contrôles, AIPD nécessaire. »
```

```
Christophe : « Fais le point sur les analyses de juillet »

Robert → active Mémorialiste + Analyste →
  « Synthèse mensuelle disponible : synthese-mensuelle-2026-07.md
   7 analyses, 5 experts, 2 patterns détectés. »
```

---

*Document : Référentiel du Bureau de la Connaissance — v1*
*Produit par Robert 🏛️ — Juillet 2026*

> 🤖 Dernier audit : 22 July 2026 à 07:40 (UTC+2)

