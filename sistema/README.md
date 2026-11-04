# Sistema de conteúdo — @radar_fitnessbr e @labdahipertrofia

- `radar/` e `lab/`: textos dos 15 posts (content.py) e gerador das artes (render.py, Playwright + Chrome, 1080×1350).
- `perfis/`: fotos de perfil e capas de destaque.
- Imagens publicadas ficam em `posts/<pagina>/<id>/` e são servidas via raw.githubusercontent.com para o Metricool.
- Metricool: marca labdahipertrofia = blogId 7878727; marca radar_fitnessbr = blogId 7879145.
- Próximo passo: refazer as capas/notícias com fotos geradas no Hugging Face (FLUX.1-Krea-dev) e agendar 1 post/dia por página.
