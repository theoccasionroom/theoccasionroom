// Two small behaviors. Elementor has built-in equivalents for both:
// the Nav Menu widget's mobile toggle and the Countdown widget.

// Mobile menu toggle
const toggle = document.querySelector('.menu-toggle');
const nav = document.getElementById('main-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
  });
}

// Live countdown
document.querySelectorAll('[data-countdown]').forEach((el) => {
  const target = new Date(el.dataset.countdown).getTime();
  const units = {};
  el.querySelectorAll('[data-unit]').forEach((span) => { units[span.dataset.unit] = span; });
  const pad = (n) => String(n).padStart(2, '0');

  const tick = () => {
    const left = Math.max(0, target - Date.now());
    const s = Math.floor(left / 1000);
    units.days.textContent = Math.floor(s / 86400);
    units.hours.textContent = pad(Math.floor((s % 86400) / 3600));
    units.minutes.textContent = pad(Math.floor((s % 3600) / 60));
    units.seconds.textContent = pad(s % 60);
  };
  tick();
  setInterval(tick, 1000);
});
