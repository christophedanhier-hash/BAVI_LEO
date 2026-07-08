#!/bin/bash
# Rebuild du wiki BAVI local
# Exécuté toutes les heures (cron) + après édition inline
set -e
cd /opt/data/BAVI_LEO

# Build avec la config locale
.venv/bin/mkdocs build --config-file mkdocs-local.yml --site-dir /opt/data/BAVI_LEO/site 2>&1 | tail -1

echo "$(date '+%Y-%m-%d %H:%M:%S') Wiki BAVI local rebuilt"
