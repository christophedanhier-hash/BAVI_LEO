---
date: 2026-06-19
bureau: bureau-michel
modele: deepseek-v4-pro
tags: [n8n, installation, plan]
statut: finalise
---

# n8n — Plan d'installation

**Date :** 19/06/2026
**Décision :** Option B — Conteneur Docker indépendant

---

## Commande unique

```bash
# Depuis l'hôte LEO (pas besoin d'être dans le conteneur Hermès)
cat /opt/data/n8n/run-n8n.sh | ssh tofdan@100.92.102.28 bash
```

Ou copier le script sur l'hôte et l'exécuter directement :

```bash
# Depuis le conteneur Hermès (via terminal tool)
cat /opt/data/n8n/run-n8n.sh > /tmp/run-n8n.sh
# ... à exécuter sur l'hôte
```

## Après installation

1. Ouvrir `http://100.92.102.28:5678`
2. Créer le compte owner (première connection)
3. Email : `leodanhieria@gmail.com`
4. Désactiver les features AI dans Settings → Usage & Plans

## Si login 401

```bash
# Depuis Penguin (Crostini)
ssh -L 5678:localhost:5678 tofdan@100.92.102.28
```
→ Ouvrir `http://localhost:5678` sur Penguin

## Mise à jour

```bash
cat /opt/data/n8n/update-n8n.sh | ssh tofdan@100.92.102.28 bash
```
