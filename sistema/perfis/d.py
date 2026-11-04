from playwright.sync_api import sync_playwright
R="#FF3D2E"; W="#F5F1EE"
icons={
"ergogenicos": f'<g transform="rotate(-35 540 960)"><rect x="390" y="880" width="300" height="160" rx="80" fill="none" stroke="{W}" stroke-width="26"/><path d="M540 880 v160 h70 a80 80 0 0 0 0-160z" fill="{R}"/></g>',
"doping": f'<path d="M540 760 L700 820 V950 C700 1050 630 1120 540 1160 C450 1120 380 1050 380 950 V820 Z" fill="none" stroke="{W}" stroke-width="26" stroke-linejoin="round"/><path d="M470 960 l50 50 l95 -105" fill="none" stroke="{R}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>',
"exames": f'<rect x="470" y="760" width="140" height="380" rx="70" fill="none" stroke="{W}" stroke-width="26"/><path d="M483 990 h114 v80 a57 57 0 0 1 -114 0z" fill="{R}"/><line x1="440" y1="760" x2="640" y2="760" stroke="{W}" stroke-width="26" stroke-linecap="round"/>',
"mitos": f'<text x="430" y="1060" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="300" fill="{W}">?</text><text x="650" y="1060" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="300" fill="{R}">!</text>',
"formacao": f'<polygon points="540,780 760,880 540,980 320,880" fill="{W}"/><path d="M420 935 v90 c0 50 240 50 240 0 v-90 l-120 55z" fill="{R}"/><line x1="760" y1="880" x2="760" y2="1010" stroke="{W}" stroke-width="18" stroke-linecap="round"/>',
"treino": f'<rect x="330" y="900" width="420" height="40" rx="10" fill="{W}"/><rect x="350" y="830" width="60" height="180" rx="14" fill="{R}"/><rect x="670" y="830" width="60" height="180" rx="14" fill="{R}"/><rect x="290" y="860" width="40" height="120" rx="10" fill="{W}"/><rect x="750" y="860" width="40" height="120" rx="10" fill="{W}"/>',
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg=b.new_page(viewport={"width":1080,"height":1920})
    for n,ic in icons.items():
        svg=f'<svg viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg"><rect width="1080" height="1920" fill="#0B0809"/><circle cx="540" cy="960" r="330" fill="#1A1012" stroke="{R}" stroke-width="14"/>{ic}</svg>'
        pg.set_content(f"<html><body style='margin:0'>{svg}</body></html>"); pg.wait_for_timeout(80)
        pg.screenshot(path=f"destaques/destaque_{n}.png")
    b.close()
