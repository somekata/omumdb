#!/usr/bin/env python3
"""大阪公立大学大学院医学研究科 細菌学 ホームページ 生成スクリプト

使い方（サイトのルートで実行）:
    python3 _tools/build.py

下の「データ」部分（INFO / CALENDARS / MEMBERS）を編集して再実行すると、
日本語・英語の全ページに反映される。生成された *.html を直接編集すると、
次回の実行時に上書きされるので注意。
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://somekata.github.io/omumdb/"
OFFICIAL = "https://www.omu.ac.jp/med/bacteriology/"
LAUNCH = "2026-11-07"

SITE = {
    "ja": {"org": "大阪公立大学大学院医学研究科", "dept": "細菌学",
           "full": "大阪公立大学大学院医学研究科 細菌学"},
    "en": {"org": "Osaka Metropolitan University Graduate School of Medicine",
           "dept": "Department of Bacteriology",
           "full": "Department of Bacteriology, Osaka Metropolitan University Graduate School of Medicine"},
}

AI_NOTE = {
    "ja": "本テキストは AI（Claude, Anthropic）を用いて作成されました。内容には誤りが含まれる可能性があります。"
          "医療上の判断には必ず公式の教科書・文献・専門家の指導を参照してください。"
          "二次利用・再配布は自己責任のもとで可能です。その際、本注記の保持を推奨します。",
    "en": "This text was created with the assistance of AI (Claude, Anthropic). It may contain errors. "
          "For any medical decision, always consult official textbooks, the literature, and qualified experts. "
          "Secondary use and redistribution are permitted at your own risk; we recommend retaining this notice.",
}

NAV = {
    "ja": [("info", "お知らせ"), ("about", "教室紹介"), ("members", "メンバー"), ("research", "研究"),
           ("education", "教育"), ("outreach", "アウトリーチ"), ("calendar", "カレンダー"),
           ("publications", "業績"), ("access", "アクセス"), ("links", "リンク")],
    "en": [("info", "News"), ("about", "About"), ("members", "Members"), ("research", "Research"),
           ("education", "Education"), ("outreach", "Outreach"), ("calendar", "Calendar"),
           ("publications", "Publications"), ("access", "Access"), ("links", "Links")],
}
PAGES = ["index"] + [s for s, _ in NAV["ja"]]
MONTHS_EN = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def sn(name):
    """学名はイタリック（血清型は立体のまま別途記述する）。"""
    return f'<i class="sn">{name}</i>'


# ======================================================================
# データ（ここを編集して再実行）
# ======================================================================
INFO = [
    dict(date="2026-11-07", kind="notice", tag_ja="お知らせ", tag_en="Notice",
         title_ja="本ホームページを開設しました",
         title_en="This website has been launched",
         body_ja=f'大阪公立大学のサーバー障害に伴い、公式のURL（<a href="{OFFICIAL}">{OFFICIAL}</a>）とは別に、'
                 "本ホームページを作成しました。本ホームページは今後も継続して運用します。",
         body_en=f'Because of a server outage at Osaka Metropolitan University, we have created this website separately '
                 f'from the official URL (<a href="{OFFICIAL}">{OFFICIAL}</a>). '
                 "We will continue to operate this website going forward."),
    dict(date="2026-11-07", kind="calendar", tag_ja="カレンダー", tag_en="Calendar",
         title_ja="11月のカレンダー「十一人の菌侍」を掲載しました",
         title_en="The November calendar, “Eleven Microbe Samurai,” is now online",
         body_ja="毎月、バイキンズ®のカレンダーを掲載しています。11月のテーマは「十一人の菌侍」です。"
                 "<a href=\"calendar.html\">カレンダーのページ</a>からご覧いただけます。",
         body_en="We publish a Baikinz® calendar every month. The theme for November is “Eleven Microbe Samurai.” "
                 "See the <a href=\"calendar.html\">Calendar page</a>."),
]

# 新しい月は末尾に追加する（トップには最後の1件が出る）
CALENDARS = [
    dict(ym="2026-11", file="assets/calendar/2026-11.png",
         label_ja="2026年11月「十一人の菌侍」", label_en="November 2026: Eleven Microbe Samurai",
         alt_ja="2026年11月のカレンダー「十一人の菌侍」。バイキンズ®のキャラクター11体が並び、下に1か月分の日付が横一列に並ぶ。",
         alt_en="November 2026 calendar, “Eleven Microbe Samurai,” with eleven Baikinz® characters above a one-row strip of the month’s dates."),
]

MEMBERS = {
    "ja": [
        ("大阪公立大学大学院医学研究科 細菌学", [
            dict(badge="教授", name="金子幸弘", en="Yukihiro Kaneko", role="教授", lead=True),
            dict(badge="准教授", name="仁木満美子", en="Mamiko Niki", role="准教授"),
            dict(badge="講師", name="老沼研一", en="Ken-ichi Oinuma", role="講師"),
        ]),
        ("刀根山結核研究所", [
            dict(badge="准教授", name="坪内泰志", en="Taishi Tsubouchi", role="准教授（刀根山結核研究所）"),
        ]),
        ("大学院生", [
            dict(badge="修士1", name="奥田諒", en="Ryo Okuda", role="修士課程 1年"),
            dict(badge="博士1", name="Naijimiding Nijiati", en="", role="博士課程 1年"),
            dict(badge="博士1", name="ウチキ", en="", role="博士課程 1年"),
        ]),
    ],
    "en": [
        ("Department of Bacteriology, Osaka Metropolitan University Graduate School of Medicine", [
            dict(badge="Prof.", name="Yukihiro Kaneko", en="", role="Professor", lead=True),
            dict(badge="Assoc.", name="Mamiko Niki", en="", role="Associate Professor"),
            dict(badge="Lect.", name="Ken-ichi Oinuma", en="", role="Lecturer"),
        ]),
        ("Toneyama Institute for Tuberculosis Research", [
            dict(badge="Assoc.", name="Taishi Tsubouchi", en="", role="Associate Professor, Toneyama Institute for Tuberculosis Research"),
        ]),
        ("Graduate students", [
            dict(badge="M1", name="Ryo Okuda", en="", role="Master’s Program, 1st year"),
            dict(badge="D1", name="Naijimiding Nijiati", en="", role="Doctoral Program, 1st year"),
            dict(badge="D1", name="Uchiki", en="", role="Doctoral Program, 1st year"),
        ]),
    ],
}

ADDRESS_JA = "〒545-8585 大阪市阿倍野区旭町1丁目4番3号 大阪公立大学 大学院医学研究科・医学部"
ADDRESS_EN = "1-4-3 Asahi-machi, Abeno-ku, Osaka 545-8585, Japan — Osaka Metropolitan University, Graduate School of Medicine"
MAP_URL = "https://www.google.com/maps/search/?api=1&query=%E5%A4%A7%E9%98%AA%E5%B8%82%E9%98%BF%E5%80%8D%E9%87%8E%E5%8C%BA%E6%97%AD%E7%94%BA1-4-3"


def pubmed(q):
    from urllib.parse import quote_plus
    return "https://pubmed.ncbi.nlm.nih.gov/?term=" + quote_plus(q)


# ======================================================================
# 共通部品
# ======================================================================
def fmt_date(lang, iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{y}年{m}月{d}日" if lang == "ja" else f"{MONTHS_EN[m - 1]} {d}, {y}"


def asset(lang, path):
    return ("" if lang == "ja" else "../") + path


def info_list(lang, limit=None):
    items = sorted(INFO, key=lambda x: x["date"], reverse=True)
    if limit:
        items = items[:limit]
    rows = []
    for it in items:
        rows.append(
            f'<li><div class="info-meta"><time datetime="{it["date"]}">{fmt_date(lang, it["date"])}</time>'
            f'<span class="tag tag-{it["kind"]}">{it["tag_" + lang]}</span></div>'
            f'<div class="info-body"><h3>{it["title_" + lang]}</h3><p>{it["body_" + lang]}</p></div></li>')
    return '<ul class="info-list">' + "".join(rows) + "</ul>"


def member_cards(lang):
    out = []
    for group, people in MEMBERS[lang]:
        out.append(f'<h2 class="sec">{group}</h2><div class="members">')
        for p in people:
            en = f'<span class="en">{p["en"]}</span>' if p["en"] else ""
            out.append(
                f'<article class="member{" featured" if p.get("lead") else ""}"><div class="badge">{p["badge"]}</div>'
                f'<div><h3>{p["name"]}{en}</h3><p class="role">{p["role"]}</p>{extra_member(lang, p)}</div></article>')
        out.append("</div>")
    return "".join(out)


def extra_member(lang, p):
    if not p.get("lead"):
        return ""
    if lang == "ja":
        return ('<ul class="mini"><li>研究分野：薬剤耐性（AMR）、臨床微生物学、バイオセーフティ、感染症教育</li>'
                "<li>大阪公立大学 BSL委員会 副委員長</li>"
                "<li>関連組織：OIRCID、RCIDS、刀根山結核研究所</li></ul>")
    return ('<ul class="mini"><li>Fields: antimicrobial resistance (AMR), clinical microbiology, biosafety, infectious disease education</li>'
            "<li>Vice-chairperson, BSL Committee, Osaka Metropolitan University</li>"
            "<li>Related organizations: OIRCID, RCIDS, Toneyama Institute for Tuberculosis Research</li></ul>")


LOGO = ('<svg viewBox="0 0 48 48" aria-hidden="true" focusable="false"><circle cx="24" cy="24" r="23" fill="#b22824"/>'
        '<rect x="15" y="9" width="18" height="31" rx="9" fill="#fff"/><circle cx="20" cy="22" r="2.1" fill="#1e2d50"/>'
        '<circle cx="28" cy="22" r="2.1" fill="#1e2d50"/><path d="M20 28q4 3 8 0" stroke="#1e2d50" stroke-width="1.8" '
        'fill="none" stroke-linecap="round"/></svg>')


def render(lang, slug, title, desc, body):
    a = lambda p: asset(lang, p)
    site = SITE[lang]
    other = "en" if lang == "ja" else "ja"
    ja_url = f"{BASE}{slug}.html" if slug != "index" else BASE
    en_url = f"{BASE}en/{slug}.html"
    sw_ja = ("index.html" if lang == "ja" else f"../{slug}.html")
    sw_en = (f"en/{slug}.html" if lang == "ja" else f"{slug}.html")
    full_title = site["full"] if slug == "index" else f"{title} | {site['full']}"
    canon = (ja_url if lang == "ja" else en_url)
    cur = ' aria-current="page"'
    nav = "".join(
        '<li><a href="%s.html"%s>%s</a></li>' % (s, cur if s == slug else "", t) for s, t in NAV[lang])
    labels = {"ja": ("本文へ移動", "メニュー", "ホーム", "公式サイト", "開設"),
              "en": ("Skip to content", "Menu", "Home", "Official site", "Launched")}[lang]
    org_label = SITE[lang]["full"]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="ja" href="{ja_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}{CALENDARS[-1]['file']}">
<meta name="theme-color" content="#1e2d50">
<link rel="icon" href="{a('assets/favicon.svg')}" type="image/svg+xml">
<link rel="stylesheet" href="{a('assets/style.css')}">
</head>
<body class="page-{slug}">
<a class="skip" href="#main">{labels[0]}</a>
<header class="site-header">
  <div class="wrap head-top">
    <a class="brand" href="index.html" aria-label="{labels[2]}：{org_label}">{LOGO}
      <span><span class="org">{site['org']}</span><span class="dept">{site['dept']}</span></span></a>
    <div class="lang" aria-label="Language"><a href="{sw_ja}" lang="ja"{' aria-current="true"' if lang == 'ja' else ''}>日本語</a><a href="{sw_en}" lang="en"{' aria-current="true"' if lang == 'en' else ''}>English</a></div>
  </div>
  <nav class="nav" aria-label="Main">
    <div class="wrap">
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">{labels[1]}</button>
      <ul id="site-nav">{nav}</ul>
    </div>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <p class="foot-links"><a href="index.html">{org_label}</a> ／ <a href="{OFFICIAL}">{labels[3]}</a></p>
    <p class="ai-note">{AI_NOTE[lang]}</p>
    <p class="copy">© 2026 {org_label} ／ {labels[4]}: {fmt_date(lang, LAUNCH)}</p>
  </div>
</footer>
<script>
(function(){{var b=document.querySelector('.nav-toggle'),n=document.getElementById('site-nav');
if(!b||!n)return;document.documentElement.classList.add('js');
b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');}});}})();
</script>
</body>
</html>
"""


def page_head(lang, h1, lead=""):
    home = "ホーム" if lang == "ja" else "Home"
    return (f'<section class="page-head"><div class="wrap"><p class="crumb"><a href="index.html">{home}</a> ／ {h1}</p>'
            f'<h1>{h1}</h1>{"<p class=lead>" + lead + "</p>" if lead else ""}</div></section>')


def wrap(inner):
    return f'<section class="section"><div class="wrap prose">{inner}</div></section>'


# ======================================================================
# 日本語ページ
# ======================================================================
def pages_ja():
    cal = CALENDARS[-1]
    P = {}

    P["index"] = ("", "大阪公立大学大学院医学研究科 細菌学のホームページ。薬剤耐性（AMR）をはじめとする細菌・真菌感染症の研究と、細菌学を楽しく学べる教育・啓発に取り組んでいます。", f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <h1 class="hero-title"><span class="org">大阪公立大学大学院医学研究科</span><span class="dept">細菌学</span></h1>
    <p class="catch">細菌を知る。細菌を楽しむ。</p>
    <p class="lead">薬剤耐性（AMR）をはじめとする細菌・真菌感染症の研究と、細菌学を楽しく学べる教育・啓発に取り組んでいます。</p>
    <p class="cta"><a class="btn" href="research.html">研究内容を見る</a><a class="btn ghost" href="members.html">メンバー</a><a class="btn ghost" href="about.html">教室紹介</a></p>
  </div>
  <a class="hero-cal" href="calendar.html"><img src="{cal['file']}" width="2400" height="600" alt="{cal['alt_ja']}"><span>今月のカレンダー：{cal['label_ja']}</span></a>
</div></section>
<section class="section"><div class="wrap">
  <h2 class="sec">お知らせ</h2>
  {info_list('ja', 4)}
  <p class="more"><a href="info.html">お知らせ一覧へ</a></p>
</div></section>
<section class="section alt"><div class="wrap">
  <h2 class="sec">研究テーマ</h2>
  <div class="cards">
    <a class="card" href="research.html#amr"><h3>薬剤耐性（AMR）</h3><p>{sn('Pseudomonas aeruginosa')}、{sn('Acinetobacter baumannii')} など、治療に難渋する耐性菌の研究。</p></a>
    <a class="card" href="research.html#fungi"><h3>真菌と抗真菌薬</h3><p>{sn('Candida')} 属による感染症の解析と、深海放線菌由来の新規抗真菌化合物の探索。</p></a>
    <a class="card" href="research.html#education"><h3>臨床細菌学と教育</h3><p>ゲーミフィケーションを活用した、細菌学・感染症教育の手法の開発。</p></a>
    <a class="card" href="research.html#biosafety"><h3>バイオセーフティと連携</h3><p>BSL委員会の活動、OIRCIDなど感染症対策の連携の枠組み。</p></a>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <h2 class="sec">教育・アウトリーチ</h2>
  <div class="cards">
    <a class="card" href="education.html#iloha"><h3>ILOHA</h3><p>2014年から続く感染症の勉強会。開催は430回を超えました。</p></a>
    <a class="card" href="education.html#bactplatform"><h3>bactPlatform</h3><p>微生物学・感染症を学べるHTML教材ツールのライブラリ。</p></a>
    <a class="card" href="outreach.html"><h3>バイキンズ®・FunFection</h3><p>「楽しさは感染する」。ゲームとキャラクターで細菌学を身近に。</p></a>
    <a class="card" href="calendar.html"><h3>バイキンズ®カレンダー</h3><p>毎月更新の月間カレンダー。{cal['label_ja']}。</p></a>
  </div>
</div></section>
""")

    P["info"] = ("お知らせ", "大阪公立大学大学院医学研究科 細菌学からのお知らせ。", page_head("ja", "お知らせ") +
                 wrap(info_list("ja")))

    P["about"] = ("教室紹介", "大阪公立大学大学院医学研究科 細菌学の紹介。理念、概要、関連組織。", page_head("ja", "教室紹介") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec">教室について</h2>
  <p>大阪公立大学大学院医学研究科 細菌学は、細菌・真菌感染症と薬剤耐性（AMR）の研究、臨床微生物学の教育、そして細菌学・感染症を身近にするための啓発活動に取り組んでいます。</p>
  <h2 class="sec">めざすもの：細菌楽人口を増やす</h2>
  <p>細菌学を「むずかしい」から「おもしろい」へ。ゲームや教材を通して、細菌を楽しむ人たち（細菌楽人口）を増やすことを、教育・啓発の軸にしています。</p>
  <h2 class="sec">概要</h2>
  <dl class="dl">
    <dt>名称</dt><dd>大阪公立大学大学院医学研究科 細菌学</dd>
    <dt>教授</dt><dd>金子幸弘</dd>
    <dt>関連組織</dt><dd>OIRCID（大阪国際感染症研究センター）／RCIDS／刀根山結核研究所</dd>
    <dt>公式サイト</dt><dd><a href="{OFFICIAL}">{OFFICIAL}</a></dd>
    <dt>本ホームページ</dt><dd>2026年11月7日開設（サーバー障害により、公式のURLとは別に作成）</dd>
  </dl>
</div></section>""")

    P["members"] = ("メンバー", "大阪公立大学大学院医学研究科 細菌学のメンバー。", page_head("ja", "メンバー") +
                    f'<section class="section"><div class="wrap">{member_cards("ja")}</div></section>')

    P["research"] = ("研究", "薬剤耐性（AMR）、真菌感染症、深海放線菌由来の新規抗真菌化合物、臨床細菌学教育、バイオセーフティなど、細菌学教室の研究内容。", page_head("ja", "研究") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec" id="amr">薬剤耐性（AMR）と耐性菌</h2>
  <p>薬剤耐性（AMR）は、世界的に深刻な課題です。当教室では、{sn('Pseudomonas aeruginosa')}（緑膿菌）や {sn('Acinetobacter baumannii')} など、治療に難渋する多剤耐性グラム陰性桿菌を中心に、耐性の実態と感染制御を研究しています。</p>
  <ul>
    <li>治療困難な耐性（DTR：difficult-to-treat resistance）を示す緑膿菌の解析</li>
    <li>カルバペネム耐性 {sn('A. baumannii')}（CRAB）に対する新規抗菌薬の有効性評価（メタ解析）</li>
    <li>多剤耐性グラム陰性桿菌の感染制御</li>
  </ul>
  <h2 class="sec" id="fungi">真菌（{sn('Candida')} 属）</h2>
  <p>{sn('Candida')} 属による侵襲性感染症を対象に、臨床データの統合解析を進めています。{sn('Candida auris')} とそれ以外の {sn('Candida')} 属によるカンジダ血症の死亡率を比較するシステマティックレビュー／メタ解析などに取り組んでいます。</p>
  <h2 class="sec" id="deepsea">深海放線菌由来の新規抗真菌化合物</h2>
  <p>深海から分離した放線菌を、新しい抗真菌化合物の探索源として研究しています。ナノポアシーケンサー（MinION）によるゲノム解析、HPLC/MSによる化合物解析、RNA-seq、マウスを用いた評価などを組み合わせて、候補化合物の探索と評価を進めます。</p>
  <h2 class="sec" id="education">臨床細菌学と教育研究</h2>
  <p>臨床微生物学の知識を、現場で使える形で伝えるための教育手法を研究しています。ゲーミフィケーションを取り入れた教材として、WHOのAWaRe分類（抗菌薬の分類）を題材にしたゲームなどを開発しています。詳しくは <a href="education.html">教育</a> と <a href="outreach.html">アウトリーチ</a> をご覧ください。</p>
  <h2 class="sec" id="biosafety">バイオセーフティ</h2>
  <p>大阪公立大学のBSL（バイオセーフティレベル）委員会の活動を通じて、病原体を安全に扱うための体制づくりに関わっています。</p>
  <h2 class="sec" id="collab">感染症対策の連携（OIRCID）</h2>
  <p>OIRCID（大阪国際感染症研究センター）は、大阪府・大阪市・大阪公立大学・大阪大学・大阪健康安全基盤研究所による5者連携の枠組みです。当教室は、その運営（ガバナンス）の設計にも関わっています。</p>
</div></section>""")

    P["education"] = ("教育", "細菌学教室の教育活動。ILOHA、bactPlatformなど。", page_head("ja", "教育") + """
<section class="section"><div class="wrap prose">
  <h2 class="sec">教育の考え方</h2>
  <p>細菌学・感染症の教育では、「知る」だけでなく「楽しむ」ことを大切にしています。学部・大学院での教育に加えて、ゲーミフィケーションや自作の教材ツールを通じて、細菌楽人口を増やすことをめざしています。</p>
  <h2 class="sec" id="iloha">ILOHA</h2>
  <p>ILOHA（Infection Lecture at OMU Hospital &amp; Affiliates）は、2014年から続く感染症の勉強会です。開催は430回を超えています。開催のご案内にはLINE公式アカウントを使っています。</p>
  <h2 class="sec" id="bactplatform">bactPlatform</h2>
  <p>微生物学・感染症を学べるHTML教材ツールのライブラリです。GitHub Pagesで公開しています。</p>
  <ul>
    <li>微生物学の実習シミュレーター</li>
    <li>免疫学・寄生虫学のシリーズ</li>
    <li>医療面接（病歴聴取）のシミュレーター</li>
    <li>感染症のチャートビューア</li>
  </ul>
</div></section>""")

    P["outreach"] = ("アウトリーチ", "バイキンズ®、FunFection、薬剤耐性（AMR）の啓発など、細菌学教室のアウトリーチ活動。", page_head("ja", "アウトリーチ") + """
<section class="section"><div class="wrap prose">
  <h2 class="sec">細菌楽人口を増やす</h2>
  <p>細菌や感染症を、もっと身近で楽しいものにするために、キャラクターやゲームを使った啓発を続けています。</p>
  <h2 class="sec">バイキンズ®</h2>
  <p>バイキンズ®は、微生物をモチーフにしたオリジナルのキャラクターです（登録商標）。毎月の<a href="calendar.html">カレンダー</a>にも登場します。</p>
  <h2 class="sec">FunFection</h2>
  <p>FunFectionは、教育ゲームと教材のブランドです。キャッチコピーは「楽しさは感染する」。バイキンズ®をモチーフに、次のようなゲームを開発しています。</p>
  <ul>
    <li><strong>バイキンズ討滅戦記：Busters Schule</strong>：WHOのAWaRe分類を中心の仕組みにしたターン制RPG</li>
    <li><strong>菌撃退シューター：BactAttack</strong>：WHOのAWaRe分類を中心の仕組みにしたシューティングゲーム（英語版あり）</li>
  </ul>
  <h2 class="sec">薬剤耐性（AMR）の啓発</h2>
  <p>薬剤耐性（AMR）の啓発に関する取り組みで、文部科学大臣賞を受賞しました。</p>
</div></section>""")

    cards = "".join(
        f'<a class="card cal-card" href="{c["file"]}"><img src="{c["file"]}" width="2400" height="600" loading="lazy" alt="{c["alt_ja"]}"><h3>{c["label_ja"]}</h3></a>'
        for c in reversed(CALENDARS))
    P["calendar"] = ("カレンダー", "毎月更新のバイキンズ®カレンダー。", page_head("ja", "カレンダー", "毎月、バイキンズ®のカレンダーを掲載しています。") + f"""
<section class="section"><div class="wrap">
  <figure class="cal-main"><a href="{cal['file']}"><img src="{cal['file']}" width="2400" height="600" alt="{cal['alt_ja']}"></a>
  <figcaption>{cal['label_ja']}（画像をクリックすると原寸で開きます）<br><a href="{cal['file']}" download>PNG画像をダウンロード</a></figcaption></figure>
  <h2 class="sec">これまでのカレンダー</h2>
  <div class="cards cal-grid">{cards}</div>
  <p class="note">バイキンズ®は登録商標です。</p>
</div></section>""")

    staff = [("Kaneko Y", "金子幸弘"), ("Niki M", "仁木満美子"), ("Oinuma K", "老沼研一"), ("Tsubouchi T", "坪内泰志")]
    pm = "".join(f'<li><a href="{pubmed(f"{q}[Author] AND Osaka[Affiliation]")}">{n}（{q}）をPubMedで検索</a></li>' for q, n in staff)
    P["publications"] = ("業績", "細菌学教室の業績。受賞、論文・著書・学会発表の検索リンク。", page_head("ja", "業績") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec">受賞</h2>
  <ul><li>文部科学大臣賞（薬剤耐性（AMR）の啓発に関する取り組み）</li></ul>
  <h2 class="sec">論文・著書・学会発表</h2>
  <p>主要な業績は、このページに順次掲載します。当面は、次のデータベースをご利用ください。</p>
  <ul>
    <li><a href="https://researchmap.jp/">researchmap</a></li>
    <li><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></li>
  </ul>
  <p>教員ごとのPubMed検索（所属に「Osaka」を含む論文）：</p>
  <ul>{pm}</ul>
  <p class="note">検索結果には同姓同名の研究者の論文が含まれたり、所属表記の違いにより漏れたりする場合があります。</p>
</div></section>""")

    P["access"] = ("アクセス・連絡先", "大阪公立大学大学院医学研究科 細菌学の所在地とお問い合わせ。", page_head("ja", "アクセス・連絡先") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec">所在地</h2>
  <p>{ADDRESS_JA}</p>
  <p><a href="{MAP_URL}">地図で見る（Googleマップ）</a></p>
  <p>建物・階などの詳しい案内は、<a href="{OFFICIAL}">公式サイト</a>および大阪公立大学の案内をご確認ください。</p>
  <h2 class="sec">お問い合わせ</h2>
  <p>共同研究、見学、大学院進学（修士課程・博士課程）に関するご相談を含め、お問い合わせは<a href="{OFFICIAL}">公式サイト</a>に掲載されている連絡先をご利用ください。</p>
</div></section>""")

    P["links"] = ("リンク", "関連サイトへのリンク。", page_head("ja", "リンク") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec">大学・教室</h2>
  <ul>
    <li><a href="{OFFICIAL}">大阪公立大学大学院医学研究科 細菌学（公式サイト）</a></li>
    <li><a href="https://www.omu.ac.jp/med/">大阪公立大学 医学部・大学院医学研究科</a></li>
    <li><a href="https://www.omu.ac.jp/">大阪公立大学</a></li>
  </ul>
  <h2 class="sec">研究・文献</h2>
  <ul>
    <li><a href="https://researchmap.jp/">researchmap</a></li>
    <li><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></li>
  </ul>
</div></section>""")
    return P


# ======================================================================
# 英語ページ
# ======================================================================
def pages_en():
    cal = CALENDARS[-1]
    f = lambda p: "../" + p
    P = {}

    P["index"] = ("", "Department of Bacteriology, Osaka Metropolitan University Graduate School of Medicine. Research on bacterial and fungal infections and antimicrobial resistance (AMR), and education and outreach that make bacteriology fun.", f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <h1 class="hero-title"><span class="org">Osaka Metropolitan University Graduate School of Medicine</span><span class="dept en">Department of Bacteriology</span></h1>
    <p class="catch">Know bacteria. Enjoy bacteria.</p>
    <p class="lead">We study bacterial and fungal infections, with a focus on antimicrobial resistance (AMR), and develop education and outreach that make bacteriology fun to learn.</p>
    <p class="cta"><a class="btn" href="research.html">Research</a><a class="btn ghost" href="members.html">Members</a><a class="btn ghost" href="about.html">About</a></p>
  </div>
  <a class="hero-cal" href="calendar.html"><img src="{f(cal['file'])}" width="2400" height="600" alt="{cal['alt_en']}"><span>This month’s calendar: {cal['label_en']}</span></a>
</div></section>
<section class="section"><div class="wrap">
  <h2 class="sec">News</h2>
  {info_list('en', 4)}
  <p class="more"><a href="info.html">All news</a></p>
</div></section>
<section class="section alt"><div class="wrap">
  <h2 class="sec">Research themes</h2>
  <div class="cards">
    <a class="card" href="research.html#amr"><h3>Antimicrobial resistance (AMR)</h3><p>Resistant pathogens that are difficult to treat, such as {sn('Pseudomonas aeruginosa')} and {sn('Acinetobacter baumannii')}.</p></a>
    <a class="card" href="research.html#fungi"><h3>Fungi and antifungal discovery</h3><p>Infections caused by {sn('Candida')} species, and the search for novel antifungal compounds from deep-sea actinomycetes.</p></a>
    <a class="card" href="research.html#education"><h3>Clinical bacteriology and education</h3><p>Gamification-based methods for teaching bacteriology and infectious diseases.</p></a>
    <a class="card" href="research.html#biosafety"><h3>Biosafety and collaboration</h3><p>The BSL committee and collaborative frameworks such as OIRCID.</p></a>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <h2 class="sec">Education and outreach</h2>
  <div class="cards">
    <a class="card" href="education.html#iloha"><h3>ILOHA</h3><p>An infectious disease study group running since 2014, with more than 430 sessions held.</p></a>
    <a class="card" href="education.html#bactplatform"><h3>bactPlatform</h3><p>A library of HTML learning tools for microbiology and infectious diseases.</p></a>
    <a class="card" href="outreach.html"><h3>Baikinz® and FunFection</h3><p>“Fun is contagious.” Games and characters that bring bacteriology closer to everyone.</p></a>
    <a class="card" href="calendar.html"><h3>Baikinz® calendar</h3><p>A new monthly calendar. {cal['label_en']}.</p></a>
  </div>
</div></section>
""")

    P["info"] = ("News", "News from the Department of Bacteriology.", page_head("en", "News") + wrap(info_list("en")))

    P["about"] = ("About", "About the Department of Bacteriology: philosophy, overview, and related organizations.", page_head("en", "About") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec">About the department</h2>
  <p>The Department of Bacteriology at Osaka Metropolitan University Graduate School of Medicine works on bacterial and fungal infections and antimicrobial resistance (AMR), education in clinical microbiology, and outreach that makes bacteriology and infectious diseases more approachable.</p>
  <h2 class="sec">Our aim: growing the community of people who enjoy bacteriology</h2>
  <p>We want to turn bacteriology from “difficult” into “fun.” Through games and learning tools, our education and outreach aim to increase the number of people who enjoy bacteria (“saikin-raku jinkō” in Japanese).</p>
  <h2 class="sec">Overview</h2>
  <dl class="dl">
    <dt>Name</dt><dd>Department of Bacteriology, Osaka Metropolitan University Graduate School of Medicine</dd>
    <dt>Professor</dt><dd>Yukihiro Kaneko</dd>
    <dt>Related organizations</dt><dd>OIRCID (Osaka International Research Center for Infectious Diseases) / RCIDS / Toneyama Institute for Tuberculosis Research</dd>
    <dt>Official site</dt><dd><a href="{OFFICIAL}">{OFFICIAL}</a> (in Japanese)</dd>
    <dt>This website</dt><dd>Launched on November 7, 2026, separately from the official URL because of a server outage</dd>
  </dl>
</div></section>""")

    P["members"] = ("Members", "Members of the Department of Bacteriology.", page_head("en", "Members") +
                    f'<section class="section"><div class="wrap">{member_cards("en")}</div></section>')

    P["research"] = ("Research", "Research in the Department of Bacteriology: antimicrobial resistance, fungal infections, deep-sea actinomycetes, clinical bacteriology education, and biosafety.", page_head("en", "Research") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec" id="amr">Antimicrobial resistance (AMR) and resistant bacteria</h2>
  <p>AMR is a serious global problem. We study the epidemiology of resistance and infection control, mainly for multidrug-resistant Gram-negative bacilli that are difficult to treat, such as {sn('Pseudomonas aeruginosa')} and {sn('Acinetobacter baumannii')}.</p>
  <ul>
    <li>Analysis of {sn('P. aeruginosa')} showing difficult-to-treat resistance (DTR)</li>
    <li>Meta-analysis of novel antimicrobial agents for carbapenem-resistant {sn('A. baumannii')} (CRAB)</li>
    <li>Infection control for multidrug-resistant Gram-negative bacilli</li>
  </ul>
  <h2 class="sec" id="fungi">Fungi ({sn('Candida')} species)</h2>
  <p>We integrate clinical data on invasive infections caused by {sn('Candida')} species, including systematic reviews and meta-analyses that compare mortality in candidemia caused by {sn('Candida auris')} and by other {sn('Candida')} species.</p>
  <h2 class="sec" id="deepsea">Novel antifungal compounds from deep-sea actinomycetes</h2>
  <p>We study actinomycetes isolated from the deep sea as a source of novel antifungal compounds. Genome analysis with a nanopore sequencer (MinION), compound analysis by HPLC/MS, RNA-seq, and evaluation in mice are combined to search for and evaluate candidate compounds.</p>
  <h2 class="sec" id="education">Clinical bacteriology and education research</h2>
  <p>We study how to teach clinical microbiology so that the knowledge can be used in practice. We develop gamified learning materials, including games built around the WHO AWaRe classification of antibacterial agents. See <a href="education.html">Education</a> and <a href="outreach.html">Outreach</a> for details.</p>
  <h2 class="sec" id="biosafety">Biosafety</h2>
  <p>Through the Biosafety Level (BSL) committee of Osaka Metropolitan University, we contribute to building systems for handling pathogens safely.</p>
  <h2 class="sec" id="collab">Collaboration on infectious disease control (OIRCID)</h2>
  <p>OIRCID (Osaka International Research Center for Infectious Diseases) is a five-party framework of Osaka Prefecture, Osaka City, Osaka Metropolitan University, Osaka University, and the Osaka Institute of Public Health. Our department is also involved in designing its governance.</p>
</div></section>""")

    P["education"] = ("Education", "Education activities: ILOHA, bactPlatform, and more.", page_head("en", "Education") + """
<section class="section"><div class="wrap prose">
  <h2 class="sec">Our approach</h2>
  <p>In teaching bacteriology and infectious diseases, we value enjoying the subject as much as knowing it. Alongside undergraduate and graduate teaching, we use gamification and self-made learning tools to increase the number of people who enjoy bacteriology.</p>
  <h2 class="sec" id="iloha">ILOHA</h2>
  <p>ILOHA (Infection Lecture at OMU Hospital &amp; Affiliates) is an infectious disease study group that has been running since 2014, with more than 430 sessions held. Announcements are sent through an official LINE account.</p>
  <h2 class="sec" id="bactplatform">bactPlatform</h2>
  <p>A library of HTML learning tools for microbiology and infectious diseases, published on GitHub Pages.</p>
  <ul>
    <li>Microbiology laboratory simulators</li>
    <li>Immunology and parasitology series</li>
    <li>Clinical history-taking simulators</li>
    <li>Infectious disease chart viewers</li>
  </ul>
</div></section>""")

    P["outreach"] = ("Outreach", "Outreach: Baikinz®, FunFection, and AMR awareness.", page_head("en", "Outreach") + """
<section class="section"><div class="wrap prose">
  <h2 class="sec">Growing the community of people who enjoy bacteriology</h2>
  <p>We use characters and games to make bacteria and infectious diseases more familiar and more fun.</p>
  <h2 class="sec">Baikinz®</h2>
  <p>Baikinz® is a set of original characters based on microorganisms (a registered trademark). They also appear in our monthly <a href="calendar.html">calendar</a>.</p>
  <h2 class="sec">FunFection</h2>
  <p>FunFection is our brand for educational games and tools, with the tagline “Fun is contagious.” Using the Baikinz® characters, we are developing games such as:</p>
  <ul>
    <li><strong>Baikinz Tōmetsu Senki: Busters Schule</strong> — a turn-based RPG built around the WHO AWaRe classification</li>
    <li><strong>BactAttack</strong> — a shooting game built around the WHO AWaRe classification (with an English version)</li>
  </ul>
  <h2 class="sec">AMR awareness</h2>
  <p>We received the Minister of Education, Culture, Sports, Science and Technology Award for our work on raising awareness of antimicrobial resistance (AMR).</p>
</div></section>""")

    cards = "".join(
        f'<a class="card cal-card" href="{f(c["file"])}"><img src="{f(c["file"])}" width="2400" height="600" loading="lazy" alt="{c["alt_en"]}"><h3>{c["label_en"]}</h3></a>'
        for c in reversed(CALENDARS))
    P["calendar"] = ("Calendar", "The monthly Baikinz® calendar.", page_head("en", "Calendar", "We publish a Baikinz® calendar every month.") + f"""
<section class="section"><div class="wrap">
  <figure class="cal-main"><a href="{f(cal['file'])}"><img src="{f(cal['file'])}" width="2400" height="600" alt="{cal['alt_en']}"></a>
  <figcaption>{cal['label_en']} (click the image to open it at full size)<br><a href="{f(cal['file'])}" download>Download the PNG image</a></figcaption></figure>
  <h2 class="sec">Past calendars</h2>
  <div class="cards cal-grid">{cards}</div>
  <p class="note">Baikinz® is a registered trademark.</p>
</div></section>""")

    staff = [("Kaneko Y", "Yukihiro Kaneko"), ("Niki M", "Mamiko Niki"), ("Oinuma K", "Ken-ichi Oinuma"), ("Tsubouchi T", "Taishi Tsubouchi")]
    pm = "".join(f'<li><a href="{pubmed(f"{q}[Author] AND Osaka[Affiliation]")}">{n} ({q}): search PubMed</a></li>' for q, n in staff)
    P["publications"] = ("Publications", "Publications and awards of the Department of Bacteriology, with search links.", page_head("en", "Publications") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec">Awards</h2>
  <ul><li>Minister of Education, Culture, Sports, Science and Technology Award (for work on raising awareness of antimicrobial resistance, AMR)</li></ul>
  <h2 class="sec">Papers, books, and presentations</h2>
  <p>We will add major publications to this page over time. In the meantime, please use the following databases.</p>
  <ul>
    <li><a href="https://researchmap.jp/">researchmap</a> (in Japanese)</li>
    <li><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></li>
  </ul>
  <p>PubMed searches by faculty member (papers with “Osaka” in the affiliation):</p>
  <ul>{pm}</ul>
  <p class="note">Results may include researchers with the same name, or miss papers because of differences in how affiliations are written.</p>
</div></section>""")

    P["access"] = ("Access and contact", "Location and contact information of the Department of Bacteriology.", page_head("en", "Access and contact") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec">Location</h2>
  <p>{ADDRESS_EN}</p>
  <p><a href="{MAP_URL}">View on Google Maps</a></p>
  <p>For details such as the building and floor, please see the <a href="{OFFICIAL}">official site</a> (in Japanese) and the guidance from Osaka Metropolitan University.</p>
  <h2 class="sec">Contact</h2>
  <p>For inquiries, including collaboration, visits, and enrollment in our Master’s and Doctoral programs, please use the contact information on the <a href="{OFFICIAL}">official site</a>.</p>
</div></section>""")

    P["links"] = ("Links", "Related links.", page_head("en", "Links") + f"""
<section class="section"><div class="wrap prose">
  <h2 class="sec">University and department</h2>
  <ul>
    <li><a href="{OFFICIAL}">Department of Bacteriology (official site, in Japanese)</a></li>
    <li><a href="https://www.omu.ac.jp/med/">Osaka Metropolitan University Graduate School of Medicine</a></li>
    <li><a href="https://www.omu.ac.jp/">Osaka Metropolitan University</a></li>
  </ul>
  <h2 class="sec">Research and literature</h2>
  <ul>
    <li><a href="https://researchmap.jp/">researchmap</a></li>
    <li><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></li>
  </ul>
</div></section>""")
    return P


# ======================================================================
# CSS ほか
# ======================================================================
CSS = r"""
:root{
  --ink:#1c1a18; --ink-soft:#4a4540; --paper:#f6f1e4; --paper-2:#efe7d3; --card:#fffdf7; --line:#ddd3bd;
  --indigo:#1e2d50; --indigo-2:#2d4170; --red:#b22824; --teal:#2a7f72; --gold:#c6983a; --radius:14px;
  --sans:"BIZ UDPGothic","BIZ UDPゴシック","Hiragino Kaku Gothic ProN","Hiragino Sans","Noto Sans JP","Noto Sans CJK JP","Yu Gothic UI","Meiryo",sans-serif;
  --serif:"Noto Serif JP","Noto Serif CJK JP","Hiragino Mincho ProN","Yu Mincho","YuMincho","BIZ UDPMincho","Times New Roman",serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;font-family:var(--sans);color:var(--ink);background:var(--paper);line-height:1.9;font-size:17px}
html[lang="en"] body{line-height:1.7}
img{max-width:100%;height:auto}
a{color:var(--indigo-2);text-underline-offset:3px}
a:hover{color:var(--red)}
.sn{font-style:italic}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.skip{position:absolute;left:-999px;top:0;background:#fff;color:#000;padding:8px 14px;z-index:100}
.skip:focus{left:8px;top:8px}

.site-header{background:var(--indigo);color:#fff;border-bottom:4px solid var(--red)}
.head-top{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:14px;padding-bottom:14px}
.brand{display:flex;align-items:center;gap:14px;color:#fff;text-decoration:none}
.brand:hover{color:#fff}
.brand svg{width:48px;height:48px;flex:none}
.brand .org{display:block;font-size:.78rem;letter-spacing:.06em;opacity:.88;line-height:1.4}
.brand .dept{display:block;font-family:var(--serif);font-weight:900;font-size:1.75rem;line-height:1.2;letter-spacing:.12em}
html[lang="en"] .brand .dept{font-size:1.3rem;letter-spacing:.03em}
.lang{display:flex;gap:6px;flex:none}
.lang a{color:#fff;border:1px solid rgba(255,255,255,.55);padding:3px 12px;border-radius:999px;text-decoration:none;font-size:.85rem}
.lang a[aria-current="true"]{background:#fff;color:var(--indigo);font-weight:700}
.nav{background:var(--indigo-2)}
.nav ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap}
.nav a{display:block;color:#fff;text-decoration:none;padding:10px 15px;font-size:.95rem;border-bottom:3px solid transparent}
.nav a:hover,.nav a[aria-current="page"]{background:rgba(255,255,255,.1);border-bottom-color:var(--gold);color:#fff}
.nav-toggle{display:none;width:100%;background:none;border:0;color:#fff;font:inherit;padding:12px 4px;text-align:left;cursor:pointer}
.nav-toggle::after{content:" ▾"}

.hero{position:relative;overflow:hidden;padding:46px 0 30px}
.hero::before{content:"";position:absolute;right:-120px;top:-170px;width:580px;height:580px;border-radius:50%;
  background:radial-gradient(circle,rgba(178,40,36,.17),rgba(178,40,36,0) 68%)}
.hero-grid{position:relative;display:grid;grid-template-columns:1fr;gap:28px;align-items:center}
.hero-title{font-family:var(--serif);font-weight:900;margin:0 0 6px;line-height:1.25;letter-spacing:.05em}
.hero-title .org{display:block;font-size:1.05rem;font-weight:700;color:var(--ink-soft);letter-spacing:.06em}
.hero-title .dept{display:block;font-size:3.6rem;letter-spacing:.18em}
.hero-title .dept.en{font-size:2.3rem;letter-spacing:.02em}
.catch{font-family:var(--serif);font-size:1.55rem;font-weight:700;color:var(--red);margin:10px 0 12px;line-height:1.5}
.lead{margin:0 0 18px;max-width:34em}
.btn{display:inline-block;background:var(--indigo);color:#fff;padding:9px 22px;border-radius:999px;text-decoration:none;font-weight:700;margin:4px 8px 4px 0;border:2px solid var(--indigo)}
.btn:hover{background:var(--red);border-color:var(--red);color:#fff}
.btn.ghost{background:transparent;color:var(--indigo)}
.btn.ghost:hover{color:#fff}
.hero-cal{display:block;text-decoration:none;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:var(--radius);
  padding:10px;box-shadow:0 12px 32px rgba(30,45,80,.2);transition:transform .2s}
.hero-cal:hover{transform:translateY(-3px);color:var(--ink)}
.hero-cal img{display:block;width:100%;border-radius:8px}
.hero-cal span{display:block;text-align:center;font-weight:700;padding:8px 4px 2px;font-size:.92rem}

.section{padding:34px 0}
.section.alt{background:var(--paper-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.sec{font-family:var(--serif);font-size:1.55rem;line-height:1.4;border-left:8px solid var(--red);padding-left:14px;margin:30px 0 16px}
.section .wrap>.sec:first-child,.prose>.sec:first-child{margin-top:0}
.page-head{background:linear-gradient(180deg,var(--paper-2),var(--paper));padding:30px 0 20px;border-bottom:1px solid var(--line)}
.page-head h1{font-family:var(--serif);font-size:2.2rem;margin:4px 0 6px;line-height:1.3;letter-spacing:.05em}
.crumb{margin:0;font-size:.85rem;color:var(--ink-soft)}
.page-head .lead{margin:6px 0 0}
.prose{max-width:860px}
.prose p{margin:0 0 1em}
.prose li{margin:.3em 0}
.note{font-size:.88rem;color:var(--ink-soft)}
.more{text-align:right;margin:10px 0 0}

.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}
.card{display:block;background:var(--card);border:1px solid var(--line);border-top:5px solid var(--indigo);border-radius:var(--radius);padding:18px 20px;text-decoration:none;color:var(--ink);transition:transform .15s,box-shadow .15s}
.card:nth-child(2){border-top-color:var(--teal)}
.card:nth-child(3){border-top-color:var(--gold)}
.card:nth-child(4){border-top-color:var(--red)}
.card:hover{transform:translateY(-3px);box-shadow:0 8px 22px rgba(30,45,80,.14);color:var(--ink)}
.card h3{font-family:var(--serif);font-size:1.15rem;margin:0 0 6px;line-height:1.4}
.card p{margin:0;font-size:.94rem;line-height:1.7}

.info-list{list-style:none;margin:0;padding:0;background:var(--card);border:1px solid var(--line);border-radius:var(--radius)}
.info-list li{display:grid;grid-template-columns:13em 1fr;gap:6px 18px;padding:16px 20px;border-bottom:1px solid var(--line)}
.info-list li:last-child{border-bottom:0}
.info-meta{display:flex;flex-direction:column;align-items:flex-start;gap:6px;font-size:.92rem;color:var(--ink-soft)}
.info-body h3{font-size:1.08rem;margin:0 0 4px;line-height:1.5}
.info-body p{margin:0;font-size:.97rem}
.tag{display:inline-block;background:var(--indigo);color:#fff;font-size:.74rem;padding:0 11px;border-radius:999px;line-height:1.7}
.tag-notice{background:var(--red)}
.tag-calendar{background:var(--teal)}

.members{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;margin-bottom:10px}
.member{display:flex;gap:16px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:18px 20px}
.member.featured{grid-column:1/-1}
.badge{flex:none;width:64px;height:64px;border-radius:50%;background:var(--indigo);color:#fff;display:grid;place-items:center;font-size:.8rem;font-weight:700;text-align:center;line-height:1.2;border:3px solid var(--gold)}
.member h3{font-family:var(--serif);font-size:1.35rem;margin:0;line-height:1.4}
.member .en{display:block;font-family:var(--sans);font-size:.85rem;font-weight:400;color:var(--ink-soft);letter-spacing:.02em}
.role{margin:2px 0 0;font-size:.93rem;color:var(--ink-soft)}
.mini{margin:8px 0 0;padding-left:1.2em;font-size:.92rem;line-height:1.7}

.dl{display:grid;grid-template-columns:11em 1fr;border-top:1px solid var(--line);background:var(--card);border-radius:8px;margin:0}
.dl dt,.dl dd{margin:0;padding:12px 14px;border-bottom:1px solid var(--line)}
.dl dt{font-weight:700;color:var(--indigo)}

.cal-main{margin:0 0 10px;text-align:center}
.cal-main img{border:1px solid var(--line);border-radius:10px;box-shadow:0 10px 28px rgba(30,45,80,.18);background:#fff}
.cal-main figcaption{margin-top:10px;font-size:.92rem;color:var(--ink-soft)}
.cal-card img{display:block;width:100%;border-radius:8px;margin-bottom:8px}
.cal-grid{grid-template-columns:repeat(auto-fill,minmax(420px,1fr))}

.site-footer{background:var(--indigo);color:#dfe5f2;margin-top:40px;padding:26px 0 30px;font-size:.9rem;line-height:1.7}
.site-footer a{color:#fff}
.foot-links{margin:0 0 12px}
.ai-note{border:1px solid rgba(255,255,255,.32);border-radius:10px;padding:12px 16px;background:rgba(255,255,255,.07);margin:0 0 12px}
.copy{margin:0;opacity:.85}

@media (max-width:860px){
  body{font-size:16px}
  .hero{padding-top:34px}
  .hero-title .dept{font-size:2.8rem}
  .hero-title .dept.en{font-size:1.9rem}
  .info-list li{grid-template-columns:1fr}
  .info-meta{flex-direction:row;align-items:center;gap:10px}
  .dl{grid-template-columns:1fr}
  .dl dt{border-bottom:0;padding-bottom:0}
  .head-top{align-items:flex-start}
  .brand .dept{font-size:1.45rem}
  .js .nav-toggle{display:block}
  .js #site-nav{display:none;flex-direction:column}
  .js #site-nav.open{display:flex}
  .page-head h1{font-size:1.8rem}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
@media print{.site-header .nav,.lang,.skip{display:none}body{background:#fff}}
"""

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><circle cx="24" cy="24" r="23" fill="#b22824"/>'
           '<rect x="15" y="9" width="18" height="31" rx="9" fill="#fff"/><circle cx="20" cy="22" r="2.1" fill="#1e2d50"/>'
           '<circle cx="28" cy="22" r="2.1" fill="#1e2d50"/><path d="M20 28q4 3 8 0" stroke="#1e2d50" stroke-width="1.8" '
           'fill="none" stroke-linecap="round"/></svg>\n')

NOT_FOUND = """<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ページが見つかりません | 大阪公立大学大学院医学研究科 細菌学</title>
<link rel="stylesheet" href="/omumdb/assets/style.css"></head>
<body><main class="section"><div class="wrap prose"><h1 class="sec">ページが見つかりません / Page not found</h1>
<p><a href="/omumdb/index.html">トップページへ戻る</a> ／ <a href="/omumdb/en/index.html">Back to the home page</a></p></div></main>
<footer class="site-footer"><div class="wrap"><p class="ai-note">@@JA@@</p><p class="ai-note">@@EN@@</p></div></footer></body></html>
""".replace("@@JA@@", AI_NOTE["ja"]).replace("@@EN@@", AI_NOTE["en"])


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    write(ROOT / "assets" / "style.css", CSS.lstrip("\n"))
    write(ROOT / "assets" / "favicon.svg", FAVICON)
    write(ROOT / "404.html", NOT_FOUND)
    write(ROOT / "robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    urls = []
    for lang, pages in (("ja", pages_ja()), ("en", pages_en())):
        assert set(pages) == set(PAGES), (lang, set(PAGES) ^ set(pages))
        for slug, (title, desc, body) in pages.items():
            out = ROOT / f"{slug}.html" if lang == "ja" else ROOT / "en" / f"{slug}.html"
            write(out, render(lang, slug, title, desc, body))
            urls.append(BASE if (lang == "ja" and slug == "index") else
                        f"{BASE}{slug}.html" if lang == "ja" else f"{BASE}en/{slug}.html")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{u}</loc><lastmod>{LAUNCH}</lastmod></url>" for u in urls]
    sm.append("</urlset>")
    write(ROOT / "sitemap.xml", "\n".join(sm) + "\n")
    print(f"generated {len(urls)} pages")


if __name__ == "__main__":
    main()
