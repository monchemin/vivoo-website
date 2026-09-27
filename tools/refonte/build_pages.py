from build_common import *
from build_data import PILLARS, SECTORS, SCENARIOS

PMAP = {p["slug"]: p for p in PILLARS}
SYSTEM = [
    ("Attirer", ["Prospection", "Pages", "Codes QR", "Campagnes"]),
    ("Capter", ["Formulaires", "Conversations", "Contacts"]),
    ("Converser", ["WhatsApp", "Instagram", "Messenger", "Courriel · SMS"]),
    ("Convertir", ["Qualification", "Rendez-vous", "Pages de vente", "Paiement"]),
    ("Vendre", ["Produits", "Services", "Commandes", "Événements"]),
    ("Fidéliser", ["Campagnes", "Points", "Relances", "Avis"]),
]
CHANNELS = [
    ("WhatsApp", "Le canal que vos clients ouvrent le plus"),
    ("Instagram", "Là où ils vous découvrent"),
    ("Messenger", "Les échanges de votre page Facebook"),
    ("Courriel", "Confirmations et infolettres"),
    ("SMS", "Les rappels qui doivent être lus"),
]
HERO_LINES = """<svg class="sy-hero-lines" viewBox="0 0 800 520" aria-hidden="true" focusable="false">
  <path d="M0 60 C 220 60, 330 250, 520 260" />
  <path d="M0 150 C 220 150, 330 255, 520 260" />
  <path d="M0 250 C 220 250, 330 260, 520 260" />
  <path d="M0 350 C 220 350, 330 265, 520 260" />
  <path d="M0 440 C 220 440, 330 270, 520 260" />
  <circle class="sy-loop" cx="640" cy="260" r="120" />
  <circle class="sy-node" cx="520" cy="260" r="6" />
  <circle class="sy-node" cx="700" cy="156" r="5" />
  <circle class="sy-node" cx="760" cy="260" r="5" />
  <circle class="sy-node" cx="700" cy="364" r="5" />
  <circle class="sy-node" cx="580" cy="364" r="5" />
  <circle class="sy-node" cx="580" cy="156" r="5" />
</svg>"""


def rail():
    lis = ""
    for i, (verb, items) in enumerate(SYSTEM, 1):
        lis += f'<li><span class="sy-rail-num">0{i}</span><h3>{verb}</h3><ul>' + "".join(f"<li>{x}</li>" for x in items) + "</ul></li>"
    return f'<ol class="sy-rail">{lis}</ol><div class="sy-return" aria-hidden="true"></div>'


def poles(pillars):
    out = '<ul class="sy-poles">'
    for p in pillars:
        out += f"""<li class="sy-pole"><a href="/solution/{p['slug']}/">
  <span class="sy-pole-num">{p['num']}<span class="sy-pole-verb">{p['verb']}</span></span>
  <h3>{p['name']}</h3>
  <div><p>{p['tagline']}</p>{chips(p['chips'])}</div>
  <span class="sy-pole-arrow" aria-hidden="true">→</span>
</a></li>"""
    return out + "</ul>"


def scenario_cards(limit=None):
    out = '<div class="sy-cards sy-cards--3">'
    for i, s in enumerate(SCENARIOS[:limit], 1):
        out += f"""<a class="sy-card" href="/scenarios/#{s['id']}">
  <span class="sy-card-num">0{i}</span>
  <h3>{s['home']}</h3>
  <p>{s['desc']}</p>
  {flow([x for x, _ in s['steps']])}
</a>"""
    return out + "</div>"


def sector_rows():
    out = '<ul class="sy-sectors">'
    for s in SECTORS:
        offer = f'<span class="sy-offer">{s["offer"]}</span>' if s["offer"] else ""
        out += f"""<li><a href="/solutions/{s['slug']}/">
  <h3>{s['name']}{offer}</h3>
  <p>{s['title']}</p>
  {flow(s['flow'])}
</a></li>"""
    return out + "</ul>"


def equation(light=False):
    return f"""<div class="sy-equation{' sy-light-eq' if light else ''}">
  <div class="sy-eq-box"><h3>Modules</h3><ul><li>CRM</li><li>Pages</li><li>Marketing</li><li>Rendez-vous</li><li>Commerce</li><li>Fidélité</li></ul><small>Offre Alma, Zagor ou Libre</small></div>
  <div class="sy-eq-op" aria-hidden="true">+</div>
  <div class="sy-eq-box"><h3>Crédits</h3><ul><li>WhatsApp</li><li>Courriel</li><li>Instagram</li><li>Messenger</li><li>SMS</li><li>Prospection</li></ul><small>Crédits, plan de crédits ou abonnement</small></div>
  <div class="sy-eq-op" aria-hidden="true">=</div>
  <div class="sy-eq-box sy-eq-box--result"><h3>Votre système</h3><p>Vous activez ce dont vous avez besoin. Vous payez ce que vous consommez.</p></div>
</div>"""


def modules_cards():
    from build_modules import MODULES
    return "".join(
        f'<a class="sy-card" href="/produit/{s}/"><span class="sy-card-num">Pôle {PMAP[pl]["num"]} · {PMAP[pl]["name"]}</span><h3>{n}</h3><span class="sy-card-more">En détail →</span></a>'
        for s, n, pl in MODULES)


# ---------------------------------------------------------------- Accueil

def build_home():
    body = f"""
<section class="sy-hero">
  {HERO_LINES}
  <div class="sy-wrap">
    <h1><span>Attirez.</span><span>Convertissez.</span><span>Faites revenir.</span></h1>
    <p class="sy-lead">Vivoo transforme vos prospects, vos conversations et vos clients en un système commercial qui travaille pour vous.</p>
    <div class="sy-actions">
      <a class="btn sy-btn-light" href="{SIGNUP}" {EXT}>Créer mon compte</a>
      <a class="btn sy-btn-ghost" href="/solution/">Découvrir le système</a>
    </div>
    <div class="sy-hero-channels" aria-label="Canaux pris en charge"><span>WhatsApp</span><span>Instagram</span><span>Messenger</span><span>Courriel</span><span>SMS</span></div>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-split">
    <div>
      {index_label("01", "Le problème")}
      <h2 class="sy-h2">Votre activité ne manque pas d'outils. <span class="sy-muted-span">Elle manque d'un système.</span></h2>
      <p class="sy-lead">Vos clients vous découvrent sur Facebook, vous écrivent sur WhatsApp, prennent rendez-vous, achètent en ligne ou reviennent en boutique. Le problème n'est pas le nombre de canaux. C'est de les faire fonctionner ensemble.</p>
    </div>
    <div>
      <ul class="sy-fragments">
        <li><span>Facebook</span> ici.</li>
        <li><span>WhatsApp</span> là.</li>
        <li>Les <span>rendez-vous</span> ailleurs.</li>
        <li>Les <span>ventes</span> dans un autre outil.</li>
        <li>Les <span>relances</span> dans votre tête.</li>
      </ul>
      <p class="sy-resolve">Vivoo connecte tout cela.</p>
    </div>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>
        {index_label("02", "Le système")}
        <h2 class="sy-h2">Un parcours. Un système. Un seul endroit.</h2>
      </div>
      <p class="sy-lead">Chaque étape de votre relation client est reliée à la suivante : ce qui se passe dans une conversation prépare le rendez-vous, la vente prépare la fidélisation.</p>
    </div>
    {rail()}
    <p class="sy-signature">Chaque interaction nourrit la suivante.</p>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>
        {index_label("03", "Les expertises")}
        <h2 class="sy-h2">Six pôles, un seul système.</h2>
      </div>
      <p class="sy-lead">Plutôt qu'une longue liste de modules, Vivoo s'organise autour de ce que vous cherchez à accomplir.</p>
    </div>
    {poles(PILLARS)}
  </div>
</section>

<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap sy-action">
    <div>
      {index_label("04", "Vivoo en action")}
      <h2 class="sy-h2">Un client découvre votre entreprise.</h2>
      <p class="sy-lead">Il voit une publicité, arrive sur votre page, vous écrit sur WhatsApp, prend rendez-vous, achète, laisse un avis et revient un mois plus tard. Pour lui, ce sont plusieurs moments. Pour Vivoo, c'est une seule relation.</p>
      {flow(["Publicité", "Page", "WhatsApp", "Contact", "Rendez-vous", "Vente", "Avis", "Relance", "Retour"], "sy-flow sy-flow--big")}
      <div class="sy-actions"><a class="sy-link" href="/scenarios/">Voir les scénarios →</a></div>
    </div>
    <figure style="margin:0">
      <a class="sy-mock" href="/contact/" aria-label="Fiche contact Vivoo : du premier clic au retour. Nous contacter">
        <div class="sy-mock-bar"><i></i><i></i><i></i></div>
        <div class="sy-mock-head">
          <div class="sy-avatar">ML</div>
          <div><strong>Marie L.</strong><span>Source : publicité Instagram</span></div>
          <div class="sy-mock-tags"><em>Cliente fidèle</em><em>320 points</em></div>
        </div>
        <ol class="sy-timeline">
          <li><span class="sy-ch">Meta</span><b>Clic sur la publicité</b><time>3 mars</time></li>
          <li><span class="sy-ch">Page</span><b>Contact créé</b><time>3 mars</time></li>
          <li><span class="sy-ch">WhatsApp</span><b>Conversation qualifiée</b><time>3 mars</time></li>
          <li><span class="sy-ch">Agenda</span><b>Rendez-vous confirmé</b><time>6 mars</time></li>
          <li><span class="sy-ch">Commerce</span><b>Vente enregistrée</b><time>6 mars</time></li>
          <li><span class="sy-ch">Courriel</span><b>Avis 5 étoiles reçu</b><time>7 mars</time></li>
          <li><span class="sy-ch">SMS</span><b>Relance automatique</b><time>5 avril</time></li>
          <li class="is-loop"><span class="sy-ch">Boutique</span><b>Elle revient ↺</b><time>8 avril</time></li>
        </ol>
      </a>
      <figcaption class="sy-mock-caption">Illustration : une fiche contact Vivoo, du premier clic au retour. <a href="/contact/">Nous contacter →</a></figcaption>
    </figure>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-split">
    <div>
      {index_label("05", "Les canaux")}
      <h2 class="sy-h2">Vos clients choisissent le canal. <span class="sy-muted-span">Vivoo garde le fil.</span></h2>
      <div class="sy-quote">
        <p>Un client peut vous découvrir sur Instagram, vous écrire sur WhatsApp, prendre rendez-vous, puis recevoir une relance par courriel.</p>
        <p>Pour lui, ce sont plusieurs interactions. Pour Vivoo, c'est une seule relation client.</p>
      </div>
    </div>
    <ul class="sy-channels">
      {"".join(f"<li>{c}<small>{d}</small></li>" for c, d in CHANNELS)}
    </ul>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>
        {index_label("06", "Scénarios")}
        <h2 class="sy-h2">Ce que Vivoo peut faire pour votre entreprise.</h2>
      </div>
      <p class="sy-lead">Ne cherchez pas une fonctionnalité. Choisissez un résultat, Vivoo enchaîne les étapes.</p>
    </div>
    {scenario_cards()}
    <div class="sy-actions"><a class="sy-link" href="/scenarios/">Voir tous les scénarios →</a></div>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>
        {index_label("07", "Solutions métier")}
        <h2 class="sy-h2">Un système adapté à votre activité.</h2>
      </div>
      <p class="sy-lead">Même plateforme, parcours différents. Vivoo se configure selon la façon dont vos clients vous trouvent, achètent et reviennent.</p>
    </div>
    {sector_rows()}
    <div class="sy-actions"><a class="sy-link" href="/solutions/">Voir toutes les solutions →</a></div>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>
        {index_label("08", "Sur le terrain")}
        <h2 class="sy-h2">Des parcours déjà en place.</h2>
      </div>
      <p class="sy-lead">Trois entreprises, trois réalités, un même besoin : arrêter de gérer la relation client de mémoire.</p>
    </div>
    <div class="sy-cards sy-cards--3">
      <a class="sy-card" href="/cas-clients/"><span class="sy-card-num">Restaurant et épicerie · Longueuil</span><h3>MakoFoods</h3><p>Capture en caisse et sur les tables, fidélité commune au restaurant et à l'épicerie, campagnes de retour.</p>{flow(["Code QR", "Fidélité", "Campagnes"])}</a>
      <a class="sy-card" href="/cas-clients/"><span class="sy-card-num">Massothérapie · Gatineau</span><h3>Kinaya</h3><p>Page d'accueil des nouveaux clients et prise de rendez-vous autonome, sans allers-retours.</p>{flow(["Capture", "Rendez-vous"])}</a>
      <a class="sy-card" href="/cas-clients/"><span class="sy-card-num">Épicerie en gros · Ottawa</span><h3>Twish Cart</h3><p>Recrutement de comptes, suivis et livraisons planifiés, fidélité sur le volume, campagnes d'arrivage.</p>{flow(["Capture", "Rendez-vous", "Fidélité", "Campagnes"])}</a>
    </div>
  </div>
</section>

<section class="sy-section sy-deep sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>
        {index_label("09", "Le modèle Vivoo")}
        <h2 class="sy-h2">Vous payez selon ce que vous utilisez.</h2>
      </div>
      <p class="sy-lead">Activez les modules dont vous avez besoin, puis utilisez vos crédits selon vos canaux et vos actions. Un modèle simple, progressif, pensé pour les petites entreprises.</p>
    </div>
    {equation()}
    <div class="sy-actions"><a class="sy-link" href="/tarifs/">Voir les tarifs →</a></div>
  </div>
</section>

{cta("Et si votre relation client fonctionnait enfin comme un système ?", "Créez votre compte et activez vos premiers modules, ou parlez à un spécialiste pour dessiner le parcours adapté à votre activité.", "Construisons votre système commercial.")}
"""
    ld = [
        {"@context": "https://schema.org", "@type": "Organization", "name": "Vivoo", "url": BASE, "logo": BASE + "/assets/img/logo-vivoo.png",
         "slogan": "Attirez. Convertissez. Faites revenir.",
         "sameAs": ["https://www.facebook.com/CRM.ViVoo/", "https://www.instagram.com/vivoocrm/", "https://www.linkedin.com/company/vivoo-crm/"],
         "parentOrganization": {"@type": "Organization", "name": "Technologies Ilema Inc.", "url": "https://ilematec.com"}},
        {"@context": "https://schema.org", "@type": "LocalBusiness", "name": "Technologies Ilema Inc. Vivoo", "image": BASE + "/assets/img/og-image.png", "url": BASE,
         "address": {"@type": "PostalAddress", "streetAddress": "2323 rue Galvani, Suite 130", "addressLocality": "Québec", "addressRegion": "QC", "postalCode": "G1N 4H7", "addressCountry": "CA"}},
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Vivoo", "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
         "description": "Vivoo est un système commercial qui relie l'acquisition, la conversation, la conversion, la vente et la fidélisation, sur WhatsApp, Instagram, Messenger, courriel et SMS.",
         "offers": {"@type": "Offer", "priceCurrency": "CAD", "description": "Modules activés selon les besoins et crédits consommés selon les canaux et les actions."},
         "publisher": {"@type": "Organization", "name": "Technologies Ilema Inc."}},
    ]
    page("/", "Vivoo. Attirez, convertissez, faites revenir",
         "Vivoo transforme vos prospects, vos conversations et vos clients en un système commercial qui travaille pour vous, sur WhatsApp, Instagram, Messenger, courriel et SMS.",
         "home", body, extra_ld=ld)


# ---------------------------------------------------------------- Solution

def build_solution_hub():
    blocks = ""
    for p in PILLARS:
        blocks += f"""<li class="sy-pole"><a href="/solution/{p['slug']}/">
  <span class="sy-pole-num">{p['num']}<span class="sy-pole-verb">{p['verb']}</span></span>
  <h3>{p['name']}</h3>
  <div><p><strong style="color:var(--navy)">{p['title']}</strong></p>{chips(p['chips'])}</div>
  <span class="sy-pole-arrow" aria-hidden="true">→</span>
</a></li>"""
    body = f"""
<section class="sy-page-hero">
  <div class="sy-wrap">
    {index_label("", "Le produit")}
    <h1 class="sy-display">Le système qui relie toute votre relation client.</h1>
    <p class="sy-lead">De la première interaction au prochain achat, Vivoo connecte chaque étape de votre parcours commercial.</p>
    {flow(["Attirer", "Capter", "Converser", "Convertir", "Vendre", "Fidéliser", "Mesurer"], "sy-flow sy-flow--big")}
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "Les pôles")}<h2 class="sy-h2">Six pôles qui travaillent ensemble.</h2></div>
      <p class="sy-lead">Chaque pôle répond à une étape du parcours. Ensemble, ils forment un seul système : ce qu'un pôle apprend sert immédiatement au suivant.</p>
    </div>
    <ul class="sy-poles">{blocks}</ul>
  </div>
</section>

<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("02", "Les fondations")}<h2 class="sy-h2">Trois couches font fonctionner le système.</h2></div>
      <p class="sy-lead">Sous les pôles, trois couches relient tout ce qui se passe, peu importe le canal ou le module.</p>
    </div>
    <ol class="sy-steps sy-steps--3">
      <li><span class="sy-step-num">CRM</span><h3>Un profil unique par client</h3><p>Conversations, rendez-vous, achats, points et avis s'ajoutent à la même fiche.</p></li>
      <li><span class="sy-step-num">Auto</span><h3>L'automatisation</h3><p>Les actions qui se répètent se déclenchent seules, au bon moment.</p></li>
      <li><span class="sy-step-num">CAPI</span><h3>La mesure</h3><p>Les conversions remontent à Meta pour améliorer vos prochaines campagnes.</p></li>
    </ol>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("03", "Pour aller plus loin")}<h2 class="sy-h2">Voyez le système en mouvement.</h2>
      <p class="sy-lead">Les scénarios montrent comment les pôles s'enchaînent dans une situation réelle. La page « Comment ça marche » explique comment démarrer.</p></div>
    <div class="sy-cards">
      <a class="sy-card" href="/scenarios/"><span class="sy-card-num">Scénarios</span><h3>Que puis-je faire avec Vivoo ?</h3><p>Six parcours concrets, de la publicité au client fidèle.</p><span class="sy-card-more">Voir les scénarios →</span></a>
      <a class="sy-card" href="/comment-ca-marche/"><span class="sy-card-num">Démarrer</span><h3>Comment ça marche ?</h3><p>Modules, canaux, crédits : cinq étapes pour lancer votre système.</p><span class="sy-card-more">Comment ça marche →</span></a>
    </div>
  </div>
</section>
<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("04", "Les modules en détail")}<h2 class="sy-h2">Dix modules, rangés par pôle.</h2></div>
      <p class="sy-lead">Pour ceux qui veulent voir chaque pièce du système de près.</p>
    </div>
    <div class="sy-cards">{modules_cards()}</div>
  </div>
</section>
{cta()}"""
    page("/solution/", "Le système Vivoo. Vivoo",
         "Acquisition, conversation, conversion, vente, fidélisation et automatisation : découvrez les six pôles du système commercial Vivoo.",
         "solution", body, trail=[("Accueil", "/"), ("Produit", None)])


def build_pillar(i, p):
    prev_p = PILLARS[i - 1] if i > 0 else None
    next_p = PILLARS[i + 1] if i + 1 < len(PILLARS) else None
    items = "".join(
        f"<li><h3>{n}</h3><p>{d}</p>" + (f'<a href="{l}">En détail →</a>' if l else "<span></span>") + "</li>"
        for n, d, l in p["items"]
    )
    if p["slug"] == "vente":
        middle = f"""
<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("02", "Toute la chaîne")}<h2 class="sy-h2">Vivoo ne s'arrête pas au paiement.</h2></div>
      <p class="sy-lead">La vente est une étape du parcours, pas sa fin. Chaque commande prépare l'avis, puis la fidélisation, puis la vente suivante.</p>
    </div>
    <ol class="sy-steps sy-steps--4">
      {"".join(f'<li><span class="sy-step-num">{j:02d}</span><h3>{s}</h3></li>' for j, s in enumerate(p["chain"], 1))}
    </ol>
  </div>
</section>"""
    elif p["slug"] == "automatisation":
        middle = f"""
<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("02", "Trois niveaux")}<h2 class="sy-h2">Automatisation, séquence, scénario.</h2></div>
      <p class="sy-lead">Trois mots souvent confondus. Chez Vivoo, ils désignent trois niveaux bien distincts.</p>
    </div>
    <div class="sy-levels">
      <div class="sy-level"><span class="sy-level-k">Niveau 1</span><h3>Automatisation</h3><p>Une action se déclenche automatiquement.</p><div class="sy-level-ex">30 jours sans achat → envoyer une relance</div></div>
      <div class="sy-level"><span class="sy-level-k">Niveau 2</span><h3>Séquence</h3><p>Plusieurs actions s'enchaînent dans le temps.</p><div class="sy-level-ex">Jour 0 → message<br>Jour 3 → relance<br>Jour 7 → offre</div></div>
      <div class="sy-level"><span class="sy-level-k">Niveau 3</span><h3>Scénario</h3><p>Un parcours commercial complet, qui combine plusieurs pôles.</p><div class="sy-level-ex">Publicité → capture → conversation → rendez-vous → vente → fidélisation</div></div>
    </div>
  </div>
</section>"""
    else:
        middle = f"""
<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("02", "Comment ça s'enchaîne")}<h2 class="sy-h2">Quatre temps, un seul mouvement.</h2></div>
      <p class="sy-lead">{p['tagline']} Voici comment ce pôle s'enchaîne dans Vivoo.</p>
    </div>
    <ol class="sy-steps sy-steps--4">
      {"".join(f'<li><span class="sy-step-num">{j:02d}</span><h3>{t}</h3><p>{d}</p></li>' for j, (t, d) in enumerate(p["method"], 1))}
    </ol>
  </div>
</section>"""
    pager = '<nav class="sy-pager" aria-label="Pôles">'
    if prev_p:
        pager += f'<a href="/solution/{prev_p["slug"]}/"><small>← Pôle {prev_p["num"]}</small>{prev_p["name"]}</a>'
    if next_p:
        pager += f'<a href="/solution/{next_p["slug"]}/"><small>Pôle {next_p["num"]} →</small>{next_p["name"]}</a>'
    else:
        pager += '<a href="/solution/"><small>Le système →</small>Vue d\'ensemble</a>'
    pager += "</nav>"
    sid, stitle = p["scenario"]
    body = f"""
<section class="sy-page-hero">
  <div class="sy-wrap">
    {index_label(p['num'], "Pôle " + p['name'] + " · " + p['verb'])}
    <h1 class="sy-display">{p['title']}</h1>
    <p class="sy-lead">{p['lead']}</p>
    {chips(p['chips'])}
  </div>
  <span class="sy-ghost-num" aria-hidden="true">{p['num']}</span>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "Ce que couvre ce pôle")}<h2 class="sy-h2">{p['tagline']}</h2></div>
    </div>
    <ul class="sy-items">{items}</ul>
  </div>
</section>
{middle}
<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("03", "Ce que vous obtenez")}<ul class="sy-checks">{"".join(f"<li>{g}</li>" for g in p['gets'])}</ul></div>
    <a class="sy-card sy-panel" href="/scenarios/#{sid}"><span class="sy-card-num">Scénario</span><h3>{stitle}</h3><p>Voyez comment ce pôle s'enchaîne avec les autres dans un parcours complet.</p><span class="sy-card-more">Voir le scénario →</span></a>
  </div>
</section>

<section class="sy-pager-wrap">
  <div class="sy-wrap">{pager}</div>
</section>
{cta()}"""
    page(f"/solution/{p['slug']}/", f"{p['name']}. {p['title'].rstrip('.')}. Vivoo",
         p["lead"], "solution/" + p["slug"], body,
         trail=[("Accueil", "/"), ("Produit", "/solution/"), (p["name"], None)])


# ---------------------------------------------------------------- Solutions par activité

def build_solutions_hub():
    body = f"""
<section class="sy-page-hero sy-page-hero--dark">
  <div class="sy-wrap">
    {index_label("", "Solutions par activité")}
    <h1 class="sy-display">Votre activité est unique. Votre système doit l'être aussi.</h1>
    <p class="sy-lead">Même plateforme, parcours différents. Pour chaque secteur, Vivoo arrive avec les modules, les pages et les scénarios qui comptent vraiment.</p>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "Les secteurs")}<h2 class="sy-h2">Choisissez votre point de départ.</h2></div>
      <p class="sy-lead">Alma et Zagor sont des offres préconfigurées : ce ne sont pas des logiciels différents, mais Vivoo déjà réglé pour votre métier.</p>
    </div>
    {sector_rows()}
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("02", "Votre secteur n'est pas dans la liste ?")}<h2 class="sy-h2">Le système s'adapte.</h2>
      <p class="sy-lead">Les pôles de Vivoo se combinent selon la façon dont vos clients vous trouvent, achètent et reviennent. Parlons de votre parcours.</p>
      <div class="sy-actions"><a class="btn btn-primary" href="{DEMO}" {EXT}>Parler à un spécialiste</a></div></div>
    <div>{flow(["Attirer", "Capter", "Converser", "Convertir", "Vendre", "Fidéliser"], "sy-vflow")}</div>
  </div>
</section>
{cta()}"""
    page("/solutions/", "Solutions par activité. Vivoo",
         "Thérapeutes, restaurants, commerce, services, événements : découvrez comment Vivoo s'adapte à votre activité, avec les offres préconfigurées Alma et Zagor.",
         "solutions", body, trail=[("Accueil", "/"), ("Solutions", None)])


def build_sector(s):
    offer_sec = ""
    if s["offer"]:
        offer_sec = f"""
<section class="sy-section sy-deep sy-reveal" id="{s['offer'].lower()}">
  <div class="sy-wrap sy-split">
    <div>{index_label("", "Offre préconfigurée")}<h2 class="sy-h2" style="font-size:clamp(3rem,9vw,6.5rem)">{s['offer']}</h2></div>
    <div><p class="sy-lead">{s['offer_text']}</p>
      <div class="sy-actions"><a class="btn sy-btn-light" href="{DEMO}" {EXT}>Démarrer avec {s['offer']}</a><a class="btn sy-btn-ghost" href="/tarifs/">Voir les tarifs</a></div></div>
  </div>
</section>"""
    case_sec = ""
    if s["case"]:
        n, where, txt = s["case"]
        case_sec = f"""
<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("03", "Sur le terrain")}<h2 class="sy-h2">{n}</h2><p class="sy-index" style="margin-top:-0.5rem">{where}</p></div>
    <div><p class="sy-lead">{txt}</p><a class="sy-link" href="/cas-clients/">Voir les cas clients →</a></div>
  </div>
</section>"""
    pill_cards = "".join(
        f'<a class="sy-card" href="/solution/{k}/"><span class="sy-card-num">Pôle {PMAP[k]["num"]}</span><h3>{PMAP[k]["name"]}</h3><p>{PMAP[k]["tagline"]}</p></a>'
        for k in s["pillars"]
    )
    title_name = s["name"] + (f" · {s['offer']}" if s["offer"] else "")
    body = f"""
<section class="sy-page-hero">
  <div class="sy-wrap">
    {index_label(s['offer'].upper() if s['offer'] else "", s['name'])}
    <h1 class="sy-display">{s['title']}</h1>
    <p class="sy-lead">{s['who']}</p>
    {flow(s['flow'], "sy-flow sy-flow--big")}
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "Ce qui change pour vous")}<h2 class="sy-h2">Un parcours pensé pour votre métier.</h2></div>
    </div>
    <ol class="sy-steps sy-steps--3">
      {"".join(f'<li><span class="sy-step-num">{j:02d}</span><h3>{t}</h3><p>{d}</p></li>' for j, (t, d) in enumerate(s['pains'], 1))}
    </ol>
  </div>
</section>
{offer_sec}
<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("02", "Les pôles mobilisés")}<h2 class="sy-h2">Ce que Vivoo active pour vous.</h2></div>
    </div>
    <div class="sy-cards">{pill_cards}</div>
  </div>
</section>
{case_sec}
{cta()}"""
    page(f"/solutions/{s['slug']}/", f"Vivoo pour {s['name'].lower()}{' · ' + s['offer'] if s['offer'] else ''}. {s['title'].split('.')[0]}.",
         f"{s['title']} {s['who']}", "solutions/" + s["slug"], body,
         trail=[("Accueil", "/"), ("Solutions", "/solutions/"), (title_name, None)])


# ---------------------------------------------------------------- Scénarios

def build_scenarios():
    blocks = ""
    for i, s in enumerate(SCENARIOS, 1):
        steps = "".join(f"<li>{t}<small>{d}</small></li>" for t, d in s["steps"])
        blocks += f"""<article class="sy-scenario sy-reveal" id="{s['id']}">
  <div>
    {index_label(f"0{i}", "Scénario · " + s['home'])}
    <h2>{s['title']}</h2>
    <p class="sy-lead">{s['text']}</p>
    {chips(s['pillars'])}
  </div>
  <ol class="sy-vflow">{steps}</ol>
</article>"""
    body = f"""
<section class="sy-page-hero sy-page-hero--dark">
  <div class="sy-wrap">
    {index_label("", "Scénarios")}
    <h1 class="sy-display">Ne cherchez pas une fonctionnalité. Construisez un parcours.</h1>
    <p class="sy-lead">Un scénario, c'est un parcours commercial complet : plusieurs pôles de Vivoo qui s'enchaînent pour produire un résultat concret.</p>
  </div>
</section>

<section class="sy-section">
  <div class="sy-wrap">{blocks}</div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("", "Et votre parcours ?")}<h2 class="sy-h2">Chaque entreprise a son scénario.</h2>
      <p class="sy-lead">Ces parcours sont des points de départ. Nous pouvons dessiner avec vous celui qui correspond à votre façon de vendre.</p></div>
    <div class="sy-levels" style="grid-template-columns:1fr">
      <div class="sy-level"><span class="sy-level-k">Automatisation</span><p>Une action se déclenche automatiquement.</p></div>
      <div class="sy-level"><span class="sy-level-k">Séquence</span><p>Plusieurs actions s'enchaînent dans le temps.</p></div>
      <div class="sy-level"><span class="sy-level-k">Scénario</span><p>Un parcours commercial complet. <a class="sy-link" href="/solution/automatisation/">Comprendre la différence →</a></p></div>
    </div>
  </div>
</section>
{cta()}"""
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Scénarios Vivoo",
          "itemListElement": [{"@type": "ListItem", "position": i, "name": s["title"], "url": f"{BASE}/scenarios/#{s['id']}"} for i, s in enumerate(SCENARIOS, 1)]}
    page("/scenarios/", "Scénarios. Ce que vous pouvez faire avec Vivoo",
         "Transformer une publicité en client, remplir son agenda, faire revenir un client inactif : six parcours concrets construits avec Vivoo.",
         "scenarios", body, trail=[("Accueil", "/"), ("Scénarios", None)], extra_ld=[ld])


# ---------------------------------------------------------------- Comment ça marche

def build_how():
    steps = [
        ("Choisissez votre offre", "Alma pour les thérapeutes, Zagor pour la restauration, ou Libre pour composer vous-même vos modules."),
        ("Connectez vos canaux", "WhatsApp, Instagram, Messenger, courriel et SMS. Vos conversations arrivent au même endroit."),
        ("Configurez votre système", "Pages, formulaires, codes QR, automatisations : partez d'un scénario prêt à l'emploi ou construisez le vôtre."),
        ("Ajoutez vos crédits", "À l'unité, avec un plan de crédits ou par abonnement. Ils servent aux envois sur vos canaux et à la prospection."),
        ("Laissez Vivoo fonctionner", "Le système capte, relance, rappelle et fidélise. Vous suivez les résultats et intervenez quand ça compte."),
    ]
    body = f"""
<section class="sy-page-hero">
  <div class="sy-wrap">
    {index_label("", "Comment ça marche")}
    <h1 class="sy-display">Cinq étapes pour lancer votre système.</h1>
    <p class="sy-lead">Pas de gros projet d'intégration. Vous démarrez petit, avec ce qui compte le plus aujourd'hui, et vous faites évoluer votre système ensuite.</p>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <ol class="sy-steps sy-steps--5">
      {"".join(f'<li><span class="sy-step-num">{j:02d}</span><h3>{t}</h3><p>{d}</p></li>' for j, (t, d) in enumerate(steps, 1))}
    </ol>
    <div class="sy-actions"><a class="btn btn-primary" href="{SIGNUP}" {EXT}>Créer mon compte</a><a class="btn btn-secondary" href="{DEMO}" {EXT}>Être accompagné</a></div>
  </div>
</section>

<section class="sy-section sy-deep sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("", "Modules + crédits")}<h2 class="sy-h2">Deux choses à comprendre. Pas plus.</h2></div>
      <p class="sy-lead">Les modules sont les fonctionnalités que vous activez. Les crédits sont ce que vous consommez quand Vivoo envoie un message ou effectue une action pour vous.</p>
    </div>
    {equation()}
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("", "Les canaux")}<h2 class="sy-h2">Vos canaux, reliés au même profil.</h2>
      <p class="sy-lead">Chaque canal connecté alimente la même fiche client. Vous pouvez en activer un seul pour commencer et ajouter les autres plus tard.</p></div>
    <ul class="sy-channels">{"".join(f"<li>{c}<small>{d}</small></li>" for c, d in CHANNELS)}</ul>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-cards sy-cards--3">
      <a class="sy-card" href="/tarifs/"><span class="sy-card-num">Tarifs</span><h3>Combien ça coûte ?</h3><p>Une offre de modules (Alma, Zagor ou Libre) et des crédits pour vos canaux.</p><span class="sy-card-more">Voir les tarifs →</span></a>
      <a class="sy-card" href="/scenarios/"><span class="sy-card-num">Scénarios</span><h3>Par où commencer ?</h3><p>Six parcours prêts à l'emploi pour démarrer vite.</p><span class="sy-card-more">Voir les scénarios →</span></a>
      <a class="sy-card" href="/faq/"><span class="sy-card-num">FAQ</span><h3>D'autres questions ?</h3><p>Fonctionnement, canaux, crédits, partenaires.</p><span class="sy-card-more">Lire la FAQ →</span></a>
    </div>
  </div>
</section>
{cta()}"""
    page("/comment-ca-marche/", "Comment ça marche. Vivoo",
         "Choisissez vos modules, connectez vos canaux, configurez votre système, ajoutez vos crédits : lancez Vivoo en cinq étapes.",
         "comment", body, trail=[("Accueil", "/"), ("Comment ça marche", None)])


# ---------------------------------------------------------------- Tarifs

def build_pricing():
    offers = [
        ("Alma", "Thérapeutes", "L'offre préconfigurée pour les pratiques de soins et d'accompagnement.",
         ["Capture des nouveaux clients", "Conversations multicanales", "Rendez-vous et rappels", "Avis et fidélisation"],
         "/solutions/therapeutes/", "Découvrir Alma", False),
        ("Zagor", "Restaurants et commerces alimentaires", "L'offre préconfigurée pour faire revenir les clients en salle et en boutique.",
         ["Capture par code QR", "Programme de fidélité", "Campagnes de retour", "Avis clients"],
         "/solutions/restaurants/", "Découvrir Zagor", False),
        ("Libre", "Toutes les activités", "Vous composez vous-même votre système, module par module.",
         ["Choisissez vos modules un à un", "Ajoutez-en quand vous grandissez", "Commerce, services, événements…"],
         SIGNUP, "Créer mon compte", True),
    ]
    credits = [
        ("Crédits", "Usage ponctuel", "Achetez des crédits quand vous en avez besoin et utilisez-les sur les canaux de votre choix."),
        ("Plan de crédits", "Usage régulier", "Un volume de crédits prévu à l'avance, adapté à votre rythme d'envoi."),
        ("Abonnement", "Usage continu", "Vos crédits se renouvellent automatiquement chaque mois, sans avoir à y penser."),
    ]
    faq = [
        ("Qu'est-ce qu'un crédit ?", "Un crédit est l'unité consommée quand Vivoo agit pour vous sur un canal : envoyer un message WhatsApp, un SMS ou un courriel, écrire sur Instagram ou Messenger, ou lancer une recherche de prospection. Chaque canal a son propre coût en crédits."),
        ("Quelle offre choisir si je ne suis ni thérapeute ni restaurateur ?", "L'offre Libre : vous activez uniquement les modules dont votre activité a besoin, et vous en ajoutez au fil du temps."),
        ("Quelle différence entre crédits, plan de crédits et abonnement ?", "Les crédits s'achètent au besoin. Le plan de crédits prévoit un volume à l'avance. L'abonnement renouvelle vos crédits chaque mois. Dans les trois cas, vous ne consommez que ce que vous envoyez."),
        ("Puis-je changer d'offre ou de formule en cours de route ?", "Oui. Vous pouvez commencer avec l'offre Libre et des crédits ponctuels, puis passer à Alma, à Zagor, à un plan ou à un abonnement quand votre système grandit."),
        ("Combien coûte Vivoo pour mon entreprise ?", "Cela dépend de votre offre et de votre volume d'envois. Un spécialiste peut calibrer avec vous l'offre et la formule de crédits adaptées à votre activité."),
    ]
    offer_html = ""
    for name, who, text, feats, href, label, is_signup in offers:
        ext = f" {EXT}" if is_signup else ""
        cls = "btn btn-primary" if name == "Libre" else "btn btn-secondary"
        offer_html += f"""<div class="sy-tier{' sy-tier--feature' if name == 'Libre' else ''}"><span class="sy-tier-for">{who}</span><h3 class="sy-tier-name">{name}</h3><p>{text}</p>
        <ul class="sy-checks">{"".join(f"<li>{f}</li>" for f in feats)}</ul>
        <a class="{cls}" href="{href}"{ext}>{label}</a></div>"""
    credit_html = "".join(
        f'<li><span class="sy-step-num">{i:02d}</span><h3>{n}</h3><p><strong>{f}.</strong> {d}</p></li>'
        for i, (n, f, d) in enumerate(credits, 1)
    )
    faq_html = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in faq)
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    body = f"""
<section class="sy-page-hero">
  <div class="sy-wrap">
    {index_label("", "Tarifs")}
    <h1 class="sy-display">Commencez simplement. Faites évoluer votre système.</h1>
    <p class="sy-lead">Deux choix, pas plus : votre offre de modules, et la façon dont vous utilisez vos crédits sur vos canaux.</p>
    {flow(["Offre de modules", "Crédits d'utilisation", "Votre système"], "sy-flow sy-flow--big")}
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "Les offres de modules")}<h2 class="sy-h2">Choisissez votre offre.</h2></div>
      <p class="sy-lead">Une offre préconfigurée pour votre métier, ou l'offre Libre pour composer votre système vous-même.</p>
    </div>
    <div class="sy-tiers">{offer_html}</div>
  </div>
</section>

<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("02", "Les crédits d'utilisation")}<h2 class="sy-h2">Utilisez vos canaux à votre rythme.</h2></div>
      <p class="sy-lead">Chaque envoi sur WhatsApp, SMS, courriel, Instagram ou Messenger, et chaque recherche de prospection, consomme des crédits. Trois façons de les obtenir :</p>
    </div>
    <ol class="sy-steps sy-steps--3">{credit_html}</ol>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("03", "Un exemple simple")}<h2 class="sy-h2">Un restaurant avec Zagor.</h2></div>
      <p class="sy-lead">Il choisit l'offre Zagor et un plan de crédits. Ce mois-ci, il envoie une promotion sur WhatsApp, un rappel par SMS et son infolettre par courriel.</p>
    </div>
    {equation(light=True)}
    <p class="sy-lead" style="margin-top:2rem">Son offre Zagor reste active tout le mois. Ses crédits ne sont consommés que par les envois qu'il a réellement faits. Le mois suivant, s'il envoie moins, il consomme moins.</p>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-narrow">
    {index_label("04", "Questions fréquentes")}
    {faq_html}
  </div>
</section>
{cta("Trouvons l'offre qui vous ressemble.", "Un spécialiste Vivoo vous aide à choisir votre offre de modules et la formule de crédits adaptées à votre activité.", "Vous payez ce que vous utilisez.")}"""
    page("/tarifs/", "Tarifs. Offres de modules et crédits. Vivoo",
         "Choisissez votre offre de modules (Alma, Zagor ou Libre) et utilisez vos canaux avec des crédits, un plan de crédits ou un abonnement.",
         "tarifs", body, trail=[("Accueil", "/"), ("Tarifs", None)], extra_ld=[ld])


# ---------------------------------------------------------------- À propos & vision

def build_about():
    body = f"""
<section class="sy-page-hero sy-page-hero--dark">
  <div class="sy-wrap">
    {index_label("", "À propos")}
    <h1 class="sy-display">Les entreprises n'ont pas besoin de plus d'outils.</h1>
    <p class="sy-lead" style="font-size:clamp(1.3rem,2.4vw,1.9rem);color:var(--sky);font-weight:600;max-width:24ch">Elles ont besoin que leurs outils travaillent ensemble.</p>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("01", "Notre vision")}<h2 class="sy-h2">Une relation client qui fonctionne comme un système.</h2></div>
    <div><p class="sy-lead">Une petite entreprise gère aujourd'hui autant de canaux qu'une grande, sans l'équipe qui va avec. Nous croyons qu'elle mérite un système qui relie chaque étape, de la première rencontre au retour du client, et qui travaille pour elle même quand elle est occupée ailleurs.</p></div>
  </div>
</section>

<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("02", "Pourquoi Vivoo")}<h2 class="sy-h2">Parce que les relances vivaient dans la tête des entrepreneurs.</h2></div>
    <div><p class="sy-lead">Les messages sur un canal, les rendez-vous sur un autre, les ventes ailleurs. Chaque outil faisait bien son travail, mais aucun ne faisait le lien. Vivoo est né pour faire ce lien : un seul profil client, un seul parcours, un seul endroit.</p></div>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("03", "Notre approche")}<h2 class="sy-h2">Le système avant l'outil.</h2></div>
      <p class="sy-lead">Nous partons du parcours de vos clients, pas de la liste de nos fonctionnalités.</p>
    </div>
    <ol class="sy-steps sy-steps--4">
      <li><span class="sy-step-num">01</span><h3>Comprendre</h3><p>Comment vos clients vous trouvent, vous écrivent, achètent et reviennent.</p></li>
      <li><span class="sy-step-num">02</span><h3>Dessiner</h3><p>Le parcours cible et le rôle de chaque canal.</p></li>
      <li><span class="sy-step-num">03</span><h3>Activer</h3><p>Les modules et les scénarios qui produisent un résultat rapidement.</p></li>
      <li><span class="sy-step-num">04</span><h3>Faire évoluer</h3><p>Le système grandit avec votre activité, un pôle à la fois.</p></li>
    </ol>
  </div>
</section>

<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("04", "Notre technologie")}<h2 class="sy-h2">Construit sur les canaux que vos clients utilisent déjà.</h2></div>
    <div><p class="sy-lead">Vivoo s'appuie sur l'API WhatsApp Business et l'écosystème Meta (Messenger, Instagram, Pixel et API de conversions), se synchronise avec Google Agenda et se connecte à Shopify, Square, Clover et WooCommerce.</p>
      {chips(["WhatsApp Business API", "Messenger", "Instagram", "Meta Pixel", "CAPI", "Google Agenda", "Shopify", "Square", "Clover", "WooCommerce"])}</div>
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("05", "Notre écosystème")}<h2 class="sy-h2">Une plateforme, un réseau.</h2></div>
    </div>
    <div class="sy-cards sy-cards--3">
      <a class="sy-card" href="https://ilematec.com" {EXT}><span class="sy-card-num">Éditeur</span><h3>Technologies Ilema</h3><p>L'entreprise québécoise qui conçoit et opère Vivoo.</p><span class="sy-card-more">ilematec.com →</span></a>
      <a class="sy-card" href="/partenaires/"><span class="sy-card-num">Partenaires</span><h3>Un réseau qui déploie Vivoo</h3><p>Agences et intégrateurs qui accompagnent leurs propres clients avec Vivoo.</p><span class="sy-card-more">Devenir partenaire →</span></a>
      <a class="sy-card" href="/vision/"><span class="sy-card-num">Manifeste</span><h3>Comment nous pensons</h3><p>Cinq principes qui guident chaque décision produit.</p><span class="sy-card-more">Lire le manifeste →</span></a>
    </div>
  </div>
</section>
{cta()}"""
    page("/a-propos/", "À propos. Vivoo",
         "Les entreprises n'ont pas besoin de plus d'outils : elles ont besoin que leurs outils travaillent ensemble. Découvrez la vision, l'approche et l'écosystème de Vivoo.",
         "apropos", body, trail=[("Accueil", "/"), ("À propos", None)])


def build_vision():
    principles = [
        ("Simple avant complexe.", "Si une fonctionnalité demande une formation pour être utilisée, elle n'est pas encore terminée."),
        ("Action avant information.", "Un tableau de bord qui ne débouche sur aucune action est une décoration. Vivoo vous dit quoi faire ensuite, ou le fait pour vous."),
        ("Relation avant données.", "Un contact n'est pas une ligne dans un tableau. C'est une personne avec un historique, des préférences et un canal favori."),
        ("Résultat avant fonctionnalité.", "Nous ne vendons pas des modules. Nous aidons à remplir un agenda, à faire revenir un client, à vendre davantage."),
        ("Vous payez ce que vous utilisez.", "Des modules que vous choisissez, des crédits que vous consommez. Pas de forfait gonflé pour des outils qui dorment."),
    ]
    body = f"""
<section class="sy-page-hero sy-page-hero--dark">
  <div class="sy-wrap">
    {index_label("", "Comment nous pensons")}
    <h1 class="sy-display">Le système avant l'outil.</h1>
    <p class="sy-lead">Cinq principes qui guident la façon dont nous concevons Vivoo, et la façon dont nous accompagnons les entreprises qui l'utilisent.</p>
  </div>
</section>

<section class="sy-section sy-dark" style="padding-top:0">
  <div class="sy-wrap">
    <ol class="sy-principles">
      {"".join(f'<li class="sy-reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in principles)}
    </ol>
  </div>
</section>
{cta()}"""
    page("/vision/", "Comment nous pensons. Le système avant l'outil. Vivoo",
         "Simple avant complexe, action avant information, relation avant données, résultat avant fonctionnalité : les principes qui guident Vivoo.",
         "apropos", body, trail=[("Accueil", "/"), ("À propos", "/a-propos/"), ("Comment nous pensons", None)])


if __name__ == "__main__":
    build_home()
    build_solution_hub()
    for i, p in enumerate(PILLARS):
        build_pillar(i, p)
    build_solutions_hub()
    for s in SECTORS:
        build_sector(s)
    build_scenarios()
    build_how()
    build_pricing()
    build_about()
    build_vision()
    print("ok")
