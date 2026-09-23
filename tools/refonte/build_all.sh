#!/bin/sh
# Régénère toutes les pages du site à partir des données de tools/refonte/.
set -e
cd "$(dirname "$0")"
python3 build_pages.py
python3 build_modules.py
python3 build_misc.py
python3 build_redirects.py
