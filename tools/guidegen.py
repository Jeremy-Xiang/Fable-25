"""Shared guide generator: build(wave, G) writes sites/<slug>/guide/index.html for each entry.
The HTML shell is lifted from gen-guides6.py so every wave's guides match."""
import os, re
_src = open(os.path.join(os.path.dirname(__file__), 'gen-guides6.py')).read()
SHELL = re.search(r"SHELL = '''(.*?)'''", _src, re.S).group(1)
def li(items): return ''.join(f'\n    <li>{i}</li>' for i in items)
def build(wave, G):
    base = os.path.join(os.path.dirname(__file__), '..', 'sites')
    shell = SHELL.replace('Wave 6', f'Wave {wave}')
    for slug, g in G.items():
        assert os.path.isdir(os.path.join(base, slug)), slug
        d = os.path.join(base, slug, 'guide'); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w').write(shell.format(
            NAME=g['name'], SUB=g['sub'], NO=slug.split('-')[0], ACCENT=g['accent'],
            ACCENT_ENC=g['accent'].replace('#', '%23'), IDEA=g['idea'], HOW=li(g['how']),
            TYPECOLOR=li(g['typecolor']), PASS=li(g['passes']), LIFT=li(g['lift']), META=g['meta']))
    print(f'wrote {len(G)} guides')
