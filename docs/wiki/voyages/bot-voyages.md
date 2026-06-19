# 🤖 Bot BAVI LEO Voyages — Guide d'utilisation

**Version :** 1.0 | **Bot :** [@bavi_leo_voyages_bot](https://t.me/bavi_leo_voyages_bot) | **Profil :** PRIVÉ Personnel

---

## 🎯 Présentation

**@bavi_leo_voyages_bot** est un assistant IA dédié à la création de roadbooks pour voyages en camping-car. Il est propulsé par **Sylvie**, l'organisatrice de voyages du cabinet BAVI LEO.

### Ce que le bot sait faire

| Fonction | Description |
|----------|-------------|
| 🗺️ **Planifier un itinéraire** | Route, étapes, distances entre chaque étape |
| 🏕️ **Trouver des aires de service** | Campings, aires CC, points d'eau, vidanges |
| 📏 **Calculer des distances** | Distances kilométriques (Haversine) entre étapes |
| 🗺️ **Générer une carte OSM** | Carte interactive du trajet via OpenStreetMap |
| 📝 **Rédiger un journal de bord** | Documentation jour par jour |
| 💰 **Transparence des coûts** | Chaque livrable affiche son coût réel |

---

## 🚀 Démarrage rapide

### En message privé

1. Ouvre Telegram et cherche **@bavi_leo_voyages_bot**
2. Envoie un message comme :

> *"Salut ! Je veux créer un roadbook pour un voyage en camping-car de 2 semaines dans les Alpes en août 2026"*

3. Le bot te guide à travers les 7 phases du Bureau Sylvie :
   - **① Cadrage** → Destination, dates, durée
   - **② Dispatch** → Activation des experts nécessaires
   - **③ Production** → Itinéraire + carte OSM
   - **④ Croisement** → Vérification cohérence
   - **⑤ Synthèse** → Vue d'ensemble
   - **⑥ Livrable** → Roadbook complet
   - **⑦ Archivage** → Publication dans le wiki

### En groupe avec des amis

1. Crée un **groupe Telegram** avec tes amis
2. Ajoute **@bavi_leo_voyages_bot** comme membre
3. Tout le monde peut discuter et contribuer — le bot répond dans le groupe
4. Chacun peut proposer des étapes, des modifications, des idées

> 💡 **Astuce :** Le bot garde le contexte de la conversation. Si un ami suggère *"On pourrait passer par Annecy"*, le bot intègre la suggestion dans le plan en cours.

---

## 📝 Créer un roadbook — Exemple complet

### Étape 1 : Lancement

```
Toi : "On veut faire un roadbook de 10 jours en camping-car
       de Bruxelles à Barcelone, fin septembre 2026"

Bot : "Super projet ! 🚐 Je commence le cadrage.
       Avez-vous déjà des réservations (ferry, camping, hôtel)
       ou partez-vous de zéro ?"
```

### Étape 2 : Affinage

```
Toi : "On part de zéro. On veut passer par la côte atlantique.
       On est 2 adultes."

Bot : "Parfait ! Je planifie l'itinéraire :
       Bruxelles → La Rochelle → Bordeaux → Biarritz → Saint-Sébastien
       → Burgos → Madrid → Valence → Barcelone

       Je calcule les distances et cherche les aires de service..."
```

### Étape 3 : Livrable

Le bot produit un roadbook structuré avec :

- **Itinéraire complet** avec distances Haversine
- **Carte OSM interactive** du trajet
- **Suggestions d'aires** à chaque étape
- **Section coûts** transparente

---

## 🌐 Cartes OSM

Le bot génère des cartes interactives via OpenStreetMap. Les cartes sont :

- ✅ **Open source** — pas de dépendance Google
- ✅ **Interactives** — zoom, clic sur les étapes
- ✅ **Légères** — s'affichent sur mobile
- ❌ **Pas de Google Maps** — vie privée et pérennité

---

## 💰 Transparence des coûts

Chaque roadbook livré inclut une section **💳 Coût du service** :

| Métrique | Exemple |
|:---------|-------:|
| Tokens consommés | 198 728 IN · 20 924 OUT |
| Coût DeepSeek réel | 0,07 € |
| Frais de service | 2,50 € |
| **Total facturé** | **2,57 €** |

> Le bot tourne sur le modèle **DeepSeek v4 Flash** via la clé API de Christophe. Les coûts sont partagés sur le budget DeepSeek commun.

---

## ❓ FAQ

### Qui peut utiliser le bot ?
Christophe et ses amis invités dans le groupe Telegram. Accès restreint aux utilisateurs autorisés.

### Le bot parle quelle langue ?
Français (belge) — format de dates JJ/MM/AAAA.

### Puis-je modifier un roadbook après création ?
Oui ! Dis simplement *"Ajoute une étape à Lyon"* ou *"On veut passer par les Gorges du Verdon"*. Le bot met à jour l'itinéraire, les distances, la carte et les coûts.

### Les données sont-elles privées ?
Oui. Le bot tourne sur le serveur LEO de Christophe. Aucune donnée n'est partagée avec des tiers.

### Combien coûte un roadbook typique ?
Comptez ~1-3 € par roadbook complet selon la complexité (nombre d'étapes, cartes générées, itérations).

### Puis-je utiliser le bot pour un voyage déjà fait ?
Oui, il peut aussi servir à documenter un voyage passé avec le journal de bord.

---

## 📋 Commandes utiles

| Commande | Action |
|----------|--------|
| `/start` | Démarrer une conversation |
| `/new` | Nouveau roadbook (reset) |
| `/title [nom]` | Donner un nom au voyage |
| `/help` | Aide rapide |

---

## 🔗 Liens

- [Wiki BAVI LEO — Accueil](../index.md)
- [Bureau Sylvie — Méthodologie complète](sylvie.md)
- [Catalogue des Skills BAVI LEO](../skills/index.md)
- [GitHub BAVI LEO](https://github.com/christophedanhier-hash/BAVI_LEO)
