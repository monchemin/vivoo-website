# Vivoo — Page : Intégrations
### `/integrations`

---

## Vivoo s'intègre à vos outils

Votre CRM, votre tableur, Zapier, Make ou n8n : Vivoo leur transmet ce qui se passe dans votre système commercial, et reçoit ce qu'ils savent de vos clients. Vos outils restent à jour, sans double saisie.

---

## 01. Vivoo informe vos outils

Dès qu'un événement se produit, Vivoo l'envoie à l'adresse de votre choix.

**Nouveau lead.** Un contact est créé dans Vivoo, avec la page d'où il vient quand il arrive d'une page.

**Lead devenu client.** Le contact passe à l'achat.

**Contact modifié.** Ses informations changent, ou il remplit de nouveau une de vos pages.

**Rendez-vous pris.** Une réservation arrive, en ligne ou dans une conversation.

**Rendez-vous modifié.** Il est déplacé, annulé, confirmé ou effectué.

**Messages reçus.** Un client vous écrit sur WhatsApp, Messenger ou Instagram, canal par canal.

**Commentaires reçus.** Quelqu'un commente une publication de votre page Facebook ou de votre compte Instagram.

Vous choisissez les événements à recevoir. Les messages et les commentaires ne sont transmis que si vous les cochez.

---

## 02. Vos outils alimentent Vivoo

**Votre boutique en ligne.** Shopify, WooCommerce, Square ou Clover : vos ventes s'ajoutent au profil de chaque client.

**Vos formulaires et vos applications.** L'API de Vivoo reçoit vos nouveaux leads, vos clients et vos commandes, qui entrent aussitôt dans vos campagnes et vos scénarios d'engagement.

---

## 03. Pour votre équipe technique

- Chaque événement est envoyé en POST, au format JSON : `id`, `type`, `version`, `created_at`, `merchant_id`, `data`.
- Chaque envoi est signé avec votre secret (en-tête `Vivoo-Signature`, HMAC SHA-256 avec horodatage).
- L'identifiant de l'événement permet d'ignorer un envoi reçu deux fois.
- En cas d'échec, Vivoo réessaie à intervalles croissants pendant plus d'une journée, et vous prévient si l'adresse ne répond plus pendant plusieurs jours.
- Un journal des envois et un bouton de test sont disponibles dans vos réglages.
- Jusqu'à trois adresses par compte.

---

## Questions fréquentes

**Faut-il un développeur ?**
Non pour Zapier, Make ou n8n : vous collez l'adresse qu'ils vous donnent et vous cochez les événements. Un développeur n'est utile que pour brancher votre propre application.

**Les messages de mes clients sont-ils transmis à mes outils ?**
Seulement si vous le décidez : les messages et les commentaires sont des événements à cocher, canal par canal.

**Comment mon outil sait-il que l'envoi vient bien de Vivoo ?**
Chaque envoi est signé avec un secret que vous seul connaissez. Votre outil vérifie la signature avant de traiter l'événement.

---

## CTA final

**Vos outils et Vivoo, enfin à jour en même temps.**

**[ Créer mon compte ]** **[ Parler à un spécialiste ]**
