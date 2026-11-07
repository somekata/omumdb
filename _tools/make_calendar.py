#!/usr/bin/env python3
"""月間カレンダー画像（縦:横 = 1:4、2400x600）を生成する。

上段に11体のバイキンズ®（_tools/chara/ の透過PNG）、下段に1か月分を横一列に並べた日付の帯。
キャラクターを入れ替えるときは CHARAS のファイル名を書き換える。

使い方: python3 make_calendar.py [出力PNG]
"""
import pathlib
import sys
import calendar as pycal

from PIL import Image, ImageChops, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).resolve().parent
CHARA_DIR = HERE / "chara"

SS = 2                          # スーパーサンプリング倍率
W, H = 2400, 600                # 縦:横 = 1:4
YEAR, MONTH = 2026, 11
OUT = sys.argv[1] if len(sys.argv) > 1 else "calendar-2026-11.png"

TITLE = "十一人の菌侍"
SEAL = "霜月"                   # 11月の和名
SUB = "細菌学"
CHARAS = ["chara9.png", "chara13.png", "chara21.png", "chara29.png", "chara4.png", "chara8.png",
          "chara14.png", "chara15.png", "chara10.png", "chara12.png", "chara18.png"]
HOLIDAYS = {3: ["文化の日"], 23: ["勤労感謝", "の日"]}
NOTES = {7: ["立冬", "HP開設"]}
WAAW = range(18, 25)            # 世界AMR啓発週間（11/18–24）

SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-%s.ttc"
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-%s.ttc"

INK = (28, 24, 22)
PAPER = (244, 236, 218)
RED = (178, 40, 36)
BLUE = (40, 80, 150)
IRON = (38, 52, 84)
WHITE = (255, 255, 255)


def font(kind, weight, size):
    return ImageFont.truetype((SANS if kind == "sans" else SERIF) % weight, int(size * SS), index=0)


def P(v):
    return int(round(v * SS))


IMG = Image.new("RGBA", (W * SS, H * SS), PAPER + (255,))
D = None


def redraw():
    global D
    D = ImageDraw.Draw(IMG)


def overlay(fn):
    ov = Image.new("RGBA", IMG.size, (0, 0, 0, 0))
    fn(ImageDraw.Draw(ov))
    IMG.alpha_composite(ov)
    redraw()


def rrect(x0, y0, x1, y1, r, fill, outline=INK, w=3):
    D.rounded_rectangle([P(x0), P(y0), P(x1), P(y1)], radius=P(r), fill=fill,
                        outline=outline, width=P(w) if outline else 0)


def line(pts, fill, w):
    D.line([(P(x), P(y)) for x, y in pts], fill=fill, width=P(w))


def text(x, y, s, f, fill, anchor="mm"):
    D.text((P(x), P(y)), s, font=f, fill=fill, anchor=anchor)


def background():
    global IMG
    rgb = IMG.convert("RGB")
    noise = Image.effect_noise((W * SS // 2, H * SS // 2), 22).resize(IMG.size)
    n = noise.point(lambda v: 232 + int(v / 255 * 23))
    IMG = ImageChops.multiply(rgb, Image.merge("RGB", (n, n, n))).convert("RGBA")
    redraw()

    def sun(dd):
        dd.ellipse([P(-170), P(-190), P(520), P(500)], fill=RED + (30,))
    overlay(sun)
    D.rectangle([P(14), P(14), P(W - 14), P(H - 14)], outline=INK, width=P(5))
    D.rectangle([P(25), P(25), P(W - 25), P(H - 25)], outline=INK, width=P(2))


def title_block():
    # 縦書きタイトル
    for i, ch in enumerate(TITLE):
        ff = font("serif", "Black", 40 if ch == "の" else 52)
        text(96, 66 + i * 53 + (6 if ch == "の" else 0), ch, ff, INK)
    # 朱印
    rrect(152, 44, 220, 188, 8, RED, RED, 1)
    rrect(157, 49, 215, 183, 5, None, WHITE, 2)
    for i, ch in enumerate(SEAL):
        text(186, 90 + i * 62, ch, font("serif", "Black", 50), WHITE)
    for i, ch in enumerate(SUB):
        text(186, 226 + i * 34, ch, font("serif", "Bold", 28), INK)
    text(W - 50, 44, "© 2026 大阪公立大学大学院医学研究科 細菌学", font("sans", "Medium", 16), (96, 86, 74), anchor="rm")


def characters():
    x0, x1, base = 250, W - 50, 362
    slot = (x1 - x0) / len(CHARAS)
    # 足元の地面（筆の線）
    D.rectangle([P(60), P(base + 1), P(W - 60), P(base + 5)], fill=INK)
    for i, name in enumerate(CHARAS):
        im = Image.open(CHARA_DIR / name).convert("RGBA")
        im = im.crop(im.getchannel("A").getbbox())
        scale = min((slot * 1.38) / im.width, 300 / im.height)
        w, h = int(im.width * scale), int(im.height * scale)
        cx = x0 + slot * (i + 0.5)

        def shadow(dd, cx=cx, w=w):
            dd.ellipse([P(cx - w * 0.45), P(base - 6), P(cx + w * 0.45), P(base + 10)], fill=(0, 0, 0, 50))
        overlay(shadow)
        res = im.resize((w * SS, h * SS), Image.LANCZOS)
        IMG.alpha_composite(res, (P(cx - w / 2), P(base - h + 2)))
    redraw()


def strip():
    x0, x1 = 60, W - 60
    y0, y1 = 374, 572
    n = pycal.monthrange(YEAR, MONTH)[1]
    cw = (x1 - x0) / n
    head_h, num_h = 34, 64
    notes_y = y0 + head_h + num_h

    def wd(d):                      # 0=日 ... 6=土
        return (pycal.weekday(YEAR, MONTH, d) + 1) % 7

    def tint(dd):
        dd.rounded_rectangle([P(x0), P(y0), P(x1), P(y1)], radius=P(10), fill=(255, 252, 244, 200))
        for d in range(1, n + 1):
            cx0 = x0 + (d - 1) * cw
            if wd(d) == 0 or d in HOLIDAYS:
                dd.rectangle([P(cx0), P(y0 + head_h), P(cx0 + cw), P(y1)], fill=(236, 170, 160, 95))
            elif wd(d) == 6:
                dd.rectangle([P(cx0), P(y0 + head_h), P(cx0 + cw), P(y1)], fill=(170, 195, 240, 95))
    overlay(tint)

    # 曜日の帯
    D.rounded_rectangle([P(x0), P(y0), P(x1), P(y0 + head_h)], radius=P(10), fill=IRON)
    D.rectangle([P(x0), P(y0 + 14), P(x1), P(y0 + head_h)], fill=IRON)
    fw = font("sans", "Bold", 22)
    fn = font("serif", "Black", 38)
    fnote = font("sans", "Bold", 15)
    for d in range(1, n + 1):
        cx0 = x0 + (d - 1) * cw
        cxm = cx0 + cw / 2
        k = wd(d)
        col = (255, 176, 166) if (k == 0 or d in HOLIDAYS) else (176, 204, 255) if k == 6 else WHITE
        text(cxm, y0 + head_h / 2 + 1, "日月火水木金土"[k], fw, col)
        ncol = RED if (k == 0 or d in HOLIDAYS) else BLUE if k == 6 else INK
        text(cxm, y0 + head_h + num_h / 2 + 2, str(d), fn, ncol)
        labels = HOLIDAYS.get(d, []) + NOTES.get(d, [])
        for j, lab in enumerate(labels):
            text(cxm, notes_y + 12 + j * 19, lab, fnote, RED if d in HOLIDAYS else INK)
    # 罫線
    for d in range(1, n):
        x = x0 + d * cw
        line([(x, y0 + head_h), (x, y1)], (150, 140, 125), 1.5)
    # 世界AMR啓発週間の帯
    a, b = min(WAAW), max(WAAW)
    bx0, bx1 = x0 + (a - 1) * cw + 3, x0 + b * cw - 3
    rrect(bx0, y1 - 36, bx1, y1 - 8, 8, RED, INK, 2)
    text((bx0 + bx1) / 2, y1 - 22, "世界AMR啓発週間 11/18–24", font("sans", "Bold", 18), WHITE)
    D.rounded_rectangle([P(x0), P(y0), P(x1), P(y1)], radius=P(10), outline=INK, width=P(4))


def main():
    redraw()
    background()
    title_block()
    characters()
    strip()
    out = IMG.convert("RGB").resize((W, H), Image.LANCZOS)
    out.save(OUT, optimize=True)
    print("saved", OUT, out.size)


if __name__ == "__main__":
    main()
