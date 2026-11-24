"""Renders site/assets/og.png (the link preview image) with headless Chrome.

    python3 make_og.py

Update COUNTS when a case study or an open-source project is added.
"""
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
CHROME = str(next(Path.home().glob(".cache/ms-playwright/chromium-*/chrome-linux64/chrome")))
COUNTS = "4 case studies · 9 open-source projects · fixed-price audit"
CARDS = [("PIPELINES", "Airflow, Dagster, ETL on AWS"), ("SCRAPING", "Clean data into your database"),
         ("AUTOMATION", "Reports &amp; alerts that run themselves"), ("AI", "Assistants on your own documents")]

cards = "".join(f'<div class="card"><i>{k}</i><b>{v}</b></div>' for k, v in CARDS)
page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap');
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:627px;background:#f4f6f8;color:#15212e;font-family:"IBM Plex Sans",sans-serif;position:relative;overflow:hidden}}
.eb{{position:absolute;left:70px;top:60px;font-family:"IBM Plex Mono",monospace;font-weight:500;color:#2456c8;letter-spacing:.12em;font-size:17px}}
h1{{position:absolute;left:70px;top:96px;width:1000px;font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:58px;line-height:1.08;letter-spacing:-.02em}}
.cards{{position:absolute;left:70px;top:321px;width:1060px;display:flex;background:#fff;border:1px solid #d9e0e7;border-radius:8px}}
.card{{flex:1;padding:20px 20px 18px;border-left:1px solid #d9e0e7}}.card:first-child{{border-left:0}}
.card i{{display:block;font-style:normal;font-family:"IBM Plex Mono",monospace;font-size:13px;color:#9a5212;letter-spacing:.04em;margin-bottom:8px}}
.card b{{font-weight:600;font-size:20px;line-height:1.25}}
.foot{{position:absolute;left:70px;top:536px;color:#5a6878;font-size:19px}}
.url{{position:absolute;right:70px;top:534px;font-family:"IBM Plex Mono",monospace;font-weight:500;color:#2456c8;font-size:21px}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:9px;background:#2456c8}}
</style></head><body><div class="eb">MOHAMED AMINE BEN AFIA · SERVICES &amp; CASE STUDIES</div>
<h1>Data pipelines, scraping, automation and AI assistants for small teams</h1>
<div class="cards">{cards}</div><div class="foot">{COUNTS}</div><div class="url">mabenafia.vercel.app</div><div class="bar"></div></body></html>"""

with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir=HERE) as f:
    f.write(page)
try:
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--hide-scrollbars", "--window-size=1200,627",
                    "--virtual-time-budget=4000", f"--screenshot={HERE / 'site/assets/og.png'}", f"file://{f.name}"],
                   check=True, capture_output=True)
finally:
    Path(f.name).unlink()
print("wrote site/assets/og.png")
