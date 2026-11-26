#!/bin/sh
# Packs the workflow into herd.alfredworkflow. Set VERSION=1.2.3 to stamp that version into the package.
# Runs on macOS and Linux (the release job), so it uses python3 for the plist rather than plutil.
set -e
cd "$(dirname "$0")"
jq empty herd.alfredui/ui.json herd-tell.alfredui/ui.json
chmod +x herd herd.alfredui/scripts/* herd-tell.alfredui/scripts/*
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT
cp -R info.plist icon.png icons herd herd.alfredui herd-tell.alfredui "$stage/"
cp -R docs/screenshots "$stage/images"  # the About text in Alfred shows these
python3 - "$stage/info.plist" "${VERSION:-}" <<'PY'
import plistlib, sys
path, version = sys.argv[1], sys.argv[2]
with open(path, "rb") as f:
    plist = plistlib.load(f)
if version:
    plist["version"] = version
with open(path, "wb") as f:
    plistlib.dump(plist, f)
PY
out=$PWD/herd.alfredworkflow
rm -f "$out"
(cd "$stage" && zip -q -r -X "$out" info.plist icon.png icons images herd herd.alfredui herd-tell.alfredui -x '*.DS_Store')
echo "Built herd.alfredworkflow${VERSION:+ $VERSION}"
