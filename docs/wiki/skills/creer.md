# ✨ Créer un nouveau bureau/skill

## 1. Définir le besoin

Quel domaine ? PRO ou PRIVÉ ? Quel workflow ?

## 2. Rédiger le prompt système

Un bon prompt de bureau BAVI LEO contient :

```yaml
---
name: mon-bureau
description: Description courte
---
```

```markdown
# Bureau X — Description

## Rôle
...

## Workflow
...

## Règles
...

## Format de sortie
...
```

## 3. Créer le skill Hermes

```bash
hermes skill create mon-bureau --file mon-bureau.md
```

## 4. Créer la page wiki

Ajouter une page dans `docs/wiki/pro/` ou `docs/wiki/prive/`

## 5. Mettre à jour la nav

Ajouter l'entrée dans `mkdocs.yml`

## 6. Déployer

```bash
git add . && git commit -m "Nouveau bureau : X" && git push
```
