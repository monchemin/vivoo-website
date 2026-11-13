/* Formulaires du site branchés sur Vivoo (pages d'acquisition gérées hors de Vivoo).
 * Chaque <form data-vivoo-form="<slug>"> envoie à https://api.vivoo.pro/public/form/<slug>/submit
 * et compte sa vue sur /track au chargement. Pas de pixel Meta : Vivoo transmet lui-même
 * les événements (fbclid gardé en sessionStorage). */
(function () {
  var API = 'https://api.vivoo.pro/public/form/';
  var forms = document.querySelectorAll('form[data-vivoo-form]');
  if (!forms.length) return;

  var MESSAGES = {
    ME23C: 'Indiquez au moins votre courriel ou votre numéro de téléphone.',
    '1001': 'Certaines informations ne sont pas valides. Vérifiez le formulaire.',
    '4004': 'Écrivez votre message avant d\'envoyer.',
    ME22: 'Ce formulaire n\'est pas disponible pour le moment. Écrivez-nous à contact@vivoo.pro.',
    PUBLIC_SUBMIT_RATE_LIMITED: 'Trop d\'envois en peu de temps. Réessayez dans quelques minutes.'
  };

  function store(get, key, value) {
    try { return get ? sessionStorage.getItem(key) : sessionStorage.setItem(key, value); } catch (e) { return null; }
  }
  function cookie(name) {
    var m = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : '';
  }

  var fbclid = new URLSearchParams(location.search).get('fbclid');
  if (fbclid) store(false, 'vivoo_fbclid', fbclid);
  else fbclid = store(true, 'vivoo_fbclid');

  function tracking() {
    var t = {};
    if (fbclid) t.fbclid = fbclid;
    var fbp = cookie('_fbp'), fbc = cookie('_fbc');
    if (fbp) t.fbp = fbp;
    if (fbc) t.fbc = fbc;
    return t;
  }

  forms.forEach(function (form) {
    var slug = form.getAttribute('data-vivoo-form');

    // Vue de la page
    var view = tracking();
    view.pageUrl = location.origin + location.pathname;
    fetch(API + slug + '/track', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(view),
      keepalive: true
    }).catch(function () {});

    var tel = form.elements.tel;
    var waBox = form.querySelector('[data-wa-question]');
    var status = form.querySelector('[data-form-status]');
    var button = form.querySelector('button[type="submit"]');

    function toggleWa() {
      if (!waBox) return;
      var show = tel.value.trim() !== '';
      waBox.hidden = !show;
      if (!show) waBox.querySelectorAll('input').forEach(function (i) { i.checked = false; });
    }
    if (tel) { tel.addEventListener('input', toggleWa); toggleWa(); }

    function showError(text) {
      status.textContent = text;
      status.hidden = false;
      status.focus();
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.hidden = true;

      if (!form.checkValidity()) { form.reportValidity(); return; }
      var digits = tel.value.replace(/\D/g, '');
      if (digits.length < 7) {
        tel.focus();
        showError('Indiquez un numéro de téléphone complet.');
        return;
      }

      var f = form.elements;
      var body = {
        name: f.name.value.trim(),
        lastName: f.lastName.value.trim(),
        email: f.email.value.trim(),
        tel: tel.value.trim(),
        subject: f.subject.value.trim(),
        message: f.message.value.trim(),
        website: f.website.value
      };
      if (!/^\s*\+/.test(body.tel)) body.countryCode = f.countryCode.value;
      var wa = form.querySelector('input[name="whatsappEnabled"]:checked');
      if (wa && wa.value === 'oui') body.whatsappEnabled = true;
      if (f.consent.checked) body.consentAt = new Date().toISOString();
      var t = tracking();
      for (var k in t) body[k] = t[k];

      button.disabled = true;
      var label = button.textContent;
      button.textContent = 'Envoi en cours…';

      fetch(API + slug + '/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      }).then(function (res) {
        if (res.status === 201) {
          var done = form.parentElement.querySelector('[data-form-done]');
          done.querySelector('[data-done-name]').textContent = body.name;
          form.hidden = true;
          done.hidden = false;
          done.focus();
          return;
        }
        return res.json().catch(function () { return {}; }).then(function (err) {
          showError(MESSAGES[err.code] || (res.status >= 500
            ? 'Le service ne répond pas pour le moment. Réessayez dans quelques minutes.'
            : 'L\'envoi n\'a pas abouti. Vérifiez le formulaire et réessayez.'));
        });
      }).catch(function () {
        showError('Connexion impossible. Vérifiez votre connexion Internet et réessayez.');
      }).then(function () {
        button.disabled = false;
        button.textContent = label;
      });
    });
  });
})();
