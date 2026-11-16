"""GitHub profile art (2026-11-16, Shane's pick: a terminal look, no game or 80s theming). Writes banner.png
(1280x400, the README) and avatar.png (512, the profile picture).
Run: ~/.local/share/homelab-bot-venv/bin/python make_banner.py"""
from PIL import Image, ImageDraw, ImageFont

MONO = "/usr/share/fonts/adwaita-mono-fonts/AdwaitaMono-Regular.ttf"
MONO_B = "/usr/share/fonts/adwaita-mono-fonts/AdwaitaMono-Bold.ttf"
BG, WIN, BAR = (13, 17, 23), (22, 27, 34), (33, 38, 45)   # GitHub's dark greys, so it sits in the page
DIM, TXT, GREEN, BLUE = (125, 133, 144), (230, 237, 243), (63, 185, 80), (88, 166, 255)


def window(W, H, pad):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((pad, pad, W - pad, H - pad), 14, fill=WIN, outline=BAR, width=2)
    d.rounded_rectangle((pad, pad, W - pad, pad + 40), 14, fill=BAR)
    d.rectangle((pad, pad + 26, W - pad, pad + 40), fill=BAR)
    for i, c in enumerate(((255, 95, 86), (255, 189, 46), (39, 201, 63))):
        x = pad + 24 + i * 24
        d.ellipse((x - 7, pad + 13, x + 7, pad + 27), fill=c)
    return img, d


def line(d, x, y, parts, f):
    for s, c in parts:
        d.text((x, y), s, font=f, fill=c)
        x += f.getlength(s)
    return x


# banner
W, H = 1280, 400
img, d = window(W, H, 20)
f, fb = ImageFont.truetype(MONO, 30), ImageFont.truetype(MONO_B, 30)
d.text((W / 2, 40), "shane@fedora: ~", font=ImageFont.truetype(MONO, 18), fill=DIM, anchor="mm")
P = [("shane@fedora", GREEN), (":", TXT), ("~", BLUE), ("$ ", TXT)]
x0, y = 60, 90
line(d, x0, y, P + [("whoami", TXT)], f)
line(d, x0, y + 46, [("Shane Runham", TXT)], ImageFont.truetype(MONO_B, 44))
line(d, x0, y + 124, P + [("ls projects/", TXT)], f)
line(d, x0, y + 170, [("vice-home/    ", BLUE), ("homelab/    ", BLUE), ("vice-bot/    ", BLUE),
                      ("vice-radio/", BLUE)], fb)
x = line(d, x0, y + 232, P, f)
d.rectangle((x + 2, y + 236, x + 18, y + 266), fill=TXT)   # the cursor
img.save("banner.png")

# avatar: a terminal prompt and the initials
S = 512
a = Image.new("RGB", (S, S), WIN)
d = ImageDraw.Draw(a)
fa = ImageFont.truetype(MONO_B, 120)
d.text((S / 2 - 6, S / 2), ">_", font=fa, fill=GREEN, anchor="rm")
d.text((S / 2 + 6, S / 2), "SR", font=fa, fill=TXT, anchor="lm")
a.save("avatar.png")
print("banner.png avatar.png")
