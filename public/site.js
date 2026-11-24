const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
menu?.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('is-open', open);
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') {
    menu.click(); menu.focus();
  }
});

const viewer = document.querySelector('#image-viewer');
let lastTrigger;
document.querySelectorAll('[data-enlarge]').forEach(button => {
  button.addEventListener('click', () => {
    lastTrigger = button;
    const source = button.querySelector('img');
    viewer.querySelector('img').src = source.src;
    viewer.querySelector('img').alt = source.alt;
    viewer.querySelector('.viewer-caption').textContent = button.dataset.caption || source.alt;
    viewer.showModal();
    document.body.classList.add('modal-open');
  });
});
viewer?.querySelector('.viewer-close').addEventListener('click', () => viewer.close());
viewer?.addEventListener('click', e => { if (e.target === viewer) viewer.close(); });
viewer?.addEventListener('close', () => {document.body.classList.remove('modal-open');lastTrigger?.focus();});

const carousel = document.querySelector('.carousel-track');
if (carousel) {
  const slides = [...carousel.children];
  const prev = document.querySelector('[data-slide="prev"]');
  const next = document.querySelector('[data-slide="next"]');
  const status = document.querySelector('.slide-status');
  let index = 0;
  function update() {
    prev.disabled = index === 0;next.disabled = index === slides.length - 1;
    status.textContent = `${index + 1} / ${slides.length}`;
  }
  function step(delta) {
    index = Math.max(0, Math.min(slides.length-1, index+delta));
    carousel.scrollTo({left: slides[index].offsetLeft - slides[0].offsetLeft, behavior: 'instant'});
    update();
  }
  prev.addEventListener('click', () => step(-1));next.addEventListener('click', () => step(1));
  carousel.addEventListener('keydown', e => {if(['ArrowLeft','ArrowRight'].includes(e.key)){e.preventDefault();step(e.key==='ArrowRight'?1:-1);}});
  let timer;
  carousel.addEventListener('scroll', () => {clearTimeout(timer);timer=setTimeout(()=>{index=slides.reduce((best,s,i)=>Math.abs(s.offsetLeft-slides[0].offsetLeft-carousel.scrollLeft)<Math.abs(slides[best].offsetLeft-slides[0].offsetLeft-carousel.scrollLeft)?i:best,0);update();},100);});
  update();
}


// Four separate hinges, inspired by Mariana's "Dance with Patrick" recording.
// Returning from a hover settles from the current pose instead of snapping to rest.
const puppetMotionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
document.querySelectorAll('.puppet-token').forEach(puppet => {
  const trigger = puppet.closest('a');
  if (!trigger) return;
  let hovered = false;
  let focused = false;
  let motions = [];
  let dancing = false;
  const limbs = [...puppet.querySelectorAll('[data-limb]')];
  const body = puppet.querySelector('.puppet-dance');
  const offsets = [0, .16, .30, .49, .66, .84, 1];
  const poses = {
    'upper-left': [0, 24, 15, 31, -4, 13, 0],
    'upper-right': [0, -18, -29, -12, 4, -23, 0],
    'lower-left': [0, 64, 78, 9, 48, -5, 0],
    'lower-right': [0, -77, -61, -15, -52, 5, 0]
  };
  function settle() {
    const targets = [...limbs, body];
    const current = targets.map(el => getComputedStyle(el).transform);
    motions.forEach(motion => motion.cancel());
    motions = [];
    dancing = false;
    if (puppetMotionPreference.matches) return;
    targets.forEach((el, i) => {
      motions.push(el.animate([{transform: current[i]}, {transform: 'none'}], {
        duration: 650, easing: 'cubic-bezier(.2,.85,.25,1)', fill: 'none'
      }));
    });
  }
  function update() {
    const shouldDance = (hovered || focused) && !puppetMotionPreference.matches && !document.hidden && !puppet.closest('.study-paused');
    if (shouldDance === dancing) return;
    if (!shouldDance) { settle(); return; }
    motions.forEach(motion => motion.cancel());
    motions = limbs.map((limb, i) => limb.animate(poses[limb.dataset.limb].map((angle, n) => ({
      transform: `rotate(${angle}deg)`, offset: offsets[n]
    })), {duration: 3100, delay: -i * 95, iterations: Infinity, easing: 'cubic-bezier(.4,0,.25,1)'}));
    motions.push(body.animate([
      {transform: 'translateY(0px) rotate(0deg)'},
      {transform: 'translateY(-28px) rotate(-1.4deg)', offset: .29},
      {transform: 'translateY(8px) rotate(1.1deg)', offset: .65},
      {transform: 'translateY(0px) rotate(0deg)'}
    ], {duration: 3100, iterations: Infinity, easing: 'ease-in-out'}));
    dancing = true;
  }
  trigger.addEventListener('pointerenter', e => {if(e.pointerType !== 'touch'){hovered = true;update();}});
  trigger.addEventListener('pointerleave', () => {hovered = false;update();});
  trigger.addEventListener('focus', () => {focused = true;update();});
  trigger.addEventListener('blur', () => {focused = false;update();});
  puppetMotionPreference.addEventListener('change', () => {
    if (puppetMotionPreference.matches) settle();
    update();
  });
  document.addEventListener('visibilitychange', update);
  document.addEventListener('portfolio:motionchange', update);
});

// A study-wide pause lets visitors inspect the objects without continuous motion.
document.querySelectorAll('.study-motion-toggle').forEach(button => {
  const study = button.closest('.study-cabinet-wrap');
  button.addEventListener('click', () => {
    const paused = study.classList.toggle('study-paused');
    button.setAttribute('aria-pressed', String(paused));
    button.textContent = paused ? 'Resume motion' : 'Pause motion';
    document.dispatchEvent(new Event('portfolio:motionchange'));
  });
});
