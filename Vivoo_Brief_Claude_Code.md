# Brief technique — Site web Vivoo (Canada/Québec)
### À l'attention de Claude Code

---

## 1. Contexte

Vivoo est une plateforme d'activation marketing (CRM marketing) multicanal, développée par Technologies Ilema Inc. (Québec, Canada). Le site à construire cible exclusivement le marché Canada/Québec pour cette version. Le contenu de chaque page est déjà rédigé et fourni en Markdown — ce brief couvre tout ce qui entoure ce contenu : stack technique, charte graphique, images, et référencement (SEO classique et pour les moteurs d'intelligence artificielle).

**Positionnement central à respecter partout :** Vivoo est un CRM marketing, pas un CRM de gestion. Il active la relation client, il ne fait pas que la stocker.

---

## 2. Stack technique recommandée

| Élément | Recommandation | Pourquoi |
|---|---|---|
| Framework | **Astro** | Rendu statique par défaut, JS minimal, excellent pour le SEO et pour les crawlers IA qui n'exécutent pas toujours JavaScript |
| Alternative | Next.js (export statique) | Si des fonctionnalités dynamiques sont prévues plus tard (formulaire avancé, blog avec CMS) |
| Contenu | Markdown/MDX dans le repo | Cohérent avec les fichiers déjà livrés (`Vivoo_Page_*.md`) — pas besoin de CMS pour cette V1 |
| Hébergement | Statique (Vercel, Netlify, ou autre à confirmer) | Simplicité, rapidité, coût minimal pour un site vitrine |

Le site doit rester **léger et épuré techniquement** autant que visuellement : pas de framework CSS lourd, pas de librairies JS superflues, pas d'animations complexes.

---

## 3. Arborescence à construire

```
/                      Accueil
/produit               Philosophie, canaux, parcours marketing
/produit/capture               Capture d'audience
/produit/audience-unifiee      Profil d'audience unifié
/produit/campagnes             Campagnes multicanal
/produit/automatisation         Automatisation (programmée, mots-clés, séquences)
/produit/rendez-vous           Prise de rendez-vous
/produit/evenements            Gestion d'événements
/produit/fidelisation          Programme de fidélisation
/produit/scenarios             Scénarios — parcours combinant plusieurs modules
/partenaires           Modèle B2B2B
/cas-clients           MakoFoods, Kinaya, Twish Cart
/faq                   Contient les tarifs (pas de page Tarifs séparée)
/contact
/mentions-legales
/blog                  Structure prête, contenu à venir
```

URL en français, sans accents ni caractères spéciaux (ex. `/secteurs/bien-etre`, pas `/secteurs/bien-être`).

Chaque page module (`/produit/*`) suit un gabarit commun : titre orienté bénéfice (h1), description courte, 3-4 capacités en prose, une FAQ dédiée de 2-3 questions, un CTA. Prévoir un composant de gabarit réutilisable plutôt que 8 pages codées indépendamment.

---

## 4. Contenu à intégrer

Les fichiers suivants sont **rédigés et finaux** — Claude Code les intègre et les structure en HTML sémantique, sans reformuler le texte :

- `Vivoo_Page_Accueil.md`
- `Vivoo_Page_Produit.md`
- `Vivoo_Page_Produit_Capture.md`
- `Vivoo_Page_Produit_AudienceUnifiee.md`
- `Vivoo_Page_Produit_Campagnes.md`
- `Vivoo_Page_Produit_Automatisation.md`
- `Vivoo_Page_Produit_RendezVous.md`
- `Vivoo_Page_Produit_Evenements.md`
- `Vivoo_Page_Produit_Fidelisation.md`
- `Vivoo_Page_Scenarios.md`
- `Vivoo_Page_Partenaires.md`
- `Vivoo_Page_Cas_Clients.md`
- `Vivoo_Page_FAQ.md`
- `Vivoo_Page_Contact.md`
- `Vivoo_Page_Mentions_Legales.md` — **gabarit structurel seulement, révision légale obligatoire avant publication**

Toutes les pages du site sont maintenant rédigées. **Voir `Vivoo_Detail_Pages.md`** pour la table des matières complète avec renvoi vers chaque fichier.

---

## 5. Charte graphique

### Couleurs

| Rôle | Couleur | Code |
|---|---|---|
| Primaire | Navy | `#0B3B61` |
| Secondaire | Bleu | `#3B78A1` |
| Fond principal | Blanc | `#FFFFFF` |
| Fond secondaire / sections alternées | Accent clair | `#EEF4F9` |

Pas de dégradés, pas d'ombres marquées. Le navy porte les titres et les CTA, le bleu les accents et liens, l'accent clair sépare visuellement les sections sans jamais être un vrai contraste.

### Typographie

**Montserrat** (Google Fonts), en 400 (texte courant) et 600 (titres). Hiérarchie simple : h1 unique par page, h2 pour les sections, h3 pour les sous-sections — pas plus de 3 niveaux.

### Style visuel

Beaucoup d'espace blanc, une seule colonne de lecture (max. ~720px) pour le texte, coins arrondis discrets sur les boutons et cartes, aucune icône décorative superflue. L'épuré est un principe, pas une contrainte esthétique secondaire.

### Logo

**À fournir par Nyemo** (fichier SVG ou PNG haute résolution). En attendant, prévoir un wordmark texte « Vivoo » en navy, dans la typographie du site, sans icône associée.

---

## 6. Ton & rédaction

- Français québécois professionnel et chaleureux
- Prose plutôt que listes à puces pour les sections persuasives (déjà respecté dans les fichiers fournis)
- Vocable marketing partout : audience, segments, campagne, scénario d'engagement, programme de fidélisation — jamais « base de données », « fiche contact » ou « CRM centralisé »

---

## 7. Images

| Emplacement | Besoin | Note |
|---|---|---|
| Hero (Accueil) | Illustration épurée liée à l'engagement multicanal | Éviter la photo de stock générique de bureau |
| Canaux (Produit) | Icônes WhatsApp, Messenger, Instagram, SMS, Email | Monochromes navy/bleu — librairie libre type Tabler Icons ou Lucide, cohérente avec le style épuré |
| Cas clients | Logos ou photos de MakoFoods, Kinaya Massothérapeute, Twish Cart | **À fournir par Nyemo si disponibles.** Sinon, blocs texte seuls plutôt qu'un placeholder générique qui sonnerait faux |
| Format | SVG pour icônes/logo, WebP pour photos | Poids optimisé — impact direct sur les Core Web Vitals |

---

## 8. SEO classique (moteurs de recherche traditionnels)

- Balises `title` et `meta description` uniques par page (voir tableau ci-dessous)
- Un seul `h1` par page, structure `Hn` strictement hiérarchique
- Texte alternatif descriptif sur chaque image
- `sitemap.xml` généré automatiquement, `robots.txt` autorisant l'indexation
- Données structurées (schema.org) : `Organization`, `LocalBusiness` (Ilema/Vivoo Québec), `SoftwareApplication` pour Vivoo, `FAQPage` sur la page FAQ, `BreadcrumbList` sur les pages profondes (ex. `/produit/rendez-vous`)
- Core Web Vitals optimisés (LCP, CLS, INP) — cohérent avec un site statique léger
- Mobile-first : la majorité du trafic PME au Québec est mobile

### Metas suggérées par page

| Page | Title | Description |
|---|---|---|
| Accueil | Vivoo — CRM marketing multicanal pour PME québécoises | Vivoo réunit WhatsApp, Messenger, Instagram, SMS et courriel dans une seule plateforme d'activation marketing. Capturez, engagez et fidélisez votre clientèle. |
| Produit | Produit — Vivoo, le CRM marketing qui active la relation client | La philosophie CRM marketing de Vivoo, ses canaux et son parcours en 4 temps : acquisition, engagement, fidélisation, mesure. |
| Partenaires | Devenir partenaire Vivoo — Programme revendeur B2B2B | Rejoignez le réseau de partenaires Vivoo et développez un revenu récurrent en accompagnant vos marchands avec une plateforme clé en main. |
| Cas clients | Cas clients Vivoo — Restauration, bien-être, commerce de gros | Comment MakoFoods, Kinaya Massothérapeute et Twish Cart utilisent Vivoo pour capter, engager et fidéliser leur clientèle. |
| FAQ | FAQ Vivoo — Fonctionnement, tarifs et modèle de crédits | Réponses aux questions les plus fréquentes sur Vivoo : fonctionnement, tarification, canaux supportés et modèle de crédits. |
| Pages modules (×7) | {Titre bénéfice du module} — Vivoo | Reprendre la capacité précise et le mot-clé recherché (ex. « Vivoo automatisation », « Vivoo rendez-vous ») |
| Scénarios | Exemples de parcours client — Vivoo | Découvrez comment les modules Vivoo s'enchaînent dans des parcours réels, d'une publicité Facebook à un rendez-vous confirmé. |

### Gabarit de balises meta (par page)

En observant capturia.io (référence supplémentaire, bien indexé et bien structuré pour les moteurs IA), voici le niveau de détail à répliquer sur chaque page — pas seulement title/description :

```html
<title>{title spécifique à la page}</title>
<meta name="description" content="{description spécifique}">
<link rel="canonical" href="https://vivoo.pro{route}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Vivoo">
<meta property="og:locale" content="fr_CA">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://vivoo.pro/og-image.png">
<meta property="og:url" content="https://vivoo.pro{route}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="https://vivoo.pro/og-image.png">

<meta name="theme-color" content="#0B3B61">
```

Une image OG statique unique suffit pour cette V1 (`og-image.png`, 1200×630, fond navy + wordmark Vivoo). Capturia génère une image OG différente par page dynamiquement — bonne pratique pour plus tard, pas prioritaire ici.

---

## 9. Optimisation pour les moteurs d'intelligence artificielle (GEO)

Les assistants IA (ChatGPT, Perplexity, Copilot, Gemini, etc.) citent de plus en plus souvent des sites directement dans leurs réponses. Quelques principes à appliquer en plus du SEO classique :

- **Rendu statique ou côté serveur obligatoire** — plusieurs crawlers IA n'exécutent pas JavaScript. Si le contenu n'existe que via une injection JS côté client, il devient invisible pour eux. Astro en rendu statique règle ce point par défaut.
- **`robots.txt`** : décider explicitement si les user-agents des crawlers IA (`GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`) sont autorisés ou bloqués — voir point à trancher plus bas.
- **Fichier `llms.txt` à la racine** : un résumé structuré et factuel de Vivoo — positionnement, modules, canaux, secteurs — dans un format que les moteurs IA peuvent consommer directement, sans avoir à parser toute la mise en page du site.
- **Contenu autonome par section** : les moteurs IA citent souvent des extraits isolés de leur contexte. Chaque section doit pouvoir se comprendre seule, sans dépendre fortement de la phrase précédente.
- **FAQ formulée comme un utilisateur la poserait à un assistant** : « Qu'est-ce qu'un CRM marketing ? », « Vivoo remplace-t-il mon système de gestion ? » — avec des réponses courtes et complètes, pas des renvois vers d'autres pages.
- **Définir l'entité dès le premier paragraphe de chaque page** : ne jamais supposer que le lecteur (humain ou crawler) sait déjà ce qu'est Vivoo.
- **Nommage cohérent** : toujours « Vivoo », jamais d'abréviation ou de variante, pour faciliter la reconnaissance d'entité par les moteurs.

Capturia.io applique bien ce principe : le bas de sa page d'accueil contient une vraie mini-FAQ en clair (pas seulement en `FAQPage` schema caché), avec des questions formulées telles qu'on les taperait dans ChatGPT, et des réponses complètes qui se suffisent à elles-mêmes, chiffres à l'appui. Vivoo devrait faire pareil.

### Exemple de FAQ à intégrer (page `/faq` + extrait en bas de l'Accueil)

**Qu'est-ce qu'un CRM marketing ?**
Un CRM marketing est une plateforme qui ne se contente pas de stocker les contacts d'une entreprise — elle les active, à travers des campagnes, des scénarios d'engagement et des programmes de fidélisation. Vivoo est un CRM marketing : il réunit WhatsApp, Messenger, Instagram, SMS et courriel pour transformer une audience captée en clientèle fidèle.

**Vivoo remplace-t-il mon système de gestion actuel ?**
Non. Vivoo ne remplace pas vos outils de gestion (facturation, inventaire, ERP) — il vient s'y ajouter comme la couche qui gère la relation avec vos clients. Vos outils de gestion structurent vos opérations ; Vivoo active la relation avec votre audience.

**Quels canaux Vivoo prend-il en charge ?**
Vivoo réunit cinq canaux dans une seule plateforme : WhatsApp, Messenger, Instagram, SMS et courriel. Chaque profil client reste unifié peu importe le canal utilisé pour vous contacter.

**Comment fonctionne le modèle de partenariat Vivoo ?**
Vivoo fonctionne selon un modèle à trois niveaux : Vivoo opère la plateforme, un réseau de partenaires déploie Vivoo auprès de leur portefeuille de marchands, et chaque marchand l'utilise pour engager sa propre clientèle.

**Combien coûte Vivoo ?**
La tarification de Vivoo repose sur un abonnement aux modules et une consommation de crédits de communication selon le volume de messages envoyés. Le tarif exact dépend de votre secteur et de votre volume — contactez-nous pour un devis adapté.

---

## 10. À trancher ou à fournir avant le développement

- [ ] Logo Vivoo (fichier source)
- [ ] Photos ou logos réels des cas clients (MakoFoods, Kinaya Massothérapeute, Twish Cart)
- [ ] Témoignages clients réels (actuellement en placeholder dans le contenu Accueil)
- [ ] Courriel et téléphone de contact (page Contact)
- [ ] Révision de la page Mentions légales par un professionnel du droit — obligatoire avant publication, notamment pour la conformité à la Loi 25 (Québec)
- [ ] Autoriser ou bloquer les crawlers IA dans `robots.txt`
- [ ] Préférence d'hébergement (Vercel, Netlify, autre)
