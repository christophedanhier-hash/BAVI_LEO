# 📋 Changelog BAVI LEO

**Version :** 2.0 (audit optimisation) | **Date :** 16 juin 2026

---

## v2.0 — Audit & Optimisation (16 juin 2026)

### Audit complet
- Analyse détaillée des 5 bureaux + LEO Admin
- Matrice des différences (orchestrateur, sous-experts, workflow, interop)
- 6 axes d'optimisation identifiés

### Optimisations skills
|| Skill | v1.0 | v2.0 (audit) | Actuel |
||-------|:---:|:-----------:|:------:|
|| `bureau-robert` | 473→370 lignes | Dispatch 7 experts, interop AO+Sophie | 110 lignes |
|| `bureau-sophie` | 575→320 lignes | Parallélisation Marché+Risques | 98 lignes |
|| `assurance-obligatoire` | 202→220 lignes | Double rôle documenté | 85 lignes |
|| `bureau-gerard` | 406→340 lignes | Dispatch conditionnel, croisement HW↔FW | 91 lignes |
|| `bureau-sylvie` | 392→310 lignes | Cartographie OSM parallélisée | 229 lignes |

### Wiki enrichi
- **Architecture BAVI LEO** — nouvelle page dédiée
- **Audit & Optimisation** — analyse complète avec différences
- Pages PRO et PRIVÉ mises à jour (v2.0)
- Skills catalogue mis à jour

### Nouvelles fonctionnalités
- Workflow standardisé 7 phases pour tous les bureaux
- Dispatch conditionnel (économie de tokens)
- Interopérabilité formelle Robert↔AO↔Sophie
- LEO Admin documenté comme bureau PRIVÉ
- Règle formats : .md travail interne → Google Workspace pour partage PRO

### Dashboard KPI BAVI LEO
- Nouveau dashboard de monitoring avec KPIs temps réel
- Sessions, tokens, coûts, budget, sources, modèles
- Collecteur Python + déploiement GitHub Actions
- Cron toutes les heures
- 📊 https://christophedanhier-hash.github.io/bavi-leo-dashboard/

---

## v1.0 — Création initiale (16 juin 2026)

- Création de BAVI_LEO : wiki + 5 skills Hermes
- 6 bureaux : Robert, Sophie, AO, Gérard, Sylvie, LEO Admin
- Wiki Material sur GitHub Pages
- Architecture PRO vs PRIVÉ
- 15 pages wiki
