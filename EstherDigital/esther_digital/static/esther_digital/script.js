'use strict';

/* Shared header and footer (edit once, shows on every page). */
const ALL_LINKS = {
  products: ['Products', '/products/'],
  about: ['About us', '/#about-us'],
  contact: ['Contact us', 'contact.html']
};
const navKeys = (document.body.dataset.nav || 'products,about,contact').split(',');
const LINKS = navKeys.map(k => ALL_LINKS[k.trim()]).filter(Boolean);
const logo = `<a href="/" aria-label="Esther Digital home" class="w-fit whitespace-nowrap py-3 text-2xl leading-tight md:text-[1.75rem]"><strong class="font-semibold">Esther</strong><span class="font-light">Digital</span></a>`;
const link = ([t, h], c = '') => `<a href="${h}" class="${c}">${t}</a>`;

document.getElementById('site-header').outerHTML = `
<header id="site-header" class="relative z-10 grid grid-cols-[minmax(0,1fr)_auto] items-center p-2.5">
  ${logo}
  <nav aria-label="Main navigation" class="hidden items-center gap-[47px] p-2.5 md:flex">${LINKS.map(l => link(l, 'hover:underline hover:underline-offset-4')).join('')}</nav>
  <button id="menu-toggle" type="button" aria-controls="mobile-nav" aria-expanded="false" aria-label="Open menu" class="min-h-12 min-w-14 cursor-pointer rounded-lg p-2.5 md:hidden">
    <span id="icon-open" aria-hidden="true" class="flex w-9 flex-col gap-[7px]"><span class="h-[3px] w-9 bg-black"></span><span class="h-[3px] w-[18px] bg-black"></span><span class="h-[3px] w-9 bg-black"></span></span>
    <svg id="icon-close" aria-hidden="true" class="hidden h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="m6 6 12 12M18 6 6 18"/></svg>
  </button>
  <nav id="mobile-nav" aria-label="Mobile navigation" class="absolute right-2.5 top-[calc(100%-4px)] hidden min-w-[180px] flex-col gap-[18px] rounded-lg border border-line bg-sand px-5 py-3 text-base shadow-card">${LINKS.map(l => link(l)).join('')}</nav>
</header>`;

document.getElementById('site-footer').outerHTML = `
<footer class="mt-[57px] grid gap-2.5 bg-moss p-5 md:min-h-[324px] md:grid-cols-3">
  <div class="flex flex-col items-center gap-5 p-2.5 md:items-start">${logo}</div>
  <div class="flex flex-col items-center gap-5 p-2.5 md:items-start">
    <h2 class="text-base font-light md:text-lg">Shop now</h2>
    <a href="/products/" class="text-sm hover:underline hover:underline-offset-4">Products</a>
  </div>
  <div class="flex flex-col items-center gap-5 p-2.5 md:items-start">
    <a href="contact.html" class="text-base font-light hover:underline hover:underline-offset-4 md:text-lg">Contact us</a>
  </div>
</footer>`;

/* Mobile menu */
const header = document.getElementById('site-header');
const toggle = document.getElementById('menu-toggle');
const menu = document.getElementById('mobile-nav');

function setMenu(open, returnFocus = false) {
  menu.classList.toggle('hidden', !open);
  menu.classList.toggle('flex', open);
  document.getElementById('icon-open').classList.toggle('hidden', open);
  document.getElementById('icon-close').classList.toggle('hidden', !open);
  toggle.setAttribute('aria-expanded', String(open));
  toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  if (!open && returnFocus) toggle.focus();
}
toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
document.addEventListener('click', e => { if (!header.contains(e.target)) setMenu(false); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false, true); });
window.matchMedia('(min-width: 768px)').addEventListener('change', () => setMenu(false));

/* Contact form (no message service connected yet) */
const form = document.getElementById('contact-form');
if (form) form.addEventListener('submit', e => {
  e.preventDefault();
  document.getElementById('form-notice').classList.remove('hidden');
});

/* Purchase dialog */
const dialog = document.getElementById('purchase-dialog');
if (dialog) {
  document.getElementById('buy-button').addEventListener('click', () => dialog.showModal());
  document.getElementById('close-dialog').addEventListener('click', () => dialog.close());
}
