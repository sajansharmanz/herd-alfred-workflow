# Draws icons/<agent>-<status>.png: the agent's logo on a dark tile, or the herd sheep, with a status dot.
# Logos come from LobeHub's icon set (MIT), fetched at a pinned version. Needs rsvg-convert (brew install librsvg).
# Run: uv run --with pillow python make-icons.py
import io, os, subprocess, urllib.request
from PIL import Image, ImageDraw

LOBEHUB = "https://cdn.jsdelivr.net/npm/@lobehub/icons-static-svg@1.106.0/icons"
# Herdr's agent kinds, and the LobeHub icon for each. Kinds without an icon get the sheep.
AGENTS = {
    "claude": "claudecode", "codex": "codex", "gemini": "gemini", "cursor": "cursor", "devin": "devin",
    "agy": "antigravity", "cline": "cline", "mastracode": "mastra", "opencode": "opencode",
    "copilot": "githubcopilot", "kimi": "kimi", "kiro": "kiro", "amp": "amp", "grok": "grok",
    "hermes": "nousresearch", "kilo": "kilocode", "qodercli": "qoder", "qwen": "qwen", "pi": "pi",
}
STATUS = {"blocked": "#FF3B30", "working": "#FF9500", "done": "#34C759", "idle": "#8E8E93"}
S = 128
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "icons")
os.makedirs(out, exist_ok=True)


def logo_tile(name):
    svg = urllib.request.urlopen(f"{LOBEHUB}/{name}.svg").read().replace(b"currentColor", b"#FFFFFF")
    png = subprocess.run(["rsvg-convert", "-w", "72", "-h", "72"], input=svg, capture_output=True, check=True).stdout
    tile = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(tile).rounded_rectangle([6, 6, S - 14, S - 14], radius=24, fill="#2C2C2E")
    logo = Image.open(io.BytesIO(png)).convert("RGBA")
    tile.alpha_composite(logo, ((S - 8 - 72) // 2, (S - 8 - 72) // 2))
    return tile


def sheep_tile():
    sheep = Image.open(os.path.join(here, "icon.png")).convert("RGBA").resize((S - 8, S - 8), Image.LANCZOS)
    tile = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    tile.alpha_composite(sheep, (0, 0))
    return tile


def with_dot(tile, colour):
    big = tile.resize((S * 4, S * 4), Image.LANCZOS)  # draw the dot at 4x, then shrink, for smooth edges
    d = ImageDraw.Draw(big)
    cx = cy = 104 * 4
    d.ellipse([cx - 24 * 4, cy - 24 * 4, cx + 24 * 4, cy + 24 * 4], fill="#1C1C1E")  # dark ring, so the dot reads on any logo
    d.ellipse([cx - 18 * 4, cy - 18 * 4, cx + 18 * 4, cy + 18 * 4], fill=colour)
    return big.resize((S, S), Image.LANCZOS)


tiles = {"herd": sheep_tile()} | {kind: logo_tile(name) for kind, name in AGENTS.items()}
for kind, tile in tiles.items():
    for status, colour in STATUS.items():
        with_dot(tile, colour).save(os.path.join(out, f"{kind}-{status}.png"), optimize=True)
print(f"{len(tiles) * len(STATUS)} icons in {out}")
