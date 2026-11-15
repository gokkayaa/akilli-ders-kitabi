# Builds data/dk2-u7.json (Ders Kitabı 2, 7. Ünite s.43–72) and data/dbt-u7.json (telaffuz s.108–120).
# usage: build_u7.py WORK   (WORK holds auto-dk2.json / auto-dbt.json from prep_unit.py)
# Answers: the official "dijital kitap" slides, checked against the book texts, the listening scripts in the
# teacher's guide and the pictures; where the slide had none (or a wrong one), from the book itself.
import sys, math
from kit import *
from words import WB, words, clean
W = sys.argv[1]
load(f'{W}/auto-dk2.json', f'{W}/auto-dbt.json')
D, T = {}, {}
B2 = lambda n, y, text, **k: BL(f'dk2{n}', y, text, **k)
BT = lambda n, y, text, **k: BL(f'dbt{n}', y, text, **k)

def split(t, k):
    """split a sentence into k lines of similar length (at word breaks)"""
    w = t.split()
    if k <= 1 or len(w) < 2: return [t]
    out, rest = [], w
    for i in range(k, 1, -1):
        tot = len(' '.join(rest)); goal = tot / i
        best = min(range(1, len(rest) - i + 2), key=lambda j: abs(len(' '.join(rest[:j])) - goal))
        out.append(' '.join(rest[:best])); rest = rest[best:]
    return out + [' '.join(rest)]
def MULTI(B, n, ys, text, x=None, g=None, per=20):
    """write text over several dotted lines (ys), using as few lines as fit ~per characters each"""
    k = min(len(ys), max(1, math.ceil(len(text) / per)))
    return [B(n, y, part, x=x, g=g) for y, part in zip(ys, split(text, k))]
def CIRC(b, n, w, near, g=None, px=0.8, py=0.6):
    x0, y0, x1, y1 = WB(b, n, w, near)
    return EL([round(x0 - px, 2), round(y0 - py, 2), round(x1 - x0 + 2 * px, 2), round(y1 - y0 + 2 * py, 2)], g=g)
def ELC(cx, cy, w, h, g=None): return EL([round(cx - w / 2, 2), round(cy - h / 2, 2), w, h], g=g)
SEASONS = {'ilkbahar', 'yaz', 'yazın', 'sonbahar', 'kış', 'kışın'}
def season_lines(b, n, y0, y1, extra=()):
    """underline every season word printed between y0 and y1 (plus words in extra)"""
    out = []
    for t, x0, a, x1, e in words(b, n):
        if y0 <= a <= y1 and (clean(t) in SEASONS or clean(t) in extra):
            if t.endswith(('.', ',')): x1 -= (x1 - x0) / len(t)
            out.append(UL([round(x0, 2), round(e + .05, 2)], [round(x1, 2), round(e + .05, 2)]))
    return out
U7 = lambda a, b: [{'no': 7, 'title': 'Hava Nasıl?', 'from': a, 'to': b}]
DBL = lambda p: f'Dil Bilgisi ve Telaffuz Kitabı s.{p}'

# =================================================================== DERS KİTABI 2 — 7. ÜNİTE
page(D, 'dk2', 43, [act('dk2-43-h', 'Üniteye Hazırlık', [7, 86.5, 87, 10.5])])

# ---- A. Hava Nasıl? — Okuma. The story (4. etkinlik) runs over s.44 (panel 1) and s.45 (panels 2–6).
page(D, 'dk2', 44, [
    act('dk2-44-1', '1. etkinlik', [5, 16.0, 44, 21.5], audio=AUD('dk2', 44, 'S.110')),
    act('dk2-44-2', '2. etkinlik', [48, 16.0, 48, 21.5], audio=AUD('dk2', 44, 'S.111')),
    act('dk2-44-3', '3. etkinlik', [5, 37.0, 92, 23.5], [
        CIRC('dk2', 44, 'ilkbahar', (33.7, 56)), CIRC('dk2', 44, 'yaz', (55.8, 56)), CIRC('dk2', 44, 'sonbahar', (83, 59.2))]),
    act('dk2-44-4', '4. etkinlik', [5, 61.0, 92, 35.5],
        season_lines('dk2', 44, 70, 96) + ON(45, *season_lines('dk2', 45, 2, 45)),
        audio=AUD('dk2', 44, 'S.112'), tiles=[[5, 61.0, 92, 35.5], {'r': [5, 3.0, 92, 92.0], 'page': 45}], cols=2, nums=False),
])
page(D, 'dk2', 45, [dict(act('dk2-45-4', '4. etkinlik', [5, 3.0, 92, 92.0], skip=True), alias={'page': 44, 'act': 'dk2-44-4'})])

# 5: Esma (ilkbahar) "çok yağmur yağar", Emre (yaz) "hava sıcak", Zeynep (sonbahar) "tabiat rengârenk"
page(D, 'dk2', 46, [
    act('dk2-46-5', '5. etkinlik', [5, 2.0, 91, 22.5], [
        NUM(8.0, 15.5, '1'), NUM(8.0, 18.9, '2'), NUM(8.3, 22.4, '3'),
        NUM(52.9, 12.0, '2'), NUM(52.9, 15.5, '4'), NUM(52.9, 18.9, '1'), NUM(52.9, 22.1, '4')]),
    act('dk2-46-6a', '6. etkinlik (a)', [5, 25.0, 91, 20.0], [
        B2(46, 43.62, 'ilkbahar', x=15), B2(46, 43.61, 'yaz', x=38), B2(46, 43.61, 'sonbahar', x=60), B2(46, 43.62, 'kış', x=82)]),
    act('dk2-46-6b', '6. etkinlik (b)', [5, 45.0, 91, 23.0],
        [B2(46, 55.32, 'bu mevsimde çok yağmur yağar.', x=30, g='es')]
        + [B2(46, y, t, x=80, g='al') for y, t in zip((50.21, 52.76, 55.32), ("Ali'ye göre en güzel mevsim kış.", 'Çünkü kışın kar yağar.', 'Arkadaşlarıyla kar topu oynar.'))]
        + [B2(46, y, t, x=30, g='em') for y, t in zip((60.84, 63.39, 65.95), ("Emre'ye göre en güzel mevsim yaz.", 'Çünkü yazın hava çok sıcak olur.', 'Sıcak havada denizde yüzer.'))]
        + [B2(46, y, t, x=80, g='ze') for y, t in zip((60.84, 63.39, 65.95), ("Zeynep'e göre en güzel mevsim sonbahar.", 'Çünkü bu mevsimde yapraklar sararır.', 'Tabiat rengârenk olur.'))]),
    act('dk2-46-7', '7. etkinlik', [5, 68.5, 91, 28.0],
        [B2(46, 80.20, "Ali, kışın Uludağ'a gitti.", g='al'), B2(46, 82.35, 'Kardan adam ve kayak yaptı.', g='al'),
         B2(46, 86.48, 'Emre, yazın tatile gitti.', g='em'), B2(46, 88.63, 'Denizde yüzdü, dondurma yedi.', g='em'),
         B2(46, 92.83, 'Zeynep, sonbaharda elma ve', g='ze'), B2(46, 94.97, 'ceviz topladı. Reçel yaptı.', g='ze')]),
])

# Gizemli Yolculuk: the şifre is the riddle on s.45; "Bilmecede hangi mevsim var?" → kış; şeftali + Uludağ → Bursa
page(D, 'dk2', 47, [
    act('dk2-47-8', '8. etkinlik', [5, 6.0, 91, 14.5]),
    act('dk2-47-gy', 'Gizemli Yolculuk', [5, 22.0, 91, 70.5], [
        B2(47, 78.16, 'Aralık, ocak, şubat.', g='ş'), B2(47, 80.30, 'Bu mevsimin ayları.', g='ş'),
        B2(47, 82.45, 'Lapa lapa kar yağar.', g='ş'), B2(47, 84.60, 'Örter bütün dağları.', g='ş'),
        TX([25.0, 57.4, 14.0, 2.0], 'Kış', g='k'), B2(47, 91.29, 'Bursa', g='t')]),
])

page(D, 'dk2', 48, [act('dk2-48-1', '1. etkinlik', [5, 12.0, 91, 74.0], audio=AUD('dk2', 48, 'S.113'))])

M49 = dict(ocak=28.05, şubat=32.65, mart=38.55, nisan=43.15, mayıs=48.55, haziran=53.65, temmuz=58.95, ağustos=64.35,
           eylül=69.25, ekim=74.35, kasım=79.85, aralık=85.55)
R49 = {'ilk': (69.35, ('mart', 'nisan', 'mayıs')), 'yaz': (72.05, ('haziran', 'temmuz', 'ağustos')),
       'son': (75.35, ('eylül', 'ekim', 'kasım')), 'kış': (78.35, ('aralık', 'ocak', 'şubat'))}
page(D, 'dk2', 49, [
    act('dk2-49-2', '2. etkinlik', [5, 2.0, 91, 44.0], [
        ELC(21.0, 11.2, 7.0, 5.0, g='ilk'), ELC(34.5, 9.4, 6.5, 5.0, g='ilk'),
        ELC(20.2, 20.4, 9.0, 5.0, g='yaz'), ELC(40.4, 21.4, 9.0, 5.0, g='yaz'),
        EL([25.1, 29.4, 7.7, 6.4], g='son'), EL([45.3, 28.5, 7.7, 6.4], g='son'),
        EL([29.5, 39.3, 7.7, 6.4], g='kış'), EL([39.4, 38.7, 7.7, 6.4], g='kış'), EL([58.0, 39.3, 7.7, 6.4], g='kış')]),
    act('dk2-49-3a', '3. etkinlik (a)', [5, 46.0, 91, 7.0], [B2(49, 51.85, 'İlkbahar, yaz, sonbahar, kış.')]),
    act('dk2-49-3b', '3. etkinlik (b)', [8, 53.5, 84, 26.5],
        [CK(M49[m], y, 2.0, g=g) for g, (y, ms) in R49.items() for m in ms]),
    act('dk2-49-3c', '3. etkinlik (c)', [8, 80.5, 86, 15.5], [
        B2(49, 85.72, 'Ben ilkbaharda çiçek toplarım.'), B2(49, 88.79, 'Ben yazın denizde yüzerim.'),
        LB(24.0, 82.1, 91.75, 'Ben sonbaharda yaprakları toplarım.'), B2(49, 94.67, 'Ben kışın kayak yaparım.')]),
])

# ---- Dinleme
page(D, 'dk2', 50, [
    act('dk2-50-1', '1. etkinlik', [5, 18.5, 46, 21.5], audio=AUD('dk2', 50, 'S.114')),
    act('dk2-50-2', '2. etkinlik', [48, 18.5, 48, 21.5], audio=AUD('dk2', 50, 'S.115')),
    act('dk2-50-3', '3. etkinlik', [5, 44.0, 91, 45.0]),
], [link([28.2, 7.6, 31.1, 2.4], 'dbt', 109, DBL(109), {'act': 'dbt111-5'}, 'dbt109-1')])
page(D, 'dk2', 51, [act('dk2-51-4', '4. etkinlik', [5, 3.0, 91, 85.0], [
    B2(51, 24.87, 'Türkiye'), B2(51, 37.03, 'karlıydı'), B2(51, 52.61, 'güneşliydi'), B2(51, 68.15, 'yağmurluydu'), B2(51, 83.73, 'rüzgârlıydı')],
    audio=AUD('dk2', 51, 'S.116'))])

C52 = (30, 55, 80)
page(D, 'dk2', 52, [
    act('dk2-52-5', '5. etkinlik', [5, 3.0, 91, 40.0], [
        ELC(48.9, 17.0, 3.6, 2.8), ELC(82.3, 10.0, 3.6, 2.8), ELC(82.3, 26.3, 3.6, 2.8), ELC(48.9, 26.3, 3.6, 2.8), ELC(15.5, 33.0, 3.6, 2.8)]
        + [NUM(x, 40.3, ch, 3.0, 3.0, g='şifre') for x, ch in zip((47.7, 53.1, 58.5, 64.0, 69.4), 'EVSİM')]),
    act('dk2-52-6', '6. etkinlik', [5, 45.0, 91, 51.0],
        MULTI(B2, 52, (67.48, 69.62, 71.77), "Negina, Mogadişu'da yaşıyor.", x=C52[0], g='n1')
        + MULTI(B2, 52, (67.48, 69.62, 71.77), "Mogadişu'da dün hava güneşliydi.", x=C52[1], g='n2')
        + MULTI(B2, 52, (67.48, 69.62, 71.77), 'Negina, arkadaşlarıyla piknik yaptı.', x=C52[2], g='n3')
        + MULTI(B2, 52, (77.75, 79.90, 82.04), "Mahmut, Kabil'de yaşıyor.", x=C52[0], g='m1')
        + MULTI(B2, 52, (77.75, 79.90, 82.04), "Kabil'de dün hava yağmurluydu.", x=C52[1], g='m2')
        + MULTI(B2, 52, (77.75, 79.90, 82.04), 'Mahmut, ailesiyle evde oturdu. Çizgi film izledi.', x=C52[2], g='m3')
        + MULTI(B2, 52, (87.82, 89.96, 92.11), "Vilora, Priştine'de yaşıyor.", x=C52[0], g='v1')
        + MULTI(B2, 52, (87.82, 89.96, 92.11), "Priştine'de dün hava rüzgârlıydı.", x=C52[1], g='v2')
        + MULTI(B2, 52, (87.82, 89.96, 92.11), 'Vilora, ablasıyla uçurtma uçurdu.', x=C52[2], g='v3')),
])
page(D, 'dk2', 53, [
    act('dk2-53-7', '7. etkinlik', [5, 9.0, 91, 26.5], [
        B2(53, 14.65, 'Bişkek’te'), B2(53, 19.29, 'Benim şehrimde dün hava soğuktu.'), B2(53, 23.94, 'Ben dün okula gittim.'),
        LB(45.3, 90.0, 28.60, 'Benim şehrimde bugün hava güneşli.'), B2(53, 33.24, 'Ben şimdi dersi dinliyorum.')]),
    act('dk2-53-sv1a', 'Söz Varlığı 1 (a)', [5, 40.0, 91, 27.5]),
    act('dk2-53-sv1b', 'Söz Varlığı 1 (b)', [5, 68.5, 91, 21.0], [
        B2(53, 84.14, 'yağıyor.', x=17), B2(53, 84.13, 'yağıyor.', x=42), B2(53, 84.14, 'esiyor.', x=63), B2(53, 84.13, 'açıyor.', x=85)]),
])
page(D, 'dk2', 54, [
    act('dk2-54-2a', 'Söz Varlığı 2 (a)', [5, 2.0, 91, 17.5], audio=AUD('dk2', 54, 'S.117')),
    act('dk2-54-2b', 'Söz Varlığı 2 (b)', [5, 19.5, 91, 17.5], [
        B2(54, 24.15, 'hava yağmurlu.'), B2(54, 27.82, 'hava karlı ve soğuk.'), B2(54, 31.56, 'hava güneşli.'), B2(54, 35.29, 'hava soğuk.')]),
    act('dk2-54-s', 'Şarkı Zamanı', [5, 44.0, 91, 46.0], audio=AUD('dk2', 54, 'M.019')),
], [link([28.4, 38.6, 31.1, 2.4], 'dbt', 111, DBL(111), {'act': 'dbt112-4'}, 'dbt111-1'),
    link([28.4, 90.8, 31.1, 2.4], 'dbt', 113, DBL(113), {'act': 'dbt114-5b'}, 'dbt113-1')])
page(D, 'dk2', 55, [
    act('dk2-55-1', 'Konuşma 1', [5, 8.0, 91, 34.5], [B2(55, 36.92, 'rüzgârlıydı'), B2(55, 41.52, 'yağmurluydu')]),
    act('dk2-55-2', 'Konuşma 2', [5, 43.0, 91, 53.0]),
])
page(D, 'dk2', 56, [
    act('dk2-56-3a', '3. etkinlik (a)', [5, 2.0, 91, 41.5]),
    act('dk2-56-3b', '3. etkinlik (b)', [5, 44.0, 91, 35.0]),
    act('dk2-56-3c', '3. etkinlik (c)', [5, 80.0, 91, 15.5],
        MULTI(B2, 56, (89.09, 91.24, 93.38), 'Trabzon’da iki gün önce hava yağmurluydu. Benim şehrimde ise hava güneşliydi.', x=20, g='a', per=24)
        + MULTI(B2, 56, (89.10, 91.25, 93.39), 'Trabzon’da dün hava bulutluydu. Benim şehrimde dün hava yağmurluydu.', x=50, g='b', per=24)
        + MULTI(B2, 56, (89.10, 91.25, 93.39), 'Trabzon’da ve benim şehrimde bugün hava güneşli.', x=80, g='c', per=24)),
])
page(D, 'dk2', 57, [
    act('dk2-57-1a', 'Yazma 1 (a)', [5, 8.0, 91, 17.0]),
    act('dk2-57-1b', 'Yazma 1 (b)', [5, 25.0, 91, 15.0], MULTI(B2, 57, (29.92, 32.07, 34.22, 36.36),
        'Ben en çok ilkbahar mevsimini seviyorum. Çünkü bu mevsimde her yerde çiçekler açıyor. Hava ılık oluyor. Bu mevsimin ayları mart, nisan ve mayıstır.', per=75)),
    act('dk2-57-2', 'Yazma 2', [5, 41.0, 91, 55.0], [
        LB(45.5, 91.4, 80.10, 'Ankara’da hava karlı.'), B2(57, 82.96, 'Gine’de hava yağmurlu.'), B2(57, 86.03, 'Riyad’da hava daha sıcak.'),
        B2(57, 89.04, 'En soğuk şehir Ankara’dır.'), B2(57, 92.01, 'Ben Ankara’da yaşamak isterim.', g='s'),
        LB(45.5, 91.6, 94.20, 'Çünkü soğuk havayı seviyorum.', g='s')]),
])

# ---- B. Dört Mevsim Türkiye
page(D, 'dk2', 58, [
    act('dk2-58-1a', 'Okuma 1 (a)', [5, 20.0, 91, 42.0]),
    act('dk2-58-1b', 'Okuma 1 (b)', [5, 66.0, 91, 29.5], [
        B2(58, 73.40, 'Ankara’nın batısında İstanbul var.'), B2(58, 82.14, 'İstanbul’un güneyinde Antalya var.', x=20),
        B2(58, 82.14, 'Erzurum’da hava soğuk ve karlı.', x=70), B2(58, 90.73, 'Rize’de hava 20 derece.', x=20),
        B2(58, 90.73, 'En sıcak şehir Antalya.', x=70)]),
])
page(D, 'dk2', 59, [act('dk2-59-2', 'Okuma 2', [5, 2.0, 91, 93.0], audio=AUD('dk2', 59, 'S.118'))])

COLS60 = dict(b=25, m=40, k=55, r=70, y=85)
def cell(rows, col, text, g, per=11):
    return MULTI(B2, 60, rows, text, x=COLS60[col], g=g, per=per)
IST, ANT, RIZ, ERZ = (14.95, 17.09, 19.24, 21.38), (24.51, 26.66, 28.81, 30.95), (34.07, 36.21, 38.36, 40.51), (43.61, 45.76, 47.90, 50.05)
page(D, 'dk2', 60, [
    act('dk2-60-3', '3. etkinlik', [7, 5.5, 87, 45.5],
        cell(IST, 'm', 'İlkbahar', 'ist') + cell(IST, 'k', 'Şemsiye, yağmurluk ve hırka', 'ist') + cell(IST, 'r', 'Yeşil, mavi ve kırmızı', 'ist')
        + cell(IST, 'y', 'Pikniğe gideriz. Sahilde yürürüz. Bisiklet süreriz.', 'ist', per=12)
        + cell(ANT, 'b', 'Akdeniz Bölgesi’nde', 'ant') + cell(ANT, 'k', 'Şapka, güneş gözlüğü ve şort', 'ant')
        + cell(ANT, 'r', 'Mavi ve yeşil', 'ant') + cell(ANT, 'y', 'Denizde yüzeriz ve güneşleniriz.', 'ant', per=12)
        + cell(RIZ, 'b', 'Karadeniz Bölgesi’nde', 'riz') + cell(RIZ, 'm', 'Sonbahar', 'riz') + cell(RIZ, 'k', 'Şemsiye ve yağmurluk', 'riz')
        + cell(RIZ, 'y', 'Çay toplarız. Kışa hazırlık yaparız.', 'riz', per=12)
        + cell(ERZ, 'b', 'Doğu Anadolu Bölgesi’nde', 'erz') + cell(ERZ, 'm', 'Kış', 'erz') + cell(ERZ, 'r', 'Beyaz', 'erz')
        + cell(ERZ, 'y', 'Kayak yaparız. Kar topu oynarız. Kardan adam yaparız.', 'erz', per=12)),
    act('dk2-60-4', '4. etkinlik', [5, 52.0, 91, 19.5], [
        B2(60, 62.02, 'İstanbul, Antalya’dan daha soğuktur.'), B2(60, 65.95, 'En sıcak şehir Antalya’dır.'), B2(60, 69.88, 'En soğuk şehir Erzurum’dur.')]),
    act('dk2-60-5', '5. etkinlik', [5, 72.0, 91, 24.0], [
        B2(60, 91.04, 'Antalya’da yaşıyor.', x=35, g='k'), B2(60, 91.04, 'Çantanıza şapka, güneş gözlüğü', x=70, g='k2'),
        B2(60, 93.18, 've şort koymayı unutmayın.', x=70, g='k2')]
        + ON(61, B2(61, 6.73, 'Rize’de yaşıyor.', x=35, g='f'), B2(61, 6.72, 'Çantanıza şemsiye ve yağmurluk', x=70, g='f2'),
             B2(61, 8.88, 'koymayı unutmayın.', x=70, g='f2'),
             B2(61, 15.87, 'Erzurum’da yaşıyor.', x=35, g='u'), B2(61, 15.87, 'Çantanıza eldiven, bere, atkı,', x=70, g='u2'),
             B2(61, 18.02, 'kazak ve mont koymayı unutmayın.', x=70, g='u2')),
        tiles=[[5, 72.0, 91, 24.0], {'r': [5, 2.0, 91, 19.0], 'page': 61}], cols=1, nums=False),
])
page(D, 'dk2', 61, [
    dict(act('dk2-61-5', '5. etkinlik', [5, 2.0, 91, 19.0], skip=True), alias={'page': 60, 'act': 'dk2-60-5'}),
    act('dk2-61-6a', '6. etkinlik (a)', [5, 28.0, 91, 44.5]),
    act('dk2-61-6b', '6. etkinlik (b)', [5, 74.0, 91, 20.0]),
])
page(D, 'dk2', 62, [
    act('dk2-62-1', 'Söz Varlığı 1', [5, 8.5, 91, 37.0], audio=AUD('dk2', 62, 'M.020')),
    act('dk2-62-2', 'Söz Varlığı 2', [5, 45.5, 91, 9.0], audio=AUD('dk2', 62, 'S.119')),
    act('dk2-62-3', 'Söz Varlığı 3', [5, 55.0, 91, 41.0],
        MULTI(B2, 62, (87.21, 89.36, 91.50), 'Hırka, gömlek ve ceket', x=17, g='i', per=14)
        + MULTI(B2, 62, (87.21, 89.35, 91.50), 'Tişört, şort, terlik ve şapka', x=40, g='y', per=14)
        + MULTI(B2, 62, (87.21, 89.35, 91.50), 'Hırka, ceket ve kazak', x=62, g='s', per=14)
        + MULTI(B2, 62, (87.21, 89.35, 91.50), 'Mont, kazak, bot, bere ve eldiven', x=84, g='k', per=14)),
])
# 4a: the arrows' colours (sarı, turuncu, kırmızı, mavi, siyah) go with yağmurluk, tişört, kazak, şapka, ayakkabı
page(D, 'dk2', 63, [
    act('dk2-63-4a', 'Söz Varlığı 4 (a)', [5, 2.0, 91, 35.5], [
        B2(63, 14.41, 'Turuncu tişört.'), B2(63, 21.41, 'Kırmızı kazak.'), B2(63, 28.31, 'Mavi şapka.'), B2(63, 34.49, 'Siyah ayakkabı.')]),
    act('dk2-63-4b', 'Söz Varlığı 4 (b)', [5, 38.0, 91, 9.5], [
        B2(63, 42.44, 'Ben sonbaharda hırka giyerim.', x=70), B2(63, 45.51, 'Ben ilkbaharda yağmurluk giyerim.', x=25),
        B2(63, 45.50, 'Ben kışın mont giyerim.', x=70)]),
    act('dk2-63-d1', 'Dinleme 1', [5, 59.0, 91, 37.0], [
        B2(63, 64.46, 'atkı, kazak,', g='k'), B2(63, 67.02, 'bere ve eldiven', g='k'), B2(63, 69.57, 'kışın giyeriz.', g='k'),
        B2(63, 81.32, 'tişört, şort,', g='y'), B2(63, 83.88, 'güneş gözlüğü,', g='y'), B2(63, 86.43, 'terlik ve gömlek', g='y'),
        B2(63, 88.99, 'yazın giyeriz.', g='y')]),
], [link([27.8, 49.4, 30.9, 2.4], 'dbt', 115, DBL(115), {'act': 'dbt116-5'}, 'dbt115-1')])
page(D, 'dk2', 64, [
    act('dk2-64-2', 'Dinleme 2', [5, 3.0, 91, 63.5], [
        B2(64, 49.23, 'kuzeyinde', x=65), B2(64, 49.23, 'güneyinde', x=86), B2(64, 56.03, 'mevsim'),
        B2(64, 62.83, 'kışın', x=48), B2(64, 62.83, 'yazın çok', x=80)], audio=AUD('dk2', 64, 'S.120')),
    act('dk2-64-3', 'Dinleme 3', [5, 68.0, 91, 28.0], [
        B2(64, 81.83, 'Başkenti Ankara’dır.', x=25), B2(64, 81.85, 'Para birimi Türk lirasıdır.', x=70),
        B2(64, 87.66, 'Nüfusu 83 milyondur.', x=25), B2(64, 87.67, 'Türkiye’de dört mevsim yaşanır.', x=70),
        B2(64, 93.48, 'Türkiye’nin iklimi ılıktır.', x=25), B2(64, 93.50, 'Çünkü İstanbul önemli bir kültür şehridir.', x=70)]),
])
page(D, 'dk2', 65, [
    act('dk2-65-4', '4. etkinlik', [5, 8.5, 91, 26.0], [
        LB(35.7, 90.8, 14.18, 'Kırgızistan'), B2(65, 20.06, 'Bişkek'), B2(65, 23.02, 'Kırgız somu'),
        B2(65, 25.94, 'Yaklaşık 7 milyon'), LB(35.7, 90.8, 28.90, 'Dört mevsim yaşanır.'),
        B2(65, 31.81, 'Kışın soğuk ve karlı, yazın sıcak olur.')]),
    act('dk2-65-sv1a', 'Söz Varlığı 1 (a)', [5, 41.5, 91, 24.5]),
    act('dk2-65-sv1b', 'Söz Varlığı 1 (b)', [5, 66.0, 91, 28.5], audio=AUD('dk2', 65, 'M.021')),
])
page(D, 'dk2', 66, [
    act('dk2-66-2', 'Söz Varlığı 2', [5, 2.0, 91, 26.0], audio=AUD('dk2', 66, 'S.121')),
    act('dk2-66-3a', 'Söz Varlığı 3 (a)', [5, 28.5, 91, 45.0]),
    act('dk2-66-3b', 'Söz Varlığı 3 (b)', [5, 74.0, 91, 22.0], [
        B2(66, 78.16, 'Kırgızistan’ın kuzeyinde Kazakistan vardır.'), B2(66, 80.31, 'Kırgızistan’ın güneyinde Tacikistan vardır.'),
        B2(66, 82.45, 'Kırgızistan’ın batısında Özbekistan vardır.'), B2(66, 84.60, 'Kırgızistan’ın doğusunda Çin vardır.')]),
])
page(D, 'dk2', 67, [
    act('dk2-67-s', 'Şarkı Zamanı', [5, 10.0, 91, 34.5], audio=AUD('dk2', 67, 'M.022')),
    act('dk2-67-k1', 'Konuşma 1', [5, 55.5, 91, 40.5]),
], [link([28.1, 6.3, 30.9, 2.4], 'dbt', 117, DBL(117), {'act': 'dbt118-4'}, 'dbt117-1'),
    link([28.1, 48.2, 30.9, 2.4], 'dbt', 119, DBL(119), {'act': 'dbt120-5b'}, 'dbt119-1')])
# from the four pictures on s.67: pazartesi -3°, salı -1° kar topu, çarşamba 7° Emre hasta, perşembe 2°
page(D, 'dk2', 68, [
    act('dk2-68-2', 'Konuşma 2', [5, 3.0, 91, 31.0], [
        B2(68, 13.77, 'Salı günü hava karlıydı.'), B2(68, 18.52, 'Salı günü çocuklar kar topu oynadı.'),
        B2(68, 23.22, 'Üçüncü gün Emre hasta oldu. Yatakta yattı.'), B2(68, 27.98, 'Çarşamba günü hava daha sıcaktı.'),
        B2(68, 32.73, 'En soğuk gün pazartesiydi.')]),
    act('dk2-68-3', 'Konuşma 3', [5, 35.0, 91, 15.0],
        MULTI(B2, 68, (43.47, 45.62, 47.76), 'Emre soğuk havada kar topu oynadı. Çok üşüdü ve hasta oldu.', x=25, g='a', per=34)
        + MULTI(B2, 68, (43.47, 45.61, 47.76), 'Mont, bere, atkı ve eldiven giyeriz. Çünkü hava çok soğuk olur.', x=70, g='b', per=34)),
    act('dk2-68-4', 'Konuşma 4', [5, 50.0, 91, 46.0]),
])
page(D, 'dk2', 69, [
    act('dk2-69-1a', 'Yazma 1 (a)', [5, 8.0, 91, 28.5]),
    act('dk2-69-2a', 'Yazma 2 (a)', [5, 39.0, 91, 24.5]),
    act('dk2-69-2b', 'Yazma 2 (b)', [5, 63.5, 91, 32.0], [
        B2(69, 77.80, 'Hava karlı.', x=17), B2(69, 77.80, 'Hava yağmurlu.', x=39),
        B2(69, 77.80, 'Hava güneşli.', x=61), B2(69, 77.80, 'Hava bulutlu.', x=83)]),
])

# ---- C. Mevsimler (TRT Çocuk; answers from the slides — the cartoon itself is not on the site)
page(D, 'dk2', 70, [
    act('dk2-70-1', '1. etkinlik', [5, 8.0, 91, 25.0], [
        B2(70, 25.02, 'İlkbahar', x=17), B2(70, 25.01, 'Yaz', x=39), B2(70, 25.02, 'Sonbahar', x=61), B2(70, 25.01, 'Kış', x=83),
        CK(42.2, 31.0, 2.4, g='c')], audio=AUD('dk2', 70, 'V.007')),
    act('dk2-70-2', '2. etkinlik', [5, 33.5, 91, 19.0], [
        B2(70, 40.51, 'Yazın hava sıcak olur.', g='y'), B2(70, 42.65, 'Denizde yüzülür.', g='y'),
        B2(70, 48.89, 'Sonbaharda hava serinler.', x=25, g='s'), B2(70, 51.03, 'Sarı yapraklar dökülür.', x=25, g='s'),
        B2(70, 48.73, 'Kışın hava soğuk ve karlı olur.', x=70, g='k'), B2(70, 50.88, 'Kar topu oynanır.', x=70, g='k')]),
    act('dk2-70-3', '3. etkinlik', [5, 53.0, 91, 11.5], [
        B2(70, 62.12, 'Yaz mevsimi', x=15), B2(70, 62.11, 'İlkbahar mevsimi', x=38), B2(70, 62.12, 'Sonbahar mevsimi', x=61), B2(70, 62.11, 'Kış mevsimi', x=83)]),
    act('dk2-70-4', '4. etkinlik', [5, 66.0, 91, 20.0], [
        B2(70, 73.56, 'Ayakkabı dükkânına niçin müşteri', x=25, g='a'), B2(70, 75.70, 'gelmediğini bulmak için gidiyorlar.', x=25, g='a'),
        B2(70, 73.47, 'Kare ülkesinin batısında.', x=70, g='b'),
        B2(70, 81.78, 'Çünkü ayakkabılar yanlış mevsimin', x=25, g='c'), B2(70, 83.93, 'dekoruna göre dizilmiş.', x=25, g='c'),
        B2(70, 81.69, 'Dükkâna neden müşteri gelmediğini', x=70, g='d'), B2(70, 83.84, 'araştırıyorlar.', x=70, g='d')]),
    act('dk2-70-5', '5. etkinlik', [32, 86.5, 62, 9.5]),
])
# s.71: Mahmut (Kabil, Afganistan) yağmur; Vilora (Priştine) kar; Esma (İstanbul) bulutlu, uçurtma; Hasan (Lahor) güneşli
page(D, 'dk2', 71, [
    act('dk2-71-g', 'Hava Nasıl?', [5, 4.0, 91, 68.0]),
    act('dk2-71-1', '1. etkinlik', [5, 73.0, 91, 22.0], [
        B2(71, 90.88, 'Afganistan', x=17), B2(71, 90.89, 'Kosova', x=39), B2(71, 90.88, 'Türkiye', x=60), B2(71, 90.88, 'Pakistan', x=81)]),
])
page(D, 'dk2', 72, [act('dk2-72-p', 'Proje Zamanı', [3, 2.0, 94, 94.0])])

# =================================================================== DİL BİLGİSİ VE TELAFFUZ (7. Ünite)
page(T, 'dbt', 108)
page(T, 'dbt', 109, [
    act('dbt109-1', '1. etkinlik', [8, 22.0, 84, 45.0], audio=AUD('dbt', 109, 'S.097')),
    act('dbt109-2', '2. etkinlik', [8, 68.0, 84, 21.5], [BT(109, 86.46, 'Ben dün bisiklet sürdüm.')]),
])
page(T, 'dbt', 110, [
    act('dbt110-3', '3. etkinlik', [10, 12.0, 80, 20.0]),
    act('dbt110-4a', '4. etkinlik (a)', [10, 34.0, 80, 27.0], [
        BT(110, 51.38, 'yaşadım', x=25), BT(110, 51.38, 'uçurdum', x=60), BT(110, 53.73, 'yüzdüm', x=22),
        BT(110, 53.73, 'fotoğraf çektim', x=58), BT(110, 56.08, 'yaptım', x=22), BT(110, 56.08, 'sevdim', x=64)]),
    act('dbt110-4b', '4. etkinlik (b)', [10, 62.0, 80, 28.5], [
        BT(110, 70.59, 'Mahmut, ilkbaharda uçurtma uçurdu.'), BT(110, 78.76, 'Mahmut, yazın denizde yüzdü.', x=30),
        BT(110, 78.76, 'Sonbaharda bol bol fotoğraf çekti.', x=70), BT(110, 87.22, 'Mahmut, kışın kayak yaptı.', x=30),
        BT(110, 87.22, 'En çok Türk yemeklerini sevdi.', x=70)]),
])
page(T, 'dbt', 111, [
    act('dbt111-5', '5. etkinlik', [8, 7.0, 84, 23.5], [
        BT(111, 13.13, 'İlkbaharda piknik yaptım.'), BT(111, 18.01, 'Yazın denizde yüzdüm.'),
        BT(111, 22.94, 'Sonbaharda reçel yaptım.'), BT(111, 27.88, 'Kışın kayak yaptım.')]),
    act('dbt111-1', '1. etkinlik', [8, 39.0, 84, 36.5], audio=AUD('dbt', 111, 'S.098')),
    act('dbt111-2', '2. etkinlik', [8, 76.0, 84, 17.5]),
])
page(T, 'dbt', 112, [
    act('dbt112-3a', '3. etkinlik (a)', [10, 12.0, 80, 20.0]),
    act('dbt112-3b', '3. etkinlik (b)', [10, 36.0, 80, 32.0], [
        BT(112, 61.13, 'yağmurluydu.', x=40), BT(112, 61.13, 'karlı ve soğuktu.', x=80),
        BT(112, 66.01, 'güneşliydi.', x=40), BT(112, 66.01, 'bulutluydu.', x=80)]),
    act('dbt112-4', '4. etkinlik', [10, 69.0, 80, 22.5], [
        BT(112, 79.58, 'Benim şehrimde dün hava yağmurluydu.', x=30), BT(112, 79.58, 'Benim şehrimde bugün hava güneşli.', x=70),
        BT(112, 89.51, 'Ben dün evde televizyon izledim.', x=30), BT(112, 89.51, 'Ben şimdi voleybol oynuyorum.', x=70)]),
])
page(T, 'dbt', 113, [
    act('dbt113-1', '1. etkinlik', [8, 13.0, 84, 17.5], audio=AUD('dbt', 113, 'S.099')),
    act('dbt113-2', '2. etkinlik', [8, 31.0, 84, 36.5], audio=AUD('dbt', 113, 'S.100')),
    act('dbt113-3', '3. etkinlik', [8, 69.5, 84, 15.5], audio=AUD('dbt', 113, 'S.101')),
])
page(T, 'dbt', 114, [
    act('dbt114-4', '4. etkinlik', [10, 7.0, 80, 46.5], audio=AUD('dbt', 114, 'S.102')),
    act('dbt114-5a', '5. etkinlik (a)', [10, 55.0, 40, 22.5], [BT(114, 74.65, 'Mevsim.')], audio=AUD('dbt', 114, 'S.103')),
    act('dbt114-5b', '5. etkinlik (b)', [52, 55.0, 38, 22.5], [
        LB(54.7, 88.2, 66.4, 'Ne kar yağdırır, ne çiçek açtırır,', g='b'), LB(54.7, 88.2, 68.4, 'O sadece yaprakları sarartır.', g='b'),
        BT(114, 70.48, 'Bil bakalım ben neyim?', g='b'), LB(54.7, 88.2, 72.7, 'Sonbahar.', g='c')]),
])
page(T, 'dbt', 115, [
    act('dbt115-1', '1. etkinlik', [8, 21.0, 84, 53.5], audio=AUD('dbt', 115, 'S.104')),
    act('dbt115-2', '2. etkinlik', [8, 76.0, 84, 17.5], [BT(115, 90.75, 'Ben kırmızı bir mont almak isterim.')]),
])
page(T, 'dbt', 116, [
    act('dbt116-3', '3. etkinlik', [10, 12.0, 80, 47.5]),
    act('dbt116-4', '4. etkinlik', [10, 61.0, 80, 24.5], [
        BT(116, 67.83, 'kırmızı tişört', x=70), BT(116, 73.18, 'beyaz pantolon', x=70), BT(116, 74.24, 'mavi ayakkabı', x=20),
        BT(116, 84.11, 'turuncu kitap', x=20), BT(116, 84.11, 'renkli bina', x=50), BT(116, 84.11, 'mavi masa', x=80)]),
    act('dbt116-5', '5. etkinlik', [10, 85.5, 80, 7.5]),
])
page(T, 'dbt', 117, [
    act('dbt117-1', '1. etkinlik', [8, 17.0, 84, 43.0], audio=AUD('dbt', 117, 'S.105')),
    act('dbt117-2', '2. etkinlik', [8, 61.0, 84, 9.0], [CK(73.2, 65.2, 2.4), CK(81.3, 68.0, 2.4)]),
    act('dbt117-3a', '3. etkinlik (a)', [8, 74.0, 84, 20.0]),
])
page(T, 'dbt', 118, [
    act('dbt118-3a', '3. etkinlik (a)', [10, 7.0, 80, 19.5], [
        BT(118, 22.06, 'Dursun, İzo’dan daha yaşlı.'), BT(118, 23.65, 'Karagöz, İzo ve Dursun’dan daha yaşlı.'), BT(118, 25.24, 'En genç İzo.')]),
    act('dbt118-3b', '3. etkinlik (b)', [10, 27.5, 80, 19.0], [BT(118, 44.21, 'Bence Karagöz hepsinden daha komik.')]),
    act('dbt118-4', '4. etkinlik', [10, 48.0, 80, 45.0], [
        BT(118, 65.42, 'Kış mevsiminden.'), BT(118, 70.36, 'Yaz mevsimi.'), BT(118, 75.24, 'Kış mevsiminden.'),
        BT(118, 80.17, 'Kış mevsimi.'), BT(118, 85.05, 'İlkbahar.'), BT(118, 89.98, 'İlkbaharı.')]),
])
page(T, 'dbt', 119, [
    act('dbt119-1', '1. etkinlik', [8, 13.0, 84, 20.5], audio=AUD('dbt', 119, 'S.106')),
    act('dbt119-2', '2. etkinlik', [8, 34.0, 84, 24.5], audio=AUD('dbt', 119, 'S.107')),
    act('dbt119-3', '3. etkinlik', [8, 60.0, 84, 20.0], [BT(119, 74.35, 'mavi.'), BT(119, 77.94, 'ilkbahar')], audio=AUD('dbt', 119, 'S.108')),
])
page(T, 'dbt', 120, [
    act('dbt120-4', '4. etkinlik', [10, 7.0, 80, 56.5], audio=AUD('dbt', 120, 'S.109')),
    act('dbt120-5a', '5. etkinlik (a)', [10, 68.0, 40, 22.5], [BT(120, 86.22, 'Eldiven.')], audio=AUD('dbt', 120, 'S.110')),
    act('dbt120-5b', '5. etkinlik (b)', [52, 68.0, 38, 22.5], [
        LB(54.7, 88.2, 79.6, 'Pantolonun kardeşi kısa,', g='b'), LB(54.7, 88.2, 81.6, 'Yazın giyilir, oh ne tasa!', g='b'),
        BT(120, 83.64, 'Dizden yukarı, serin serin,', g='b'), LB(54.7, 88.2, 85.6, 'Bul bakalım, nedir benim?', g='b'),
        LB(54.7, 88.2, 87.6, 'Şort.', g='c')]),
])

dump('dk2-u7', D, 0.7826, 'Ders Kitabı 2', U7(43, 72))
dump('dbt-u7', T, 0.6669, 'Dil Bilgisi ve Telaffuz Kitabı', U7(108, 120))
print('ok', len(D), len(T), sum(len(p['activities']) for p in D.values()), sum(len(p['activities']) for p in T.values()))
