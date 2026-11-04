# Capas de destaque do @radar_fitnessbr (1080x1920, ícone centralizado)
from playwright.sync_api import sync_playwright
import os
A="#C8FF2E"; W="#F3F5F2"; HERE=os.path.dirname(os.path.abspath(__file__))
icons={
"hyrox": f'<circle cx="540" cy="990" r="150" fill="none" stroke="{W}" stroke-width="26"/><rect x="505" y="790" width="70" height="40" rx="10" fill="{W}"/><line x1="540" y1="830" x2="540" y2="840" stroke="{W}" stroke-width="26"/><path d="M540 990 L540 875 A115 115 0 0 1 640 935 Z" fill="{A}"/><line x1="540" y1="990" x2="610" y2="920" stroke="{A}" stroke-width="22" stroke-linecap="round"/><circle cx="540" cy="990" r="20" fill="{W}"/>',
"crossfit": f'<path d="M470 930 C430 860 450 800 540 800 C630 800 650 860 610 930" fill="none" stroke="{W}" stroke-width="34" stroke-linecap="round"/><circle cx="540" cy="1020" r="135" fill="{A}"/><rect x="455" y="905" width="170" height="40" rx="20" fill="{A}"/>',
"agenda": f'<rect x="370" y="820" width="340" height="320" rx="30" fill="none" stroke="{W}" stroke-width="26"/><rect x="370" y="820" width="340" height="80" rx="20" fill="{A}"/><line x1="450" y1="790" x2="450" y2="850" stroke="{W}" stroke-width="26" stroke-linecap="round"/><line x1="630" y1="790" x2="630" y2="850" stroke="{W}" stroke-width="26" stroke-linecap="round"/><circle cx="540" cy="1020" r="40" fill="{A}"/>',
"resultados": f'<path d="M440 820 h200 v90 a100 100 0 0 1 -200 0z" fill="{A}"/><path d="M440 845 h-50 a50 50 0 0 0 50 70 M640 845 h50 a50 50 0 0 1 -50 70" fill="none" stroke="{W}" stroke-width="20"/><line x1="540" y1="1010" x2="540" y2="1080" stroke="{W}" stroke-width="26"/><rect x="450" y="1080" width="180" height="40" rx="10" fill="{W}"/>',
"carreira": f'<rect x="360" y="880" width="360" height="250" rx="28" fill="none" stroke="{W}" stroke-width="26"/><path d="M470 880 v-40 a20 20 0 0 1 20 -20 h100 a20 20 0 0 1 20 20 v40" fill="none" stroke="{W}" stroke-width="26"/><rect x="360" y="970" width="360" height="40" fill="{A}"/>',
"formacao": f'<polygon points="540,800 760,900 540,1000 320,900" fill="{W}"/><path d="M420 955 v90 c0 50 240 50 240 0 v-90 l-120 55z" fill="{A}"/><line x1="760" y1="900" x2="760" y2="1030" stroke="{W}" stroke-width="18" stroke-linecap="round"/>',
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg=b.new_page(viewport={"width":1080,"height":1920})
    for n,ic in icons.items():
        svg=f'<svg viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg"><rect width="1080" height="1920" fill="#0A0C0F"/><circle cx="540" cy="960" r="330" fill="#12171C" stroke="{A}" stroke-width="14"/>{ic}</svg>'
        pg.set_content(f"<html><body style='margin:0'>{svg}</body></html>"); pg.wait_for_timeout(80)
        pg.screenshot(path=f"{HERE}/destaques_radar/destaque_{n}.png")
    b.close()
