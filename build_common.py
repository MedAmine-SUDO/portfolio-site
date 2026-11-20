EMAIL = "benafiamohamedamine@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/mabenafia/"
GITHUB = "https://github.com/MedAmine-SUDO"
UPWORK = "https://www.upwork.com/freelancers/~01de6a80acbbaa49db"
CALL_EN = f"mailto:{EMAIL}?subject=20-min%20call"
CALL_FR = f"mailto:{EMAIL}?subject=Appel%20de%2020%20min"

def t(en, fr):
    return f'<span data-l="en">{en}</span><span data-l="fr">{fr}</span>'

def blk(en, fr):
    return f'<div data-l="en">{en}</div><div data-l="fr">{fr}</div>'

def page(title_en, title_fr, desc_en, body, root=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title_en}</title>
<meta name="title-en" content="{title_en}">
<meta name="title-fr" content="{title_fr}">
<meta name="description" content="{desc_en}">
<meta property="og:title" content="{title_en}">
<meta property="og:description" content="{desc_en}">
<meta name="theme-color" content="#f4f6f8">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{root}assets/site.css">
<script src="{root}assets/lang.js"></script>
</head>
<body>
<div class="top"><div class="wrap">
  <a class="brand" href="{root or './'}">Mohamed Amine Ben Afia</a>
  <nav class="nav" aria-label="Main">
    <a href="{root}#services">{t("Services","Services")}</a>
    <a href="{root}#work">{t("Work","Réalisations")}</a>
    <a class="hide-sm" href="{root}#projects">{t("Projects","Projets")}</a>
    <a href="{root}#contact">{t("Contact","Contact")}</a>
    <span class="lang" role="group" aria-label="Language / Langue"><button type="button" data-set="en" aria-pressed="true" onclick="setLang('en')">EN</button><button type="button" data-set="fr" aria-pressed="false" onclick="setLang('fr')">FR</button></span>
  </nav>
</div></div>
<div class="wrap">
{body}
<footer>
  <span>{t("Mohamed Amine Ben Afia · Data engineering, AI &amp; automation · Monastir, Tunisia · remote worldwide","Mohamed Amine Ben Afia · Data engineering, IA &amp; automatisation · Monastir, Tunisie · à distance partout")}</span>
  <span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{LINKEDIN}">LinkedIn</a> · <a href="{GITHUB}">GitHub</a></span>
</footer>
</div>
</body>
</html>
'''

def cs_header(chips, h1, lede, extra="", root="../"):
    chip_html = "".join(f"<span>{c}</span>" for c in chips)
    return f'''<header class="page">
  <a class="back" href="{root}#work">{t("← All work","← Toutes les réalisations")}</a>
  <div class="client">{chip_html}</div>
  <h1>{h1}</h1>
  <p class="lede">{lede}</p>
  {extra}
</header>'''

def cs_cta(root="../"):
    return f'''<section aria-labelledby="next">
  <span class="eyebrow">{t("Similar problem?","Un problème similaire ?")}</span>
  <h2 id="next">{t("Tell me about it in a 20-minute call","Parlons-en lors d'un appel de 20 minutes")}</h2>
  <p>{t("I'll tell you honestly whether I can help, and what a fixed-price version of the fix would look like.","Je vous dis franchement si je peux aider, et à quoi ressemblerait la solution à prix fixe.")}</p>
  <div class="actions"><a class="btn primary" data-l="en" href="{CALL_EN}">Book a free 20-min call</a><a class="btn primary" data-l="fr" href="{CALL_FR}">Réserver un appel gratuit de 20 min</a><a class="btn ghost" href="{root}#services">{t("See services","Voir les services")}</a></div>
</section>'''
