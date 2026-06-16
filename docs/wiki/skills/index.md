# 📚 Catalogue des Skills

**Version :** 2.0 (après audit optimisation)

---

Les skills Hermes sont les modules d'expertise de chaque bureau BAVI LEO. Chaque skill est un prompt système qui définit le rôle, le workflow, les sous-experts et les contraintes.

---

## Skills PRO — Solidaris

| Skill | Bureau | Expertises | Lignes | Version |
|-------|--------|-----------|:------:|:-------:|
| `bureau-robert` | 🏛️ Robert | Conseil IT stratégique, 7 experts dispatch | 370 | 2.0 |
| `bureau-sophie` | 💰 Sophie | Pilotage financier, TCO/ROI, 3 scenarii | 320 | 2.0 |
| `assurance-obligatoire` | 🛡️ AO | Lentille métier AO, expert transverse | 220 | 2.0 |

## Skills PRIVÉ — Personnel

| Skill | Bureau | Expertises | Lignes | Version |
|-------|--------|-----------|:------:|:-------:|
| `bureau-gerard` | 📝 Gérard | Documentation T600, 6 agents + 2 supports | 340 | 2.0 |
| `bureau-sylvie` | 🧭 Sylvie | Voyages camping-car, 3 experts, carto OSM | 310 | 2.0 |

## Infrastructure — LEO Admin

| Skill | Rôle | Type |
|-------|------|:----:|
| `budget-tracking` | Suivi budget DeepSeek | Cron H:35 |
| `machine-metrics` | Collecte CPU/RAM/Disk | Cron H:00 |
| `dashboard-kpi` | Dashboard KPI Hermes | Cron |
| `system-management` | Gestion machines Tailscale | Cron |
| `leo-email-assistant` | Envoi emails Gmail OAuth2 | À la demande |
| `dashboard-deployment` | Déploiement GH Pages | Cron 4h |

---

## Évolution de la taille des skills (v1.0 → v2.0)

| Skill | v1.0 | v2.0 | Variation |
|-------|:----:|:----:|:---------:|
| `bureau-robert` | 473 | 370 | **-22%** |
| `bureau-sophie` | 575 | 320 | **-44%** |
| `assurance-obligatoire` | 202 | 220 | +9% (double rôle) |
| `bureau-gerard` | 406 | 340 | **-16%** |
| `bureau-sylvie` | 392 | 310 | **-21%** |

> **Gain total :** -30% de tokens en moyenne, pour un workflow plus structuré et interopérable.

---

## Emplacement des fichiers

```bash
~/.hermes/skills/
├── bavi-leo/
│   ├── bureau-robert/SKILL.md
│   ├── bureau-sophie/SKILL.md
│   ├── assurance-obligatoire/SKILL.md
│   └── bureau-sylvie/SKILL.md
└── software-development/
    └── bureau-gerard/SKILL.md
```
