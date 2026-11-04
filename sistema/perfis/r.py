from playwright.sync_api import sync_playwright
radar = """<svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg">
<defs><radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#14181C"/><stop offset="1" stop-color="#0A0C0F"/></radialGradient>
<linearGradient id="s" x1="540" y1="540" x2="540" y2="130" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#C8FF2E" stop-opacity=".0"/><stop offset="1" stop-color="#C8FF2E" stop-opacity=".55"/></linearGradient></defs>
<rect width="1080" height="1080" fill="url(#g)"/>
<g fill="none" stroke="#C8FF2E">
<circle cx="540" cy="540" r="400" stroke-width="10" opacity=".9"/>
<circle cx="540" cy="540" r="290" stroke-width="6" opacity=".45"/>
<circle cx="540" cy="540" r="180" stroke-width="6" opacity=".45"/>
<line x1="140" y1="540" x2="940" y2="540" stroke-width="4" opacity=".25"/>
<line x1="540" y1="140" x2="540" y2="940" stroke-width="4" opacity=".25"/></g>
<path d="M540 540 L540 140 A400 400 0 0 1 823 257 Z" fill="url(#s)" transform="rotate(10 540 540)"/>
<line x1="540" y1="540" x2="823" y2="257" stroke="#C8FF2E" stroke-width="10" stroke-linecap="round" transform="rotate(10 540 540)"/>
<circle cx="540" cy="540" r="34" fill="#C8FF2E"/>
<circle cx="735" cy="400" r="22" fill="#C8FF2E"/><circle cx="735" cy="400" r="44" fill="#C8FF2E" opacity=".2"/>
</svg>"""
lab = """<svg viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg">
<defs><radialGradient id="g" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#1A1012"/><stop offset="1" stop-color="#0B0809"/></radialGradient></defs>
<rect width="1080" height="1080" fill="url(#g)"/>
<polygon points="540,150 878,345 878,735 540,930 202,735 202,345" fill="none" stroke="#FF3D2E" stroke-width="22" stroke-linejoin="round"/>
<polygon points="540,215 822,378 822,702 540,865 258,702 258,378" fill="none" stroke="#FF3D2E" stroke-width="5" opacity=".35"/>
<g fill="#FF3D2E"><circle cx="540" cy="150" r="30"/><circle cx="878" cy="345" r="30"/><circle cx="878" cy="735" r="30"/><circle cx="540" cy="930" r="30"/><circle cx="202" cy="735" r="30"/><circle cx="202" cy="345" r="30"/></g>
<text x="540" y="615" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="250" letter-spacing="-12" fill="#F5F1EE">LAB</text>
<rect x="400" y="660" width="280" height="14" fill="#FF3D2E"/>
</svg>"""
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg=b.new_page(viewport={"width":1080,"height":1080})
    for n,s in [("perfil_radar_fitnessbr",radar),("perfil_labdahipertrofia",lab)]:
        pg.set_content(f"<html><body style='margin:0'>{s}</body></html>"); pg.wait_for_timeout(100)
        pg.screenshot(path=f"{n}.png")
    b.close()
