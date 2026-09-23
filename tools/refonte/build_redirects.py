"""Anciennes URL remplacées par la refonte : redirections simples."""
import os
from build_common import ROOT


def redirect(rel, target, title):
    html = f'''<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="UTF-8">
<title>{title}. Vivoo</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://vivoo.pro{target}">
<meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
<p>Cette page a déménagé : <a href="{target}">{title}</a>.</p>
</body>
</html>
'''
    with open(os.path.join(ROOT, rel), "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    redirect("produit/index.html", "/solution/", "Le système Vivoo")
    redirect("produit/scenarios/index.html", "/scenarios/", "Scénarios")
    print("ok")
