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
