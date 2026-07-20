---
date: 2026-07-16
bureau: bureau-robert
version: v1
tags: [prompt, notebooklm, presentation, strategie, solidaris, pro]
statut: finalise
type: prompt
---

# 🏛️ Prompt NotebookLM — Présentation Stratégique IA pour Solidaris
## À coller dans NotebookLM après avoir importé les 3 sources

---

## INSTRUCTIONS DE PRÉSENTATION

Tu es un conseiller stratégique IA. À partir des 3 sources fournies, génère une **présentation structurée** destinée au Comité de Direction de Solidaris (Direction AO, DSI, Budget, RSSI).

### Format attendu

Un document structuré avec les sections suivantes :

---

## SECTION 1 — Résumé exécutif (1 slide)

- Synthèse en 5 points clés
- Message principal : pourquoi Solidaris doit agir maintenant

## SECTION 2 — Contexte : l'IA en 2026-2028

Basé sur la **Note Stratégique Amodei** :
- Les 4 prédictions clés de Dario Amodei (CEO Anthropic)
- Implications concrètes pour une mutualité comme Solidaris
- Horizo

## SECTION 3 — Opportunité : Copilot Cowork

Basé sur le **Dossier Cowork** :
- Qu'est-ce que Copilot Cowork (définition simple)
- Ce qu'il peut faire pour les agents AO
- Les 4 buckets de coûts (vulgarisé)
- Grille tarifaire : Light / Medium / Heavy

## SECTION 4 — Scénarios budgétaires

Basé sur le **Dossier Cowork** (section 7) :
- **Scénario A — Pilote 50 users** : ~109 000 $/an
- **Scénario B — Partiel 200 users** : ~420 000 $/an
- **Scénario C — Généralisation 1 000 users** : ~2 100 000 $/an
- Coût moyen par utilisateur et par mois
- Tableau comparatif des 3 scénarios

## SECTION 5 — Comparatif : Cowork vs Alternative

Basé sur le **Dossier Cowork** (section 8) :
- **Cowork** : Intégration M365 native, coût élevé, vendor lock-in
- **API directe (via Robert)** : Coût 10-100× moins cher, personnalisable, à construire
- Tableau comparatif (prix, flexibilité, sécurité, délai)

## SECTION 6 — Points d'attention

Basé sur le **Dossier Cowork** (section 9) + **Référentiel Robert** :
- RGPD / données de santé
- AI Act (classification)
- NIS2
- Dépendance stratégique Microsoft
- Licence M365 Copilot obligatoire (30 $/user/mois)

## SECTION 7 — Recommandations

Basé sur le **Dossier Cowork** (section 10) :

**Court terme (T3-T4 2026) :**
1. Demander un devis partenaire Microsoft CSP
2. Vérifier le DPA Azure pour les données santé
3. Comparer Cowork vs API directe sur un cas d'usage AO précis
4. Lancer un POC 5 utilisateurs Cowork (1 mois)

**Moyen terme (2027) :**
5. Décider : Cowork, API directe, ou hybride
6. Négocier contrat pluriannuel
7. Former les équipes

## SECTION 8 — Conclusion

- « Personne n'est prêt, mais Solidaris peut l'être »
- La Direction AO a déjà une longueur d'avance (Robert, experts, gouvernance)
- Prochaine étape concrète

---

## RÈGLES DE MISE EN FORME

- Langue : **Français**
- Ton : **Professionnel mais accessible** (pas trop technique)
- Public : **Comité de Direction Solidaris** (non technique)
- Utilise des **tableaux** pour les chiffres et comparaisons
- Utilise des **listes à puces** pour les recommandations
- Pas de code, pas de jargon technique
- Les montants sont en **USD** (préciser)

---

## SOURCES À UTILISER

Les 3 documents suivants sont déjà importés dans le notebook :
1. `dossier-strategique-copilot-cowork-20260716.md` — Analyse détaillée Cowork
2. `note-strategique-predictions-amodei-20260716.md` — Prédictions IA
3. `evolution-bureau-robert-v2-ia-business.md` — Contexte et gouvernance Robert

> 🤖 Dernier audit : 20 July 2026 à 09:14 (UTC+2)

