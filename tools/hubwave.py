"""Add a wave section to sites/index.html. add(wave, title, blurb, rows, old_title, new_title, old_desc, new_desc)
rows: (slug, NAME, tagline, tech, accent). Uses the shared renderWave() helper (inserted once)."""
import os, json
P = os.path.join(os.path.dirname(__file__), '..', 'sites', 'index.html')
HELPER = '''
// Waves 7+ share one renderer: [slug, NAME, tagline, tech, accent]
function renderWave(gridId, list){
  const grid = document.getElementById(gridId);
  grid.innerHTML = list.map(s=>`
  <a class="w4-card" href="${s[0]}/" style="--a:${s[4]}">
    <div class="shot">
      <span class="no">№ ${s[0].split('-')[0]}</span>
      <img loading="lazy" src="assets/thumbs/${s[0]}.jpg" alt="Screenshot of ${s[1]}">
    </div>
    <div class="body">
      <h3><span class="dot"></span>${s[1]}</h3>
      <p>${s[2]}</p>
      <span class="tag">${s[3]}</span>
    </div>
  </a>`).join('');
  grid.querySelectorAll('.w4-card').forEach((c,i)=>{
    new IntersectionObserver((es,o)=>es.forEach(e=>{ if(e.isIntersecting){ setTimeout(()=>e.target.classList.add('in'), (i%3)*90); o.unobserve(e.target);} }),{threshold:.15}).observe(c);
  });
}
'''
def add(wave, title, blurb, rows, swaps):
    s = open(P).read()
    assert f'id="wave{wave}"' not in s, 'already added'
    for slug, *_ in rows:
        assert os.path.isfile(os.path.join(os.path.dirname(P), slug, 'index.html')), slug
        assert os.path.isfile(os.path.join(os.path.dirname(P), slug, 'guide', 'index.html')), slug + ' guide'
        assert os.path.isfile(os.path.join(os.path.dirname(P), 'assets', 'thumbs', slug + '.jpg')), slug + ' thumb'
    sec = f'''
<section class="wave4" id="wave{wave}">
  <div class="w4-head">
    <h2>Wave {wave} — {title}</h2>
    <p>{blurb}</p>
  </div>
  <div class="w4-grid" id="w{wave}grid"></div>
</section>
'''
    prev = f'<div class="w4-grid" id="w{wave-1}grid"></div>\n</section>\n'
    assert prev in s; s = s.replace(prev, prev + sec)
    data = '[\n' + ',\n'.join('  ' + json.dumps(list(r), ensure_ascii=False) for r in rows) + '\n]'
    js = ('' if 'function renderWave' in s else HELPER) + f"const WAVE{wave} = {data};\nrenderWave('w{wave}grid', WAVE{wave});\n"
    i = s.rindex('</script>'); s = s[:i] + js + s[i:]
    nav = f'<a href="#wave{wave-1}">see wave {wave-1} ↓</a>'
    assert nav in s; s = s.replace(nav, nav + f'\n    <a href="#wave{wave}">see wave {wave} ↓</a>')
    for a, b in swaps:
        assert a in s, a; s = s.replace(a, b)
    open(P, 'w').write(s); print('hub: wave', wave, 'added,', len(rows), 'cards')
