---
date: 2026-07-18
bureau: bureau-leo
auteur: LEO
version: v1.0
modele: deepseek-v4-flash
tags: [bavi, leo, architecture, bureaux, bots, skills, hermes, guide, pour-les-nuls, notebooklm]
statut: ✅ Nouveau
type: guide
hide:
  - toc
---

> **Dernière mise à jour rédactionnelle :** 18/07/2026 — Leo 🦁
> **Usage :** Document source pour Google NotebookLM (presentation BAVI LEO)

# BAVI LEO pour les Nuls

## Qu'est-ce que BAVI LEO ?

BAVI = **Bureaux Agentiques Virtuels**. C'est une facon d'organiser un assistant IA comme une vraie entreprise, avec des bureaux specialises, des procedures documentees, et des robots qui communiquent entre eux.

Concretement, Christophe (le createur) a transforme son IA personnelle en une equipe de 10 experts numeriques qui travaillent 24h/24 sans intervention humaine.

## L'architecture en 3 couches

```
Humain (Christophe)
     |
     v
[Gateway Telegram]  <-- 4 bots
     |
     v
[10 Bureaux]  <-- Michel, Robert, Sophie, Sylvia, etc.
     |
     v
[130+ Skills]  <-- Les procedures de chaque bureau
```

## Les 10 bureaux

Chaque bureau est un assistant specialise avec son propre role et ses propres outils :

| Bureau | Role | Analogie humaine |
|--------|------|------------------|
| Michel | Infrastructure, serveurs, crons | Le technicien informatique |
| Robert | Conseil strategique, 16 experts | Le comite de direction |
| Sophie | Finances, budget, factures | La comptable |
| Sylvia | Voyages, roadbooks, itineraires | L'agente de voyages |
| LEO | Dossiers personnels, analyses | L'assistant personnel |
| Emile | Pedagogie, formations | Le formateur |
| Gerard | Documentation technique T600 | Le documentaliste |
| Virginie | Sante, medecins, rendez-vous | L'infirmiere |
| Versioning | Gestion des versions de documents | L'archiviste |
| Connaissance | Base de connaissances centralisee | La bibliothecaire |

## Les 4 bots Telegram

BAVI LEO parle via 4 robots Telegram distincts, chacun specialise :

1. **LEO** (bot personnel) : dialogue avec Christophe, repond aux questions, gere les dossiers
2. **LEO Hub** (bot collectif) : point d'entree pour les sollicitations externes
3. **Michel / Leo Copilot** (bot infra) : execute les taches techniques (38 crons)
4. **Gateway** (hub de connexion) : achemine les messages vers le bon bot

## Le systeme de skills

Les skills sont les "procedures" de chaque bureau. Il y en a plus de 130, reparties par theme :

- Skills infrastructure : backup, monitoring, dashboards, deploiement
- Skills productivite : email, calendrier, budget, documents
- Skills recherche : veille IA, blogs, Youtube, arXiv
- Skills creatifs : ASCII art, diagrammes, animations, design
- Skills bureaux : chaque bureau a ses propres skills metier

Un skill est un fichier markdown (.md) qui decrit une procedure. Simple, lisible, versionne sur GitHub.

## Comment Hermes Agent fait le lien

Hermes Agent est le "cerveau" qui relie tout :
- Il fournit le gateway Telegram pour que les bots parlent aux humains
- Il execute les crons (taches planifiees) : 38 crons + 6 watchdogs
- Il charge les skills au moment de l'analyse pour donner le contexte au LLM
- Il gere la memoire persistante entre les sessions
- Il route les demandes vers le bon bureau via le dispatch conditionnel

## Les chiffres cles

- **10** bureaux specialises
- **4** bots Telegram simultanes
- **130+** skills documentes
- **38** crons Hermes + 6 watchdogs = **44** taches automatisees
- **16** experts dans le bureau Robert (DeepSeek V4)
- Budget total : **moins de 30 euros par mois**
- Un dashboard temps reel avec 20 indicateurs (CPU, budget, crons, etc.)
- 100% open source, pas de vendor lock-in

## Exemple d'une journee type

06:00 - Backup automatique des fichiers critiques
06:05 - Releve du solde DeepSeek dans Google Sheets
06:10 - Mise a jour du dashboard KPI
06:15 - Collecte CPU/RAM/disque des 3 machines
06:20 - Verification que tous les crons tournent
06:25 - Mise a jour de l'activite GitHub
08:00 - Analyse de 17 sources RSS, envoi de la veille IA par email
Toutes les 30 min - Classification des emails entrants
18:00 - Synchronisation Drive <> GitHub

Tout cela sans intervention humaine. BAVI LEO anticipe et agit.

## Pourquoi c'est unique

Ce n'est pas un simple chatbot. C'est un ecosysteme complet ou :
- Chaque bureau est independant mais peut appeler les autres
- Les procedures sont documentees (skills = heritage)
- Les taches tournent en automatique (crons = employes fiables)
- Tout est visible (dashboard = transparence totale)
- Tout est versionne (GitHub = pas de perte de connaissance)

---

*Document genere le 18/07/2026 — BAVI LEO pour les Nuls v1.0*
