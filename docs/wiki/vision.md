# 🎯 Vision BAVI LEO

**Version :** 2.0 (après audit optimisation)

---

## Pourquoi BAVI LEO ?

BAVI (Bureau Agentic Virtuel Intégré) était une application web locale avec CrewAI. BAVI LEO transpose ce concept dans Hermes Agent.

| BAVI (ancien) | BAVI LEO v1.0 | BAVI LEO v2.0 (optimisé) |
|---------------|---------------|--------------------------|
| App web FastAPI | Telegram natif | Telegram natif |
| CrewAI multi-agents | Skills Hermes monolithiques | Skills dispatch + interop |
| SQLite + serveur | Zéro infra | Zéro infra |
| Interface navigateur | Message mobile | Message mobile |
| Pas de recherche web | web_search intégré | web_search intégré |
| Pas de cron | Automatisation Hermes | Automatisation Hermes |
| — | — | **Dispatch conditionnel** (-30% tokens) |
| — | — | **Parallélisation phases** (2x plus rapide) |
| — | — | **Interopérabilité formelle** (bureaux connectés) |

---

## Principes fondateurs (réaffirmés après optimisation)

1. **PRO vs PRIVÉ** — Distinction claire. Les bureaux PRO (Solidaris) sont isolés des bureaux personnels.
2. **1 à N bureaux** — Le système est extensible. Nouveau besoin ? Nouveau bureau.
3. **Wiki = base de connaissance** — Ce wiki évolue avec chaque nouveau bureau, skill et projet.
4. **LEO est l'orchestrateur** — Tu parles à LEO, LEO aiguille vers le bon bureau.

## Nouveaux principes (v2.0)

5. **Dispatch conditionnel** — Seuls les sous-experts pertinents sont activés. Économie de tokens.
6. **Parallélisation** — Les phases indépendantes sont traitées en parallèle.
7. **Interopérabilité** — Les bureaux communiquent entre eux formellement.
8. **Traçabilité** — Chaque phase produit un artefact identifiable.

---

## Comment ça marche

1. Tu m'appelles sur Telegram avec une demande
2. Je détecte le bureau cible (par le nom dans ta demande)
3. Je charge le skill Hermes correspondant
4. Le skill définit mon rôle, mes sous-experts, mon workflow et mes contraintes
5. Seuls les experts pertinents sont activés (dispatch conditionnel)
6. Les phases parallélisables le sont
7. Si nécessaire, j'appelle un autre bureau (interopérabilité)
8. Je produis le livrable
9. Le résultat est archivé dans le wiki

---

## Roadmap

| Prochaine étape | Priorité | Statut |
|-----------------|:--------:|:------:|
| Nouveaux bureaux PRO (Compliance, QA) | 🟡 Moyenne | À définir |
| Nouveaux bureaux PRIVÉ (Jardin, Bricolage) | 🟢 Faible | Idée |
| Amélioration continue des workflows | 🔴 Haute | En cours |
