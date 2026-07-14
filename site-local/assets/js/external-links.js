/**
 * external-links.js — Ouvre tous les liens externes dans un nouvel onglet
 * S'applique aux liens qui pointent en dehors du site BAVI LEO.
 * Exécuté après le chargement du DOM.
 */
document.addEventListener('DOMContentLoaded', function() {
  const siteUrl = (document.querySelector('meta[property="og:url"]') || {}).content
    || window.location.origin + window.location.pathname.split('/').slice(0, 3).join('/');

  document.querySelectorAll('a[href]').forEach(function(link) {
    const href = link.getAttribute('href');
    if (!href) return;

    // Ignorer les ancres internes, les liens relatifs (même site), javascript:, mailto:, tel:
    if (href.startsWith('#') || href.startsWith('javascript:') ||
        href.startsWith('mailto:') || href.startsWith('tel:')) return;

    // Les liens relatifs (sans protocole, sans //) pointent vers le même site
    if (!href.startsWith('http://') && !href.startsWith('https://') && !href.startsWith('//')) return;

    // Vérifier si c'est un lien externe
    try {
      const linkUrl = new URL(href, window.location.origin);
      const currentOrigin = window.location.origin;

      // Si c'est le même origin et le même chemin de base, c'est interne
      if (linkUrl.origin === currentOrigin) return;
    } catch(e) {
      return; // URL malformée, on ignore
    }

    // Lien externe → target="_blank" + rel pour sécurité
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
  });
});
