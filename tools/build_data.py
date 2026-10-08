# Builds data/dk.json and data/dbt.json for Ünite 1 from auto-extracted page data + authored answers.
# Coordinates are % of the trimmed page (x of width, y of height).
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
AU = json.load(open(sys.argv[1]))

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

DK, DBT = {}, {}
def page(store, book, n, acts=(), links=()):
    p = {'img': f'img/{book}/{n:03d}.jpg', 'activities': list(acts)}
    if links: p['links'] = list(links)
    store[str(n)] = p

# =================================================================== DERS KİTABI
page(DK, 'dk', 15)

# ---- s.16
dk16_3 = dict(
    head=[5, 67.0, 78, 7.6],
    tiles=[{'r': [3.5, 3.0, 93.5, 55.7], 'page': 17}, [5, 74.8, 92, 19.6]], cols=1, nums=False)
page(DK, 'dk', 16, [
    act('dk16-1', '1. etkinlik', [2, 8.0, 95, 58.6], audio=AUD('dk', 16, 'S.010')),
    act('dk16-3', '3. etkinlik', [4, 67.0, 93, 27.2], [CK(39.0, 92.0, 2.6)], audio=AUD('dk', 16, 'S.011'), **dk16_3),
])
# ---- s.17
page(DK, 'dk', 17, [
    dict(act('dk17-3', '3. etkinlik', [3.5, 3.0, 93.5, 55.7], skip=True), alias={'page': 16, 'act': 'dk16-3'}),
    act('dk17-4', '4. etkinlik', [4, 61.7, 93, 33.6], [
        NUM(32.9, 93.6, 'A', 3, 2.6), NUM(38.3, 93.6, 'D', 3, 2.6), NUM(43.6, 93.6, 'I', 3, 2.6),
        NUM(49.0, 93.6, 'N', 3, 2.6), NUM(56.4, 93.6, 'N', 3, 2.6), NUM(61.8, 93.6, 'E', 3, 2.6)]),
])
# ---- s.18
page(DK, 'dk', 18, [
    act('dk18-5', '5. etkinlik', [4, 1.0, 92, 24.2], [
        LN([42.6, 13.3], [51.4, 22.6], dot=[43.6, 13.3]), LN([42.6, 18.0], [51.4, 8.7], dot=[43.6, 18.0]),
        LN([42.6, 22.6], [51.4, 18.0], dot=[43.6, 22.6])]),
    act('dk18-6', '6. etkinlik', [4, 25.2, 92, 30.6], [
        BL('dk18', 42.6, 'Merhaba'), BL('dk18', 44.9, 'adın ne', x=60), BL('dk18', 47.4, 'Benim adım ……'),
        BL('dk18', 49.7, 'Memnun'), BL('dk18', 52.1, 'Ben', x=30), BL('dk18', 52.1, 'memnun oldum', x=50)]),
    act('dk18-gy', 'Gizemli Yolculuk', [7, 55.9, 90, 39.7], [BL('dk18', 70.1, 'Benim adım ……')]),
])
# ---- s.19 (+ s.20 üst: Dinleme 1'in devamı)
din19 = dict(head=[0, 63.2, 100, 10.5], tiles=[[7.5, 73.9, 86, 17.4], {'r': [7.5, 3.4, 85, 18.5], 'page': 20}, {'r': [4, 23.6, 88.5, 18.6], 'page': 20}], cols=1)
page(DK, 'dk', 19, [
    act('dk19-sv', 'Söz Varlığı 1', [0, 1.2, 100, 52.1], [
        BL('dk19', 18.9, 'Merhaba', h=1.9), BL('dk19', 26.5, 'Benim adım ……', h=1.9),
        BL('dk19', 34.0, 'öğrenciyim', h=1.9), BL('dk19', 41.3, 'Ben de memnun oldum.', h=1.9)]),
    act('dk19-din', 'Dinleme 1', [0, 62.8, 100, 30.0], audio=AUD('dk', 19, 'S.012'), **din19),
], [link([30.0, 58.3, 31.6, 2.3], 'dbt', 8, 'Dil Bilgisi ve Telaffuz Kitabı s.8', {'act': 'dbt11-4'})])
# ---- s.20
page(DK, 'dk', 20, [
    dict(act('dk20-din', 'Dinleme 1', [3.5, 3.4, 89, 38.8], skip=True), alias={'page': 19, 'act': 'dk19-din'}),
    act('dk20-3', '3. etkinlik', [4, 44.6, 92, 50.4], [
        BL('dk20', 71.1, 'Günaydın', x=45), BL('dk20', 71.1, 'İyi geceler', x=70),
        BL('dk20', 91.8, 'İyi günler', x=30), BL('dk20', 91.7, 'İyi akşamlar', x=65)]),
])
# ---- s.21
L21 = [(44.0, 26.9, '3'), (44.0, 30.0, '5'), (44.0, 33.1, '6'), (44.0, 39.2, '4'), (44.0, 42.3, '2')]
R21 = [(90.1, 26.6, '6'), (90.1, 29.7, '5'), (90.1, 32.7, '2'), (90.1, 35.7, '3'), (90.1, 41.9, '4')]
page(DK, 'dk', 21, [
    act('dk21-4', '4. etkinlik', [4.5, 2.6, 92, 43.4],
        [NUM(x, y, t, 2.2, 2.2, g='sol') for x, y, t in L21] + [NUM(x, y, t, 2.2, 2.2, g='sag') for x, y, t in R21],
        audio=AUD('dk', 21, 'S.013')),
    act('dk21-5', '5. etkinlik', [4.5, 46.4, 92, 19.4], [
        BL('dk21', 51.9, 'Merhaba', h=1.6), BL('dk21', 53.2, 'nasılsın', h=1.6),
        BL('dk21', 62.6, 'iyiyim, teşekkür ederim', h=1.6), BL('dk21', 55.8, 'nasılsınız', h=1.6)]),
    act('dk21-6', '6. etkinlik', [4.5, 66.1, 92, 28.6], [
        BL('dk21', 80.5, 'Merhaba'), BL('dk21', 85.1, 'ederim, iyiyim', x=45), BL('dk21', 85.1, 'nasılsın', x=65),
        BL('dk21', 87.3, 'Teşekkür', x=28), BL('dk21', 87.3, 'Ben', x=45), BL('dk21', 87.3, 'iyiyim', x=58),
        BL('dk21', 89.6, 'kal'), BL('dk21', 91.9, 'Güle güle')]),
])
# ---- s.22
page(DK, 'dk', 22, [
    act('dk22-sv1', 'Söz Varlığı 1', [3, 1.8, 93, 27.8], audio=AUD('dk', 22, 'S.014')),
    act('dk22-2', '2. etkinlik', [3, 29.9, 93, 41.3], [
        LN([72.2, 43.8], [69.0, 50.8], g='a', dot=[72.2, 43.8]), LN([69.0, 50.8], [74.4, 48.2], g='a'),
        LN([27.0, 62.9], [25.6, 64.9], g='b', dot=[27.0, 62.9]), LN([25.6, 64.9], [30.4, 70.1], g='b'),
        LN([72.2, 62.9], [69.2, 67.5], g='c', dot=[72.2, 62.9]), LN([69.2, 67.5], [74.6, 64.9], g='c')]),
    act('dk22-3', '3. etkinlik', [3, 72.4, 40, 22.4], [
        BL('dk22', 78.6, 'Hayırlı sabahlar.', x=35), BL('dk22', 83.5, 'İyi günler.', x=35),
        BL('dk22', 88.3, 'İyi akşamlar.', x=35), BL('dk22', 93.2, 'İyi geceler.', x=35)]),
    act('dk22-4', '4. etkinlik', [43, 72.4, 54, 22.4], [
        NUM(68.8, 91.4, '1', g='n1'), NUM(91.6, 84.8, '2', g='n2'), NUM(68.8, 77.9, '3', g='n3'),
        NUM(91.6, 91.5, '4', g='n4'), NUM(68.8, 84.7, '5', g='n5'), NUM(91.6, 78.0, '6', g='n6')]),
])
# ---- s.23
page(DK, 'dk', 23, [
    act('dk23-1', 'Şarkı Zamanı 1', [0, 11.3, 100, 80.5], audio=AUD('dk', 23, 'M.001', 'M.002')),
], [link([28.4, 6.9, 30.8, 2.0], 'dbt', 12, 'Dil Bilgisi ve Telaffuz Kitabı s.12', {'act': 'dbt13-4'}),
    link([28.5, 92.7, 30.8, 2.0], 'dbt', 14, 'Dil Bilgisi ve Telaffuz Kitabı s.14', {'act': 'dbt15-5'})])
# ---- s.24
page(DK, 'dk', 24, [
    act('dk24-1', 'Konuşma 1', [3, 2.6, 92, 54.8]),
    act('dk24-2', '2. etkinlik', [3, 57.8, 49, 35.2], audio=AUD('dk', 24, 'S.015')),
    act('dk24-3', '3. etkinlik', [52, 57.8, 45, 36.0], [
        BL('dk24', 78.7, 'Merhaba. Benim adım ……. ', h=1.8), BL('dk24', 80.8, 'Ben öğrenciyim.', h=1.8),
        BL('dk24', 83.0, '…… yaşındayım.', h=1.8), BL('dk24', 85.1, 'Ben ……lıyım.', h=1.8),
        BL('dk24', 87.2, 'Ben …… ve Türkçe konuşuyorum.', h=1.8)]),
])
# ---- s.25 alfabe
LET = [  # (x0, x1, y, letter, row)
    (23.4, 30.1, 23.9, 'B', 1), (37.1, 43.5, 28.3, 'c', 1), (50.6, 57.0, 23.8, 'Ç', 1), (64.1, 70.5, 27.9, 'd', 1), (77.0, 83.4, 23.8, 'E', 1),
    (12.0, 18.4, 43.3, 'f', 2), (25.2, 31.7, 39.9, 'G', 2), (37.8, 44.0, 44.1, 'ğ', 2), (51.0, 57.4, 40.2, 'H', 2), (63.0, 69.0, 43.8, 'ı', 2), (76.5, 83.0, 39.3, 'İ', 2),
    (13.0, 19.2, 58.9, 'j', 3), (25.5, 31.8, 55.3, 'K', 3), (39.6, 45.7, 59.2, 'l', 3), (51.8, 58.5, 55.6, 'M', 3), (63.3, 69.4, 59.2, 'n', 3), (76.2, 82.6, 54.9, 'O', 3),
    (12.8, 19.3, 73.2, 'ö', 4), (25.2, 31.4, 69.9, 'P', 4), (38.9, 45.4, 74.0, 'r', 4), (50.8, 57.0, 70.2, 'S', 4), (64.6, 70.9, 74.0, 'ş', 4), (76.7, 83.0, 69.6, 'T', 4),
    (17.2, 23.4, 89.1, 'u', 5), (29.9, 36.4, 86.2, 'Ü', 5), (43.3, 49.8, 90.2, 'v', 5), (56.7, 63.1, 86.1, 'Y', 5), (68.6, 75.0, 89.3, 'z', 5)]
page(DK, 'dk', 25, [act('dk25-1', 'Yazma 1', [3, 7.0, 94, 85.5], [LB(a, b, y, t, h=3.6, g=f'r{r}') for a, b, y, t, r in LET])])
# ---- s.26
def R26(cx, cy, word, y): return [EL([cx - 6.6, cy - 2.8, 13.2, 5.6], g=word, dot=[cx - 7.4, cy]), BL('dk26', y, word, g=word)]
page(DK, 'dk', 26, [
    act('dk26-2', '2. etkinlik', [4, 2.2, 92, 36.4],
        R26(60.5, 16.3, 'ıspanak', 16.8) + R26(47.0, 22.4, 'okul', 22.8) + R26(33.4, 28.5, 'üzüm', 28.9) + R26(60.5, 34.6, 'öğretmen', 35.0),
        audio=AUD('dk', 26, 'S.016')),
    act('dk26-3', '3. etkinlik', [4, 39.2, 92, 20.0], audio=AUD('dk', 26, 'S.017')),
    act('dk26-4', '4. etkinlik', [4, 62.0, 92, 29.6], [
        LB(44.9, 65.7, 71.1, 'Senin adın ne'), BL('dk26', 73.6, 'Merhaba'), LB(33.2, 51.8, 78.6, 'öğrenciyim'),
        BL('dk26', 81.2, 'Memnun oldum.'), BL('dk26', 88.7, 'Güle güle.')]),
])
# ---- s.27
F27 = [((14.5, 40.7), (68.5, 43.3)), ((32.0, 40.7), (86.5, 43.3)), ((52.0, 40.7), (14.5, 43.3)), ((69.5, 40.7), (32.5, 43.3)), ((83.0, 40.7), (50.5, 43.3))]
page(DK, 'dk', 27, [
    act('dk27-1', 'Okuma 1', [3, 9.8, 94, 21.4], audio=AUD('dk', 27, 'S.018')),
    act('dk27-2', '2. etkinlik', [3, 31.6, 94, 14.0], [LN(list(a), list(b), dot=list(a)) for a, b in F27]),
    act('dk27-3', '3. etkinlik', [3, 46.6, 94, 47.4], [], audio=AUD('dk', 27, 'S.019')),
])
# ---- s.28
COLS28 = [(23.4, 'Mustafa', 'Türkiyeli'), (37.3, 'Muhammed', 'Pakistanlı'), (51.2, 'Hasan', 'Ürdünlü'), (65.1, 'Negina', 'Somalili'), (79.0, 'Vilora', 'Kosovalı')]
page(DK, 'dk', 28, [
    act('dk28-4', '4. etkinlik', [3, 2.6, 94, 17.0],
        [it for x, a, b in COLS28 for it in (TX([x + .4, 12.2, 12.8, 2.9], a, g=a), TX([x + .4, 15.9, 12.8, 2.9], b, g=a))]),
    act('dk28-5', '5. etkinlik', [3, 19.6, 94, 23.6], [
        BL('dk28', 29.0, 'Nerelisin'), BL('dk28', 38.1, 'Merhaba', x=35), BL('dk28', 39.6, 'Nerelisin', x=30),
        BL('dk28', 41.1, 'Somaliliyim', x=35), BL('dk28', 35.1, 'Benim adım'), BL('dk28', 38.1, 'Merhaba Vilora.', x=80),
        BL('dk28', 39.6, 'Nerelisin', x=70), BL('dk28', 41.1, 'Kosovalıyım', x=75)]),
    act('dk28-6', '6. etkinlik', [3, 43.8, 94, 15.6], [BL('dk28', 56.2, '……lıyım', x=50), BL('dk28', 56.2, 'Türkiyeli', x=85)]),
    act('dk28-sv1', 'Söz Varlığı 1', [3, 59.6, 94, 22.8], [
        BL('dk28', 71.6, 'Ben Senegalliyim.', x=30), BL('dk28', 71.6, 'Ben Romanyalıyım.', x=50),
        BL('dk28', 71.6, 'Ben Kosovalıyım.', x=65), BL('dk28', 71.6, 'Ben Tunusluyum.', x=85)]),
    act('dk28-sv2', 'Söz Varlığı 2', [3, 82.6, 94, 12.0], [BL('dk28', 93.1, '……lı')]),
])
# ---- s.29
CK29 = {'Beşir': [(19.6, 51.0), (23.6, 53.3), (40.1, 55.7)], 'Asiya': [(74.9, 51.0), (68.0, 53.3), (91.6, 55.7)],
        'Efe': [(18.1, 64.5), (17.2, 66.9), (39.3, 69.3), (21.2, 71.7)], 'Hanna': [(75.1, 64.5), (67.7, 66.9), (71.1, 69.3), (67.0, 71.7)]}
page(DK, 'dk', 29, [
    act('dk29-1', 'Dinleme 1', [3, 9.4, 94, 33.6], audio=AUD('dk', 29, 'S.020')),
    act('dk29-2', '2. etkinlik', [3, 37.6, 94, 40.0], [CK(x, y, 2.4, g=k) for k, v in CK29.items() for x, y in v], audio=AUD('dk', 29, 'S.021')),
    act('dk29-3', '3. etkinlik', [3, 78.0, 94, 16.6], [
        BL('dk29', 93.6, 'Asiya, Boşnakça konuşuyor.', x=25), BL('dk29', 89.4, 'Beşir, Arapça konuşuyor.'), BL('dk29', 93.6, 'Efe, Türkçe konuşuyor.', x=70)]),
], [link([29.9, 5.7, 30.8, 2.0], 'dbt', 16, 'Dil Bilgisi ve Telaffuz Kitabı s.16', {'act': 'dbt18-10'})])
# ---- s.30
N30 = [('2', 14.4), ('3', 9.0), ('4', 25.2), ('5', 27.9), ('6', 19.8), ('7', 22.5), ('8', 9.0), ('9', 33.3), ('10', 30.6)]
N30 = [('2', 14.4), ('3', 11.7), ('4', 25.2), ('5', 27.9), ('6', 19.8), ('7', 22.5), ('8', 9.0), ('9', 33.3), ('10', 30.6)]
page(DK, 'dk', 30, [
    act('dk30-4', '4. etkinlik', [3, 3.2, 92, 32.6], [NUM(11.0, y, t, 2.4, 2.3) for t, y in N30]),
    act('dk30-5', '5. etkinlik', [3, 38.0, 92, 30.2], [
        BL('dk30', 44.9, 'Benim adım', g='efe'), BL('dk30', 46.6, 'On üç', g='efe'), BL('dk30', 48.4, 'Türkiyeliyim', g='efe'), BL('dk30', 50.2, 'Türkçe', g='efe'),
        BL('dk30', 61.0, 'on üç', x=35, g='asiya'), BL('dk30', 63.4, 'Bosna-Hersekli', x=35, g='asiya'), BL('dk30', 65.8, 'Boşnakça', x=35, g='asiya'),
        BL('dk30', 58.4, 'Onun adı', g='besir'), BL('dk30', 60.9, 'on bir', x=78, g='besir'), BL('dk30', 63.2, 'Sudanlı', x=78, g='besir'), BL('dk30', 65.6, 'Arapça konuşuyor', x=78, g='besir')]),
    act('dk30-6', '6. etkinlik', [3, 70.0, 92, 25.0]),
])
# ---- s.31
page(DK, 'dk', 31, [
    act('dk31-1', 'Söz Varlığı 1', [3, 1.8, 94, 51.4], audio=AUD('dk', 31, 'S.022')),
    act('dk31-2', '2. etkinlik', [3, 53.6, 94, 13.4], audio=AUD('dk', 31, 'S.023')),
    act('dk31-3', '3. etkinlik', [3, 71.2, 94, 14.2], [
        BL('dk31', 83.9, 'dokuz', x=30), BL('dk31', 81.6, '17', x=50, h=3.4), BL('dk31', 83.9, 'on üç', x=65), BL('dk31', 81.6, '19', x=85, h=3.4)]),
])
# ---- s.32
CELL = lambda x, y, t, g: TX([x, y, 2.9, 2.2], t, 'l', g=g)
page(DK, 'dk', 32, [
    act('dk32-4', '4. etkinlik', [3, 2.4, 92, 39.4], audio=AUD('dk', 32, 'M.003')),
    act('dk32-5', '5. etkinlik', [3, 42.4, 92, 13.0], [
        LN([28.2, 45.7], [86.2, 51.8], dot=[28.2, 45.7]), LN([42.5, 45.7], [57.2, 51.8], dot=[42.5, 45.7]), LN([57.1, 45.7], [13.7, 51.8], dot=[57.1, 45.7]),
        LN([71.5, 45.7], [28.2, 51.8], dot=[71.5, 45.7]), LN([86.2, 45.7], [71.7, 51.8], dot=[86.2, 45.7])]),
    act('dk32-6', '6. etkinlik', [3, 57.6, 94, 37.0], [
        BL('dk32', 64.6, 'Özbekistan', x=35, g='c2'), CELL(39.3, 66.4, 'lı', 'c2'), CELL(36.9, 70.0, 'çe', 'c2'),
        BL('dk32', 68.2, 'İspanyalı', x=48, g='c3'), CELL(51.2, 70.0, 'ca', 'c3'),
        BL('dk32', 64.6, 'Tunus', x=60, g='c4'), CELL(63.1, 70.0, 'ça', 'c4'),
        BL('dk32', 68.2, 'Almanyalı', x=75, g='c5'), CELL(77.1, 70.0, 'ca', 'c5'),
        BL('dk32', 64.6, 'İngiltere', x=88, g='c6'), CELL(90.6, 66.4, 'li', 'c6'), CELL(89.3, 69.7, 'ce', 'c6'),
        LB(26.0, 83.5, 80.5, 'Almanyalı. O Almanya’da yaşıyor. Hanna Almanca konuşuyor.'),
        LB(24.5, 83.5, 84.3, 'Sudanlı. O Sudan’da yaşıyor. Beşir Arapça konuşuyor.'),
        LB(23.3, 83.5, 88.1, '……lıyım. ……’da yaşıyorum. …… konuşuyorum.'),
        LB(29.5, 83.5, 91.8, '……lı. O ……’da yaşıyor. …… konuşuyor.')]),
])
# ---- s.33
page(DK, 'dk', 33, [
    act('dk33-1', 'Şarkı Zamanı 1', [0, 8.6, 100, 76.6], audio=AUD('dk', 33, 'M.004', 'M.005')),
], [link([28.4, 4.6, 30.6, 2.0], 'dbt', 19, 'Dil Bilgisi ve Telaffuz Kitabı s.19', {'act': 'dbt20-4'}, act_='dbt19-1'),
    link([27.9, 92.1, 30.6, 2.0], 'dbt', 20, 'Dil Bilgisi ve Telaffuz Kitabı s.20 (Telaffuz)', {'act': 'dbt21-4'}, act_='dbt20-t1')])
# ---- s.34
page(DK, 'dk', 34, [
    act('dk34-1', 'Konuşma 1', [3, 2.0, 94, 47.4]),
    act('dk34-2', '2. etkinlik', [3, 49.8, 94, 26.0], [
        BL('dk34', 58.0, 'Merhaba. Benim adım ……. ', h=1.8), BL('dk34', 60.1, '…… yaşındayım. ……lıyım.', h=1.8),
        BL('dk34', 62.2, '……’da yaşıyorum.', h=1.8), BL('dk34', 64.3, '…… konuşuyorum.', h=1.8)]),
    act('dk34-y1', 'Yazma 1', [3, 76.6, 94, 18.2]),
])
# ---- s.35
HG = [  # (cx, y_dots, text, row)  — numbers in the top triangles, words in the bottom ones
    (14.2, 34.1, '0', 1), (31.9, 41.0, 'bir', 1), (50.0, 33.8, '2', 1), (67.6, 41.0, 'üç', 1), (85.7, 33.8, '4', 1),
    (14.0, 54.5, 'beş', 2), (32.1, 47.3, '6', 2), (49.7, 54.5, 'yedi', 2), (67.8, 47.3, '8', 2), (85.5, 54.5, 'dokuz', 2),
    (14.2, 60.7, '10', 3), (31.9, 67.9, 'on bir', 3), (50.0, 60.7, '12', 3), (67.6, 67.8, 'on üç', 3), (85.7, 60.7, '14', 3),
    (23.0, 81.3, 'on beş', 4), (41.0, 74.1, '16', 4), (58.9, 81.3, 'on yedi', 4), (76.6, 74.1, '18', 4),
    (40.4, 94.8, 'on dokuz', 5), (59.6, 87.5, '20', 5)]
page(DK, 'dk', 35, [
    act('dk35-2', '2. etkinlik', [52, 2.0, 46, 25.0], [
        BL('dk35', 11.2, 'Merhaba. Benim adım ……. ', h=1.8), BL('dk35', 13.3, '……lıyım.', h=1.8), BL('dk35', 15.4, '…… yaşındayım.', h=1.8),
        BL('dk35', 17.6, '……’da yaşıyorum.', h=1.8), BL('dk35', 19.7, '…… konuşuyorum.', h=1.8)]),
    act('dk35-3', '3. etkinlik', [3, 26.4, 94, 69.6],
        [LB(round(cx - (2.6 if t.isdigit() else 5.5), 2), round(cx + (2.6 if t.isdigit() else 5.5), 2), y, t, h=(2.4 if t.isdigit() else 2.0), g=f'r{r}') for cx, y, t, r in HG]),
])
# ---- s.36 TRT
page(DK, 'dk', 36, [
    act('dk36-1', '1. etkinlik', [5, 8.6, 85, 21.0], [
        NUM(19.2, 21.1, '2', 2.4, 2.4, g='sira'), NUM(46.4, 21.1, '1', 2.4, 2.4, g='sira'), NUM(73.9, 21.1, '3', 2.4, 2.4, g='sira'),
        CK(30.4, 27.2, 2.6, g='konu')], audio=AUD('dk', 36, 'V.001')),
    act('dk36-2', '2. etkinlik', [5, 29.8, 82, 16.2], [
        BL('dk36', 37.3, 'Suriyeli'), BL('dk36', 44.7, 'Ahed', x=47), BL('dk36', 44.9, 'on bir', x=70)]),
    act('dk36-3', '3. etkinlik', [5, 47.8, 83, 19.4], [
        CK(32.1, 54.8, 2.6, g='r1'), CK(70.4, 54.8, 2.6, g='r1'), CK(39.4, 57.6, 2.6, g='r2'), CK(70.4, 57.6, 2.6, g='r2'),
        CK(39.4, 60.5, 2.6, g='r3'), CK(70.4, 60.5, 2.6, g='r3'), CK(32.1, 63.3, 2.6, g='r4'), CK(70.4, 63.3, 2.6, g='r4')]),
    act('dk36-4', '4. etkinlik', [5, 67.2, 83, 21.4], [
        BL('dk36', 84.2, 'Kendini tanıtır mısın', x=15), BL('dk36', 82.0, 'Benim adım', x=35), BL('dk36', 82.1, 'Hoş geldin', x=55),
        BL('dk36', 84.2, 'Benim adım', x=60), BL('dk36', 86.3, 'memnun oldum')]),
    act('dk36-5', '5. etkinlik', [26, 88.6, 62, 9.0]),
])
# ---- s.37
page(DK, 'dk', 37, [
    act('dk37-1', 'Maarif Türkçe Grubu', [18, 6.0, 64, 88.0], head=[33, 6.6, 34, 4.4],
        tiles=[[20.5, 11.6, 59, 39.8], [20.5, 51.4, 59, 42.2]], cols=2),
])
# ---- s.38
page(DK, 'dk', 38, [act('dk38-1', 'Proje Zamanı 1', [3, 2.0, 94, 92.5])])

# =================================================================== DİL BİLGİSİ VE TELAFFUZ
page(DBT, 'dbt', 7)
page(DBT, 'dbt', 8, [
    act('dbt8-1', '1. etkinlik', [7.0, 20.2, 83.0, 73.1], audio=AUD('dbt', 8, 'S.001'),
        head=[11.5, 20.65, 67.5, 6.2], tiles=[[18.5, 26.85, 69.5, 21.4], [18.5, 48.25, 69.5, 22.5], [18.5, 70.75, 69.5, 22.6]], cols=2)])
abc = dict(head=[9.3, 11.75, 64.2, 11.55],
           tiles=[[9.6, 23.3, 78.3, 34.35], [9.6, 57.65, 78.3, 34.95], {'r': [11.0, 7.0, 79.5, 33.8], 'page': 10}, {'r': [11.0, 41.4, 79.5, 34.4], 'page': 10}], cols=2)
page(DBT, 'dbt', 9, [act('dbt9-2', '2. etkinlik', [7.0, 11.75, 86.0, 81.0], audio=AUD('dbt', 9, 'S.002'), **abc)])
page(DBT, 'dbt', 10, [dict(act('dbt10-2', '2. etkinlik', [10, 6.5, 81, 70], skip=True), alias={'page': 9, 'act': 'dbt9-2'})])
W11 = {  # word: (picture y, col1 y, col2 y, col3 y, col2 fill, col3 fill)
    'kitap': (65.0, 80.5, 58.1, 65.4, ('ki', 58.5, 57), ('itap', 65.8, 79)),
    'pencere': (72.6, 58.1, 72.9, 88.0, ('re', 73.3, 61), ('encere', 88.5, 79)),
    'sınıf': (80.2, 88.0, 88.0, 80.5, ('nıf', 88.5, 59), ('ınıf', 80.9, 79)),
    'zürafa': (87.8, 72.9, 65.4, 58.1, ('ra', 65.8, 59), ('ürafa', 58.5, 79))}
it11 = []
for w, (yp, y1, y2, y3, f2, f3) in W11.items():
    it11 += [LN([24.4, yp], [32.0, y1], g=w, dot=[24.4, yp]), LN([45.2, y1], [52.2, y2], g=w), LN([65.3, y2], [72.4, y3], g=w),
             BL('dbt11', f2[1], f2[0], x=f2[2], g=w), BL('dbt11', f3[1], f3[0], x=f3[2], g=w)]
page(DBT, 'dbt', 11, [
    act('dbt11-3', '3. etkinlik', [8, 7.4, 82, 40.0]),
    act('dbt11-4', '4. etkinlik', [8, 48.0, 82, 44.0], it11),
])
page(DBT, 'dbt', 12, [
    act('dbt12-1', '1. etkinlik', [8, 16.4, 86, 28.0], audio=AUD('dbt', 12, 'S.003')),
    act('dbt12-2', '2. etkinlik', [8, 47.8, 86, 43.2], audio=AUD('dbt', 12, 'S.004')),
])
E13 = [([48.5, 20.4, 10.5, 2.9], 'F', 38.5), ([75.5, 20.4, 8.8, 2.9], 'E', 45.3), ([65.2, 36.2, 8.0, 2.9], 'R', 52.0),
       ([38.4, 36.2, 8.8, 2.9], 'İ', 58.7), ([21.7, 36.2, 8.8, 2.9], 'N', 65.5)]
page(DBT, 'dbt', 13, [
    act('dbt13-3', '3. etkinlik', [8, 7.4, 82, 40.0], [it for r, l, x in E13 for it in (EL(r, g=l), NUM(x, 44.8, l, 3.2, 2.8, g=l))]),
    act('dbt13-4', '4. etkinlik', [8, 49.0, 84, 38.0], [
        BL('dbt13', 61.5, 'sorabilirsin.', x=70), BL('dbt13', 68.1, 'öğrenci', x=30), LB(59.2, 75.5, 81.3, 'Rica ederim')]),
])
page(DBT, 'dbt', 14, [
    act('dbt14-1', '1. etkinlik', [8, 12.0, 88, 10.6], audio=AUD('dbt', 14, 'S.005')),
    act('dbt14-2', '2. etkinlik', [8, 25.4, 88, 23.4], audio=AUD('dbt', 14, 'S.006')),
    act('dbt14-3', '3. etkinlik', [8, 50.8, 88, 25.0], audio=AUD('dbt', 14, 'S.007')),
])
page(DBT, 'dbt', 15, [
    act('dbt15-4', '4. etkinlik', [8, 5.0, 82, 60.6], audio=AUD('dbt', 15, 'S.008'),
        head=[9, 7.0, 82, 7.4], tiles=[[21, 15.0, 57, 26.4], [9, 41.5, 73, 23.6]], cols=2, nums=False),
    act('dbt15-5', '5. etkinlik', [8, 66.0, 82, 26.0], audio=AUD('dbt', 15, 'S.009')),
])
page(DBT, 'dbt', 16, [
    act('dbt16-1', '1. etkinlik', [8, 20.8, 88, 28.4], audio=AUD('dbt', 16, 'S.010')),
    act('dbt16-2', '2. etkinlik', [8, 49.6, 88, 39.6], [BL('dbt16', 78.1, '……lıyım.'), BL('dbt16', 86.3, 'Ben ……’da yaşıyorum.')]),
])
page(DBT, 'dbt', 17, [
    act('dbt17-3', '3. etkinlik', [8, 11.4, 82, 21.4]),
    act('dbt17-4', '4. etkinlik', [8, 33.4, 82, 13.8], [
        FL([58.6, 37.2, 11.8, 2.3]), FL([30.5, 40.6, 13.8, 2.3]), FL([70.5, 40.6, 13.8, 2.3]), FL([34.4, 44.4, 15.6, 2.3])]),
    act('dbt17-5', '5. etkinlik', [8, 47.4, 82, 27.6], [
        BL('dbt17', 57.8, 'Sen Kongolusun.'), BL('dbt17', 61.6, 'Biz Gineliyiz.'), BL('dbt17', 65.4, 'Ben Suriyeliyim.'),
        BL('dbt17', 69.1, 'O Tunuslu.'), BL('dbt17', 72.9, 'Biz Faslıyız.')]),
    act('dbt17-6', '6. etkinlik', [8, 75.4, 82, 16.0], [
        LB(53.2, 86.0, 80.8, '……, sen nerelisin?'), LB(53.2, 86.0, 83.8, '……lıyım.'),
        LB(53.2, 86.0, 86.9, 'Nerede yaşıyorsun?'), LB(53.2, 86.0, 89.9, '……’da yaşıyorum.')]),
])
page(DBT, 'dbt', 18, [
    act('dbt18-7', '7. ve 8. etkinlik', [8, 11.6, 86, 21.2]),
    act('dbt18-9', '9. etkinlik', [8, 33.0, 86, 20.4], [
        BL('dbt18', 43.0, 'Arapça'), BL('dbt18', 45.3, 'Pakistanlı'), BL('dbt18', 47.7, 'Kamerun', x=20),
        BL('dbt18', 47.7, 'Fransızca', x=72), BL('dbt18', 50.0, 'Boşnak'), BL('dbt18', 52.4, 'İngiltere', x=20), BL('dbt18', 52.4, 'İngilizce', x=72)]),
    act('dbt18-10', '10. etkinlik', [8, 53.8, 86, 38.0], [
        BL('dbt18', 69.1, 'Kosovalı.', x=50, g='una'), BL('dbt18', 70.7, 'Una Arnavut.', x=50, g='una'), BL('dbt18', 72.2, 'Una, Arnavutça konuşuyor.', x=50, g='una'),
        BL('dbt18', 69.1, 'Kırgızistanlı.', x=80, g='aziz'), BL('dbt18', 70.7, 'Aziz Kırgız.', x=80, g='aziz'), BL('dbt18', 72.2, 'Aziz, Kırgızca konuşuyor.', x=80, g='aziz'),
        BL('dbt18', 86.9, 'Tanzanyalı.', x=30, g='fat'), BL('dbt18', 88.5, 'Fatoumata Tanzanyalı.', x=25, g='fat'), BL('dbt18', 90.0, 'Fatoumata, Svahilice konuşuyor.', x=25, g='fat'),
        BL('dbt18', 86.9, 'Tunuslu.', x=55, g='has'), BL('dbt18', 88.5, 'Hasan Arap.', x=50, g='has'), BL('dbt18', 90.0, 'Hasan, Arapça konuşuyor.', x=50, g='has'),
        BL('dbt18', 86.9, 'İspanyalı.', x=80, g='sof'), BL('dbt18', 88.5, 'Sofia İspanyol.', x=78, g='sof'), BL('dbt18', 90.0, 'Sofia, İspanyolca konuşuyor.', x=78, g='sof')]),
])
page(DBT, 'dbt', 19, [
    act('dbt19-1', '1. etkinlik', [8, 17.0, 84, 24.6], audio=AUD('dbt', 19, 'S.011')),
    act('dbt19-2', '2. etkinlik', [8, 42.4, 84, 27.6]),
    act('dbt19-3', '3. etkinlik', [8, 70.2, 84, 21.4], audio=AUD('dbt', 19, 'S.012')),
])
page(DBT, 'dbt', 20, [
    act('dbt20-4', '4. etkinlik', [8, 6.6, 84, 39.4], [
        LN([21.0, 24.3], [41.0, 30.3], g='b', dot=[21.0, 24.3]), BL('dbt20', 37.5, 'on bir yaşındayım.', x=40, g='b'),
        LN([61.2, 24.3], [81.4, 30.3], g='e', dot=[61.2, 24.3]), BL('dbt20', 37.5, 'on üç yaşındayım.', x=80, g='e'),
        LN([81.3, 24.3], [61.4, 30.3], g='h', dot=[81.3, 24.3]), BL('dbt20', 37.5, 'on iki yaşındayım.', x=60, g='h'),
        TX([15.2, 43.2, 74, 2.4], 'Merhaba. Benim adım ……. Ben …… yaşındayım.', 'l', g='kendi')]),
    act('dbt20-t1', 'Telaffuz 1', [8, 48.4, 84, 27.6], audio=AUD('dbt', 20, 'S.013')),
    act('dbt20-t2', 'Telaffuz 2', [8, 76.4, 84, 16.4], audio=AUD('dbt', 20, 'S.014')),
])
page(DBT, 'dbt', 21, [
    act('dbt21-3', '3. etkinlik', [8, 5.0, 84, 60.0], audio=AUD('dbt', 21, 'S.015')),
    act('dbt21-4', '4. etkinlik', [8, 65.6, 84, 26.0], audio=AUD('dbt', 21, 'S.016')),
])

# ---- underlines on s.27 come from the slide images (thin strokes): pick them from the mapped slide data
SL = json.load(open(sys.argv[2]))
ul = [a for a in SL if a['page'] == ['dk', 27] and a['kind'] == 'line' and abs(a['from'][1] - a['to'][1]) < 0.5]
ul.sort(key=lambda a: (a['from'][0] > 50, a['from'][1]))
A27 = DK['27']['activities'][2]
A27['items'] = [dict(UL(a['from'], a['to']), id=f'dk27-3-{k+1}') for k, a in enumerate(ul)]

for name, store, aspect, title in (('dk', DK, 0.7855, 'Ders Kitabı'), ('dbt', DBT, 0.6669, 'Dil Bilgisi ve Telaffuz Kitabı')):
    json.dump({'id': name, 'title': title, 'aspect': aspect, 'pages': store}, open(f'{ROOT}/data/{name}.json', 'w'), ensure_ascii=False, indent=1)
print('ok', len(DK), len(DBT), 'underlines', len(A27['items']))
