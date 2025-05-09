const CACHE_NAME = '2equals12-cache-v1';
const urlsToCache = [
  '/',
  '/topics',
  '/quotes',
  '/about',
  '/static/css/styles.css',
  '/static/img/logo.svg',
  '/static/img/favicon.svg'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
