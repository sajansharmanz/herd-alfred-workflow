#!/bin/sh
# Packs info.plist, herd and the options form into herd.alfredworkflow.
set -e
cd "$(dirname "$0")"
plutil -lint info.plist >/dev/null
jq empty herd.alfredui/ui.json
chmod +x herd herd.alfredui/scripts/*
zip -q -r -o -X herd.alfredworkflow.tmp info.plist icon.png herd herd.alfredui
mv herd.alfredworkflow.tmp herd.alfredworkflow
echo "Built herd.alfredworkflow"
