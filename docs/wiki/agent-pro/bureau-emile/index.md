# 🎓 Bureau Émile — Assistant Pédagogique

**Bureau BAVI LEO — Mémoire de fin d'études en Sciences de l'Éducation**

## Présentation

Le Bureau Émile accompagne une étudiante dans la rédaction de son mémoire. Il combine :

| Composant | Rôle |
|-----------|------|
| 📖 **Wiki** | [emile-wiki](https://christophedanhier-hash.github.io/emile-wiki/) — Plan, chapitres, biblio |
| ☁️ **Drive** | Dossier partagé `bavi/bureau-emilie` — Brouillons, notes |
| 🤖 **Bot** | Profil Hermes `emile` — Relecture, suggestions, coaching |

## Architecture

- **Modèle principal** : DeepSeek v4 Flash
- **Fallback** : Gemini 3.5 Flash (contexte > 128K tokens)
- **Sync** : Drive → GitHub (wiki automatiquement à jour)

## Travaux

| Date | Sujet | Livrable |
|------|-------|----------|
| 26/06/2026 | Mise en place du bureau | Wiki, profil Hermes, Drive |

---
*Bureau créé par BAVI LEO — Bureau Michel 🔧*
