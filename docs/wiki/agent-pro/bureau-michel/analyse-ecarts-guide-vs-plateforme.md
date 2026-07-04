---
date: 2026-07-04
bureau: bureau-michel
auteur: LEO
version: v2
modele: deepseek-v4-flash
tags: [analyse, guide, hermes, leo, ecart]
statut: archive (résolu)
type: analyse
---

# Analyse des écarts — Guide Hermès vs Plateforme réelle

## Résumé

Le guide « Hermès pour les Nuls » (6 440 lignes) a été confronté à la plateforme LEO réelle. **10 écarts majeurs** identifiés.

---

## 1. Nombre de bots : 3 → 4

| Dans le guide | Réalité |
|:--------------|:--------|
| 3 bots (Léo, Léo Copilote, Sylvia) | 4 bots (+ Émile 🎓) |

Le guide mentionne systématiquement "3 bots Telegram". Émile (profil pédagogique, créé le 25/06) est absent de toutes les sections.

**Correction :** Ajouter Émile dans :
- Présentation (3 bots → 4 bots)
- Tableau des profils (Ch.7)
- Schémas d'architecture (Ch.3)
- Chiffres clés (Ch.15)

---

## 2. Crons : 25 ou 30 ?

| Dans le guide | Réalité |
|:--------------|:--------|
| "25 crons" (Ch.26) | ~30 crons |

Le guide mentionne 25 crons dans certains chapitres et 30 dans d'autres. Aucune des deux valeurs n'est vérifiée après le crash.

**Note (04/07/2026) :** Après correction du guide v3.3, la valeur est maintenant de **14 crons** (après suppression de l'auto-fix-daemon orphelin et consolidation post-crash).

---

## 3. Dashboards : 7 → 1 unifié

| Dans le guide | Réalité (04/07/2026) |
|:--------------|:---------------------|
| 7 dashboards | **1 seul dashboard** (leo-dashboard) — les 7 pré-crash sont OBSOLÈTES |

> ⚠️ **Mise à jour majeure du 04/07/2026 :** Les 7 dashboards pré-crash (dashboard-leo/KPI, leo-global-dashboard, bavi-leo-dashboard, crons-dashboard, github-dashboard, leo-metrics, n8n-dashboard) sont obsolètes et figés au 30/06/2026. Le SEUL dashboard valable est le **leo-dashboard** généré par `collect-v2.py` (9 sources unifiées).

---

## 4. Nombre de machines : correct

3 machines (LEO, Yoga, Penguin) — conforme.

RAS.

---

## 5. Ollama : modèle obsolète ?

| Dans le guide | Réalité |
|:--------------|:--------|
| qwen2.5:7b | qwen2.5:7b (inchangé) |

L'analyse du Bureau Michel (26/06) recommande Gemma 4 26B MoE mais n'a pas été implémentée. Le guide est correct pour l'instant.

---

## 6. Budget : chiffres obsolètes

| Dans le guide | Réalité |
|:--------------|:--------|
| $19.46 (solde DeepSeek) | $60.31 |

Le guide mentionne l'ancien solde $19.46. Le compte a été rechargé à $29.99 le 29/06.

**Note (04/07/2026) :** Le coût réel estimé depuis le début est d'environ **$19.97** (tous profils confondus), contre $0.41 affiché par les anciens dashboards pré-crash. Le nouveau collecteur `collect-v2.py` fournit désormais un suivi fiable.

---

## 7. Token Google : information erronée

Le guide pourrait mentionner le "token mort" — cette information est fausse (le token LEO est valide et fonctionne).

---

## 8. Guide d'installation : obsolète

Le Ch.4 mentionne une installation via pip et Docker qui date de la v0.16.0. La version actuelle peut avoir des prérequis différents.

**Correction :** Vérifier la procédure d'installation auprès de la doc officielle.

---

## 9. Routes Tailscale

Quelques adresses IP mentionnées dans la partie technique pourraient être obsolètes. Les IPs Tailscale sont stables mais à vérifier.

**Note (04/07/2026) :** L'URL n8n a été corrigée de `100.92.102.28:5678` à `localhost:5678` dans le collecteur (timeouts aléatoires).

---

## 10. Pièges : le crash du 30/06

Le guide a été écrit AVANT le crash du 30/06. Les leçons du crash (sessions vidées, tokens à surveiller, rebuild.sh) ne sont pas documentées.

**Correction :** Ajouter un piège "Sessions non persistantes au reboot" dans Ch.31.

---

## Plan de correction (v2 — 04/07/2026)

| # | Écart | Priorité | Correctif |
|:-:|:------|:--------:|:----------|
| 1 | 3 bots → 4 | 🔴 | Ajouter Émile partout |
| 3 | 7 dashboards → 1 unifié | 🔴 | Mise à jour complète (guide v3.3) |
| 6 | Budget obsolète | 🟡 | Mettre à jour les chiffres (réel ~$19.97) |
| 10 | Crash non documenté | 🟡 | Ajouter piège + rebuild.sh |
| 2 | Crons 25/30 → 14 | 🟡 | Valeur corrigée dans guide v3.3 |
| 7 | Token Google | 🟢 | Vérifier avant d'écrire |
| 8 | Installation | 🟢 | Vérifier doc officielle |
| 9 | Routes Tailscale | 🟢 | n8n corrigé (localhost) |
*Document mis à jour le 04/07/2026 — 22:48:00 — Léo 🦁*
