# Shared helpers for building unit data (coordinates in % of the trimmed page).
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
AU = {}
def load(*files):
    for f in files: AU.update(json.load(open(f)))
def P(book, n): return f'{book}{n}'

def BL(pg, y, text, x=None, h=None, g=None, x0=None, x1=None):
    """snap to a detected dotted blank on page pg near y (and containing x)"""
    cands = [b for b in AU[pg]['blanks'] if abs(b[2] - y) <= 0.7 and (x is None or b[0] - 0.8 <= x <= b[1] + 0.8)]
    if not cands: raise SystemExit(f'no blank on {pg} near y={y} x={x} for {text!r}')
    b = min(cands, key=lambda b: (abs(b[2] - y), 0 if x is None else min(abs(b[0]-x), abs(b[1]-x))))
    it = {'type': 'blank', 'line': [x0 if x0 is not None else b[0], x1 if x1 is not None else b[1], b[2]], 'text': text}
    if h: it['h'] = h
    if g: it['g'] = g
    return it
def LB(x0, x1, y, text, h=None, g=None):
    it = {'type': 'blank', 'line': [x0, x1, y], 'text': text}
    if h: it['h'] = h
    if g: it['g'] = g
    return it
def TX(rect, text, align='c', g=None):
    it = {'type': 'text', 'rect': rect, 'text': text}
    if align != 'c': it['align'] = align
    if g: it['g'] = g
    return it
def NUM(cx, cy, text, w=2.4, h=2.4, g=None): return TX([round(cx - w/2, 2), round(cy - h/2, 2), w, h], text, g=g)
def LN(f, t, g=None, dot=None):
    it = {'type': 'line', 'from': f, 'to': t}
    if g: it['g'] = g
    if dot: it['dot'] = dot
    return it
def CK(x, y, s=None, g=None):
    it = {'type': 'check', 'at': [x, y]}
    if s: it['s'] = s
    if g: it['g'] = g
    return it
def EL(rect, g=None, dot=None):
    it = {'type': 'ellipse', 'rect': rect}
    if g: it['g'] = g
    if dot: it['dot'] = dot
    return it
def FL(rect, g=None):
    it = {'type': 'fill', 'rect': rect}
    if g: it['g'] = g
    return it
def UL(f, t, g=None):
    it = {'type': 'uline', 'from': f, 'to': t}
    if g: it['g'] = g
    return it

HAVE = lambda book, code: os.path.exists(f'{ROOT}/audio/{book}/{code.replace(".", "")}.mp3')
def AUD(book, n, *codes):
    out = []
    for c in codes:
        a = next(a for a in AU[P(book, n)]['audio'] if a['code'] == c)
        e = {'code': c, 'rect': [round(v, 2) for v in a['r']]}
        if HAVE(book, c): e['src'] = f'audio/{book}/{c.replace(".", "")}.mp3'
        out.append(e)
    return out

def act(i, label, rect, items=(), audio=(), head=None, tiles=None, cols=None, nums=None, skip=False):
    A = {'id': i, 'label': label, 'rect': rect, 'items': []}
    for k, it in enumerate(items): A['items'].append(dict(it, id=f'{i}-{k+1}'))
    if audio: A['audio'] = list(audio)
    if head: A['head'] = head
    if tiles: A['tiles'] = tiles
    if cols: A['cols'] = cols
    if nums is not None: A['nums'] = nums
    if skip: A['skip'] = True
    return A
def link(rect, book, page, label, until, act_=None):
    L = {'rect': rect, 'go': {'book': book, 'page': page}, 'label': label, 'until': until}
    if act_: L['go']['act'] = act_
    return L


def page(store, book, n, acts=(), links=()):
    p = {'img': f'img/{book}/{n:03d}.jpg', 'activities': list(acts)}
    if links: p['links'] = list(links)
    store[str(n)] = p
def dump(name, store, aspect, title, units):
    json.dump({'id': name, 'title': title, 'aspect': aspect, 'units': units, 'pages': store}, open(f'{ROOT}/data/{name}.json', 'w'), ensure_ascii=False, indent=1)
def ON(n, *items):
    """answers that sit on the continuation page n of an activity that started on an earlier page"""
    return [dict(it, page=n) for it in items]
