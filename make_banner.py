"""GitHub profile banner (2026-11-16): the duotone look of the Discord server icon (make_badge.py), 1280x400."""
import os, sys
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps
BOT = os.path.expanduser("~/homelab/discord-bot")
sys.path.insert(0, BOT)
from make_badge import duotone, ADW
W, H = 1280, 400
INK, ACC = (24, 8, 30), (255, 200, 120)
g = Image.open(f"{BOT}/assets/scenes/rooftop.jpg").convert("L")
g = g.crop((0, 0, int(g.width * 0.46), g.height))  # the city, left of Jason and Lucia
s = W / g.width; g = g.resize((W, int(g.height * s)), Image.LANCZOS)
g = g.crop((0, int(g.height * 0.18), W, int(g.height * 0.18) + H))
img = duotone(ImageOps.autocontrast(g, cutoff=1), [(0, INK), (0.5, (230, 80, 120)), (1, (255, 226, 160))])
shade = Image.linear_gradient("L").rotate(90).resize((W, H))  # dark on the left, under the text
img.paste(Image.new("RGB", (W, H), INK), (0, 0), shade.point(lambda x: int(x * 0.8)))
def mask(text, f, x, y, stroke=0, track=0):
    m = Image.new("L", (W, H)); d = ImageDraw.Draw(m)
    for c in (text if track else [text]):
        d.text((x, y), c, font=f, fill=255, stroke_width=stroke, stroke_fill=255); x += f.getlength(c) + track
    return m
yt = ImageFont.truetype(f"{BOT}/assets/fonts/Yellowtail-Regular.ttf", 150)
word = mask("Shane Runham", yt, 70, 70, stroke=4)
img.paste(Image.new("RGB", (W, H), INK), (6, 10), word.filter(ImageFilter.GaussianBlur(10)))
img.paste((255, 255, 255), (0, 0), word)
cap = ImageFont.truetype(ADW, 30); cap.set_variation_by_name("Bold")
img.paste((255, 255, 255), (0, 0), mask("HOMELAB  ·  SMART TV  ·  DISCORD BOTS", cap, 120, 292, track=5))
ImageDraw.Draw(img).rounded_rectangle((70, 304, 104, 309), 3, fill=ACC)
img.save("banner.png"); print("banner.png")
