# 🏢 Bureaux PRO — Solidaris

Les bureaux PRO couvrent le périmètre métier de Christophe chez Solidaris : conseil IT stratégique, pilotage financier, et expertise Assurance Obligatoire.

---

## Bureaux disponibles

| Bureau | Domaine | Workflow | Interop |
|--------|---------|:--------:|---------|
| 🏛️ **Robert** | Conseil IT stratégique AO | 7 phases | → AO, Sophie |
| 💰 **Sophie** | Pilotage économique & financier IT | 7 phases (parallèle) | → Robert |
| 🛡️ **Assurance Obligatoire** | Lentille métier AO transverse | 3 phases (expert unique) | → Robert, direct |

---

## Relations entre bureaux PRO

```mermaid
flowchart LR
    Robert["Robert"]
    AO["Assurance Obligatoire"]
    Sophie["Sophie"]

    Robert -->|"impact AO"| AO
    Robert -->|"business case"| Sophie
    Sophie -->|"alignement stratégique"| Robert
    AO <-->|"double mode"| Robert

    style Robert fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style AO fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style Sophie fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    linkStyle default stroke-width:2px,fill:none
```

---

## Utilisation

Lancez un bureau depuis Telegram :
- `bureau-robert : <ta demande>`
- `bureau-sophie : <ta demande>`
- `assurance-obligatoire : <ta demande>`

---

## Principes

- **Neutralité technique** : pas de stack imposée
- **Ancrage AO** : le contexte par défaut est l'écosystème mutualiste belge
- **Non décisionnel** : LEO analyse, propose, alerte — tu décides
- **Dispatch conditionnel** : seuls les experts pertinents sont activés
