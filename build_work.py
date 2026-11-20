from build_common import *

def fig(b, span, em=None):
    e = f"<em>{em}</em>" if em else ""
    return f'<div class="fig" role="listitem"><b>{b}</b><span>{span}</span>{e}</div>'

def vl(items):
    return '<ul class="vlist">' + "".join(f'<li><span class="k">{k}</span><span class="v">{v}</span></li>' for k, v in items) + "</ul>"

def steps(items, n=5):
    return f'<ol class="steps" style="--n:{n}">' + "".join(f"<li><b>{b}</b><span>{s}</span></li>" for b, s in items) + "</ol>"

def chips(groups):
    return '<dl class="tools">' + "".join(f'<div><dt>{dt}</dt><dd class="chips">' + "".join(f"<span>{c}</span>" for c in cs) + "</dd></div>" for dt, cs in groups) + "</dl>"

def sec(id_, eyebrow, h2, inner):
    return f'<section aria-labelledby="{id_}"><span class="eyebrow">{eyebrow}</span><h2 id="{id_}">{h2}</h2>{inner}</section>'

def ba(b_en, b_fr, bs_en, bs_fr, a_en, a_fr, as_en, as_fr):
    return f'<div class="ba"><div class="before"><b>{t(b_en,b_fr)}</b><span>{t(bs_en,bs_fr)}</span></div><div><b>{t(a_en,a_fr)}</b><span>{t(as_en,as_fr)}</span></div></div>'

# ---------- Health-tech practitioner database ----------
health = cs_header(
  [t("Health-tech startup","Startup santé"), t("Tunisia","Tunisie"), t("Web scraping · data cleaning","Web scraping · nettoyage de données")],
  t("Turning scattered practitioner listings into a clean database a health-tech product can launch on","Transformer des annonces de praticiens éparpillées en une base propre pour lancer un produit santé"),
  t("A Tunisian health-tech startup needed a directory of healthcare practitioners to seed its product. The data was public, but spread across directory sites, split over many pages, and full of duplicates and inconsistent formats. I built a pipeline that collects it, cleans it and loads it into their MySQL database, one specialty at a time.",
    "Une startup tunisienne de la santé avait besoin d'un annuaire de praticiens pour alimenter son produit. Les données étaient publiques, mais réparties sur plusieurs annuaires, découpées en de nombreuses pages, pleines de doublons et de formats incohérents. J'ai construit un pipeline qui les collecte, les nettoie et les charge dans leur base MySQL, spécialité par spécialité."),
  '<div class="figures" role="list">' + fig("1,000+" , t("practitioner records delivered, cleaned and deduplicated","fiches praticiens livrées, nettoyées et dédoublonnées"))
  + fig("4–6", t("specialties covered across Tunisia, starting with every dentist in the country","spécialités couvertes dans toute la Tunisie, en commençant par tous les dentistes du pays"))
  + fig(t("1 <small>setting</small>","1 <small>paramètre</small>"), t("to add a new specialty or country: the pipeline is driven by configuration","pour ajouter une spécialité ou un pays : le pipeline est piloté par configuration"))
  + '</div><p class="note">' + t("Counts are ranges from my own project records, not an export of the client's database.","Les chiffres sont des fourchettes issues de mes propres notes de projet, pas un export de la base du client.") + "</p>")
health += sec("problem", t("The business problem","Le problème"), t("A directory product is only as good as the data it starts with","Un annuaire ne vaut que par les données avec lesquelles il démarre"),
  "<p>" + t("The startup's product needed real practitioners on day one: names, specialties, cities, addresses and phone numbers, in a structure its database could use. The sources disagreed with each other, listed the same doctor several times, and some of them only rendered their listings with JavaScript.",
            "Le produit devait afficher de vrais praticiens dès le premier jour : noms, spécialités, villes, adresses et téléphones, dans une structure exploitable par sa base. Les sources se contredisaient, listaient plusieurs fois le même médecin, et certaines n'affichaient leurs annonces qu'en JavaScript.") + "</p>")
health += sec("built", t("What I built","Ce que j'ai construit"), t("A pipeline from public listings to rows in their database","Un pipeline des annonces publiques jusqu'aux lignes de leur base"),
  steps([(t("Crawl","Parcourir"), t("Walk every results page of each directory, specialty by specialty","Parcourir chaque page de résultats de chaque annuaire, spécialité par spécialité")),
         (t("Render","Afficher"), t("Drive a real browser with Selenium where listings load with JavaScript","Piloter un vrai navigateur avec Selenium quand les annonces se chargent en JavaScript")),
         (t("Clean","Nettoyer"), t("Merge duplicate entries for the same practitioner across pages and sources","Fusionner les doublons d'un même praticien entre pages et sources")),
         (t("Normalize","Normaliser"), t("One format for cities, phone numbers and specialty names","Un seul format pour les villes, les téléphones et les spécialités")),
         (t("Load","Charger"), t("Insert into the client's MySQL tables, ready to seed the product","Insertion dans les tables MySQL du client, prêtes à alimenter le produit"))]))
health += sec("hard", t("The hard parts","Les difficultés"), t("Where the time actually went","Là où le temps est vraiment passé"),
  vl([(t("Pagination","Pagination"), t("Results were split across many pages per specialty. The crawler walks every page so no practitioner is skipped or counted twice.","Les résultats étaient répartis sur de nombreuses pages par spécialité. Le crawler parcourt chaque page pour qu'aucun praticien ne soit oublié ou compté deux fois.")),
      (t("JavaScript &amp; blocking","JavaScript &amp; blocages"), t("Some sites only showed listings after scripts ran, and some pushed back on automated traffic. Those go through Selenium; simple pages use plain HTTP requests.","Certains sites n'affichaient les annonces qu'après exécution de scripts, d'autres bloquaient le trafic automatisé. Ceux-là passent par Selenium ; les pages simples par de simples requêtes HTTP.")),
      (t("Duplicates","Doublons"), t("The same practitioner appeared several times with small differences in name or address. Records are matched and merged before loading.","Le même praticien apparaissait plusieurs fois avec de petites différences de nom ou d'adresse. Les fiches sont rapprochées et fusionnées avant le chargement.")),
      (t("Normalization","Normalisation"), t("Cities, phone formats and specialty labels were written many ways. Each field maps to one standard value, so the product can filter and search on it.","Villes, formats de téléphone et intitulés de spécialités s'écrivaient de mille façons. Chaque champ correspond désormais à une valeur standard, pour que le produit puisse filtrer et chercher dessus."))]))
health += sec("result", t("Result","Résultat"), t("A seeded database, and a repeatable way to grow it","Une base alimentée, et un moyen reproductible de l'enrichir"),
  "<p>" + t("The client got a clean, structured practitioner database to launch with, loaded straight into the tables their product reads. The work was split into phases: dentists across Tunisia first, then further specialties. Because specialties and countries are configuration, each new phase is a short job instead of a new project.",
            "Le client a obtenu une base de praticiens propre et structurée pour son lancement, chargée directement dans les tables lues par son produit. Le travail était découpé en phases : d'abord les dentistes de toute la Tunisie, puis d'autres spécialités. Comme spécialités et pays sont de la configuration, chaque nouvelle phase est une courte mission, pas un nouveau projet.") + "</p>"
  + chips([(t("Collection","Collecte"), ["Python","Selenium","requests","BeautifulSoup"]), (t("Data","Données"), ["pandas","MySQL",t("Deduplication","Dédoublonnage"),t("Data normalization","Normalisation")])]))
health += cs_cta()

# ---------- Textile wholesaler ----------
tex = cs_header(
  [t("Textile wholesaler","Grossiste textile"), t("Tunisia","Tunisie"), t("Returning client","Client fidèle"), t("Inventory · HR reporting","Stock · reporting RH")],
  t("Taking a textile wholesaler from paper notebooks to stock alerts and attendance reports that run themselves","Faire passer un grossiste textile des cahiers papier aux alertes de stock et aux rapports de présence automatiques"),
  t("I know this company from the inside: I worked there during my studies, from the warehouse floor to running its IT. When they wanted to modernize, they came back to me. I delivered two systems: a fabric inventory app with low-stock alerts, and automatic attendance reports built on their ZKTeco time clock. Both are in daily use.",
    "Je connais cette entreprise de l'intérieur : j'y ai travaillé pendant mes études, du dépôt jusqu'à la gestion de son informatique. Quand elle a voulu se moderniser, elle est revenue vers moi. J'ai livré deux systèmes : une application de gestion du stock de tissus avec alertes de seuil, et des rapports de présence automatiques basés sur leur pointeuse ZKTeco. Les deux sont utilisés tous les jours."),
  '<div class="figures" role="list" style="--n:4">'
  + fig("1,000+", t("fabric references tracked, all on paper before","références de tissu suivies, toutes sur papier avant"))
  + fig("3", t("alert channels: in the app, by email, and on WhatsApp for critical stock","canaux d'alerte : dans l'appli, par e-mail, et sur WhatsApp pour le stock critique"))
  + fig("0 <small>→</small> 3", t("attendance reports: daily, weekly and monthly, where there were none","rapports de présence : quotidien, hebdomadaire et mensuel, là où il n'y en avait aucun"))
  + fig(t("In use","En service"), t("both systems still run every day, as of November 2026","les deux systèmes tournent encore chaque jour, en novembre 2026"))
  + "</div>")
tex += sec("inv", t("Build 1 · Fabric inventory","Réalisation 1 · Stock de tissus"), t("Knowing what is in the depot without walking the aisles","Savoir ce qu'il y a au dépôt sans parcourir les allées"),
  '<div class="cols"><div class="col"><p>' + t("Stock lived in paper notebooks. Finding out whether a fabric was available meant asking someone or checking the depot, and a reference running out was usually noticed when a client asked for it. I built a Python application on a PostgreSQL database that records every movement in and out and makes any reference searchable in seconds.",
     "Le stock vivait dans des cahiers. Savoir si un tissu était disponible voulait dire demander à quelqu'un ou aller voir au dépôt, et une rupture se remarquait souvent quand un client la demandait. J'ai construit une application Python sur une base PostgreSQL qui enregistre chaque entrée et sortie et retrouve n'importe quelle référence en quelques secondes.") + "</p>"
  + ba("Paper notebooks","Cahiers papier","before: stock known by memory and handwritten pages","avant : un stock connu de mémoire et sur des pages manuscrites","Searchable stock app","Appli de stock consultable","after: every movement recorded, current levels on screen","après : chaque mouvement enregistré, niveaux à jour à l'écran")
  + '</div><div class="col"><h3>' + t("Low-stock alerts","Alertes de stock bas") + ' <span class="tag">' + t("two levels","deux niveaux") + '</span></h3><ul class="tiers">'
  + '<li><span class="lvl">' + t("Low","Bas") + '</span><span>' + t("Highlighted in the app and sent by email","Mis en évidence dans l'appli et envoyé par e-mail") + "</span></li>"
  + '<li class="crit"><span class="lvl">' + t("Critical","Critique") + '</span><span>' + t("Pops up in the app instantly and sends a WhatsApp notification, so the right person sees it right away","S'affiche instantanément dans l'appli et envoie une notification WhatsApp, pour que la bonne personne le voie tout de suite") + "</span></li></ul></div></div>")
tex += sec("att", t("Build 2 · Attendance reports","Réalisation 2 · Rapports de présence"), t("Turning raw time-clock punches into reports HR can use","Transformer les pointages bruts en rapports exploitables par les RH"),
  '<div class="cols"><div class="col"><p>' + t("The team clocked in and out on a ZKTeco machine, but nobody turned that data into anything: there were no reports at all. I built a Python app that pulls the punches directly from the device, so nobody has to export files, and produces the reports on a schedule.",
     "L'équipe pointait sur une machine ZKTeco, mais personne n'exploitait ces données : il n'y avait aucun rapport. J'ai construit une application Python qui récupère les pointages directement depuis l'appareil, sans export manuel, et produit les rapports automatiquement.") + "</p>"
  + ba("Raw machine data","Données brutes","before: punches stored on the device, never reported","avant : des pointages stockés dans l'appareil, jamais exploités","Reports in the inbox","Rapports dans la boîte mail","after: hours, lateness and absences, emailed automatically","après : heures, retards et absences, envoyés automatiquement par e-mail")
  + '</div><div class="col">' + vl([(t("Reports","Rapports"), t("Hours worked per employee, daily, weekly and monthly.","Heures travaillées par employé, par jour, par semaine et par mois.")),
     (t("Flags","Signalements"), t("Lateness, absences and missing punches.","Retards, absences et pointages manquants.")),
     (t("Payroll","Paie"), t("A payroll-ready export, so month-end starts from clean numbers.","Un export prêt pour la paie : la fin de mois part de chiffres propres.")),
     (t("Delivery","Envoi"), t("Emailed on a schedule; nobody has to remember to run it.","Envoyé par e-mail à heure fixe ; personne n'a besoin d'y penser."))]) + "</div></div>")
tex += sec("stack", t("Toolbox","Outils"), t("What it runs on","Sur quoi ça tourne"),
  chips([(t("Inventory","Stock"), ["Python","PostgreSQL",t("Email alerts","Alertes e-mail"),t("WhatsApp notifications","Notifications WhatsApp")]), (t("Attendance","Présence"), ["Python",t("ZKTeco device integration","Intégration pointeuse ZKTeco"),t("Scheduled reports","Rapports planifiés"),t("Payroll export","Export paie")])]))
tex += cs_cta()

# ---------- Meeting rooms ----------
rooms = cs_header(
  [t("Software company","Éditeur de logiciels"), t("~40 people","~40 personnes"), t("Workflow automation · Slack","Automatisation · Slack")],
  t("Ending the “is this room actually taken?” chase at a 40-person software company","Fini les « cette salle est-elle vraiment prise ? » dans un éditeur de logiciels de 40 personnes"),
  t("Meeting rooms were booked by hand in a shared Excel file, usually shortly before the meeting. People often forgot to remove their booking once they were done, so rooms looked taken when they were free. I automated the cleanup and the reminders around that same file, so bookings match reality and nobody has to change how they work.",
    "Les salles de réunion se réservaient à la main dans un fichier Excel partagé, souvent peu avant la réunion. Les gens oubliaient régulièrement de retirer leur réservation après coup : les salles paraissaient prises alors qu'elles étaient libres. J'ai automatisé le nettoyage et les rappels autour de ce même fichier, pour que les réservations reflètent la réalité sans changer les habitudes de personne."))
rooms += sec("problem", t("The business problem","Le problème"), t("Forgotten bookings cost more than the room","Une réservation oubliée coûte plus cher que la salle"),
  "<p>" + t("When a booking stayed in the file after a meeting ended, the next person who needed the room, later that day or the next, had to find whoever booked it and ask whether it was still in use. If that person was busy, in another meeting or away, the answer came late or not at all. Meetings started late, people lost time, and everyone got frustrated with a file that couldn't be trusted.",
            "Quand une réservation restait dans le fichier après la réunion, la personne suivante, plus tard dans la journée ou le lendemain, devait retrouver celle qui avait réservé et lui demander si la salle était encore utilisée. Si cette personne était occupée, en réunion ou absente, la réponse arrivait tard ou jamais. Les réunions commençaient en retard, on perdait du temps, et tout le monde se méfiait d'un fichier peu fiable.") + "</p>")
rooms += sec("how", t("What I built","Ce que j'ai construit"), t("One day in the life of a booking","La journée type d'une réservation"),
  '<ol class="steps clock" style="--n:4">' + "".join(f'<li><span class="when">{w}</span><b>{b}</b><span>{s}</span></li>' for w, b, s in [
    (t("Every morning","Chaque matin"), t("Fresh start","Repartir à zéro"), t("Yesterday's leftover bookings are cleared and conflicts are fixed, so the file opens clean","Les réservations restantes de la veille sont supprimées et les conflits corrigés : le fichier démarre propre")),
    (t("Any time","À tout moment"), t("Book as usual","Réserver comme avant"), t("People keep booking in the same Excel file; nothing new to learn","On continue à réserver dans le même fichier Excel ; rien de nouveau à apprendre")),
    (t("Before the meeting","Avant la réunion"), t("Reminder","Rappel"), t("A Slack message reminds the person their meeting and room are coming up","Un message Slack rappelle à la personne que sa réunion et sa salle approchent")),
    (t("When it ends","À la fin"), t("Keep or release","Garder ou libérer"), t("A Slack ping asks whether to keep the booking or free the room","Un message Slack demande s'il faut garder la réservation ou libérer la salle"))]) + "</ol>")
rooms += sec("rules", t("The rules","Les règles"), t("Clean every day, without breaking what should stay","Nettoyer chaque jour, sans casser ce qui doit rester"),
  vl([(t("Daily reset","Remise à zéro"), t("Each morning the automation removes bookings that no longer apply, so the day starts from what is really planned.","Chaque matin, l'automatisation retire les réservations qui ne sont plus valables : la journée part de ce qui est vraiment prévu.")),
      (t("Protected meetings","Réunions protégées"), t("Rules keep specific recurring meetings in place, so standing meetings never disappear in the cleanup.","Des règles conservent certaines réunions récurrentes : les réunions fixes ne disparaissent jamais au nettoyage.")),
      (t("Conflicts","Conflits"), t("Overlapping bookings for the same room are detected and resolved before anyone walks into a double-booked room.","Les réservations qui se chevauchent sur une même salle sont détectées et résolues avant que quiconque tombe sur une salle réservée deux fois.")),
      (t("Where people are","Là où sont les gens"), t("Reminders and pings go to the company Slack, where the team already works, so they get seen.","Rappels et messages arrivent sur le Slack de l'entreprise, là où l'équipe travaille déjà : ils sont vus."))]))
rooms += sec("result", t("Result","Résultat"), t("A booking file people can trust","Un fichier de réservation fiable"),
  "<p>" + t("A room marked as taken is now actually taken. Nobody has to track down a colleague to ask whether they are still using a room, and the shared file stays the single place to book, as before. The change was entirely behind the scenes.",
            "Une salle marquée comme prise est désormais vraiment prise. Plus besoin de courir après un collègue pour savoir s'il utilise encore une salle, et le fichier partagé reste le seul endroit où réserver, comme avant. Tout le changement s'est fait en coulisses.") + "</p>"
  + chips([(t("Automation","Automatisation"), ["Python",t("Scheduled jobs","Tâches planifiées"),t("Rule-based cleanup","Nettoyage par règles")]), (t("Integrations","Intégrations"), [t("Excel (shared file)","Excel (fichier partagé)"),"Slack"])]))
rooms += cs_cta()

for slug, te, tf, d, b in [
  ("practitioner-database","Practitioner Database · Case Study","Base de praticiens · Étude de cas","Scraping, cleaning and loading Tunisian practitioner listings into a health-tech startup's MySQL database.",health),
  ("textile-stock-attendance","Textile Stock & Attendance · Case Study","Stock textile & présence · Étude de cas","A fabric inventory app with low-stock alerts and automatic ZKTeco attendance reports for a textile wholesaler.",tex),
  ("meeting-rooms","Meeting Room Cleanup · Case Study","Salles de réunion · Étude de cas","Daily cleanup of forgotten meeting-room bookings plus Slack reminders at a 40-person software company.",rooms)]:
    open(f"site/work/{slug}.html","w").write(page(te, tf, d, b, root="../"))
print("work ok")
