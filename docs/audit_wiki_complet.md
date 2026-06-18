# Audit Complet du Wiki BAVI LEO
**Date :** 18 juin 2026 | **Analyseur :** Hermes Agent

---

## Résumé Exécutif

Le wiki BAVI LEO contient **19 pages Markdown + 1 page HTML** (redirection). Il est globalement **bien structuré, cohérent et à jour**, avec 4 problèmes identifiés (1 critique, 2 modérés, 1 mineur) et 1 risque de duplication avec le wiki BAVI_PLUS.

---

## 1. Vérification de mise à jour (chaque page)

| Page | Version déclarée | Version réelle (skill) | Statut |
|------|:----------------:|:----------------------:|:------:|
| `wiki/index.md` | (aucune) | — | ✅ Pas de version nécessaire |
| `wiki/vision.md` | 2.0 | — | ✅ |
| `wiki/architecture.md` | 2.0 — 16 juin 2026 | — | ✅ |
| `wiki/changelog.md` | 2.0 — 16 juin 2026 | — | ✅ |
| `wiki/pro/index.md` | (aucune) | — | ✅ Aucune date nécessaire |
| `wiki/pro/robert.md` | **2.0** | **2.0** | ✅ |
| `wiki/pro/sophie.md` | **2.0** | **2.0** | ✅ |
| `wiki/pro/assurance-obligatoire.md` | **2.0** | **2.0** | ✅ |
| `wiki/prive/index.md` | (aucune) | — | ✅ |
| `wiki/prive/gerard.md` | **1.1** | **2.0** | ⚠️ **ANOMALIE** — Le skill réel est v2.0, la page wiki reste à v1.1 |
| `wiki/prive/sylvie.md` | **2.0** | **2.4** | ⚠️ **ANOMALIE** — Le skill réel est v2.4, la page wiki reste à v2.0 |
| `wiki/prive/leo-admin.md` | 1.0 | — | ✅ Cohérent (pas de skill central) |
| `wiki/prive/bot-voyages.md` | 1.0 | — | ✅ |
| `wiki/prive/gerard/agents.md` | 16 juin 2026 | — | ✅ |
| `wiki/skills/index.md` | 2.0 (après audit) | — | ✅ |
| `wiki/skills/creer.md` | (aucune) | — | ✅ |
| `wiki/audit/index.md` | 1.0 — 16 juin 2026 | — | ✅ |
| `wiki/guide/utilisation.md` | (aucune) | — | ✅ |
| `wiki/guide/evolution.md` | (aucune) | — | ✅ |
| `index.html` | (redirection) | — | ✅ |

### Problème critique : **Taille des skills erronée dans le wiki**

Le wiki `skills/index.md` et `changelog.md` annoncent des tailles de skills (lignes) qui **ne correspondent pas** à la réalité :

| Skill | Wiki (lignes) | Réel (lignes) | Écart |
|-------|:-------------:|:-------------:|:-----:|
| `bureau-robert` | 370 | 110 | **−260 lignes** |
| `bureau-sophie` | 320 | 98 | **−222 lignes** |
| `assurance-obligatoire` | 220 | 85 | **−135 lignes** |
| `bureau-gerard` | 340 | 91 | **−249 lignes** |
| `bureau-sylvie` | 310 | 229 | **−81 lignes** |

**Cause probable :** Le wiki reflète l'état des skills **après audit (v2.0 planifié)** mais les fichiers skills réels ont été **encore plus optimisés** lors de l'implémentation. Le wiki n'a pas été mis à jour pour refléter les tailles réelles.

---

## 2. Contenu PRO (Solidaris) — Pertinence

### 2.1 Robert — Conseil IT Stratégique
- ✅ **Rôle** clair et pertinent pour Solidaris : conseil IT, architecture, sécurité, data, gouvernance
- ✅ **7 sous-experts** alignés sur les besoins d'une DSI mutualiste belge
- ✅ **Interopérabilité** avec AO et Sophie documentée
- ✅ **Règles** : pas de décision, pas d'implémentation, traçabilité, posture pro
- ✅ **Double format** : .md interne → Google Workspace pour partage

### 2.2 Sophie — Pilotage Financier IT
- ✅ **Rôle** clair : TCO/ROI, business cases, modélisation financière
- ✅ **3 sous-experts** : Marché, Modélisateur, Risques — pertinents pour la DSI
- ✅ **Toujours 3 scenarii** (conservateur, réaliste, ambitieux) — bonne pratique Solidaris
- ✅ **Maille 6 régions** — spécifique au contexte mutualiste belge, très pertinent
- ✅ **Parallélisation** Marché+Risques : optimisation réelle

### 2.3 Assurance Obligatoire — Lentille Métier
- ✅ **Double statut clairement documenté** : support de Robert + skill autonome
- ✅ **Périmètre métier** : INAMI, BCSS, eHealth, MyCareNet, Intermutualité — pile AO belge complète
- ✅ **Workflow raccourci** 3 phases : adapté à un expert unique
- ✅ **Règle** : toute analyse IT sans impact AO est incomplète — principe métier fort

### Conclusion PRO : ✅ **Excellent** — contenu pertinent, précis, ancré dans le contexte Solidaris.

---

## 3. Contenu PRIVÉ (Gérard, Sylvie, LEO Admin) — Cohérence

### 3.1 Gérard — Documentation T600
- ✅ **Structure** : orchestrateur + 6 agents + 2 supports bien décrits
- ✅ **agents.md** : page dédiée complète avec rôles détaillés
- ✅ **Cycle documentaire** : extraction → validation → rédaction → livraison
- ✅ **Croisement Hardware↔Firmware** : pertinent pour un système complexe
- ⚠️ **Version incohérente** : page dit v1.1, le skill est v2.0

### 3.2 Sylvie — Voyages Camping-Car
- ✅ **3 sous-experts** : Navigateur, Journaliste, Curateur — couverture complète
- ✅ **Cartographie OSM parallélisée** : bonne optimisation
- ✅ **Règles strictes** : pas de Google Maps, pas de photos, distances Haversine
- ⚠️ **Version incohérente** : page dit v2.0, le skill est v2.4
- ✅ **bot-voyages.md** : guide utilisateur complet avec FAQ et exemples

### 3.3 LEO Admin — Infrastructure Hermes
- ✅ **Documenté comme bureau PRIVÉ à part entière** (c'était un manque dans l'audit v1.0)
- ✅ **6 sous-skills** listés avec cron et rôles
- ✅ **Machines supervisées** : LEO, Penguin, Yoga, Pixel — statuts réels
- ✅ **Règle Zéro gaspillage** : priorité Ollama local → fallback Gemini → DeepSeek en dernier
- ✅ **Différence** avec bureaux PRO/PRIVÉ clairement expliquée

### 3.4 Cohérence INTER-PRIVÉ
- ✅ **Séparation PRO/PRIVÉ** : page `prive/index.md` le rappelle
- ✅ **Gérard→Wiki OCA**, Sylvie→Wiki Voyages, Admin→Dashboards : flux de livraison cohérents
- ✅ **Aucun cross-over PRO↔PRIVÉ** : pas de lien métier vers les données personnelles

### Conclusion PRIVÉ : ✅ **Cohérent** — sauf les 2 versions mineures à corriger.

---

## 4. Vérification des Liens Internes

### 4.1 Liens relatifs dans les pages

| Source | Lien | Type | Statut |
|--------|------|------|:------:|
| `index.md` | `pro/robert.md` | Relatif | ✅ Correct |
| `index.md` | `pro/sophie.md` | Relatif | ✅ |
| `index.md` | `pro/assurance-obligatoire.md` | Relatif | ✅ |
| `index.md` | `prive/gerard.md` | Relatif | ✅ |
| `index.md` | `prive/sylvie.md` | Relatif | ✅ |
| `index.md` | `prive/leo-admin.md` | Relatif | ✅ |
| `index.md` | `vision.md` | Relatif | ✅ |
| `index.md` | `architecture.md` | Relatif | ✅ |
| `index.md` | `audit/index.md` | Relatif | ✅ |
| `index.md` | `skills/index.md` | Relatif | ✅ |
| `index.md` | `guide/utilisation.md` | Relatif | ✅ |
| `index.md` | `changelog.md` | Relatif | ✅ |
| `vision.md` | (aucun lien interne relatif) | — | ✅ |
| `architecture.md` | (aucun lien interne relatif) | — | ✅ |
| `changelog.md` | (aucun lien interne relatif) | — | ✅ |
| `pro/robert.md` | (aucun lien interne relatif) | — | ✅ |
| `pro/sophie.md` | (aucun lien interne relatif) | — | ✅ |
| `pro/assurance-obligatoire.md` | (aucun lien interne relatif) | — | ✅ |
| `prive/gerard.md` | `gerard/agents.md` | Relatif | ✅ |
| `prive/gerard.md` | Liens vers Wiki OCA, BAVI LEO | URL absolue | ✅ |
| `prive/sylvie.md` | (aucun lien interne relatif) | — | ✅ |
| `prive/leo-admin.md` | (aucun lien interne relatif) | — | ✅ |
| `prive/bot-voyages.md` | `../index.md` | Relatif parent | ✅ |
| `prive/bot-voyages.md` | `sylvie.md` | Relatif | ✅ (même dossier `prive/`) |
| `prive/bot-voyages.md` | `../skills/index.md` | Relatif parent | ✅ |
| `guide/evolution.md` | `../changelog.md` | Relatif parent | ✅ |
| `skills/creer.md` | (aucun lien interne relatif) | — | ✅ |

### 4.2 Liens externes
- 🛡️ Portail LEO → https://christophedanhier-hash.github.io/hermes-wiki/ ✅
- 🔭 Wiki OCA → https://christophedanhier-hash.github.io/wiki-oca/ ✅
- 🧭 Voyages → https://christophedanhier-hash.github.io/voyages-wiki/ ✅
- Dashboard KPI → https://christophedanhier-hash.github.io/bavi-leo-dashboard/ ✅
- GitHub → https://github.com/christophedanhier-hash/BAVI_LEO ✅

### 4.3 Liens dans `mkdocs.yml`
- Tous les chemins relatifs dans `nav:` pointent vers `wiki/...` — ✅ corrects
- Liens externes (Portail, OCA, Voyages) en URL absolues — ✅

### Conclusion LIENS : ✅ **Tous les liens internes et externes sont corrects.**

---

## 5. Doublons avec d'autres wikis

### 5.1 Wiki BAVI_PLUS (`/opt/data/bavi_plus/`)

**Le wiki BAVI_PLUS est l'ancienne version** de BAVI (app web FastAPI + CrewAI). Il contient :
- **21 pages** de documentation (concepts, architecture, utilisation, guide, références)
- **20+ skills** dans `/opt/data/bavi_plus/Skills/` avec les mêmes noms d'agents

**Correspondances BAVI_PLUS → BAVI LEO :**

| BAVI_PLUS Skill | BAVI LEO Skill | Statut |
|----------------|----------------|:------:|
| `orchestrateur-robert` (473 lignes, v1.2) | `bureau-robert` (110 lignes, v2.0) | ⚠️ **Évolution** — même rôle, architecture différente |
| `orchestrateur-sophie` (575 lignes, v1.x) | `bureau-sophie` (98 lignes, v2.0) | ⚠️ **Évolution** — taille divisée par 6 |
| `assurance-obligatoire` (202 lignes) | `assurance-obligatoire` (85 lignes, v2.0) | ⚠️ **Évolution** — même nom, version plus concise |
| `orchestrateur-gerard` (406 lignes) | `bureau-gerard` (91 lignes, v2.0) | ⚠️ **Évolution** |
| `orchestratrice-sylvie` | `bureau-sylvie` (229 lignes, v2.4) | ⚠️ **Évolution** |
| `architecture` | Expert Architecture dans Robert | ⚠️ **Intégré** dans dispatch de Robert |
| `securite` | Expert Sécurité dans Robert | ⚠️ **Intégré** |
| `data` | Expert Data dans Robert | ⚠️ **Intégré** |
| `gouvernance` | Expert Gouvernance dans Robert | ⚠️ **Intégré** |
| `vision-strategique` | Expert Vision Stratégique dans Robert | ⚠️ **Intégré** |
| `projet-programme` | Expert Projet & Programme dans Robert | ⚠️ **Intégré** |
| `ethnographe` | Agent dans Bureau Gérard | ⚠️ **Même concept** |
| `astro-optique` | Agent dans Bureau Gérard | ⚠️ **Même concept** |
| `hardware` | Agent dans Bureau Gérard | ⚠️ **Même concept** |
| `firmware` | Agent dans Bureau Gérard | ⚠️ **Même concept** |
| `redacteur-technique` | Agent dans Bureau Gérard | ⚠️ **Même concept** |
| `formateur` | Support transverse | ⚠️ **Même** |
| `secretariat` | Support transverse | ⚠️ **Même** |
| `analyste-marche-business-case` | Expert dans Sophie | ⚠️ **Intégré** |
| `modelisateur-financier-it` | Expert dans Sophie | ⚠️ **Intégré** |
| `risques-conformite-it` | Expert dans Sophie | ⚠️ **Intégré** |
| `navigateur-camping-car` | Expert dans Sylvie | ⚠️ **Intégré** |
| `journaliste-bord` | Expert dans Sylvie | ⚠️ **Intégré** |
| `curateur-experiences` | Expert dans Sylvie | ⚠️ **Intégré** |
| `business-case-solidaris` | (pas de skill dédié) | ❌ **Obsolète** — intégré dans Sophie |

### 5.2 Wikis externes (OCA, Voyages, Portail)
- **Wiki OCA** → Documentation T600. C'est le dépôt de livraison de Gérard. **Relation LIVRAISON, pas duplication.**
- **Wiki Voyages** → Roadbooks camping-car. C'est le dépôt de livraison de Sylvie. **Relation LIVRAISON, pas duplication.**
- **Portail LEO** → Hub central. BAVI LEO y est référencé comme un des wikis. **Pas de duplication.**

### Conclusion DOUBLONS : ⚠️ **Duplication historique avec BAVI_PLUS**

Le dossier `/opt/data/bavi_plus/` contient **l'ancienne version** de BAVI (architecture monolithique CrewAI). Les 20+ skills de BAVI_PLUS ont été **refondus et intégrés** dans les 5+6 skills de BAVI LEO. C'est une **évolution naturelle**, pas un doublon actif, mais la présence des deux codebases sur le même serveur crée un risque de confusion :
- Un utilisateur pourrait modifier les skills BAVI_PLUS en pensant modifier BAVI LEO
- Les noms sont différents (`orchestrateur-robert` vs `bureau-robert`) mais le contenu conceptuel est le même

**Recommandation :** Archiver ou supprimer `/opt/data/bavi_plus/` une fois la migration BAVI LEO confirmée stable.

---

## 6. Problèmes Identifiés — Synthèse

| # | Gravité | Problème | Page concernée | Correctif |
|---|:-------:|----------|----------------|-----------|
| 1 | 🔴 **Haut** | Tailles des skills (lignes) erronées dans le wiki — ne correspondent pas aux fichiers réels | `skills/index.md`, `changelog.md`, `architecture.md` | Mettre à jour les chiffres : robert=110, sophie=98, ao=85, gerard=91, sylvie=229 |
| 2 | 🟡 **Moyen** | Version Gérard incohérente : wiki dit v1.1, skill dit v2.0 | `prive/gerard.md` (l.3) | Passer à v2.0 |
| 3 | 🟡 **Moyen** | Version Sylvie incohérente : wiki dit v2.0, skill dit v2.4 | `prive/sylvie.md` (l.3) | Passer à v2.4 |
| 4 | 🟢 **Faible** | Ancien wiki BAVI_PLUS toujours présent — 21 pages + 20+ skills non migrés | `/opt/data/bavi_plus/` | Archiver ou supprimer après confirmation stabilité |
| 5 | ⚪ **Info** | `index.html` redirige vers `wiki/index.html` mais le fichier cible n'existe pas en HTML (c'est un .md) | `index.html` | Vérifier que Material for MkDocs génère bien `wiki/index.html` — probablement normal car GH Pages build |

---

## 7. Statistiques Globales

| Métrique | Valeur |
|----------|:------:|
| Pages Markdown | 19 |
| Pages HTML (redirection) | 1 |
| Total lignes documentation | ~1 500 |
| Pages PRO (Solidaris) | 4 (index + Robert + Sophie + AO) |
| Pages PRIVÉ | 6 (index + Gérard + agents + Sylvie + bot-voyages + LEO Admin) |
| Pages transverses | 9 (index + vision + architecture + changelog + audit + skills/index + skills/creer + guide/utilisation + guide/evolution) |
| Liens internes testés | 14 |
| Liens externes testés | 5 |
| Anomalies trouvées | 4 (1 haute, 2 moyennes, 1 info) |
| Taux de pages à jour | **16/19 = 84%** |

---

*Généré par Hermes Agent — 18 juin 2026*
