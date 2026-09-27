"""Pages /produit/* (modules en détail) au style de la refonte.

Le contenu vient de modules.json (extrait des anciennes pages) : c'est ce
fichier qu'il faut modifier pour changer le texte d'un module.
"""
import json, os
from build_common import *
from build_data import PILLARS

HERE = os.path.dirname(os.path.abspath(__file__))
PMAP = {p["slug"]: p for p in PILLARS}

MODULES = [
    ("capture", "Capture d'audience", "acquisition"),
    ("prospection", "Prospection", "acquisition"),
    ("audience-unifiee", "Audience unifiée", "conversation"),
    ("rendez-vous", "Rendez-vous", "conversion"),
    ("commerce", "Commerce connecté", "vente"),
    ("evenements", "Gestion d'événements", "vente"),
    ("campagnes", "Campagnes multicanal", "fidelisation"),
    ("fidelisation", "Programme de fidélisation", "fidelisation"),
    ("reputation", "Réputation", "fidelisation"),
    ("automatisation", "Automatisation", "automatisation"),
]


def paras(ps):
    return "".join(f"<p>{p}</p>" for p in ps)


def build_module(slug, name, pillar, data):
    p = PMAP[pillar]
    feats = data["features"]
    cols = "sy-steps--3" if len(feats) % 3 == 0 else "sy-steps--4"
    features = "".join(
        f'<li><span class="sy-step-num">{i:02d}</span><h3>{h}</h3>{paras(ps)}</li>'
        for i, (h, ps) in enumerate(feats, 1)
    )
    extra = ""
    for h, ps, _ in data.get("extra", []):
        extra += f"""
<section class="sy-section sy-dark sy-reveal">
  <div class="sy-wrap sy-split">
    <div>{index_label("", "En plus")}<h2 class="sy-h2">{h}</h2></div>
    <div><p class="sy-lead">{" ".join(ps)}</p></div>
  </div>
</section>"""
    faq = "".join(f'<div class="faq-item"><h3>{q}</h3>{paras(a)}</div>' for q, a in data.get("faq", []))
    siblings = [(s, n) for s, n, pl in MODULES if pl == pillar and s != slug]
    related = f'<a class="sy-card" href="/solution/{pillar}/"><span class="sy-card-num">Pôle {p["num"]} · {p["verb"]}</span><h3>{p["name"]}</h3><p>{p["tagline"]}</p><span class="sy-card-more">Voir le pôle →</span></a>'
    for s, n in siblings:
        related += f'<a class="sy-card" href="/produit/{s}/"><span class="sy-card-num">Module du même pôle</span><h3>{n}</h3><p>{DATA[s]["h1"]}.</p><span class="sy-card-more">En détail →</span></a>'
    sid, stitle = p["scenario"]
    related += f'<a class="sy-card" href="/scenarios/#{sid}"><span class="sy-card-num">Scénario</span><h3>{stitle}</h3><p>Voyez ce module s\'enchaîner avec les autres dans un parcours complet.</p><span class="sy-card-more">Voir le scénario →</span></a>'

    n_related = len(siblings) + 2
    body = f"""
<section class="sy-page-hero">
  <div class="sy-wrap">
    <a class="sy-back" href="/solution/{pillar}/">← Pôle {p['name']}</a>
    <p class="sy-index"><span class="sy-mod-icon" aria-hidden="true">{data['icon']}</span><b>{p['num']}</b> — Module · {name}</p>
    <h1 class="sy-display">{data['h1']}</h1>
    <p class="sy-lead">{" ".join(data['lead'])}</p>
  </div>
  <span class="sy-ghost-num" aria-hidden="true">{p['num']}</span>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("01", "Ce que le module permet")}<h2 class="sy-h2">{name}, concrètement.</h2></div>
      <p class="sy-lead">Un module du pôle {p['name'].lower()} : {p['tagline'][0].lower() + p['tagline'][1:]}</p>
    </div>
    <ol class="sy-steps {cols}">{features}</ol>
  </div>
</section>
{extra}
<section class="sy-section sy-alt sy-reveal">
  <div class="sy-wrap sy-narrow">
    {index_label("02", "Questions fréquentes")}
    {faq}
  </div>
</section>

<section class="sy-section sy-reveal">
  <div class="sy-wrap">
    <div class="sy-head sy-head--split">
      <div>{index_label("03", "Dans le système")}<h2 class="sy-h2">Ce module ne travaille jamais seul.</h2></div>
      <p class="sy-lead">Chaque module s'inscrit dans un pôle, et chaque pôle nourrit le suivant.</p>
    </div>
    <div class="sy-cards{' sy-cards--3' if n_related == 3 else ''}">{related}</div>
  </div>
</section>
{cta(data['cta'], " ".join(data.get('cta_p') or []) or "Créez votre compte et activez ce module, ou parlez à un spécialiste pour l'intégrer à votre parcours.")}"""
    page(f"/produit/{slug}/", data["title"], data["desc"], "solution/" + pillar, body,
         trail=[("Accueil", "/"), ("Produit", "/solution/"), (p["name"], f"/solution/{pillar}/"), (name, None)],
         extra_ld=data.get("jsonld"))


DATA = json.load(open(os.path.join(HERE, "modules.json"), encoding="utf-8"))

if __name__ == "__main__":
    for slug, name, pillar in MODULES:
        build_module(slug, name, pillar, DATA[slug])
    print("ok")
