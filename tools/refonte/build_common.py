import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "site")
BASE = "https://vivoo.pro"
SIGNUP = "https://app.vivoo.pro/signup/initiate"
LOGIN = "https://app.vivoo.pro"
DEMO = "https://app.vivoo.pro/book/zrNLzn"
EXT = 'target="_blank" rel="noopener"'

PILLARS_NAV = [
    ("acquisition", "Acquérir", "Acquisition"),
    ("conversation", "Converser", "Conversation"),
    ("conversion", "Convertir", "Conversion"),
    ("vente", "Vendre", "Vente"),
    ("fidelisation", "Fidéliser", "Fidélisation"),
    ("automatisation", "Automatiser", "Automatisation"),
]
SECTORS_NAV = [
    ("therapeutes", "Alma", "Thérapeutes"),
    ("restaurants", "Zagor", "Restaurants"),
    ("commerce", "", "Commerce"),
    ("services", "", "Services"),
    ("evenements", "", "Événements"),
]


def head(title, desc, path, jsonld=None):
    ld = ""
    for obj in jsonld or []:
        ld += '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>\n"
    url = BASE + path
    return f"""<!doctype html>
<html lang="fr-CA">
<head>
<script>
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {{
  document.documentElement.classList.add('vv-js');
}}
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Vivoo">
<meta property="og:locale" content="fr_CA">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://vivoo.pro/assets/img/og-image.png">
<meta property="og:url" content="{url}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://vivoo.pro/assets/img/og-image.png">

<meta name="theme-color" content="#0B3B61">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/css/style.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
{ld}</head>
<body>
"""


def cur(active, key):
    return ' aria-current="page"' if active == key else ""


def header(active=""):
    sol = "\n".join(
        f'          <li><a href="/solution/{s}/"{cur(active, "solution/" + s)}><span class="sy-mega-k">{v}</span><span>{n}</span></a></li>'
        for s, v, n in PILLARS_NAV
    )
    sec = "\n".join(
        f'          <li><a href="/solutions/{s}/"{cur(active, "solutions/" + s)}><span class="sy-mega-k">{o or "&nbsp;"}</span><span>{n}</span></a></li>'
        for s, o, n in SECTORS_NAV
    )
    return f"""<header class="site-header sy-header">
  <div class="container">
    <a class="logo" href="/" aria-label="Vivoo. Accueil">
      <img src="/assets/img/logo-vivoo.png" alt="Vivoo" width="120" height="32">
    </a>
    <button class="nav-toggle" type="button" aria-label="Ouvrir le menu" onclick="document.body.classList.toggle('nav-open')">☰</button>
    <nav class="main-nav" aria-label="Navigation principale">
      <div class="has-submenu">
        <a href="/solution/"{cur(active, "solution")}>Solution</a>
        <ul class="submenu sy-mega">
          <li><a href="/solution/"><span class="sy-mega-k">Le système</span><span>Vue d'ensemble</span></a></li>
{sol}
          <li class="sy-mega-sep" role="presentation"></li>
          <li><a href="/comment-ca-marche/"{cur(active, "comment")}><span class="sy-mega-k">Démarrer</span><span>Comment ça marche</span></a></li>
        </ul>
      </div>
      <div class="has-submenu">
        <a href="/solutions/"{cur(active, "solutions")}>Solutions</a>
        <ul class="submenu sy-mega">
          <li><a href="/solutions/"><span class="sy-mega-k">Par activité</span><span>Vue d'ensemble</span></a></li>
{sec}
        </ul>
      </div>
      <a href="/scenarios/"{cur(active, "scenarios")}>Scénarios</a>
      <a href="/tarifs/"{cur(active, "tarifs")}>Tarifs</a>
      <a href="/a-propos/"{cur(active, "apropos")}>À propos</a>
      <span class="nav-spacer" aria-hidden="true"></span>
      <a class="nav-login" href="{LOGIN}" {EXT}>Connexion</a>
      <a class="nav-cta" href="{SIGNUP}" {EXT}>Créer mon compte</a>
    </nav>
  </div>
</header>
"""


FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">
          <img src="/assets/img/logo-vivoo.png" alt="Vivoo" width="90" height="24">
        </div>
        <p><strong>Attirez. Convertissez. Faites revenir.</strong></p>
        <p>Vivoo relie vos prospects, vos conversations, vos rendez-vous, vos ventes et vos clients dans un seul système commercial, sur WhatsApp, Instagram, Messenger, courriel et SMS.</p>
      </div>
      <div>
        <h3>Solution</h3>
        <ul>
          <li><a href="/solution/">Le système Vivoo</a></li>
{chr(10).join(f'          <li><a href="/solution/{s}/">{n}</a></li>' for s, v, n in PILLARS_NAV)}
          <li><a href="/comment-ca-marche/">Comment ça marche</a></li>
        </ul>
      </div>
      <div>
        <h3>Solutions</h3>
        <ul>
{chr(10).join(f'          <li><a href="/solutions/{s}/">{n}{" · " + o if o else ""}</a></li>' for s, o, n in SECTORS_NAV)}
          <li><a href="/scenarios/">Scénarios</a></li>
          <li><a href="/tarifs/">Tarifs</a></li>
        </ul>
      </div>
      <div>
        <h3>Vivoo</h3>
        <ul>
          <li><a href="/a-propos/">À propos</a></li>
          <li><a href="/vision/">Comment nous pensons</a></li>
          <li><a href="/cas-clients/">Cas clients</a></li>
          <li><a href="/partenaires/">Partenaires</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/faq/">FAQ</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
      <div>
        <h3>Réseaux &amp; légal</h3>
        <ul>
          <li><a href="https://www.facebook.com/CRM.ViVoo/" {EXT}>Facebook</a></li>
          <li><a href="https://www.instagram.com/vivoocrm/" {EXT}>Instagram</a></li>
          <li><a href="https://www.linkedin.com/company/vivoo-crm/" {EXT}>LinkedIn</a></li>
          <li><a href="https://api.whatsapp.com/send?phone=15557480505" {EXT}>WhatsApp</a></li>
          <li><a href="/mentions-legales/">Mentions légales</a></li>
          <li><a href="/conditions/">Conditions d'utilisation</a></li>
          <li><a href="/privacy/">Politique de confidentialité</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Technologies Ilema Inc. Vivoo. Tous droits réservés.</span>
      <span>Éditeur : <a href="https://ilematec.com" {EXT}>Technologies Ilema Inc.</a>, Québec, Canada</span>
    </div>
  </div>
</footer>
<script>
document.querySelectorAll('.has-submenu > a').forEach(function (a) {{
  a.addEventListener('click', function (e) {{
    if (window.innerWidth <= 1080) {{
      e.preventDefault();
      a.parentElement.classList.toggle('open');
      var submenu = a.parentElement.querySelector('.submenu');
      submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
    }}
  }});
}});

(function () {{
  var targets = document.querySelectorAll('.sy-reveal, .vv-reveal');
  if (!document.documentElement.classList.contains('vv-js') || !('IntersectionObserver' in window)) {{
    targets.forEach(function (el) {{ el.classList.add('is-visible'); }});
    return;
  }}
  var io = new IntersectionObserver(function (entries) {{
    entries.forEach(function (entry) {{
      if (entry.isIntersecting) {{
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold: 0.12 }});
  targets.forEach(function (el) {{ io.observe(el); }});
}})();
</script>
</body>
</html>
"""


def breadcrumb_ld(trail):
    items = []
    for i, (name, path) in enumerate(trail, 1):
        it = {"@type": "ListItem", "position": i, "name": name}
        if path:
            it["item"] = BASE + path
        items.append(it)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def breadcrumb_html(trail):
    parts = []
    for name, path in trail[:-1]:
        parts.append(f'<a href="{path}">{name}</a>')
    parts.append(f'<span aria-current="page">{trail[-1][0]}</span>')
    return '<nav class="breadcrumb container sy-crumb" aria-label="Fil d\'Ariane">' + '<span class="sep"> › </span>'.join(parts) + "</nav>\n"


def flow(steps, cls="sy-flow"):
    return f'<ol class="{cls}">' + "".join(f"<li>{s}</li>" for s in steps) + "</ol>"


def chips(items):
    return '<ul class="sy-chips">' + "".join(f'<li class="sy-chip">{c}</li>' for c in items) + "</ul>"


def cta(title="Construisons votre système commercial.", text="Créez votre compte et activez les premiers modules, ou parlez à un spécialiste pour dessiner le parcours adapté à votre activité.", sign="Attirez. Convertissez. Faites revenir."):
    return f"""<section class="sy-cta">
  <div class="sy-wrap">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="sy-actions">
      <a class="btn sy-btn-light" href="{SIGNUP}" {EXT}>Créer mon compte</a>
      <a class="btn sy-btn-ghost" href="{DEMO}" {EXT}>Parler à un spécialiste</a>
    </div>
    <div class="sy-cta-sign">{sign}</div>
  </div>
</section>
"""


def index_label(num, label):
    return f'<p class="sy-index"><b>{num}</b> — {label}</p>' if num else f'<p class="sy-index">{label}</p>'


def page(path, title, desc, active, body, trail=None, extra_ld=None):
    ld = list(extra_ld or [])
    crumb = ""
    if trail:
        ld.insert(0, breadcrumb_ld(trail))
        crumb = breadcrumb_html(trail)
    html = head(title, desc, path, ld) + header(active) + crumb + "<main>\n" + body + "</main>\n" + FOOTER
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    return out
