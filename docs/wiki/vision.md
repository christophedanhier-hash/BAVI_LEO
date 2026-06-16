# 🎯 Vision BAVI LEO

## Pourquoi BAVI LEO ?

BAVI (Bureau Agentic Virtuel Intégré) était une application web locale avec CrewAI. BAVI LEO transpose ce concept dans Hermes Agent :

| BAVI (ancien) | BAVI LEO (nouveau) |
|---------------|-------------------|
| App web FastAPI | Telegram natif |
| CrewAI multi-agents | Skills Hermes + LLM direct |
| SQLite + serveur | Zéro infra |
| Interface navigateur | Message mobile |
| Pas de recherche web | web_search intégré |
| Pas de cron | Automatisation Hermes |

## Principes fondateurs

1. **PRO vs PRIVÉ** — Distinction claire. Les bureaux PRO (Solidaris) sont isolés des bureaux personnels.
2. **1 à N bureaux** — Le système est extensible. Nouveau besoin ? Nouveau bureau.
3. **Wiki = base de connaissance** — Ce wiki évolue avec chaque nouveau bureau, skill et projet.
4. **LEO est l'orchestrateur** — Tu parles à LEO, LEO aiguille vers le bon bureau.

## Comment ça marche

1. Tu m'appelles sur Telegram avec une demande
2. Je charge le skill Hermes du bureau correspondant
3. Le skill définit mon rôle, mon workflow et mes contraintes
4. Je produis le livrable (analyse, note, business case, doc)
5. Le résultat est documenté ici — le wiki grandit
