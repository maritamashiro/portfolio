"""Build a portable static portfolio using Python's standard library only."""
from pathlib import Path
import shutil
import hashlib
import re
from html import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)
shutil.copytree(ROOT / 'public', OUT, dirs_exist_ok=True)
STYLE_VERSION = hashlib.sha256((ROOT / 'public/style.css').read_bytes()).hexdigest()[:10]
SCRIPT_VERSION = hashlib.sha256((ROOT / 'public/site.js').read_bytes()).hexdigest()[:10]

ICONS = {
'leaf': '<path d="M25 139 Q6 49 141 22 Q155 117 25 139Z" fill="#dce4cc"/><path d="M19 151 121 40M48 115 40 75M70 94 110 93M91 73 86 44"/><path d="M38 126 68 109 61 87 96 69 100 51" stroke="#b87349" stroke-width="7"/><circle cx="41" cy="125" r="12" fill="#b5b1a6"/><path d="M95 45h11v13H95Z" fill="#f5d66f"/>',
'mask': '<path d="M20 56 Q49 35 78 59 Q111 33 143 50 L134 89 Q103 120 81 95 Q45 117 23 86Z"/><path d="M34 68Q54 54 67 72Q53 84 34 68ZM95 70Q111 53 130 65Q114 83 95 70Z"/><path d="M23 87Q9 116 17 137M136 87Q155 104 148 124"/><path d="M53 25 46 13M71 24 74 9" stroke="#eb007a"/>',
'creature': '<path d="M37 57Q56 35 85 50Q120 36 136 71L127 106Q94 124 57 109Q35 104 37 57Z" fill="#e9a070"/><ellipse cx="70" cy="46" rx="8" ry="21"/><ellipse cx="98" cy="43" rx="7" ry="21"/><circle cx="70" cy="44" r="2" fill="#211e1c"/><circle cx="98" cy="42" r="2" fill="#211e1c"/><path d="M68 79Q85 94 101 78M58 110 47 137M113 112 127 135"/><circle cx="111" cy="92" r="14" fill="#c4bfad"/><path d="M110 78 95 67" stroke="#b87349" stroke-width="5"/>',
'mechanism': '<path d="M29 50 113 36 143 56 57 70ZM29 50V124L58 145V70M58 145 145 128V56M29 124 114 109 145 128M114 36V109"/><ellipse cx="92" cy="101" rx="19" ry="31"/><path d="M53 100 150 84 158 95 165 94M79 21Q111 1 137 24"/><path d="m130 11 7 13-16-1" stroke="#eb007a"/>',
'eye': '<path d="M15 82Q79 7 149 78Q84 145 15 82Z"/><ellipse cx="81" cy="78" rx="24" ry="29"/><circle cx="81" cy="78" r="10" fill="#211e1c"/><path d="M20 41V21H43M126 21H148V40M20 118V137H43M126 137H148V116" stroke="#eb007a"/>',
'paper': '<path d="M29 30 122 23 137 137 35 143Z" fill="#fffaf2"/><path d="m103 26 1 25 22-5M45 69 111 62M47 85 114 79M48 102 93 98M48 120 105 114"/>',
'shell': '<path d="M80 133Q5 112 21 58Q29 30 51 42Q65 17 87 31Q108 17 121 45Q146 42 149 68Q157 110 80 133ZM80 133 39 47M80 133 62 35M80 133 86 32M80 133 112 40M80 133 141 66M80 133 23 76"/>',
'heart': '<path d="M83 133 19 63 36 29 66 25 83 45 104 25 133 29 150 63Z" stroke="#b95c5c"/><path d="M19 63 66 25 83 133 104 25 150 63M19 63 83 45 150 63" stroke="#b95c5c"/>',
'pencil': '<path d="m54 137 6-97 11-22 9 23-7 98Z"/><path d="m60 40 20 1M61 128l13 1M70 20l1 11"/><path d="m98 142 2-93 11-21 10 23-10 94Z"/><path d="m100 49 21 2M101 132l11 1"/>',
'flower': '<path d="M82 137Q63 88 89 63M89 63Q53 57 58 32Q73 18 88 44Q94 9 111 23Q125 41 104 54Q142 43 144 65Q140 88 106 70Q121 100 99 102Q82 96 89 63Z"/><path d="M77 112Q39 117 41 91Q68 86 77 112Z"/>',
 'ornament': '<path d="M54 29Q77 9 105 30L122 69Q120 123 83 140Q39 117 42 70Z" stroke="#b87349"/><path d="M54 29Q85 64 105 30M43 74Q79 98 120 70M53 112Q82 91 110 115"/><circle cx="82" cy="61" r="8" fill="#e9a070"/>',
'connected': '<path d="M30 85H88L82 132H39ZM88 97Q121 86 113 109Q108 119 86 116M48 66Q36 53 49 39M67 66Q56 52 69 39M109 51Q122 38 137 51M100 39Q123 15 147 38"/><circle cx="123" cy="61" r="3" fill="#eb007a"/>',
'installation': '<path d="M24 56 79 29 146 48 90 78ZM24 56V133L90 152V78M90 152 146 120V48"/><path d="M44 88 67 96 64 119 41 110Z" fill="#dce4cc"/><circle cx="114" cy="100" r="15" fill="#e9a070"/><path d="m48 48 13-7 10 5-13 7Z" fill="#eb007a"/>',
'typewriter': '<path d="M46 62 43 18 123 21 120 63M27 64 139 62 153 132 15 132ZM40 76 128 76 136 113 30 114ZM41 124H122M56 33H111M56 45H97M23 58H39M128 56H145"/><path d="M43 86H125M38 98H131M53 77 48 112M70 77 67 112M88 77 88 112M105 77 109 112"/>',
'arrow': '<path d="M22 142Q124 114 119 29M93 47 120 25 140 52" stroke="#eb007a" stroke-width="4"/>',
}

def icon(name, cls='', title=''):
    return f'<svg class="drawn {cls}" viewBox="0 0 170 170" aria-hidden="true">{ICONS[name]}</svg>'

def image(name, alt='', cls='', lazy=True):
    return f'<img src="{{base}}assets/{name}" alt="{escape(alt, quote=True)}" class="{cls}" {"loading=lazy" if lazy else "fetchpriority=high"} decoding="async">'

def photo(name, alt, cls=''):
    return f'<button class="photo-button {cls}" data-enlarge data-caption="{escape(alt, quote=True)}" aria-label="Enlarge: {escape(alt, quote=True)}">{image(name, alt)}</button>'

NAV=[('work/','Work'),('on-my-desk/','On my desk'),('illustration/','Illustration'),('about/','About me'),('contact/','Contact')]

def page(route, title, body, active='', desc='The portfolio of Mariana Tamashiro: creative technologist, educator, tinkerer.'):
    depth=route.strip('/').count('/')+1 if route else 0
    base='../'*depth
    links=''.join(f'<a href="{base}{path}"'+(' aria-current="page"' if label==active else '')+f'>{label.lower()}</a>' for path,label in NAV)
    html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#faf6ee"><title>{escape(title)} · Mariana Tamashiro</title><meta name="description" content="{escape(desc,quote=True)}"><link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="{base}fonts/courier-prime-regular.ttf" as="font" type="font/ttf" crossorigin><link rel="stylesheet" href="{base}style.css?v={STYLE_VERSION}"><script src="{base}site.js?v={SCRIPT_VERSION}" defer></script></head>
<body><a class="skip-link" href="#main">Skip to content</a><header class="site-header"><a href="{base or './'}" class="signature" aria-label="Mariana Tamashiro, home">MARIANA<br>TAMASHIRO</a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation">Menu</button><nav id="navigation" class="site-nav" aria-label="Main navigation">{links}</nav></header>
<main id="main">{body.replace('{base}',base)}</main><footer class="site-footer"><span>Mariana Tamashiro · made with curiosity</span><a href="mailto:mari.tamashiro@gmail.com">Let's make something together</a></footer>
<dialog class="viewer" id="image-viewer" aria-label="Enlarged image"><button class="viewer-close">Close</button><img alt=""><p class="viewer-caption"></p></dialog></body></html>'''
    dest=OUT/route/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(html)

# The Markdown document controls homepage project names, questions, and order.
PROJECTS = re.findall(r'^## (.+)\n+([^\n]+)', (ROOT/'content/portfolio-project-questions.md').read_text(), re.M)
QUESTIONS = dict(PROJECTS)
PRESENTATION = {
    'Xenoflora Olfacta': ('xenoflora', None),
    'Beyond Ornaments': ('beyond-ornaments', 'ornament'),
    'Creature Kit': ('creature-kit', 'creature'),
    'Teaching IoT': ('teaching-iot', 'connected'),
    'Face Hacking': ('face-hacking', 'mask'),
    'Immersive Coding': ('immersive-coding', 'installation'),
    'Tinker Forest': ('tinker-forest', 'leaf'),
    'Talk to Me': ('talk-to-me', 'typewriter'),
}
if set(QUESTIONS) != set(PRESENTATION):
    raise ValueError('Each selected project needs its own route and visual token.')

# Only verified project imagery belongs on the shelves. Missing assets use the project name.
PROJECT_MEDIA = {
    'Xenoflora Olfacta': ('xenoflora-cutout.webp', 'cutout'),
    'Creature Kit': ('creature-kit-token.webp', 'photograph'),
    'Teaching IoT': ('teaching-iot-token.webp', 'photograph'),
    'Face Hacking': ('face-hacking-token.webp', 'photograph'),
    'Immersive Coding': ('immersive-coding-token.webp', 'photograph'),
    'Tinker Forest': ('tinker-circuit.webp', 'photograph'),
}

def project_token(name, cls=''):
    if name in PROJECT_MEDIA:
        filename, treatment = PROJECT_MEDIA[name]
        return image(filename, '', 'project-token '+treatment+' '+cls, lazy=False)
    return f'<span class="word-token {cls}">{escape(name)}</span>'

def shelf_object(name, question):
    route, symbol = PRESENTATION[name]
    token = project_token(name)
    label = escape(name+': '+question, quote=True)
    return f'<a class="shelf-object" href="{{base}}work/{route}/" aria-label="{label}">{token}<span class="object-label">{escape(name)}<span class="object-question">{escape(question)}</span></span></a>'

def shelf(items):
    return '<div class="shelf-row">'+''.join(items)+'<svg class="shelf-line" viewBox="0 0 900 14" preserveAspectRatio="none" aria-hidden="true"><path d="M2 7Q90 2 172 6T350 6T520 7T710 6T898 8M6 9Q180 6 340 8T650 9T894 10" stroke="currentColor" stroke-width="1" fill="none"/></svg></div>'

home_shelves = ''.join(shelf([shelf_object(name,question) for name,question in PROJECTS[start:start+3]]) for start in range(0,len(PROJECTS),3))
page('', 'Home',f'<div class="home"><section class="home-intro"><h1 class="display">MARIANA<br>TAMASHIRO</h1><p class="tagline">creative technologist,<br>educator, tinkerer</p><a class="quiet-link" href="work/">Explore my work</a></section><section class="cabinet" aria-label="Selected projects">{home_shelves}</section></div>')

def project_object(label, href, main, fragment, second='paper'):
    url = href if href.startswith('https://') else '{base}'+href
    return f'<a class="project-object" href="{url}" aria-label="{label}">{main}{icon(fragment,"fragment")}{icon(second,"fragment second")}<span class="object-label">{label}</span></a>'

def collection(title, objects):
    return f'<section class="collection" id="{title.lower()}"><h2 class="display">{title}</h2><div class="collection-field">'+''.join(objects)+'</div></section>'

archive='https://maritamashiro4.wixsite.com/mariana-tamashiro/'
art=[project_object('Xenoflora Olfacta','work/xenoflora/',image('xenoflora-cutout.webp','','main-token'),'flower','shell'),project_object('Illustrated notes','illustration/live/',icon('paper','main-token'),'flower','pencil')]
research=[project_object('Xenoflora Olfacta','work/xenoflora/',image('xenoflora-cutout.webp','','main-token'),'eye','paper'),project_object('Hack Facial Recognition — original archive',archive+'face-hacking',project_token('Face Hacking','main-token'),'pencil','paper')]
education=[project_object('Tinker Forest','work/tinker-forest/',project_token('Tinker Forest','main-token'),'creature','paper'),project_object('Creature Kit — original archive',archive+'creature-kit',project_token('Creature Kit','main-token'),'leaf','pencil'),project_object('Movement Kit — original archive',archive+'movement-kit',icon('mechanism','main-token'),'arrow','paper'),project_object('Mask Kit — original archive',archive+'mask-kit',icon('mask','main-token'),'paper','pencil')]
page('work','Work','<header class="page-opening"><h1 class="display">Work</h1><p>A collection of things I make, explore, and share.</p></header><div class="collections">'+collection('Art',art)+collection('Research',research)+collection('Education',education)+'</div><p class="collection-note">Some projects live between collections. Selected links open the original project archive.</p>','Work')

def project_header(title, subtitle, authors, description):
    return '<p class="breadcrumb"><a href="{base}work/">Work</a> / '+title+'</p>'+f'<header class="project-heading"><h1 class="display">{title}</h1><p class="project-subtitle">{subtitle}</p><p class="authors">A project by {authors}</p><p class="project-description">{description}</p></header>'

xeno=project_header('Xenoflora Olfacta',QUESTIONS['Xenoflora Olfacta'],'Mariana Tamashiro, Louis Badr, Geetanjali Minsky, and Edward Zhaozheng Liu.','An imagined flower invites a close sensory encounter. Translucent bioplastic petals, a levitating vessel, and a specially composed scent bring a speculative life form into the room.')
xeno+='<section class="experience" aria-label="Encountering Xenoflora">'+photo('xenoflora-paper-0-0.webp','Xenoflora: a visitor encounters the flower, its enclosure, and the levitating blue plant.','primary')+photo('xenoflora-enclosure.webp','The blue flower inside its organic white enclosure.','detail')+'<div class="cutout">'+image('xenoflora-cutout.webp','Curled translucent blue bioplastic petals in their vessel.')+'</div><p class="annotation">a closer encounter '+icon('arrow')+'</p></section>'
xeno+='<div class="project-body"><section class="project-section" id="design"><h2>Design and fabrication</h2><p class="section-intro">The form brings together material exploration, parametric design, and physical interaction. Each element contributes to the impression of a living specimen from somewhere unfamiliar.</p><h3>Materials and form</h3><p>Alginate bioplastics give the petals their translucent, crystalline appearance. A magnetically levitating vessel holds the flower inside a white Voronoi enclosure, developed with Rhino and Grasshopper.</p>'+image('xenoflora-sketch.webp','Original development sketches of the enclosure, flower, vessel, and scent elements.','sketch-wide')+'<div class="process-block">'+photo('xenoflora-flower.webp','The curled bioplastic flower in its white vessel.')+'<div class="text"><h3>Working with translucency</h3><p>Curled surfaces catch and transmit light. The material becomes part of the imagined organism: delicate, unfamiliar, and visibly made.</p><p class="annotation">folds, light, and a little uncertainty</p></div></div><div class="process-block" id="interaction"><div class="text"><h3>Scent and interaction</h3><p>Scent offers another way to meet the flower. A specially composed fragrance becomes part of its identity, inviting visitors to come closer and imagine its world.</p><p>A XIAO microcontroller and capacitive sensing support the interaction, while light contributes to its quiet, living presence.</p></div>'+photo('xenoflora-levitation.webp','The bioplastic flower in its magnetically levitating vessel.')+'</div></section><section class="project-section"><h2>Out in the world</h2><figure class="outcome">'+photo('xenoflora-exhibit.webp','Xenoflora exhibited at FAB2026 in Boston.')+'<figcaption><h3>FAB2026</h3><p>Boston, Massachusetts</p><p class="small">An encounter with Xenoflora beyond the studio.</p></figcaption></figure></section><p class="question">What do you think an alien flower smells like?</p><nav class="next-project" aria-label="More projects"><a href="{base}work/">All work</a><a href="{base}work/tinker-forest/">Tinker Forest</a></nav></div>'
page('work/xenoflora','Xenoflora Olfacta',xeno,'Work','An artistic exploration of bioplastics and smell: encounter Xenoflora Olfacta, an imagined alien flower.')

tinker=project_header('Tinker Forest',QUESTIONS['Tinker Forest'],'Mariana Tamashiro and Andrea Devore.','A collaborative forest grows as visitors make their own light-up creatures. Everyday craft materials and simple electronics invite families to tinker, experiment, and add something of their own.')
tinker+='<div class="project-body">'+photo('tinker-family.webp','A family making creatures together at Tinker Forest.')+'<section class="project-section" id="making" style="margin-top:60px"><h2>Design and fabrication</h2><h3>Making together</h3><p>A shared making table offers craft materials, simple circuits, and examples. Participants create a creature, explore light or vibration, and contribute it to the growing forest.</p><div class="process-block"><div><h3>Small circuits, many possibilities</h3><p>LEDs, batteries, and vibration motors become expressive ingredients. The activity leaves room for visitors to make their own decisions about form and behavior.</p></div>'+photo('tinker-circuit.webp','A handmade creature with a visible coin-cell battery and LEDs.')+'</div></section><section class="project-section"><h2>Out in the world</h2><h3>Maker Faire Denver · 2018</h3><p>A collaborative making experience for families and visitors.</p></section><p class="question">What creature would you add to our forest?</p><nav class="next-project" aria-label="More projects"><a href="{base}work/">All work</a><a href="{base}work/xenoflora/">Xenoflora Olfacta</a></nav></div>'
page('work/tinker-forest','Tinker Forest',tinker,'Work')

for name, question in PROJECTS:
    route, symbol = PRESENTATION[name]
    if route in ('xenoflora', 'tinker-forest'):
        continue
    preview = '<p class="breadcrumb"><a href="{base}work/">Work</a> / '+escape(name)+'</p>'
    preview += f'<header class="project-heading"><h1 class="display">{escape(name)}</h1><p class="project-subtitle">{escape(question)}</p></header>'
    preview += '<section class="reading project-preview">'+project_token(name)+'<p class="eyebrow">Project preview</p><p>The full project story and images are being brought into this new portfolio.</p><a href="{base}">Back to the project shelves</a></section>'
    page('work/'+route, name, preview, 'Work', question)

desk='<header class="page-opening"><h1 class="display">On my desk</h1><p>experiments, fragments, things in progress</p></header><section class="desk" aria-label="A desk of material explorations"><figure class="experiment">'+image('xenoflora-petal.webp','Blue bioplastic material exploration.')+'<figcaption>translucent possibilities<br><a href="{base}work/xenoflora/#design">Bioplastic studies</a></figcaption></figure><figure class="experiment">'+icon('leaf')+'<figcaption>a leaf that lights up<br><a href="{base}work/tinker-forest/">Tinker Forest</a></figcaption></figure><figure class="experiment">'+photo('xenoflora-sketch.webp','Sketches exploring the Xenoflora enclosure and flower.')+'<figcaption>thinking through drawing</figcaption></figure><figure class="experiment">'+icon('mechanism')+'<figcaption>what could move?</figcaption></figure><figure class="experiment">'+photo('illustration-2.webp','Illustrated moments from Kyoto and Tokyo.')+'<figcaption>notes from a shared moment</figcaption></figure><figure class="experiment">'+icon('shell')+'<figcaption>collecting curious forms</figcaption></figure>'+icon('pencil','pencils')+'</section>'
page('on-my-desk','On my desk',desk,'On my desk')

intro='I capture important, funny, and joyful moments of a workshop and later share the illustrated notes with participants as a meaningful souvenir.'
collab='The illustrated notes below are from a collaboration with the Wonderful Idea Co., from the “Tinkering World Tour” in which artists, makers, and tinkerers from around the world virtually showed their studios and shared their work.'
page('illustration','Illustration','<header class="page-opening"><h1 class="display">Illustration</h1><p>Ideas, encounters, and little things worth remembering.</p></header><section class="illustration-intro"><div><h2>Live illustration</h2><p>'+intro+'</p><a href="{base}illustration/live/">Explore live illustration</a></div><a href="{base}illustration/live/" aria-label="View Live Illustration">'+image('illustration-1.webp','Illustrated notes from the Tinkering World Tour in New Mexico.','print')+'</a></section><section><h2>Drawn along the way</h2><p>A selection of illustrated notes from the Tinkering World Tour.</p><div class="illustration-intro">'+photo('illustration-2.webp','Kyoto and Tokyo: illustrated notes from the Tinkering World Tour.')+photo('illustration-3.webp','Berlin: illustrated notes from the Tinkering World Tour.')+'</div></section>','Illustration')
live='<p class="breadcrumb"><a href="{base}illustration/">Illustration</a> / Live illustration</p><header class="page-opening"><h1 class="display">Live illustration</h1><p>'+intro+'</p></header><section class="collaboration"><div><p class="eyebrow">Selected collaboration</p><h2>Tinkering World Tour</h2></div><p>'+collab+'</p></section>'
for n,label in [(1,'New Mexico'),(2,'Kyoto & Tokyo'),(3,'Berlin')]:
    live+=f'<figure class="illustration-feature">'+photo(f'illustration-{n}.webp',label+': illustrated notes from the Tinkering World Tour.','print')+f'<figcaption>{label}</figcaption></figure>'
live+='<section class="carousel" aria-label="More illustrated moments"><div class="carousel-heading"><h2>More illustrated moments</h2><div class="carousel-controls"><button data-slide="prev" aria-label="Previous illustration">‹</button><span class="slide-status" aria-live="polite"></span><button data-slide="next" aria-label="Next illustration">›</button></div></div><div class="carousel-track" tabindex="0" aria-label="Illustrations; use left and right arrow keys to browse">'
for n,label in [(1,'New Mexico'),(2,'Kyoto & Tokyo'),(3,'Berlin')]:live+='<div class="carousel-slide">'+photo(f'illustration-{n}.webp',label+': illustrated notes from the Tinkering World Tour.')+f'<p>{label}</p></div>'
live+='</div></section><p class="question">What are you bringing people together for?</p><a href="{base}contact/">Tell me about your event</a>'
page('illustration/live','Live illustration',live,'Illustration',intro)

page('about','About me','<header class="page-opening"><h1 class="display">About me</h1><p>creative technologist, educator, tinkerer</p></header><section class="reading"><p class="portrait-statement">Hi, I’m Mariana. I work across design, education, research, and making.</p><p>I’m a Brazilian designer and educator based in Paris. My work explores playful ways to engage with technology, through materials, objects, and invitations to create.</p><p>I’m an Assistant Professor at the Institute for Future Technologies at ESILV. I hold a PhD from Aarhus University, a master’s degree from the University of Colorado Boulder, and a design degree from the University of São Paulo.</p><p class="question">What could we make together?</p><a href="{base}contact/">Get in touch</a></section>','About me')
page('contact','Contact','<header class="page-opening"><h1 class="display">Contact</h1><p>A conversation is a good place to start.</p></header><section class="reading"><p>For creative collaborations, live illustration, and making things together:</p><p class="portrait-statement"><a href="mailto:mari.tamashiro@gmail.com">mari.tamashiro@gmail.com</a></p><div class="contact-links"><a href="https://www.instagram.com/marianatamashiro" rel="me">Instagram</a><a href="https://www.linkedin.com/in/maritamashiro/" rel="me">LinkedIn</a></div><p>Based in Paris, with connections further afield.</p></section>','Contact')

(OUT/'404.html').write_text((OUT/'index.html').read_text().replace('<title>Home','<title>Page not found'))
(OUT/'.nojekyll').touch()
print('Built',len(list(OUT.rglob('index.html'))),'pages in',OUT)
