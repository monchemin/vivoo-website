"""Pages institutionnelles au style de la refonte : contact, FAQ, cas clients,
partenaires, blog et pages légales.

Les textes légaux sont repris tels quels depuis pages.json (champ "body").
"""
import json, os
from build_common import *

HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, "pages.json"), encoding="utf-8"))
# Pages d'acquisition Vivoo branchées sur les formulaires du site (gérées hors de Vivoo).
CONTACT_SLUG = "urfuZx"
PARTNER_SLUG = "aPZjVK"

COUNTRIES = [("CA", "Canada (+1)"), ("US", "États-Unis (+1)"), ("FR", "France (+33)"), ("BE", "Belgique (+32)"),
             ("CH", "Suisse (+41)"), ("CI", "Côte d'Ivoire (+225)"), ("SN", "Sénégal (+221)"), ("CM", "Cameroun (+237)"),
             ("BJ", "Bénin (+229)"), ("TG", "Togo (+228)"), ("GA", "Gabon (+241)"), ("CD", "RD Congo (+243)"),
             ("MA", "Maroc (+212)"), ("TN", "Tunisie (+216)")]


def vivoo_form(slug, subject, message_label, message_hint, submit, done_title, done_text):
    """Formulaire envoyé à la page d'acquisition Vivoo <slug> (voir assets/js/vivoo-form.js).
    subject : liste de choix [(valeur, libellé)] ou texte fixe envoyé en champ caché."""
    if isinstance(subject, str):
        subject_html = f'<input type="hidden" name="subject" value="{subject}">'
    else:
        opts = "".join(f'<option value="{v}">{l}</option>' for v, l in subject)
        subject_html = f"""<div><label for="{slug}-subject">Sujet</label>
        <select id="{slug}-subject" name="subject">{opts}</select></div>"""
    countries = "".join(f'<option value="{c}">{l}</option>' for c, l in COUNTRIES)
    return f"""<div class="vv-form-box">
      <form class="contact-form vv-form" data-vivoo-form="{slug}" novalidate>
        <p class="vv-form-note">Les champs marqués d'un <span aria-hidden="true">*</span><span class="sr-only">astérisque</span> sont obligatoires.</p>
        <div class="form-row">
          <div><label for="{slug}-name">Prénom <span aria-hidden="true">*</span></label>
          <input id="{slug}-name" name="name" type="text" autocomplete="given-name" required></div>
          <div><label for="{slug}-lastName">Nom <span aria-hidden="true">*</span></label>
          <input id="{slug}-lastName" name="lastName" type="text" autocomplete="family-name" required></div>
        </div>
        <div><label for="{slug}-email">Courriel <span aria-hidden="true">*</span></label>
        <input id="{slug}-email" name="email" type="email" autocomplete="email" required></div>
        <div class="vv-tel">
          <div><label for="{slug}-country">Pays</label>
          <select id="{slug}-country" name="countryCode" autocomplete="country">{countries}</select></div>
          <div><label for="{slug}-tel">Téléphone <span aria-hidden="true">*</span></label>
          <input id="{slug}-tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" placeholder="418 555 0123" aria-describedby="{slug}-tel-hint" required>
          <small id="{slug}-tel-hint" class="vv-hint">Sans indicatif, le pays choisi est utilisé.</small></div>
        </div>
        <fieldset class="vv-wa" data-wa-question hidden>
          <legend>Ce numéro est-il sur WhatsApp ?</legend>
          <label><input type="radio" name="whatsappEnabled" value="oui"> Oui</label>
          <label><input type="radio" name="whatsappEnabled" value="non"> Non</label>
        </fieldset>
        {subject_html}
        <div><label for="{slug}-message">{message_label} <span aria-hidden="true">*</span></label>
        <textarea id="{slug}-message" name="message" rows="5" placeholder="{message_hint}" required></textarea></div>
        <div class="vv-trap" aria-hidden="true"><label for="{slug}-website">Site web</label>
        <input id="{slug}-website" name="website" type="text" tabindex="-1" autocomplete="off"></div>
        <div class="form-checkbox">
          <input id="{slug}-consent" name="consent" type="checkbox">
          <label for="{slug}-consent">J'accepte de recevoir les communications de Vivoo. Je peux me désabonner à tout moment. <a href="/privacy/">Politique de confidentialité</a></label>
        </div>
        <p class="vv-form-error" data-form-status role="alert" tabindex="-1" hidden></p>
        <button class="btn btn-primary" type="submit">{submit}</button>
      </form>
      <div class="vv-form-done" data-form-done tabindex="-1" hidden>
        <h3>Merci <span data-done-name></span> !</h3>
        <p><strong>{done_title}</strong></p>
        <p>{done_text}</p>
      </div>
    </div>
    <script src="/assets/js/vivoo-form.js" defer></script>"""


def hero(label, h1, lead="", dark=False, extra=""):
    return f"""<section class="sy-page-hero{' sy-page-hero--dark' if dark else ''}">
  <div class="sy-wrap">
    {index_label("", label)}
    <h1 class="sy-display">{h1}</h1>
    {f'<p class="sy-lead">{lead}</p>' if lead else ''}
    {extra}
  </div>
</section>
"""


# ---------------------------------------------------------------- Contact

def build_contact():
    d = P["contact"]
    body = hero("Contact", "Parlons de votre prochaine étape.",
                "Une question sur Vivoo, une démonstration, ou un intérêt pour le programme de partenariat : écrivez-nous, l'équipe vous répond directement.") + f"""
<section class="sy-section" id="formulaire">
  <div class="sy-wrap sy-split vv-form-split">
    <div>
      {index_label("", "Écrire")}
      <h2 class="sy-h2">Écrivez-nous.</h2>
      <p class="sy-lead">Décrivez votre activité et ce que vous cherchez : l'équipe Vivoo vous répond rapidement, par courriel ou par téléphone.</p>
      <ul class="vv-alt-links">
        <li><a href="{DEMO}" {EXT}><strong>Parler à un spécialiste</strong> Réservez un moment pour voir Vivoo en action →</a></li>
        <li><a href="{SIGNUP}" {EXT}><strong>Créer mon compte</strong> Commencez tout de suite et activez vos premiers modules →</a></li>
      </ul>
    </div>
    {vivoo_form(CONTACT_SLUG,
                [("Question sur Vivoo", "Une question sur Vivoo"), ("Démonstration", "Une démonstration"),
                 ("Tarifs", "Les tarifs"), ("Partenariat", "Le programme de partenariat"),
                 ("Support", "Le support d'un compte existant"), ("Autre", "Autre chose")],
                "Votre message", "Votre activité, vos objectifs, vos questions…", "Envoyer mon message",
                "Votre message est bien parvenu à l'équipe Vivoo.", "Nous vous répondons rapidement, par courriel ou par téléphone.")}
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap sy-split">
    <div>
      {index_label("", "Coordonnées")}
      <h2 class="sy-h2">Vivoo, une plateforme de Technologies Ilema.</h2>
    </div>
    <div class="sy-contact">
      <p><strong>Adresse</strong><br>2323 rue Galvani, Suite 130<br>Québec (Québec) G1N 4H7</p>
      <p><strong>Courriel</strong><br><a href="mailto:contact@vivoo.pro">contact@vivoo.pro</a></p>
      <p><strong>Éditeur</strong><br>Technologies Ilema Inc. · <a href="https://ilematec.com" {EXT}>ilematec.com</a> · <a href="https://www.facebook.com/ilematec/" {EXT}>Facebook Ilema</a></p>
      {d['social']}
    </div>
  </div>
</section>
{cta("Vous préférez voir Vivoo en action ?", "Un spécialiste vous montre comment Vivoo relie vos canaux, vos rendez-vous, vos ventes et vos clients.", "Construisons votre système commercial.")}"""
    page("/contact/", d["title"], d["desc"], "", body, trail=[("Accueil", "/"), ("Contact", None)], extra_ld=d["jsonld"])


# ---------------------------------------------------------------- FAQ

FAQ = [
    ("Général", [
        ("Qu'est-ce que Vivoo ?", "Vivoo est un système commercial qui relie l'acquisition, la conversation, la conversion, la vente et la fidélisation. Il réunit WhatsApp, Instagram, Messenger, SMS et courriel pour transformer vos prospects, vos conversations et vos clients en un parcours qui travaille pour vous."),
        ("Vivoo remplace-t-il mon système de gestion actuel ?", "Non. Vivoo ne remplace pas vos outils de gestion (facturation, inventaire, ERP). Il vient s'y ajouter comme la couche qui gère la relation avec vos clients. Vos outils de gestion structurent vos opérations ; Vivoo fait vivre la relation."),
        ("Ai-je besoin de compétences techniques pour utiliser Vivoo ?", "Non. La plateforme est pensée pour être utilisée sans connaissance en programmation, que ce soit par une équipe seule ou par un réseau de marchands."),
    ]),
    ("Fonctionnement", [
        ("Quels canaux Vivoo prend-il en charge ?", "Vivoo réunit cinq canaux dans une seule plateforme : WhatsApp, Messenger, Instagram, SMS et courriel. Chaque profil client reste unifié peu importe le canal utilisé pour vous contacter."),
        ("Les modules de Vivoo fonctionnent-ils ensemble ou séparément ?", "Ensemble. Une publicité, une page de capture, une automatisation et un rendez-vous peuvent s'enchaîner dans un même parcours. Voir des exemples concrets sur la page Scénarios."),
    ]),
    ("Agent IA et intégrations", [
        ("Qu'est-ce que l'Agent IA de Vivoo ?", "Un agent qui répond à vos clients sur WhatsApp, Messenger et Instagram, de jour comme de nuit. Il connaît votre entreprise, présente vos offres, propose vos disponibilités et réserve le rendez-vous sans quitter la conversation."),
        ("Puis-je reprendre une conversation menée par l'Agent IA ?", "Oui, à tout moment. L'agent ne répond jamais dans une conversation prise en charge par une personne de votre équipe, et vous pouvez la lui rendre ensuite."),
        ("Mes clients peuvent-ils réserver sans quitter la conversation ?", "Oui. Sur WhatsApp, Messenger et Instagram, l'Agent IA propose les créneaux disponibles de votre calendrier, le client choisit et reçoit sa confirmation et ses rappels."),
        ("Vivoo peut-il envoyer ses données à mes autres outils ?", "Oui. Nouveaux leads, rendez-vous, messages et commentaires reçus : Vivoo les envoie à votre CRM, à Zapier, à Make ou à n8n, et reçoit vos leads, vos clients et vos commandes. Voir la page Intégrations."),
        ("Puis-je connecter Claude ou ChatGPT à Vivoo ?", "Oui. Votre assistant IA se connecte à votre compte Vivoo et y agit avec vos droits : il retrouve un client, ajoute une note, crée une tâche, étiquette un contact ou prend un rendez-vous. Voir la page Intégration IA."),
    ]),
    ("Partenariat", [
        ("Comment fonctionne le modèle de partenariat Vivoo ?", "Vivoo fonctionne selon un modèle à trois niveaux : Vivoo opère la plateforme, un réseau de partenaires déploie Vivoo auprès de son portefeuille de marchands, et chaque marchand l'utilise pour engager sa propre clientèle."),
    ]),
    ("Tarification", [
        ("Combien coûte Vivoo ?", "Vivoo repose sur deux choix : une offre de modules (Alma, Zagor ou Libre) et des crédits d'utilisation des canaux (crédits, plan de crédits ou abonnement). Le tarif dépend de votre offre et de votre volume d'envois. Contactez-nous pour une proposition adaptée."),
        ("Comment fonctionnent les crédits d'utilisation ?", "Chaque envoi sur un canal (WhatsApp, SMS, courriel, Instagram, Messenger) et chaque recherche de prospection consomme des crédits. Vous pouvez les acheter au besoin, prévoir un plan de crédits ou choisir un abonnement qui les renouvelle chaque mois."),
    ]),
]


def build_faq():
    d = P["faq"]
    blocks = ""
    for i, (cat, qs) in enumerate(FAQ, 1):
        items = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in qs)
        blocks += f"""<div class="sy-faq-group sy-reveal">
  <div>{index_label(f"{i:02d}", cat)}</div>
  <div>{items}</div>
</div>"""
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for _, qs in FAQ for q, a in qs]}
    body = hero("FAQ", "Questions fréquentes.",
                "Fonctionnement, canaux, partenariat, offres et crédits : les réponses aux questions que l'on nous pose le plus souvent.") + f"""
<section class="sy-section">
  <div class="sy-wrap">{blocks}</div>
</section>
<section class="sy-section--tight sy-alt">
  <div class="sy-wrap">
    <div class="sy-cards sy-cards--3">
      <a class="sy-card" href="/tarifs/"><span class="sy-card-num">Tarifs</span><h3>Offres et crédits</h3><p>Alma, Zagor ou Libre, et trois façons d'utiliser vos crédits.</p><span class="sy-card-more">Voir les tarifs →</span></a>
      <a class="sy-card" href="/comment-ca-marche/"><span class="sy-card-num">Démarrer</span><h3>Comment ça marche</h3><p>Cinq étapes pour lancer votre système.</p><span class="sy-card-more">Comment ça marche →</span></a>
      <a class="sy-card" href="/scenarios/"><span class="sy-card-num">Scénarios</span><h3>Exemples concrets</h3><p>Six parcours, de la publicité au client fidèle.</p><span class="sy-card-more">Voir les scénarios →</span></a>
    </div>
  </div>
</section>
{cta("Une question qui ne trouve pas réponse ici ?", "Écrivez-nous : l'équipe Vivoo vous répond directement.", "Construisons votre système commercial.")}"""
    page("/faq/", d["title"], d["desc"], "", body, trail=[("Accueil", "/"), ("FAQ", None)], extra_ld=[ld])


# ---------------------------------------------------------------- Cas clients

CASES = [
    ("MakoFoods", "Restaurant et épicerie · Longueuil", "restaurants",
     ["Entre le service en salle et les allées d'épicerie, MakoFoods gère deux flux de clientèle qui n'ont pas les mêmes habitudes d'achat, mais qui méritent tous deux d'être reconnus au retour.",
      "Une page de capture affichée en caisse et sur les tables permet à chaque client de rejoindre l'audience MakoFoods en quelques secondes. Le programme de fidélisation prend ensuite le relais : chaque achat, qu'il vienne du côté restaurant ou épicerie, nourrit le même profil client. Les campagnes ciblées viennent ensuite réactiver les clients moins fréquents, avec des offres qui parlent au bon moment."],
     ["Page de capture", "Fidélisation", "Campagnes"], ["Code QR", "Profil client", "Fidélité", "Campagne", "Retour"]),
    ("Kinaya Massothérapeute", "Massothérapie · Gatineau", "therapeutes",
     ["Pour une pratique de massothérapie, chaque minute passée sur la gestion des rendez-vous est une minute qui n'est pas consacrée aux clients. Kinaya utilise Vivoo pour simplifier les deux bouts de la relation client : l'arrivée de nouveaux clients et la gestion de leur agenda.",
      "Une page de capture accueille les nouveaux clients dès leur premier contact, tandis que le calendrier intégré permet une prise de rendez-vous autonome, sans allers-retours par téléphone ou message. Le résultat : moins d'administration, plus de temps pour la pratique elle-même."],
     ["Calendrier", "Page de capture"], ["Page de capture", "Nouveau client", "Rendez-vous", "Consultation"]),
    ("Twish Cart", "Épicerie en gros · Ottawa", "commerce",
     ["La vente en gros repose sur des cycles d'achat réguliers et des relations clients qui durent dans le temps. Twish Cart s'appuie sur Vivoo pour structurer l'ensemble de ce parcours, de la première prise de contact jusqu'à la fidélité à long terme.",
      "La page de capture recrute de nouveaux comptes clients, le module de rendez-vous organise les suivis et livraisons, la fidélisation récompense le volume d'achats récurrent, et les campagnes assurent que chaque promotion ou nouvel arrivage rejoint les bons clients au bon moment."],
     ["Campagnes", "Page de capture", "Rendez-vous", "Fidélisation"], ["Capture", "Compte client", "Suivi", "Livraison", "Fidélité", "Nouvel arrivage"]),
]


def build_cases():
    d = P["cas-clients"]
    blocks = ""
    for i, (name, where, sector, paras_, tags, fl) in enumerate(CASES, 1):
        blocks += f"""<article class="sy-scenario sy-reveal">
  <div>
    {index_label(f"{i:02d}", where)}
    <h2>{name}</h2>
    {"".join(f'<p class="sy-lead">{p}</p>' for p in paras_)}
    {chips(tags)}
  </div>
  <div>
    <p class="sy-index">Le parcours</p>
    {flow(fl, "sy-vflow")}
    <a class="sy-link" href="/solutions/{sector}/">Voir la solution pour ce secteur →</a>
  </div>
</article>"""
    body = hero("Cas clients", "Trois commerces, trois réalités, un même besoin.",
                "Arrêter de gérer la relation client de mémoire, et commencer à la faire fonctionner comme un système. Voici comment Vivoo s'intègre concrètement sur le terrain.", dark=True) + f"""
<section class="sy-section">
  <div class="sy-wrap">{blocks}</div>
</section>
{cta("Votre commerce a sa propre réalité. Vivoo s'y adapte.", "Discutons de vos canaux, de votre clientèle et des modules qui feraient la plus grande différence pour vous.", "Construisons votre système commercial.")}"""
    page("/cas-clients/", d["title"], d["desc"], "", body, trail=[("Accueil", "/"), ("Cas clients", None)], extra_ld=d["jsonld"])


# ---------------------------------------------------------------- Partenaires

def build_partners():
    d = P["partenaires"]
    why = [
        ("Un revenu récurrent", "Chaque marchand actif représente une offre de modules et une consommation de crédits renouvelée mois après mois."),
        ("Une autonomie commerciale réelle", "Vous fixez vos propres conditions avec vos marchands, sur votre marché, selon votre connaissance du terrain."),
        ("Un accompagnement continu", "Formation, support technique et évolution constante de la plateforme, pour que votre offre reste compétitive sans effort de développement de votre côté."),
        ("Un marché en croissance", "Les praticiens du bien-être, les courtiers immobiliers et les conseillers financiers cherchent activement à moderniser leur relation client. Un terrain fertile pour votre portefeuille."),
    ]
    body = hero("Partenaires", "Devenez partenaire Vivoo.",
                "Vivoo ne vend pas directement à chaque commerce. Nous travaillons avec des partenaires qui déploient la plateforme auprès de leur propre réseau de marchands. Vous gardez la relation commerciale, nous fournissons la technologie, l'infrastructure et l'accompagnement.",
                extra='<div class="sy-actions"><a class="btn btn-primary" href="#devenir-partenaire">Devenir partenaire</a></div>') + f"""
<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "Le modèle")}<h2 class="sy-h2">Trois niveaux, des rôles clairs.</h2></div>
      <p class="sy-lead">Ce modèle vous laisse l'autonomie commerciale complète sur votre marché, pendant que nous assurons la fiabilité de la plateforme derrière vous.</p>
    </div>
    <ol class="sy-steps sy-steps--3">
      <li><span class="sy-step-num">01</span><h3>Vivoo</h3><p>Développe et opère la plateforme : les canaux, l'Agent IA, les campagnes, les scénarios de fidélisation, les intégrations avec les outils de vos marchands. C'est notre responsabilité, en continu.</p></li>
      <li><span class="sy-step-num">02</span><h3>Le partenaire</h3><p>C'est vous. Vous recrutez et accompagnez votre portefeuille de marchands, vous définissez vos conditions commerciales et vous êtes leur interlocuteur au quotidien.</p></li>
      <li><span class="sy-step-num">03</span><h3>Le marchand</h3><p>Utilise Vivoo pour engager sa propre clientèle : capter une audience, lancer des campagnes, faire vivre un programme de fidélisation, sans gérer directement la relation avec Vivoo.</p></li>
    </ol>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("02", "Votre rôle")}<h2 class="sy-h2">La relation avec vos marchands reste la vôtre.</h2></div>
    <div>
      <p class="sy-lead">Vous êtes l'interlocuteur unique de vos marchands : accueil, formation, support de premier niveau et facturation selon vos propres tarifs. Vivoo vous fournit un modèle de crédits transparent pour approvisionner vos marchands, ainsi que le support technique nécessaire pour que votre réseau reste opérationnel.</p>
      <p class="sy-lead">Vous n'avez pas à sous-traiter cette relation. Notre rôle est de vous donner les outils pour bien la servir.</p>
    </div>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("03", "Pourquoi devenir partenaire")}<h2 class="sy-h2">Un partenariat qui travaille pour vous.</h2></div>
    </div>
    <ol class="sy-steps sy-steps--4">
      {"".join(f'<li><span class="sy-step-num">{i:02d}</span><h3>{t}</h3><p>{p}</p></li>' for i, (t, p) in enumerate(why, 1))}
    </ol>
  </div>
</section>

<section class="sy-section sy-reveal" id="devenir-partenaire">
  <div class="sy-wrap sy-split vv-form-split">
    <div>
      {index_label("04", "Candidature")}
      <h2 class="sy-h2">Parlons de votre réseau.</h2>
      <p class="sy-lead">Dites-nous qui vous êtes, sur quel marché vous travaillez et quels marchands vous accompagnez. L'équipe Vivoo revient vers vous pour en discuter.</p>
    </div>
    {vivoo_form(PARTNER_SLUG, "Devenir partenaire",
                "Votre réseau et votre marché", "Votre entreprise, votre pays ou région, le type et le nombre de marchands que vous accompagnez…",
                "Envoyer ma candidature",
                "Votre candidature est bien parvenue à l'équipe Vivoo.", "Nous vous contactons pour discuter de votre marché et d'un partenariat.")}
  </div>
</section>

<section class="sy-cta">
  <div class="sy-wrap">
    <h2>Prêt à élargir votre offre avec Vivoo ?</h2>
    <p>Discutons de votre marché et de la façon dont un partenariat Vivoo peut s'y intégrer.</p>
    <div class="sy-actions">
      <a class="btn sy-btn-light" href="#devenir-partenaire">Devenir partenaire</a>
      <a class="btn sy-btn-ghost" href="/contact/">Nous contacter</a>
    </div>
    <div class="sy-cta-sign">Une plateforme, un réseau.</div>
  </div>
</section>
"""
    page("/partenaires/", d["title"], d["desc"], "apropos", body, trail=[("Accueil", "/"), ("Partenaires", None)], extra_ld=d["jsonld"])


# ---------------------------------------------------------------- Intégrations

INTEGRATION_EVENTS = [
    ("Nouveau lead", "Un contact est créé dans Vivoo, avec la page d'où il vient quand il arrive d'une page."),
    ("Lead devenu client", "Le contact passe à l'achat."),
    ("Contact modifié", "Ses informations changent, ou il remplit de nouveau une de vos pages."),
    ("Rendez-vous pris", "Une réservation arrive, en ligne ou dans une conversation."),
    ("Rendez-vous modifié", "Il est déplacé, annulé, confirmé ou effectué."),
    ("Messages reçus", "Un client vous écrit sur WhatsApp, Messenger ou Instagram, canal par canal."),
    ("Commentaires reçus", "Quelqu'un commente une publication de votre page Facebook ou de votre compte Instagram."),
]
INTEGRATION_FAQ = [
    ("Faut-il un développeur ?", "Non pour Zapier, Make ou n8n : vous collez l'adresse qu'ils vous donnent et vous cochez les événements. Un développeur n'est utile que pour brancher votre propre application."),
    ("Les messages de mes clients sont-ils transmis à mes outils ?", "Seulement si vous le décidez : les messages et les commentaires sont des événements à cocher, canal par canal."),
    ("Comment mon outil sait-il que l'envoi vient bien de Vivoo ?", "Chaque envoi est signé avec un secret que vous seul connaissez. Votre outil vérifie la signature avant de traiter l'événement."),
]


def build_integrations():
    events = "".join(f"<li><h3>{n}</h3><p>{d}</p><span></span></li>" for n, d in INTEGRATION_EVENTS)
    tech = [
        "Chaque événement est envoyé en POST, au format JSON : identifiant, type, version, date, compte et données.",
        "Chaque envoi est signé avec votre secret (en-tête Vivoo-Signature, HMAC SHA-256 avec horodatage).",
        "L'identifiant de l'événement permet d'ignorer un envoi reçu deux fois.",
        "En cas d'échec, Vivoo réessaie à intervalles croissants pendant plus d'une journée, et vous prévient si l'adresse ne répond plus pendant plusieurs jours.",
        "Un journal des envois et un bouton de test sont disponibles dans vos réglages, jusqu'à trois adresses par compte.",
    ]
    faq = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in INTEGRATION_FAQ)
    ld = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in INTEGRATION_FAQ]}]
    body = hero("Intégrations", "Vivoo s'intègre à vos outils.",
                "Votre CRM, votre tableur, Zapier, Make ou n8n : Vivoo leur transmet ce qui se passe dans votre système commercial, et reçoit ce qu'ils savent de vos clients. Vos outils restent à jour, sans double saisie.") + f"""
<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "Vivoo informe vos outils")}<h2 class="sy-h2">Chaque événement, au moment où il se produit.</h2></div>
      <p class="sy-lead">Vous choisissez les événements à recevoir et l'adresse où les envoyer. Les messages et les commentaires ne sont transmis que si vous les cochez.</p>
    </div>
    <ul class="sy-items">{events}</ul>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("02", "Vos outils alimentent Vivoo")}<h2 class="sy-h2">Ce que vos outils savent, Vivoo le sait aussi.</h2></div>
    <div>
      <p class="sy-lead"><strong>Votre boutique en ligne.</strong> Shopify, WooCommerce, Square ou Clover : vos ventes s'ajoutent au profil de chaque client.</p>
      <p class="sy-lead"><strong>Vos formulaires et vos applications.</strong> L'API de Vivoo reçoit vos nouveaux leads, vos clients et vos commandes, qui entrent aussitôt dans vos campagnes et vos scénarios d'engagement.</p>
    </div>
  </div>
</section>

<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("03", "Pour votre équipe technique")}<h2 class="sy-h2">Des envois signés, fiables et vérifiables.</h2></div>
    <ul class="sy-checks">{"".join(f"<li>{t}</li>" for t in tech)}</ul>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-narrow">
    {index_label("04", "Questions fréquentes")}
    {faq}
  </div>
</section>
{cta("Vos outils et Vivoo, enfin à jour en même temps.", "Créez votre compte et branchez vos outils, ou parlez à un spécialiste pour relier Vivoo à votre façon de travailler.")}"""
    page("/integrations/", "Intégrations : CRM, Zapier, Make, Shopify. Vivoo",
         "Vivoo envoie ses événements (nouveaux leads, rendez-vous, messages et commentaires reçus) à votre CRM, à Zapier, à Make ou à n8n, et reçoit vos leads, vos clients et vos commandes.",
         "integrations", body, trail=[("Accueil", "/"), ("Intégrations", None)], extra_ld=ld)


# ---------------------------------------------------------------- Intégration IA

AI_BASE = [
    ("Les mêmes actions", "Une note, une tâche, une étiquette ou un rendez-vous créé par une IA est identique à celui créé par votre équipe : mêmes vérifications, mêmes effets."),
    ("Les mêmes règles", "Un rendez-vous pris par une IA suit le même parcours qu'une réservation en ligne : créneaux proposés seulement, confirmation et rappels au client, acompte demandé quand la prestation en prévoit un."),
    ("Les mêmes droits", "Une IA ne voit et ne touche que ce qui lui est permis : vos modules actifs, votre rôle, votre portefeuille de contacts."),
    ("Un seul journal", "Chaque action d'une IA est enregistrée, réussie ou refusée : qui, quoi, sur quel contact, quand."),
]
AI_ASSISTANT = [
    ("Retrouver et comprendre un client", "« Qui sont mes leads de la semaine ? », « Résume-moi l'historique de ce client » : contacts, messages, notes, rendez-vous, factures."),
    ("Noter et relancer", "Il ajoute une note au dossier, crée une tâche de suivi, clôt une tâche faite."),
    ("Gérer les rendez-vous", "Il cherche un créneau libre, réserve pour un client, déplace ou annule un rendez-vous. Le client reçoit sa confirmation comme s'il avait réservé lui-même."),
    ("Étiqueter vos contacts", "Il pose ou retire une de vos étiquettes ; vos séquences liées à l'étiquette se déclenchent comme d'habitude."),
    ("Répartir le travail", "Il assigne un contact à un membre de votre équipe."),
    ("Brancher une page de votre site", "Il prépare tout ce qu'il faut pour qu'une page de votre site inscrive à un événement ou envoie un formulaire dans Vivoo."),
]
AI_CONNECT = [
    ("Copier l'adresse", "Elle est affichée dans la page « Assistant IA » de votre compte Vivoo."),
    ("Ajouter le connecteur", "Collez-la dans les connecteurs de votre assistant."),
    ("Autoriser l'accès", "Vivoo vous demande de confirmer le compte et les droits accordés."),
    ("Demander", "Posez votre première question à votre assistant."),
]
AI_AGENT = [
    ("Il répond tout de suite", "Sur WhatsApp, Messenger et Instagram, avec ce que vous lui avez appris de votre entreprise."),
    ("Il réserve dans la conversation", "Il propose vos créneaux, le client choisit, le rendez-vous est confirmé dans votre agenda avec ses rappels."),
    ("Il garde trace", "Il note ce qu'il apprend sur le client et crée une tâche pour votre équipe quand une personne doit intervenir."),
    ("Vous gardez la main", "Votre équipe reprend la conversation quand elle le souhaite."),
]
AI_CONTROL = [
    "Connexion sécurisée (OAuth) : votre assistant n'a jamais votre mot de passe.",
    "Vos droits, rien de plus : un membre au rôle utilisateur ne donne accès qu'à ses contacts.",
    "Les actions qui modifient vos données sont signalées à votre assistant, qui vous demande votre accord avant de les faire.",
    "Aucune action en masse : un contact à la fois.",
    "Pas d'envoi de messages ni de campagnes par votre assistant.",
    "Chaque assistant connecté apparaît dans vos sessions et se déconnecte en un clic ; une connexion inutilisée pendant 30 jours se ferme d'elle-même.",
]
AI_FAQ = [
    ("Quels assistants puis-je connecter ?", "Claude, ChatGPT et tout assistant compatible avec le protocole MCP (Model Context Protocol). Vous collez l'adresse de votre compte Vivoo dans ses connecteurs, puis vous autorisez l'accès."),
    ("Quelle différence entre mon assistant IA et l'Agent IA ?", "Votre assistant exécute ce que vous lui demandez, quand vous le lui demandez. L'Agent IA agit seul, dans les conversations avec vos clients. Les deux passent par les mêmes actions et les mêmes règles."),
    ("Mon assistant voit-il tous mes contacts ?", "Il voit ce que vous voyez : les mêmes modules, le même rôle, le même portefeuille de contacts."),
    ("Mon assistant peut-il écrire à mes clients ?", "Non. Il consulte, note, relance, étiquette, assigne et gère les rendez-vous. Les messages restent envoyés par votre équipe, vos campagnes, vos scénarios ou l'Agent IA."),
    ("Faut-il un abonnement de plus ?", "Non. La connexion d'un assistant fait partie de Vivoo, pour tous les comptes. Les actions proposées dépendent des modules que vous avez activés."),
]


def build_ai_integration():
    def items(rows):
        return "".join(f"<li><h3>{n}</h3><p>{d}</p><span></span></li>" for n, d in rows)
    faq = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in AI_FAQ)
    ld = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in AI_FAQ]}]
    body = hero("Intégration IA", "Vos IA travaillent dans Vivoo, avec les mêmes règles que votre équipe.",
                "Votre assistant IA exécute ce que vous lui demandez. L'Agent IA agit seul dans vos conversations. Les deux passent par la même base : les mêmes actions, les mêmes règles et le même journal que votre équipe dans Vivoo.") + f"""
<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "La couche de base")}<h2 class="sy-h2">Une seule base pour toutes vos IA.</h2></div>
      <p class="sy-lead">Qu'une action vienne de votre équipe, de votre assistant ou de l'Agent IA, Vivoo l'exécute de la même façon.</p>
    </div>
    <ul class="sy-items">{items(AI_BASE)}</ul>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head">
      <div>{index_label("02", "Deux façons de faire travailler l'IA")}<h2 class="sy-h2">Vous dirigez, ou elle agit seule.</h2></div>
    </div>
    <div class="sy-cards">
      <a class="sy-card" href="#assistant"><span class="sy-card-num">Actions dirigées</span><h3>Votre assistant IA</h3><p>Vous connectez Claude, ChatGPT ou un autre assistant compatible à votre compte Vivoo. Vous lui demandez, il exécute, avec vos droits.</p><span class="sy-card-more">Voir ce qu'il fait →</span></a>
      <a class="sy-card" href="#agent"><span class="sy-card-num">Actions automatiques</span><h3>L'Agent IA</h3><p>Il répond à vos clients sur WhatsApp, Messenger et Instagram, de jour comme de nuit, présente vos offres et réserve le rendez-vous dans la conversation, sans que vous ayez à intervenir.</p><span class="sy-card-more">Voir ce qu'il fait →</span></a>
    </div>
  </div>
</section>

<section class="sy-section sy-reveal" id="assistant">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("03", "Votre assistant IA")}<h2 class="sy-h2">Demandez, votre assistant le fait dans Vivoo.</h2></div>
      <p class="sy-lead">Votre assistant se connecte à votre compte par le protocole MCP et agit pour vous, sur vos contacts, vos tâches et vos rendez-vous.</p>
    </div>
    <ul class="sy-items">{items(AI_ASSISTANT)}</ul>
    <ol class="sy-steps sy-steps--4" style="margin-top:3rem">
      {"".join(f'<li><span class="sy-step-num">{i:02d}</span><h3>{t}</h3><p>{p}</p></li>' for i, (t, p) in enumerate(AI_CONNECT, 1))}
    </ol>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal" id="agent">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("04", "L'Agent IA")}<h2 class="sy-h2">Il agit seul, dans vos conversations.</h2></div>
      <p class="sy-lead">Pendant que vous travaillez, l'Agent IA répond, qualifie et réserve, avec les mêmes règles que votre équipe.</p>
    </div>
    <ul class="sy-items">{items(AI_AGENT)}</ul>
    <div class="sy-actions" style="margin-top:2rem"><a class="btn btn-secondary" href="/produit/agent-ia/">Découvrir l'Agent IA</a></div>
  </div>
</section>

<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("05", "Vous gardez le contrôle")}<h2 class="sy-h2">Vos données restent sous votre autorité.</h2></div>
    <ul class="sy-checks">{"".join(f"<li>{t}</li>" for t in AI_CONTROL)}</ul>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-narrow">
    {index_label("06", "Questions fréquentes")}
    {faq}
  </div>
</section>
{cta("Faites travailler vos IA dans votre système commercial.", "Créez votre compte et connectez votre assistant, ou parlez à un spécialiste pour voir ce que l'IA peut faire dans votre parcours.")}"""
    page("/integration-ia/", "Intégration IA : Claude, ChatGPT et Agent IA. Vivoo",
         "Connectez Claude, ChatGPT ou un autre assistant compatible MCP à Vivoo pour les actions que vous dirigez, et laissez l'Agent IA agir seul dans vos conversations, avec les mêmes règles que votre équipe.",
         "integration-ia", body, trail=[("Accueil", "/"), ("Intégration IA", None)], extra_ld=ld)


# ---------------------------------------------------------------- Blog

def build_blog():
    d = P["blog"]
    body = hero("Blog", "Le blog Vivoo arrive bientôt.",
                "Nous préparons des ressources sur les parcours clients, la conversation multicanale, l'automatisation et la fidélisation.",
                extra=f'<div class="sy-actions"><a class="btn btn-primary" href="/scenarios/">Voir les scénarios</a><a class="btn btn-secondary" href="/contact/">Nous contacter</a></div>') + cta()
    page("/blog/", d["title"], d["desc"], "", body, trail=[("Accueil", "/"), ("Blog", None)], extra_ld=d["jsonld"])


# ---------------------------------------------------------------- Pages légales

def build_legal(slug, crumb):
    d = P[slug]
    updated = f'<p class="sy-index" style="margin-top:1.5rem">{d["updated"]}</p>' if d["updated"] else ""
    body = hero("Légal", d["h1"] + ".", extra=updated) + f"""
<section class="sy-section sy-section--tight">
  <div class="sy-wrap sy-narrow sy-legal">
    {d['body']}
  </div>
</section>
"""
    page(f"/{slug}/", d["title"], d["desc"], "", body, trail=[("Accueil", "/"), (crumb, None)], extra_ld=d["jsonld"])


if __name__ == "__main__":
    build_contact()
    build_faq()
    build_cases()
    build_partners()
    build_integrations()
    build_ai_integration()
    build_blog()
    build_legal("mentions-legales", "Mentions légales")
    build_legal("conditions", "Conditions d'utilisation")
    build_legal("privacy", "Politique de confidentialité")
    print("ok")
