// Preloader animation
document.addEventListener('DOMContentLoaded', function() {
    const preloader = document.getElementById('preloader');
  
    document.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', function(event) {
        const href = link.getAttribute('href');
        if (href && !href.startsWith('#') && !href.startsWith('javascript')) {
          preloader.classList.remove('hidden');
        }
      });
    });
  
    window.addEventListener('load', () => {
      preloader.classList.add('hidden');
    });
  });
  
  // Scroll-based Nav Background Color
  const nav = document.getElementById('main-nav');
  const navLinks = document.getElementById('nav-links');
  
  if (nav && navLinks) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 100) {
        nav.classList.remove('bg-transparent');
        nav.classList.add('bg-white', 'bg-opacity-90', 'shadow-md');
        navLinks.classList.remove('text-white');
        navLinks.classList.add('text-black');
      } else {
        nav.classList.add('bg-transparent');
        nav.classList.remove('bg-white', 'bg-opacity-90', 'shadow-md');
        navLinks.classList.add('text-white');
        navLinks.classList.remove('text-black');
      }
    });
  }

  