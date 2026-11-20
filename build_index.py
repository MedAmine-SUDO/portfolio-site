from build_common import *

def svc(k, title, desc, bullets, proofs):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    pr = " ".join(f'<a href="{h}">{l}</a>' for l, h in proofs)
    return f'''<article class="svc">
  <span class="k">{k}</span>
  <h3>{title}</h3>
  <p>{desc}</p>
  <ul>{lis}</ul>
  <div class="proof"><span class="lbl">{t("Proof","Preuves")}</span>{pr}</div>
</article>'''

def card(href, k, title, desc, arrow, out=None):
    o = f'<p class="out">{out}</p>' if out else f'<span class="arrow">{arrow}</span>'
    return f'<a class="card" href="{href}"><span class="k">{k}</span><h3>{title}</h3><p>{desc}</p>{o}</a>'

body = f'''
<header class="hero">
  <div class="who"><strong>Mohamed Amine Ben Afia</strong> · {t("Data engineer · Monastir, Tunisia · working remotely","Data engineer · Monastir, Tunisie · en télétravail")}</div>
  <h1>{t("I build the data pipelines, automations and AI assistants that small teams run their business on","Je construis les pipelines de données, les automatisations et les assistants IA sur lesquels les petites équipes font tourner leur activité")}</h1>
  <p class="lede">{t("Four years on a data platform that still runs in production for 93 client companies. Now I work directly with startups and small businesses: fixed scope, clear price, documented, and the code is yours.","Quatre ans sur une plateforme de données qui tourne toujours en production pour 93 entreprises clientes. Aujourd'hui, je travaille directement avec des startups et des PME : périmètre défini, prix clair, tout est documenté, et le code vous appartient.")}</p>
  <div class="actions">
    <a class="btn primary" data-l="en" href="{CALL_EN}">Book a free 20-min call</a><a class="btn primary" data-l="fr" href="{CALL_FR}">Réserver un appel gratuit de 20 min</a>
    <a class="btn ghost" href="#work">{t("See the work","Voir les réalisations")}</a>
  </div>
  <div class="figures" role="list" style="--n:4">
    <div class="fig" role="listitem"><b>~220</b><span>{t("client data flows I migrated to Apache Airflow on AWS","flux de données clients que j'ai migrés vers Apache Airflow sur AWS")}</span></div>
    <div class="fig" role="listitem"><b>98.6%</b><span>{t("task success on that platform, a year after I left","de tâches réussies sur cette plateforme, un an après mon départ")}</span></div>
    <div class="fig" role="listitem"><b>3</b><span>{t("freelance clients: health-tech, textile, software","clients freelance : santé, textile, logiciel")}</span></div>
    <div class="fig" role="listitem"><b>7</b><span>{t("public projects you can open, try and read","projets publics à ouvrir, tester et lire")}</span></div>
  </div>
</header>

<section id="services" aria-labelledby="services-h">
  <span class="eyebrow">{t("Services","Services")}</span>
  <h2 id="services-h">{t("Four things I do well, each with work you can check","Quatre choses que je fais bien, chacune avec des réalisations vérifiables")}</h2>
  <div class="services">
    {svc(t("Data engineering","Data engineering"),
         t("Data pipelines &amp; migrations","Pipelines de données &amp; migrations"),
         t("Move fragile scripts and cron jobs to a real orchestrator, or build a pipeline from scratch: scheduled, monitored and easy to re-run.","Passer des scripts fragiles et des tâches cron à un vrai orchestrateur, ou construire un pipeline de zéro : planifié, surveillé et facile à relancer."),
         [t("ETL pipelines in Python and SQL","Pipelines ETL en Python et SQL"),
          t("Apache Airflow or Dagster, including migrations from cron or Celery","Apache Airflow ou Dagster, y compris la migration depuis cron ou Celery"),
          t("Alerts and searchable logs, so you hear about failures before your clients do","Alertes et logs consultables, pour connaître les pannes avant vos clients"),
          t("AWS (S3, Lambda, ECS, MWAA) or a lean self-hosted stack","AWS (S3, Lambda, ECS, MWAA) ou une stack auto-hébergée légère")],
         [(t("Integration platform","Plateforme d'intégration"),"work/integration-platform"),(t("EU Trade Explorer","EU Trade Explorer"),"https://eu-trade-explorer.streamlit.app/")])}
    {svc(t("Data collection","Collecte de données"),
         t("Web scraping","Web scraping"),
         t("Turn public websites into clean, structured data in your database or spreadsheet, once or on a schedule.","Transformer des sites publics en données propres et structurées dans votre base ou votre tableur, une fois ou de façon planifiée."),
         [t("Paginated and JavaScript-heavy sites","Sites paginés ou chargés en JavaScript"),
          t("Duplicates merged, fields normalized","Doublons fusionnés, champs normalisés"),
          t("Scheduled runs for price or stock monitoring","Exécutions planifiées pour suivre les prix ou les stocks"),
          t("Delivered to MySQL, PostgreSQL, Excel or Google Sheets","Livré dans MySQL, PostgreSQL, Excel ou Google Sheets")],
         [(t("Health-tech database","Base de données santé"),"work/practitioner-database"),(t("Price tracker","Suivi de prix"),"https://medamine-sudo.github.io/competitor-price-tracker/"),(t("Paris 2024 camps","Camps Paris 2024"),"https://paris2024-training-camps.streamlit.app/")])}
    {svc(t("Automation","Automatisation"),
         t("Business automation","Automatisation métier"),
         t("Remove repetitive admin work: reports that build themselves, alerts that reach the right person, shared files that stay clean.","Supprimer le travail administratif répétitif : des rapports qui se font tout seuls, des alertes qui arrivent à la bonne personne, des fichiers partagés qui restent propres."),
         [t("Daily, weekly and monthly reports by email","Rapports quotidiens, hebdomadaires et mensuels par e-mail"),
          t("Alerts on Slack, email or WhatsApp","Alertes sur Slack, par e-mail ou sur WhatsApp"),
          t("Excel and Google Sheets clean-ups and syncs","Nettoyage et synchronisation de fichiers Excel et Google Sheets"),
          t("Orders, invoices and payments for shops and distributors","Commandes, factures et paiements pour commerces et distributeurs")],
         [(t("Textile wholesaler","Grossiste textile"),"work/textile-stock-attendance"),(t("Meeting-room cleanup","Salles de réunion"),"work/meeting-rooms"),(t("Order &amp; Invoice API","API Commandes &amp; Factures"),"https://github.com/MedAmine-SUDO/order-invoice-api")])}
    {svc(t("AI","IA"),
         t("AI assistants &amp; integrations","Assistants IA &amp; intégrations"),
         t("An assistant that answers your customers from your own documents, in French, English or Tunisian darija, and passes real leads to your team.","Un assistant qui répond à vos clients à partir de vos propres documents, en français, en anglais ou en darija, et transmet les vrais prospects à votre équipe."),
         [t("Answers on your website or WhatsApp","Réponses sur votre site ou sur WhatsApp"),
          t("Leads saved to Google Sheets, team alerted by email","Prospects enregistrés dans Google Sheets, équipe alertée par e-mail"),
          t("MCP servers that connect AI tools to your data","Serveurs MCP qui connectent les outils IA à vos données"),
          t("Costs measured before you commit","Coûts mesurés avant de vous engager")],
         [(t("AI assistant demo","Démo de l'assistant IA"),"https://ai-customer-assistant-demo.vercel.app"),(t("LearnHub MCP server","Serveur MCP LearnHub"),"https://github.com/MedAmine-SUDO/learnhub-mcp-server")])}
  </div>
</section>

<section id="start" aria-labelledby="start-h">
  <span class="eyebrow">{t("Where to start","Par où commencer")}</span>
  <h2 id="start-h">{t("A fixed-price audit, then a fixed-price build","Un audit à prix fixe, puis une réalisation à prix fixe")}</h2>
  <div class="offer">
    <div>
      <h3>{t("Data &amp; Automation Audit","Audit Data &amp; Automatisation")}</h3>
      <p>{t("About a day of my time on your pipelines, scripts or manual processes. You get a clear picture of what to fix first, and a price for fixing it.","Environ une journée de travail sur vos pipelines, vos scripts ou vos processus manuels. Vous savez clairement quoi corriger en premier, et combien ça coûte.")}</p>
      <ul>
        <li>{t("A call to understand your setup and what is slowing you down","Un appel pour comprendre votre organisation et ce qui vous ralentit")}</li>
        <li>{t("A review of the pipelines, scripts, files or processes involved","Une revue des pipelines, scripts, fichiers ou processus concernés")}</li>
        <li>{t("A short written report: what breaks, what costs you time, what to fix first","Un court rapport écrit : ce qui casse, ce qui vous fait perdre du temps, quoi corriger en premier")}</li>
        <li>{t("A fixed-price quote for the fixes, with no obligation to go ahead","Un devis à prix fixe pour les corrections, sans obligation de suite")}</li>
      </ul>
    </div>
    <div>
      <div class="price">{t("€250","350 TND")}</div>
      <span class="small">{t("Fixed price · in Tunisia: 350 TND","Prix fixe · hors Tunisie : 250 €")}</span>
      <div class="actions"><a class="btn primary" data-l="en" href="mailto:{EMAIL}?subject=Data%20%26%20Automation%20Audit">Ask for an audit</a><a class="btn primary" data-l="fr" href="mailto:{EMAIL}?subject=Audit%20Data%20%26%20Automatisation">Demander un audit</a></div>
    </div>
  </div>
  <div class="terms">
    <div><b>{t("Free 20-minute call","Appel gratuit de 20 minutes")}</b><span>{t("Tell me the problem. I'll tell you honestly whether I can help.","Expliquez-moi le problème. Je vous dis franchement si je peux aider.")}</span></div>
    <div><b>{t("Fixed price, agreed first","Prix fixe, validé avant")}</b><span>{t("Every project is quoted at a fixed price before I start. Quote within 48 hours.","Chaque projet a un prix fixe, validé avant de commencer. Devis sous 48 heures.")}</span></div>
    <div><b>{t("The code is yours","Le code vous appartient")}</b><span>{t("Documented, in your own repository, with a handover.","Documenté, dans votre propre dépôt, avec une passation.")}</span></div>
  </div>
</section>

<section id="work" aria-labelledby="work-h">
  <span class="eyebrow">{t("Client work","Réalisations clients")}</span>
  <h2 id="work-h">{t("What I built, and what it changed","Ce que j'ai construit, et ce que ça a changé")}</h2>
  <div class="grid" style="--n:2">
    {card("work/integration-platform", t("EdTech platform · 2021–2025","Plateforme EdTech · 2021–2025"), t("The integration platform behind a European learning product","La plateforme d'intégration derrière un produit e-learning européen"), t("Three generations of the platform that syncs every client's HR data into the product, ending with ~220 flows on Apache Airflow (AWS MWAA).","Trois générations de la plateforme qui synchronise les données RH de chaque client avec le produit, jusqu'à ~220 flux sur Apache Airflow (AWS MWAA)."), "", t("Still in production a year later: ~1,400 task runs a day, 98.6% success.","Toujours en production un an après : ~1 400 tâches par jour, 98,6 % de réussite."))}
    {card("work/practitioner-database", t("Health-tech startup · scraping","Startup santé · scraping"), t("A practitioner database to launch a health-tech product","Une base de praticiens pour lancer un produit santé"), t("Public listings across Tunisia collected, deduplicated, normalized and loaded into the client's MySQL database.","Annonces publiques de toute la Tunisie collectées, dédoublonnées, normalisées et chargées dans la base MySQL du client."), "", t("1,000+ records over 4–6 specialties; a new specialty is one setting.","1 000+ fiches sur 4 à 6 spécialités ; une nouvelle spécialité = un paramètre."))}
    {card("work/textile-stock-attendance", t("Textile wholesaler · automation","Grossiste textile · automatisation"), t("From paper notebooks to stock alerts and automatic attendance reports","Des cahiers papier aux alertes de stock et aux rapports de présence automatiques"), t("A PostgreSQL stock app with alerts by app, email and WhatsApp, plus reports pulled straight from the ZKTeco time clock.","Une application de stock PostgreSQL avec alertes dans l'appli, par e-mail et WhatsApp, plus des rapports tirés directement de la pointeuse ZKTeco."), "", t("1,000+ fabric references; both systems used every day.","1 000+ références de tissu ; les deux systèmes sont utilisés tous les jours."))}
    {card("work/meeting-rooms", t("Software company · automation","Éditeur de logiciels · automatisation"), t("Ending the “is this room actually taken?” chase","Fini les « cette salle est-elle vraiment prise ? »"), t("A daily cleanup of forgotten bookings in a shared Excel file, with Slack reminders before and after each meeting.","Un nettoyage quotidien des réservations oubliées dans un fichier Excel partagé, avec des rappels Slack avant et après chaque réunion."), "", t("~40 people; bookings now match reality.","~40 personnes ; les réservations reflètent enfin la réalité."))}
  </div>
</section>

<section id="projects" aria-labelledby="projects-h">
  <span class="eyebrow">{t("Open source","Open source")}</span>
  <h2 id="projects-h">{t("Projects you can open, try and read","Des projets à ouvrir, tester et lire")}</h2>
  <p>{t("Each one runs for real, and the READMEs list the bugs I found by running them.","Chacun tourne pour de vrai, et les README listent les bugs trouvés en les faisant tourner.")}</p>
  <div class="grid" style="--n:4">
    {card("https://eu-trade-explorer.streamlit.app/", "Dagster · DuckDB · Streamlit", "EU Trade Explorer", t("Eurostat trade data, about 5 million rows a month, with memory fixes measured and documented.","Les données commerciales d'Eurostat, environ 5 millions de lignes par mois, avec des correctifs mémoire mesurés et documentés."), t("Open the dashboard →","Ouvrir le tableau de bord →"))}
    {card("https://ai-customer-assistant-demo.vercel.app", "RAG · n8n · FastAPI", t("AI Customer Assistant","Assistant client IA"), t("Answers customers from a business's own documents, captures leads into Google Sheets and alerts the team.","Répond aux clients à partir des documents de l'entreprise, enregistre les prospects dans Google Sheets et alerte l'équipe."), t("Try the demo →","Tester la démo →"))}
    {card("https://medamine-sudo.github.io/competitor-price-tracker/", "Scraping · PostgreSQL", t("Competitor Price Tracker","Suivi des prix concurrents"), t("Daily prices from Tunisian online shops, matched across sites, with price history, Excel report and email alerts.","Prix quotidiens de boutiques en ligne tunisiennes, rapprochés entre sites, avec historique, rapport Excel et alertes e-mail."), t("Open the demo →","Ouvrir la démo →"))}
    {card("https://github.com/MedAmine-SUDO/order-invoice-api", "FastAPI · PostgreSQL", t("Order &amp; Invoice API","API Commandes &amp; Factures"), t("Orders, invoices and credit notes for a Tunisian shop or distributor: PDF invoices with QR codes, payments, unpaid tracking, TVA journal.","Commandes, factures et avoirs pour un commerce ou distributeur tunisien : factures PDF avec QR code, paiements, suivi des impayés, journal TVA."), t("Read the code →","Lire le code →"))}
    {card("https://github.com/MedAmine-SUDO/learnhub-mcp-server", "MCP · AWS Lambda", "LearnHub MCP Server", t("Connects AI assistants to an LMS API, with OAuth, rate limiting and paging of large results.","Connecte les assistants IA à l'API d'un LMS, avec OAuth, limitation de débit et pagination des gros résultats."), t("Read the code →","Lire le code →"))}
    {card("https://paris2024-training-camps.streamlit.app/", "Scraping · Streamlit", "Paris 2024 Training Camps", t("A tested scraper, a clean dataset of 999 Olympic training camps, and a live map.","Un scraper testé, un jeu de données propre de 999 centres de préparation olympiques, et une carte interactive."), t("Open the explorer →","Ouvrir la carte →"))}
    {card("https://medamine-sudo.github.io/savebrain/", "React · Supabase · AI", "SaveBrain", t("Turns saved Instagram and Facebook posts into a private to-do list with reminders.","Transforme vos publications Instagram et Facebook enregistrées en liste de tâches privée avec rappels."), t("Open the app →","Ouvrir l'appli →"))}
    {card(GITHUB, t("Everything else","Tout le reste"), "GitHub", t("Smaller projects, templates and experiments.","Petits projets, templates et expériences."), "github.com/MedAmine-SUDO →")}
  </div>
</section>

<section id="contact" aria-labelledby="contact-h">
  <span class="eyebrow">{t("Contact","Contact")}</span>
  <h2 id="contact-h">{t("Tell me what's slowing your team down","Dites-moi ce qui ralentit votre équipe")}</h2>
  <p>{t("Email is fastest. Write in English or French.","L'e-mail est le plus rapide. Écrivez-moi en français ou en anglais.")}</p>
  <div class="contact">
    <a class="card" href="mailto:{EMAIL}"><span class="k">{t("Email","E-mail")}</span><b>{EMAIL}</b><span class="arrow">{t("Write to me →","M'écrire →")}</span></a>
    <a class="card" href="{LINKEDIN}"><span class="k">LinkedIn</span><b>in/mabenafia</b><span class="arrow">{t("Send a message →","Envoyer un message →")}</span></a>
    <a class="card" href="{UPWORK}"><span class="k">Upwork</span><b>{t("Hire me on Upwork","Me recruter sur Upwork")}</b><span class="arrow">{t("View profile →","Voir le profil →")}</span></a>
  </div>
</section>
'''
open("site/index.html","w").write(page(
  "Mohamed Amine Ben Afia · Data, AI & Automation",
  "Mohamed Amine Ben Afia · Data, IA & Automatisation",
  "Data pipelines, web scraping, business automation and AI assistants for startups and small businesses. Fixed scope, clear price, the code is yours.",
  body, root=""))
print("index ok")
