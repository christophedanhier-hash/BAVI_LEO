---
bureau: michel
date: 2026-06-28
version: v1
tags: [penguin, crostini, audit, infra, systeme]
status: finalisé
title: "Audit Penguin — Debian 13, 6.3GB RAM"
---

# Audit Penguin — 28/06/2026

## Système
| Élément | Valeur |
|---|---|
| **OS** | Debian GNU/Linux 13 (trixie) |
| **Kernel** | 6.6.119-09251-gf81e51484dec |
| **CPU** | 12th Gen Intel Core i3-1215U |
| **RAM** | 6.3 GiB total — 4.8 GiB used (77%), 1.5 GiB available |
| **Disque /** | 40 GB — 6.5 GB used (17%) |
| **Disque cros** | 75 MB — 74 MB used (100%) → NORMAL |
| **Swap** | 0 (pas de swap) |
| **Uptime** | 12h59 (depuis 27/06 18:08) |
| **Load** | 0.13 |

## Réseau & Accès
| Port | Service |
|---|---|
| 22 | SSH (ouvert) |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 631 | CUPS |
| 3389 | RDP |
| 5901 | VNC |
| 7681 | TTYD |
| 8123 | ? |
| 8765 | Panel Dashboard |
| 9119 | Hermes Dashboard |
| 11434 | Ollama |
| 20241 | ? |
| **IP Tailscale** | 100.113.110.40 |
| **Hostname TS** | penguin |

## Services Crostini
| Service | Statut |
|---|---|
| **cros-garcon** | ✅ Active (user service) |
| **vshd** | ✅ Active (system) |
| **SSH** | ✅ Enabled |

## Outils Développement
| Outil | Version |
|---|---|
| Git | 2.47.3 |
| Python | 3.13.5 |
| Node | 20.20.2 |
| VS Code | Installé (actif) |
| Kilo Code | ❌ Non installé |
| Docker | ❌ Non installé |

## Clés SSH Autorisées (4)
- `hermes@43c360aea788`
- `hermes_leo`
- `yoga`
- 1 clé sans commentaire

## Erreurs Système
- `vshd: Failed to read from stdio` × 3 → cosmétique, normal

## Consommation Mémoire Top
1. VS Code NodeService: 640 MB (9.9%)
2. VS Code renderer: 377 MB (5.7%)
3. Kilo Code: 354 MB (5.4%)
4. VS Code renderer: 256 MB (3.9%)
5. VS Code main: 210 MB (3.2%)

**Constats:**
- VS Code + Kilo Code = ~2 GB RAM à eux seuls
- RAM disponible faible (1.5 GB), risque de saturation
- Si Terminal Crostini ne s'ouvre plus → `vmc stop termina` dans Crosh
*Document mis à jour le 04/07/2026 à 00:00 — Léo 🦁*

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)

