---
date: 2026-07-14
bureau: bureau-robert
version: v1.0
modele: deepseek-v4-pro
tags: [kilo-code, tofdan, site, prompt, astrophotographie]
statut: prompt
type: note
---

# 💻 Prompt pour Kilo Code — Développement site tofdan.be

> **Contexte :** Tu es leo-copilot, assistant code utilisant le modèle local qwen2.5:7b et les providers deepseek, openai, gemini, grok, anthropic. Tu travailles sur le serveur LEO via SSH, avec les outils en ligne de commande. Tu dois créer le nouveau site www.tofdan.be pour remplacer l'actuel Google Sites.

---

## 🎯 Objectif

Refaire le site **www.tofdan.be** (actuellement sur Google Sites) en HTML/CSS/JS statique, responsive, et moderne. Le thème est **l'astrophotographie** (Tof & Syl). Le site sera servi par Nginx sur le serveur LEO.

---

## 📁 Structure à créer

```
/var/www/tofdan.be/
├── index.html              ← Accueil (astro + présentation)
├── astro.html              ← Section astrophotographie
├── app-astro.html          ← Page d'info + lien vers l'App Astro
├── news.html               ← Actualités
├── materiel.html           ← Mon matériel (télescopes, caméras)
├── album.html              ← Galerie photos
├── meteo-astro.html        ← Météo pour observation
├── biblio.html             ← Bibliographie
├── chat.html               ← Contact / Message
├── css/
│   └── style.css           ← Design responsive
├── js/
│   └── main.js             ← Interactivité
└── images/                 ← Photos astro (Lune, Soleil, ciel)
```

---

## 🎨 Design

- **Thème :** Astrophotographie — fond sombre (#0a0a1a), étoiles, tons bleu/violet (#4f46e5, #7c3aed)
- **Responsive :** Mobile-first, adaptation desktop
- **Typographie :** Lisible sur fond sombre — polices système ou Google Fonts (ex: Inter, Space Grotesk)
- **Éléments :** Header avec navigation, hero image (ciel étoilé ou Lune), sections de contenu, footer avec crédits "(C) Tofdan - 2025"

---

## 📄 Pages et leur contenu

### index.html — Accueil
- Hero : "ASTRO PHOTOGRAPHIE" (comme le site actuel)
- Message de bienvenue (Texte existant à reprendre du Google Sites)
- Photos Lune et Soleil en vedette
- Lien vers Facebook
- Footer : "(C) Tofdan - 2025"

### astro.html — Astrophotographie
- Présentation de la passion pour l'astronomie
- Photos du ciel, Lune, Soleil
- Latitude : 50°32' N, Longitude : 4°36' E

### app-astro.html — App Astro
- Présentation de l'application interactive
- Lien cliquable : https://christophedanhier-hash.github.io/Projet-Astro/www/index.html
- Texte de présentation

### news.html — Actualités
- Articles ou news (à venir)

### materiel.html — Mon matériel
- Liste du matériel d'observation (télescopes, caméras, oculaires)

### album.html — Galerie photos
- Grille de photos astro (placeholder)

### meteo-astro.html — Météo
- Conditions météo pour l'observation astronomique

### biblio.html — Bibliographie
- Ressources, livres, liens utiles

### chat.html — Contact
- Formulaire de contact simple
- Ou lien vers la page "Message et Chat" existante

---

## 🖼️ Contenu à reprendre du site actuel

Le site Google Sites actuel (www.tofdan.be) contient des textes et photos à récupérer :
- Message d'accueil : "Nous sommes heureux de vous présenter notre tout nouveau site web..."
- Citation : "Cette passion est venue suite à une séance d'observation..."
- Signature : "Syl & Tof"
- Photos de la Lune et du Soleil
- Liens : Facebook, conditions d'utilisation

---

## 📦 Livrables

1. Fichiers HTML/CSS/JS statiques dans `/var/www/tofdan.be/`
2. Design responsive (mobile + desktop)
3. Navigation cohérente entre toutes les pages
4. Footer avec copyright et liens
5. Optimisation pour chargement rapide (fichiers statiques)

---

## 🛠️ Commandes pour déploiement

```bash
# Après développement, copier sur le serveur :
sudo cp -r * /var/www/tofdan.be/
sudo chown -R www-data:www-data /var/www/tofdan.be/
sudo systemctl reload nginx
```
*Document mis à jour le 04/07/2026 à 00:00 — Léo 🦁*

> 🤖 Dernier audit : 20 July 2026 à 09:14 (UTC+2)

