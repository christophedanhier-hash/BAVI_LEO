---
date: 2026-07-07
bureau: bureau-michel
version: v1
modele: deepseek-v4-flash
tags: [fable, distillation, ollama, local-model, agentic, gpu, infrastructure]
statut: analyse
type: analyse
---

# 🔬 Analyse — Modèles Claude Fable Distillés sur LEO

> **Bureau :** Michel 🔧
> **Expert :** SysAdmin + Scripteur
> **Modèle :** DeepSeek Pro (sous-agent)
> **Date :** 07/07/2026

---

## 🎬 Contexte

Analyse de la vidéo [Claude Fable Distillation — Hermes Agent Local](https://youtu.be/P51ebCFwnss) et étude de faisabilité pour faire tourner un modèle local distillé des capacités agentiques de Claude Fable sur notre infrastructure LEO.

**Concept :** La communauté a capturé 2.3M de traces d'exécution de Claude Fable (sessions code, logs d'actions, appels d'outils, raisonnements) avant son retrait. Ces traces ont été utilisées pour distiller la **méthode de travail agentique** de Fable dans des modèles open-source plus petits (1.5B-27B). Ces modèles n'ont pas la connaissance de Fable mais son *style de raisonnement, planification, et utilisation d'outils*.

---

## 🔧 Infrastructure LEO

| Composant | Valeur |
|-----------|--------|
| GPU | NVIDIA RTX 3050, **8GB VRAM** (7.9 Go libre) |
| RAM | 22GB (16GB libre) |
| CPU | Intel i7-7700K (4C/8T) |
| Ollama | v0.30.8, Docker, GPU passthrough |
| NVIDIA | Driver 595.71, CUDA 13.2 |
| Stockage | 364 Go libre |
| Modèle actuel | qwen2.5:7b (Q4_K_M, 4.7 GB) |
| Benchmark | **43 tok/s** génération, **1120 tok/s** prompt eval |

---

## 📊 Modèles GGUF disponibles (distillés Fable 5)

| Modèle | Downloads | Taille GGUF | VRAM estimée | Tient sur RTX 3050 ? |
|--------|:---------:|:-----------:|:------------:|:--------------------:|
| **Qwen3.6-14B-A3B-FableVibes** (MoE) Q3_K_M | 55k | 6.77 GB | ~7.3 GB | ✅ Oui |
| **Qwable-9B-Claude-Fable-5** Q4_K_M | 39k | 5.63 GB | ~6.1 GB | ✅ Large marge |
| **gemma-4-12B-agentic** Q3_K_M | 384k | 6.09 GB | ~6.6 GB | ✅ Oui |
| **gemma-4-12B-coder-fable5** Q3_K_M | 675k ⭐ | 6.09 GB | ~6.6 GB | ✅ Oui |
| Qwen3.5-9B-Fable-5 Q4_K_M | 24k | 5.78 GB | ~6.3 GB | ✅ Confortable |
| CodeMate-Qwen-1.5B (trop petit) | 738 | 0.99 GB | ~1.5 GB | ✅ Trivial |
| Qwen3.6-27B-Fable (trop gros) | 18k | ~16 GB | >8 GB | ❌ Non |

---

## 🏆 Recommandation

### Top 1 : Qwen3.6-14B-A3B-FableVibes (MoE)

**Pourquoi :** Modèle Mixture-of-Experts. 14B paramètres totaux, mais seulement **~3B d'actifs par token**. Résultat : qualité d'un 14B avec la vitesse d'un 3B. Comparable à qwen2.5:7b en vitesse (35-50 tok/s estimés).

### Top 2 : Qwable-9B-Claude-Fable-5 Q4_K_M

Modèle 9B dense, tient avec large marge VRAM (6.1 GB). Moins risqué.

### Top 3 : gemma-4-12B-agentic Q3_K_M

Version spécifiquement distillée pour les *actions agentiques* (outils, planification). Très pertinent pour notre usage mais un peu plus serré en VRAM.

---

## 📝 Procédure d'installation

```bash
# Télécharger le GGUF
wget -O ~/Projets_Dev/Qwen3.6-14B-A3B-FableVibes-Q3_K_M.gguf \
  "https://huggingface.co/tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF/resolve/main/Qwen3.6-14B-A3B-FableVibes-Q3_K_M.gguf"

# Copier dans le volume Docker d'Ollama
docker cp ~/Projets_Dev/Qwen3.6-14B-A3B-FableVibes-Q3_K_M.gguf ollama:/root/.ollama/models/

# Importer dans Ollama
docker exec ollama ollama create fable-moe \
  --modelfile "FROM /root/.ollama/models/Qwen3.6-14B-A3B-FableVibes-Q3_K_M.gguf"

# Tester
docker exec ollama ollama run fable-moe "Hello, what can you do?"
```

---

## ⚠️ Risques

| Risque | Probabilité | Mitigation |
|--------|:-----------:|------------|
| VRAM overflow (ctx long) | Moyenne | Démarrer avec ctx 4K, augmenter graduellement |
| Latence excessive | Faible | MoE (3B actifs) résout le problème |
| Conflit avec qwen2.5:7b | Faible | Ne charger qu'un modèle à la fois |
| Corruption téléchargement | Faible | Vérifier SHA256 |

---

## 📎 Références

- Vidéo originale : https://youtu.be/P51ebCFwnss
- Rapports liés : `analyse-acces-credentials-20260630.md` (infra GPU du 30/06)
- Modèle recommandé : https://huggingface.co/tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF
- Backup : https://huggingface.co/empero-ai/Qwable-9B-Claude-Fable-5-GGUF

> 🤖 Dernier audit : 24/07/2026 à 11:46 (UTC+2)
