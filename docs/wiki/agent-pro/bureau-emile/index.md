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
| 26/06/2026 | Mise en place complète | Wiki, profil Hermes, bot Telegram, gateway s6, cron Drive sync |
| 26/06/2026 | Documentation finale | Analyse bureau-michel, skill bureau-emile, nav BAVI LEO |

## Architecture technique
- **Profil** : `/opt/data/profiles/emile/` · DeepSeek v4 Flash + Gemini fallback
- **Gateway** : s6-supervisé · `/run/service/gateway-emile`
- **Cron** : `Émile — Drive Sync → Wiki` · every 60m

---
*Bureau créé et maintenu par BAVI LEO — Bureau Michel 🔧*
