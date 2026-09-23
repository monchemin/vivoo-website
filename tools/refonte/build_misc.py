"""Pages institutionnelles au style de la refonte : contact, FAQ, cas clients,
partenaires, blog et pages légales.

Les textes légaux sont repris tels quels depuis pages.json (champ "body").
"""
import json, os
from build_common import *

HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, "pages.json"), encoding="utf-8"))
CONTACT_FORM = "https://app.vivoo.pro/forms/urfuZx"
PARTNER_FORM = "https://app.vivoo.pro/forms/aPZjVK"


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
<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-cards sy-cards--3">
      <a class="sy-card" href="{CONTACT_FORM}" {EXT}><span class="sy-card-num">01 · Écrire</span><h3>Formulaire de contact</h3><p>Remplissez le formulaire en ligne, l'équipe Vivoo vous répond rapidement.</p><span class="sy-card-more">Remplir le formulaire →</span></a>
      <a class="sy-card" href="{DEMO}" {EXT}><span class="sy-card-num">02 · Voir</span><h3>Parler à un spécialiste</h3><p>Réservez un moment pour voir Vivoo en action et dessiner votre parcours.</p><span class="sy-card-more">Réserver un échange →</span></a>
      <a class="sy-card" href="{SIGNUP}" {EXT}><span class="sy-card-num">03 · Essayer</span><h3>Créer mon compte</h3><p>Vous préférez commencer tout de suite ? Créez votre compte et activez vos premiers modules.</p><span class="sy-card-more">Créer mon compte →</span></a>
    </div>
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
                extra=f'<div class="sy-actions"><a class="btn btn-primary" href="{PARTNER_FORM}" {EXT}>Devenir partenaire</a></div>') + f"""
<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "Le modèle")}<h2 class="sy-h2">Trois niveaux, des rôles clairs.</h2></div>
      <p class="sy-lead">Ce modèle vous laisse l'autonomie commerciale complète sur votre marché, pendant que nous assurons la fiabilité de la plateforme derrière vous.</p>
    </div>
    <ol class="sy-steps sy-steps--3">
      <li><span class="sy-step-num">01</span><h3>Vivoo</h3><p>Développe et opère la plateforme : les canaux, les campagnes, les scénarios de fidélisation, les intégrations. C'est notre responsabilité, en continu.</p></li>
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

<section class="sy-cta">
  <div class="sy-wrap">
    <h2>Prêt à élargir votre offre avec Vivoo ?</h2>
    <p>Discutons de votre marché et de la façon dont un partenariat Vivoo peut s'y intégrer.</p>
    <div class="sy-actions">
      <a class="btn sy-btn-light" href="{PARTNER_FORM}" {EXT}>Devenir partenaire</a>
      <a class="btn sy-btn-ghost" href="/contact/">Nous contacter</a>
    </div>
    <div class="sy-cta-sign">Une plateforme, un réseau.</div>
  </div>
</section>
"""
    page("/partenaires/", d["title"], d["desc"], "apropos", body, trail=[("Accueil", "/"), ("Partenaires", None)], extra_ld=d["jsonld"])


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
    build_blog()
    build_legal("mentions-legales", "Mentions légales")
    build_legal("conditions", "Conditions d'utilisation")
    build_legal("privacy", "Politique de confidentialité")
    print("ok")
