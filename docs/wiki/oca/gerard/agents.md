# 🧠 Les agents du Bureau Gérard

Le Bureau Gérard réunit **6 agents spécialistes** (dont 1 orchestrateur) et **2 skills support transverses** partagés avec les autres bureaux du cabinet virtuel.

---

## Orchestrateur

### `orchestrateur-gerard` — Gérard

> *Chef d'équipe du Bureau Gérard — coordination & livraison*

**Rôle :** Gérard est l'orchestrateur principal. Il combine deux fonctions :
1. **Coordination des 5 agents spécialistes** (ethnographe, astro-optique, hardware, firmware, redacteur-technique)
2. **Interface unique du pilote** : cadrage, arbitrage, contrôle qualité, livraison

**Principe :** Gérard ne décide jamais du fond technique et n'implémente jamais. Il coordonne la production documentaire et garantit la traçabilité.

**Quand l'utiliser :** construction de documentation d'équipement technique, assemblage d'un manuel, lancement d'un cycle ethnographe → experts → rédacteur.

---

## Les 5 experts métier

### `ethnographe` — The Interviewer

> *Extracteur de connaissance — traducteur du tacite vers le structuré*

**Rôle :** Traduit les discussions informelles, notes manuscrites, schémas et souvenirs des spécialistes en données brutes structurées. Posture d'enquêteur neutre et factuelle : n'invente aucune donnée, marque les lacunes.

**Position :** toujours en **amont** — sa sortie alimente tout le Bureau Gérard.

**Quand l'utiliser :** extraction de connaissance tacite, structuration d'entretien, décodage de schéma, construction de fiche composants.

!!! tip "Toujours mobiliser en premier"
    `ethnographe` est systématiquement mobilisé en entrée de cycle quand l'information est portée par un expert humain.

---

### `astro-optique` — The Astronomer-Physicist

> *Référent scientifique — optique, mécanique céleste, astronomie de position*

**Rôle :** Garantit que la documentation respecte les lois de l'optique et de l'astronomie de position : mise en station, suivi sidéral, backlash, erreur périodique. Valide l'intégrité conceptuelle des solutions.

**Position :** validation **transverse** — à mobiliser dès qu'une procédure touche à l'alignement ou aux tolérances.

**Quand l'utiliser :** validation de procédure de mise en station, collimation, calcul de tolérance de pointage.

---

### `hardware` — The Hardware Specialist

> *Référent électronique-électricité — câblage, alimentation, BOM, protections*

**Rôle :** Documente l'architecture matérielle, la distribution d'énergie, la protection des circuits, la connectique et les nomenclatures. Évalue l'obsolescence et propose des remplacements.

**Position :** **croisement** — entre extraction (ethnographe) et assemblage (redacteur-technique).

**Quand l'utiliser :** schéma de câblage, BOM, distribution d'alimentation, audit de protection, arbre de diagnostic électrique.

---

### `firmware` — The Firmware Expert

> *Systèmes embarqués — analyse de code C/Arduino/ESP32, rétro-ingénierie*

**Rôle :** Analyse le code des microcontrôleurs, documente la logique algorithmique, cartographie I/O, identifie la dette technique. Trace chaque assertion à sa source.

**Position :** **croisement** — entre extraction (ethnographe) et assemblage (redacteur-technique).

**Quand l'utiliser :** analyse de fichier `.ino`, documentation firmware, cartographie I/O, audit de bibliothèque tierce.

---

### `redacteur-technique` — The Lead Technical Writer

> *Architecte documentaire — assemblage final, harmonisation, mise en page*

**Rôle :** Assemble, harmonise et met en page la documentation technique finale (Markdown, manuels, fiches) à partir des contributions des autres agents. Normalise la terminologie, fusionne les contributions hétérogènes.

**Position :** **aval terminal** — reçoit les contributions de tous et produit le livrable final.

**Quand l'utiliser :** assemblage de documentation, production d'un manuel, harmonisation d'un corpus Markdown.

!!! tip "Toujours mobiliser en fin de cycle"
    `redacteur-technique` est systématiquement mobilisé en sortie pour consolider les contributions.

---

## Skills support transverses

Ces skills ne sont **pas** des agents dédiés du Bureau Gérard. Ils sont mobilisables par n'importe quel bureau BAVI.

### `secretariat`

> *Assistant de secrétariat virtuel — plume administrative et lecture des flux*

**Rôle :** Rédaction de mails, notes de service, comptes-rendus, rapports, synthèses. Adapte automatiquement le ton, le format et le canal selon le destinataire. FR principalement, NL et EN si demandé.

**Dans le cycle Bureau Gérard :** mail d'accompagnement d'un manuel, note de service, CR de revue documentaire, relance d'expert.

**Distinction :** `secretariat` couvre les gestes courts ; `redacteur-technique` produit le corpus long.

---

### `formateur`

> *Formateur virtuel — conception de parcours pédagogiques structurés*

**Rôle :** Conçoit et délivre des cours structurés progressifs. Construit un parcours complet : objectifs, prérequis, théorie, exemples, exercices, évaluation. Adapte le format à la demande.

**Dans le cycle Bureau Gérard :** transposer un livrable documentaire en module pédagogique — formation des mainteneurs, parcours d'apprentissage, montée en compétence des opérateurs.

**Distinction :** `formateur` s'appuie sur les livrables déjà produits par `redacteur-technique` ; il ne réécrit jamais le manuel source.

---

## Tableau récapitulatif

| # | Agent | Alias | Périmètre | Phase |
|---|-------|-------|-----------|:-----:|
| 1 | `orchestrateur-gerard` | Gérard | Coordination globale, cadrage, livraison | Pilotage |
| 2 | `ethnographe` | The Interviewer | Extraction de connaissance tacite | Amont |
| 3 | `astro-optique` | The Astronomer-Physicist | Validation scientifique | Validation |
| 4 | `hardware` | The Hardware Specialist | Électronique, câblage, BOM | Croisement |
| 5 | `firmware` | The Firmware Expert | Systèmes embarqués, code, I/O | Croisement |
| 6 | `redacteur-technique` | The Lead Technical Writer | Assemblage, harmonisation, livrable | Aval |
| ⬜ | `secretariat` *(support)* | — | Geste secrétarial court | Transverse |
| ⬜ | `formateur` *(support)* | — | Transposition pédagogique | Transverse |

---

*Documentation générée par LEO — BAVI LEO, 16 juin 2026*
