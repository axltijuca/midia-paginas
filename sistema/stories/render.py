# Modelos de stories do @axltijuca (1080x1920). Zonas seguras: 250px topo / 340px base sem texto.
import base64, os, sys, json
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__)); REPO=os.path.join(HERE,'..','..')
def img(p):
    p=os.path.join(REPO,p); ext='png' if p.endswith('png') else 'jpeg'
    return f"data:image/{ext};base64,"+base64.b64encode(open(p,'rb').read()).decode()
CSS="""
*{box-sizing:border-box;margin:0}
body{width:1080px;height:1920px;background:#0E1218;color:#F4F1EA;font-family:'Inter',sans-serif;overflow:hidden;position:relative}
.d{font-family:'Barlow Condensed',sans-serif;font-weight:800;text-transform:uppercase;letter-spacing:.01em;line-height:.92}
.tag{position:absolute;top:270px;left:80px;font:700 30px 'Barlow Condensed';letter-spacing:.22em;text-transform:uppercase;color:#C9A45C;display:flex;align-items:center;gap:18px}
.tag::before{content:"";width:46px;height:4px;background:#C9A45C}
.handle{position:absolute;bottom:250px;left:0;right:0;text-align:center;font:600 30px 'Inter';color:#F4F1EA;opacity:.75;letter-spacing:.04em}
.bg{position:absolute;inset:0;background-size:cover;background-position:center}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,18,24,.85) 0%,rgba(14,18,24,.1) 28%,rgba(14,18,24,.15) 55%,rgba(14,18,24,.96) 82%)}
.frame{position:absolute;left:130px;right:130px;top:380px;height:900px;border-radius:28px;background-size:cover;background-position:center;box-shadow:0 30px 80px rgba(0,0,0,.6);outline:3px solid #C9A45C;outline-offset:14px}
.big{position:absolute;left:80px;right:80px;bottom:420px}
.big h1{font-size:132px;text-shadow:0 4px 24px rgba(0,0,0,.7)}
.big p{font:500 44px/1.35 'Inter';margin-top:26px;color:#d9d4c8}
.gold{color:#C9A45C}
.pill{display:inline-block;margin-top:34px;background:#C9A45C;color:#0E1218;font:800 40px 'Barlow Condensed';letter-spacing:.06em;text-transform:uppercase;padding:18px 34px;border-radius:12px}
.list{list-style:none;padding:0;margin-top:40px;display:flex;flex-direction:column;gap:30px}
.list li{font:500 50px/1.3 'Inter';padding-left:54px;position:relative}
.list li::before{content:"";position:absolute;left:0;top:22px;width:28px;height:4px;background:#C9A45C}
.film{position:absolute;left:90px;right:90px;top:400px;height:960px;background:#F4F1EA;padding:28px 28px 120px;transform:rotate(-2.2deg);box-shadow:0 30px 70px rgba(0,0,0,.6)}
.film div{width:100%;height:100%;background-size:cover;background-position:center;filter:sepia(.25) contrast(1.05)}
.film span{position:absolute;bottom:34px;left:0;right:0;text-align:center;font:700 46px 'Barlow Condensed';letter-spacing:.12em;color:#0E1218}
.arrow{font:800 120px 'Barlow Condensed';color:#C9A45C;line-height:1}
"""
def page(body): return f"<html><head><style>{CSS}</style></head><body>{body}<div class='handle'>@axltijuca</div></body></html>"
T={
'novo':lambda s:page(f"<div class='tag'>Novo no perfil</div><div class='frame' style=\"background-image:url('{img(s['img'])}')\"></div><div class='big' style='bottom:330px;text-align:center'><h1 class='d' style='font-size:96px'><span class='gold'>↑</span> {s['title']}</h1><div class='pill'>Toque no perfil</div></div>"),
'resultado':lambda s:page(f"<div class='bg' style=\"background-image:url('{img(s['img'])}')\"></div><div class='shade'></div><div class='tag'>Resultado</div><div class='big'><h1 class='d'>{s['title']}</h1><p>{s['text']}</p></div>"),
'dica':lambda s:page(f"<div class='tag'>Dica rápida</div><div class='big' style='top:520px;bottom:auto'><h1 class='d' style='font-size:150px'>{s['title']}</h1><ul class='list'>{''.join('<li>'+x+'</li>' for x in s['items'])}</ul></div>"),
'bastidor':lambda s:page(f"<div class='bg' style=\"background-image:url('{img(s['img'])}')\"></div><div class='shade'></div><div class='tag'>Bastidores</div><div class='big'><h1 class='d' style='font-size:104px'>{s['title']}</h1></div>"),
'prova':lambda s:page(f"<div class='tag'>O que os alunos dizem</div><div style='position:absolute;left:50px;right:50px;top:400px;height:1000px;display:flex;align-items:center;justify-content:center'><img src=\"{img(s['img'])}\" style='width:100%;border-radius:22px;box-shadow:0 30px 80px rgba(0,0,0,.6);outline:3px solid #C9A45C;outline-offset:12px'></div><div class='big' style='bottom:330px'><h1 class='d' style='font-size:96px'>{s['title']}</h1></div>"),
'chamada':lambda s:page(f"<div class='tag'>Consultoria online</div><div class='big' style='top:620px;bottom:auto'><h1 class='d' style='font-size:220px'>{s['title']}</h1><p>{s['text']}</p><div class='pill'>Me manda CONSULTORIA no direct</div></div>"),
'arquivo':lambda s:page(f"<div class='tag'>Arquivo TDF</div><div class='film'><div style=\"background-image:url('{img(s['img'])}')\"></div><span>{s['year']}</span></div><div class='big' style='bottom:330px'><h1 class='d' style='font-size:84px'>{s['title']}</h1></div>"),
'novo_reel':lambda s:page(f"<div class='tag'>Reel novo no perfil</div><div class='big' style='top:560px;bottom:auto'><div class='arrow'>▶</div><h1 class='d' style='font-size:150px;margin-top:30px'>{s['title']}</h1><p>{s['text']}</p><div class='pill'>Toque no perfil e assista</div></div>"),
'pessoal':lambda s:page(f"<div class='bg' style=\"background-image:url('{img(s['img'])}')\"></div><div class='shade'></div><div class='big'><h1 class='d' style='font-size:96px'>{s['title']}</h1></div>"),
}
def render(items,outdir):
    os.makedirs(outdir,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
        for it in items:
            pg.set_content(T[it['t']](it)); pg.wait_for_timeout(150)
            pg.screenshot(path=os.path.join(outdir,it['name']+'.jpg'),type='jpeg',quality=90)
        b.close()
if __name__=='__main__':
    render(json.load(open(sys.argv[1])),sys.argv[2])
