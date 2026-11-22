"""Check every generated internal link and asset without third-party packages."""
import re
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT=Path(__file__).resolve().parents[1]/'dist'
errors=[]
class Parser(HTMLParser):
    def __init__(self): super().__init__();self.refs=[];self.ids=set();self.h1=0;self.projects=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='h1':self.h1+=1
        if 'shelf-object' in d.get('class','').split():self.projects.append(d)
        if 'id' in d:self.ids.add(d['id'])
        for key in ['href','src']:
            if d.get(key):self.refs.append(d[key])

pages={}
for p in ROOT.rglob('*.html'):
    parser=Parser();parser.feed(p.read_text());pages[p.resolve()]=parser
    if parser.h1!=1:errors.append(f'{p}: expected one main heading, found {parser.h1}')
for path,parser in pages.items():
    for ref in parser.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        target=(path.parent/unquote(u.path)).resolve() if u.path else path
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{path.relative_to(ROOT)}: missing {ref}')
        elif u.fragment and target.suffix=='.html' and u.fragment not in pages.get(target,Parser()).ids:errors.append(f'{path.relative_to(ROOT)}: missing anchor {ref}')
selected=re.findall(r'^## (.+)\n+([^\n]+)',(ROOT.parent/'content/portfolio-project-questions.md').read_text(),re.M)
items=pages[(ROOT/'index.html').resolve()].projects
if [item.get('aria-label') for item in items]!=[name+': '+question for name,question in selected]:
    errors.append('Homepage projects and questions must match the Markdown in order.')
if len({item['href'] for item in items})!=len(selected):
    errors.append('Each selected project needs a distinct shelf link.')
for item,(name,question) in zip(items,selected):
    target=ROOT/item['href']/'index.html'
    if target.exists() and escape(question) not in target.read_text():
        errors.append(f'{name}: missing authored project question.')
if errors:raise SystemExit('\n'.join(errors))
print(f'Passed: {len(pages)} HTML pages, all internal links, fragments, and referenced assets.')
