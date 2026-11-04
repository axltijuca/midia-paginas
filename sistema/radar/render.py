import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from content import POSTS, HANDLE
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
FOTOS = os.path.join(HERE, "..", "fotos", "radar")
import base64
os.makedirs(OUT, exist_ok=True)
e = html.escape

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0A0C0F;--ink:#F3F5F2;--mute:#9AA39A;--acc:#C8FF2E;--line:#1E242B}
body{width:1080px;height:1350px;background:var(--bg);color:var(--ink);font-family:'Inter',sans-serif;overflow:hidden;position:relative}
.radar{position:absolute;right:-260px;top:-260px;width:900px;height:900px;border-radius:50%;
 background:repeating-radial-gradient(circle, transparent 0 88px, rgba(200,255,46,.10) 88px 90px);}
.sweep{position:absolute;right:-260px;top:-260px;width:900px;height:900px;border-radius:50%;
 background:conic-gradient(from 150deg, transparent 0deg, rgba(200,255,46,.16) 55deg, transparent 55.5deg);-webkit-mask:radial-gradient(circle, #000 0 60%, transparent 72%);}
.grid{position:absolute;inset:0;background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:90px 90px;opacity:.35}
.top{position:absolute;left:80px;right:80px;top:72px;display:flex;justify-content:space-between;align-items:center;z-index:2}
.brand{display:flex;align-items:center;gap:14px;font-weight:900;letter-spacing:.18em;font-size:26px}
.dot{width:18px;height:18px;border-radius:50%;background:var(--acc);box-shadow:0 0 0 7px rgba(200,255,46,.18),0 0 0 15px rgba(200,255,46,.08)}
.tag{font-weight:800;font-size:22px;letter-spacing:.16em;color:var(--bg);background:var(--acc);padding:10px 18px}
.foot{position:absolute;left:80px;right:80px;bottom:64px;display:flex;justify-content:space-between;font-size:24px;color:var(--mute);font-weight:600;z-index:2}
.wrap{position:absolute;left:80px;right:80px;z-index:2}
h1{font-family:'Inter Display','Inter';font-weight:900;letter-spacing:-.035em;line-height:.98}
.cover h1{font-size:104px}
.cover .wrap{bottom:190px}
.sub{margin-top:38px;font-size:34px;font-weight:600;color:var(--acc)}
.n{font-family:'Inter Display';font-weight:900;font-size:220px;line-height:.8;color:var(--acc);letter-spacing:-.05em}
.point .wrap,.stat .wrap,.list .wrap,.versus .wrap,.cta .wrap,.poll .wrap{top:170px;bottom:150px;display:flex;flex-direction:column;justify-content:center}
.point h2,.stat h2,.list h2,.cta h2,.versus h2{font-family:'Inter Display';font-weight:900;font-size:72px;line-height:1.02;letter-spacing:-.03em;margin-top:44px}
p.body{margin-top:34px;font-size:40px;line-height:1.38;color:#C9CFC7;font-weight:500;max-width:880px}
.big{font-family:'Inter Display';font-weight:900;font-size:230px;line-height:.85;color:var(--acc);letter-spacing:-.06em}
.list ul{list-style:none;margin-top:46px}
.list li{font-size:40px;font-weight:600;padding:22px 0;border-bottom:2px solid var(--line);display:flex;gap:26px}
.list li b{color:var(--acc);font-weight:900;min-width:52px}
.vs{margin-top:50px;display:grid;gap:26px}
.card{border:2px solid var(--line);padding:38px 40px;background:rgba(255,255,255,.02)}
.card.a{border-left:10px solid var(--acc)}
.card.b{border-left:10px solid var(--ink)}
.card h3{font-weight:900;letter-spacing:.14em;font-size:28px}
.card.a h3{color:var(--acc)}
.card p{margin-top:16px;font-size:38px;line-height:1.3;font-weight:500;color:#D5DAD3}
.cta{background:var(--acc);color:var(--bg)}
.cta h2{font-size:96px}
.cta p.body{color:#1B2207;font-weight:600}
.cta .foot{color:#2A3410}
.cta .tag{background:var(--bg);color:var(--acc)}
.cta .dot{background:var(--bg);box-shadow:0 0 0 7px rgba(10,12,15,.15)}
.handle{margin-top:70px;align-self:flex-start;display:inline-block;background:var(--bg);color:var(--acc);font-weight:900;font-size:44px;padding:20px 30px;letter-spacing:-.01em}
.news .wrap{bottom:200px}
.kicker{font-size:30px;font-weight:800;letter-spacing:.12em;color:var(--acc)}
.news h1{font-size:88px;margin-top:30px}
.news p.body{font-size:42px}
.bar{width:140px;height:12px;background:var(--acc);margin-bottom:40px}
.poll h1{font-size:84px}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:80px}
.opt{border:3px solid var(--acc);padding:60px 30px;text-align:center}
.opt .l{font-size:40px;font-weight:900;color:var(--acc)}
.opt .t{font-size:62px;font-weight:900;margin-top:16px;letter-spacing:-.02em}
.opt.b{border-color:var(--ink)} .opt.b .l{color:var(--ink)}

.ph{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0}
.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.05) 22%,rgba(0,0,0,.15) 42%,var(--bg) 80%)}
.withphoto .grid,.withphoto .hex,.withphoto .radar,.withphoto .sweep{display:none}
.withphoto h1{text-shadow:0 4px 30px rgba(0,0,0,.6)}
.withphoto .kicker{text-shadow:0 2px 12px rgba(0,0,0,.95),0 0 4px rgba(0,0,0,.9)}
.withphoto.cover h1{font-size:92px}
.withphoto.news h1{font-size:80px}
.withphoto .foot{color:#cfcfcf}
"""

def frame(cls, inner, tag, idx, total, bg=True, photo=None):
    deco = '<div class="grid"></div><div class="radar"></div><div class="sweep"></div>' if bg else ''
    if photo:
        b64 = base64.b64encode(open(photo,'rb').read()).decode()
        deco = f'<div class="ph" style="background-image:url(data:image/jpeg;base64,{b64})"></div>'
        cls += " withphoto"
    pg = f"{idx}/{total}" if total > 1 else ""
    return f"""<html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{cls}">{deco}
<div class="top"><div class="brand"><span class="dot"></span>RADAR FITNESS</div><div class="tag">{e(tag)}</div></div>
{inner}
<div class="foot"><span>{HANDLE}</span><span>{pg}</span></div></body></html>"""

def slide_html(s, tag, idx, total, photo=None):
    k = s["k"]
    if k == "cover":
        inner = f'<div class="wrap"><div class="bar"></div><h1>{e(s["title"])}</h1><div class="sub">{e(s["sub"])}</div></div>'
    elif k == "point":
        inner = f'<div class="wrap"><div class="n">{e(s["n"])}</div><h2>{e(s["title"])}</h2><p class="body">{e(s["body"])}</p></div>'
    elif k == "stat":
        inner = f'<div class="wrap"><div class="big">{e(s["big"])}</div><h2>{e(s["title"])}</h2><p class="body">{e(s["body"])}</p></div>'
    elif k == "list":
        lis = "".join(f'<li><b>{i+1:02d}</b>{e(t)}</li>' for i, t in enumerate(s["items"]))
        inner = f'<div class="wrap"><h2 style="margin-top:0">{e(s["title"])}</h2><ul>{lis}</ul></div>'
    elif k == "versus":
        a, b = s["a"], s["b"]
        inner = f'''<div class="wrap"><h2 style="margin-top:0">{e(s["title"])}</h2><div class="vs">
<div class="card a"><h3>{e(a[0])}</h3><p>{e(a[1])}</p></div>
<div class="card b"><h3>{e(b[0])}</h3><p>{e(b[1])}</p></div></div></div>'''
    elif k == "cta":
        inner = f'<div class="wrap"><h2 style="margin-top:0">{e(s["title"])}</h2><p class="body">{e(s["body"])}</p><div class="handle">{HANDLE}</div></div>'
        return frame("cta", inner, "SEGUE", idx, total, bg=False)
    elif k == "news":
        inner = f'<div class="wrap"><div class="kicker">{e(s["kicker"])}</div><h1>{e(s["title"])}</h1><p class="body">{e(s["body"])}</p></div>'
        return frame("news", inner, s["tag"], idx, total, photo=photo)
    elif k == "poll":
        inner = f'''<div class="wrap"><h1>{e(s["title"])}</h1><div class="opts">
<div class="opt a"><div class="l">A</div><div class="t">{e(s["a"])}</div></div>
<div class="opt b"><div class="l">B</div><div class="t">{e(s["b"])}</div></div></div>
<p class="body" style="margin-top:60px">Comenta A ou B 👇</p></div>'''
        return frame("poll", inner, s["tag"], idx, total)
    return frame(k, inner, tag, idx, total, photo=photo if k == "cover" else None)

only = sys.argv[1:] or None
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width":1080,"height":1350})
    for post in POSTS:
        if only and post["id"] not in only: continue
        tag = post["slides"][0].get("tag", "")
        total = len(post["slides"])
        for i, s in enumerate(post["slides"], 1):
            ph = os.path.join(FOTOS, post['id'] + '.jpg')
            pg.set_content(slide_html(s, tag, i, total, ph if (i == 1 and os.path.exists(ph)) else None))
            pg.wait_for_timeout(80)
            pg.screenshot(path=f"{OUT}/radar_{post['id']}_{i:02d}.png")
        with open(f"{OUT}/radar_{post['id']}_legenda.txt", "w") as f:
            f.write(post["caption"])
    b.close()
print("done")
