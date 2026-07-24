# 📋 Journal d'Audit Rédactionnel — BAVI_LEO

Dernier passage d'audit automatique : **24/07/2026**

## Résumé du passage

- **Total fichiers analysés** : 129 (actifs, hors archives/annexes)
- **Méthode** : Audit manuel déterministe (regex + vérité terrain) — 0 appel API (clé DeepSeek expirée)
- **Correctifs appliqués** : 169 patches auto-fix (partagés avec hermes-wiki)
- **Anomalies détectées** : 0 restante (toutes corrigées)
- **Statut global du wiki** : ✅ Tous fichiers à jour

## Correctifs appliqués (24/07/2026)

| Correctif | Fichiers | Détail |
|-----------|----------|--------|
| Footer audit → 24/07/2026 07:57 | 169 | Harmonisation date sur tous fichiers actifs |
| `41 crons` → `42 crons (39 actifs)` | 52 | Comptage exact partagé hermes-wiki |
| `39 crons` → `42 crons (39 actifs)` | 18 | Idem |
| `4 bots` → `5 bots` | 11 | 5 profils = 5 bots Telegram |
| `4 profils` → `5 profils` | 10 | default, emile, michel, robert, sylvia |
| `gemini-2.5-flash` → `gemini-3.5-flash` | 9 | Provider Google = gemini-3.5-flash |
| Références n8n → `(retiré 13/07/2026)` | 24 | Glossaires, exemples, annexes |
| Port dashboard 8765 → +9119 | 3 | Panel 8765 + Hermes dashboard 9119 |

## Vérité terrain (référence 24/07/2026)

| Composant | Valeur |
|-----------|--------|
| **Profils Hermes** | 5 (default, emile, michel, robert, sylvia) |
| **Bots Telegram** | 5 (un par profil, DM + handles) |
| **Crons** | 42 total (39 actifs, 2 désactivés, 1 pending) |
| **Dashboards** | Port 8765 (panel) + 9119 (Hermes dashboard) |
| **Modèles** | deepseek-v4-flash, deepseek-v4-pro, gemini-3.5-flash, qwen2.5:7b |
| **Providers** | deepseek (défaut), custom:ollama, custom:google, custom:openrouter |
| **Fallback chain** | deepseek-v4-flash → gemini-3.5-flash → qwen2.5:7b |
| **n8n** | ❌ Docker retiré le 13/07/2026 |
| **Timezone** | Europe/Brussels (UTC+2) |

## Remarques BAVI_LEO

- Les pages du guide-hermes-complet/ (9 fichiers) sont cohérentes
- Les dossiers personnels (quad, skoda, vélos) sont corrects
- Les analyses de scope (bureaux) sont à jour
- Les pages T600 (bureau-gerard) sont techniques et spécifiques — OK
- Les archives (bureau-*/archive/) ne sont pas modifiées — conservation historique

## Anomalies résiduelles

| Page | Section | Gravité | Problème |
|------|---------|---------|----------|
| — | — | — | **Aucune** — toutes corrigées |

---

> 🤖 Généré automatiquement par l'Auditeur de Wiki LEO le 24/07/2026 à 07:57 (UTC+2)
