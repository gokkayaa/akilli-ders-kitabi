# Builds data/dk2.json (Ders Kitabı 2, 6. Ünite) and data/dbt-u6.json (telaffuz s.93–108).
# usage: build_u6.py WORK   (WORK holds auto-dk2.json / auto-dbt.json from prep_unit.py)
# Answers come from the teacher's slides (6_Unite_DUZENLENMIS.pptx); where the slide had none, from the book itself.
import sys
from kit import *
W = sys.argv[1]
load(f'{W}/auto-dk2.json', f'{W}/auto-dbt.json')
D, T = {}, {}
B2 = lambda n, y, text, **k: BL(f'dk2{n}', y, text, **k)
BT = lambda n, y, text, **k: BL(f'dbt{n}', y, text, **k)
def OPT(x, y, g=None):
    """circle an option letter (a./b./c.) centred at x,y"""
    return EL([round(x - 1.7, 2), round(y - 1.25, 2), 3.4, 2.5], g=g)

# =================================================================== DERS KİTABI 2
page(D, 'dk2', 7, [act('dk2-7-h', 'Üniteye Hazırlık', [7, 86.5, 87, 10.5])])

page(D, 'dk2', 8, [
    act('dk2-8-1', '1. etkinlik', [5, 19.0, 45, 17.5], audio=AUD('dk2', 8, 'S.092')),
    act('dk2-8-2', '2. etkinlik', [50, 19.0, 45, 17.5], audio=AUD('dk2', 8, 'S.093')),
    act('dk2-8-3', '3. etkinlik', [4, 37.5, 92, 55.5], [
        B2(8, 76.22, 'şeftali', x=18, g='r2'), B2(8, 76.22, '12', x=36, g='r2'),
        B2(8, 80.0, 'İki kilo patates', x=15, g='r3'), B2(8, 80.05, '8', x=36, g='r3'),
        B2(8, 83.73, 'Bir kilo acı biber', x=15, g='r4'), B2(8, 83.73, '8', x=36, g='r4'),
        B2(8, 89.61, '35')]),
])

# s.9 story continues on s.10 (panels 5–6)
page(D, 'dk2', 9, [
    act('dk2-9-4', '4. etkinlik', [5, 2.0, 90, 93.5], audio=AUD('dk2', 9, 'S.094'),
        tiles=[[5, 9.5, 90, 85.5], {'r': [5, 1.5, 90, 37.0], 'page': 10}], cols=2, nums=False, head=[5, 2.0, 90, 5.5]),
])
page(D, 'dk2', 10, [
    dict(act('dk2-10-4', '4. etkinlik', [5, 1.5, 90, 37.0], skip=True), alias={'page': 9, 'act': 'dk2-9-4'}),
    act('dk2-10-5', '5. etkinlik', [5, 38.0, 90, 21.5], [CK(50.0, 58.4, 2.6)]),
    act('dk2-10-6', '6. etkinlik', [5, 59.5, 90, 36.0], [
        CK(20.1, 76.0, 2.6, g='a'), B2(10, 78.93, 'manava gidiyor.', g='a'),
        CK(38.8, 91.0, 2.6, g='b'), B2(10, 94.0, 'tatlı biberden alıyor.', x=30, g='b'),
        CK(61.1, 91.0, 2.6, g='c'), B2(10, 94.0, 'Osman Dede kırmızı elmadan alıyor.', x=70, g='c')]),
])

page(D, 'dk2', 11, [
    act('dk2-11-7', '7. etkinlik', [5, 2.0, 90, 63.5], [
        B2(11, 33.65, 'şeftali', x=12), B2(11, 33.65, 'kırmızı elma', x=28), B2(11, 33.65, 'yeşil elma', x=42),
        B2(11, 33.65, 'tatlı biber', x=72), B2(11, 33.65, 'acı biber', x=86),
        LN([33.0, 16.6], [70.5, 24.8], g='b1', dot=[33.0, 16.6]), B2(11, 40.30, 'Osman Dede bir kilo tatlı biber alıyor.', x=30, g='b1'),
        LN([77.5, 17.3], [31.0, 24.8], g='b4', dot=[77.5, 17.3]), B2(11, 37.13, 'Osman Dede dört kilo kırmızı elma alıyor.', x=70, g='b4'),
        LN([46.0, 17.6], [17.2, 24.8], g='b2', dot=[46.0, 17.6]), B2(11, 40.30, 'Osman Dede iki kilo şeftali alıyor.', x=70, g='b2'),
        CK(33.6, 49.2, 2.6, g='c1'), B2(11, 52.71, 'Bir kilo patates dört lira.', g='c1'),
        CK(61.1, 60.4, 2.6, g='c2'), B2(11, 63.75, 'Osman Dede manava toplam elli lira ödüyor.', g='c2')]),
    act('dk2-11-8', '8. etkinlik', [4, 66.0, 92, 29.5], [
        B2(11, 74.89, 'Hoşça kal.'), B2(11, 77.45, 'Ne kadar?'), B2(11, 80.00, 'Hoş bulduk.'), B2(11, 82.56, 'Kolay gelsin.'),
        B2(11, 85.11, 'Hayırlı işler.'), B2(11, 87.67, 'Kaç lira?'), B2(11, 90.22, 'Yine beklerim.')]),
])

page(D, 'dk2', 12, [
    act('dk2-12-8b', '8. etkinlik (b)', [8, 3.0, 85, 45.5], [
        B2(12, 16.28, 'Hayırlı işler.'), B2(12, 20.57, 'Hoş geldin.'), B2(12, 22.72, 'buldum'),
        B2(12, 31.30, 'kaç lira'), B2(12, 37.74, 'ne kadar'), B2(12, 44.18, 'Hoşça kal.'), B2(12, 46.33, 'Yine beklerim.')]),
    act('dk2-12-9', '9. etkinlik', [5, 49.0, 90, 43.5], tiles=[[5, 56.5, 90, 36.0], {'r': [6, 2.5, 88, 21.5], 'page': 13}], cols=1, nums=False),
])
page(D, 'dk2', 13, [
    dict(act('dk2-13-9', '9. etkinlik', [6, 2.5, 88, 21.5], skip=True), alias={'page': 12, 'act': 'dk2-12-9'}),
    act('dk2-13-gy', 'Gizemli Yolculuk', [5, 25.0, 90, 70.0]),
])

# İzo's list, priced from the Manav Rıza list on s.14 (the slide had older prices)
I15 = [(10.20, '22 lira'), (11.83, '24 lira'), (13.52, '15 lira'), (15.15, '6 lira'), (16.84, '6 lira'), (18.47, '5 lira'), (20.16, '1,50 lira')]
ROWS15 = [(44.79, 46.1, 'Elli lira', [89.0]), (51.85, 53.2, 'Elli lira', [89.0]), (58.85, 60.2, 'Elli lira', [89.0]), (65.90, 67.3, 'Yirmi lira', [78.8]),
          (72.95, 74.3, 'Otuz lira', [68.5, 78.8]), (79.95, 81.4, 'Beş lira', [58.3]), (87.00, 88.4, 'On lira', [68.5])]
page(D, 'dk2', 14, [
    act('dk2-14-1', '1. etkinlik', [5, 9.0, 90, 26.0], audio=AUD('dk2', 14, 'S.095')),
    act('dk2-14-2', '2. etkinlik', [5, 36.0, 90, 27.5], audio=AUD('dk2', 14, 'S.096')),
    act('dk2-14-3', '3. etkinlik (a)', [5, 64.0, 90, 28.5], ON(15, *[LB(77.9, 82.0, y, t) for y, t in I15], LB(66.6, 71.3, 21.80, '79,50')), tiles=[[5, 64.0, 90, 28.5], {'r': [5, 1.5, 90, 28.5], 'page': 15}], cols=1, nums=False),
])
page(D, 'dk2', 15, [
    dict(act('dk2-15-3a', '3. etkinlik (a)', [5, 1.5, 90, 28.5], skip=True), alias={'page': 14, 'act': 'dk2-14-3'}),
    act('dk2-15-3b', '3. etkinlik (b)', [5, 30.0, 90, 66.0],
        [it for k, (by, cy, t, xs) in enumerate(ROWS15) for it in [LB(16.7, 30.9, by, t, g=f'r{k}')] + [CK(x, cy, 2.6, g=f'r{k}') for x in xs]]
        + [B2(15, 94.72, '215 lira')]),
])

# ---- s.16: Dil Bilgisi → telaffuz s.93–95, then Dinleme
L16 = [((28.0, 31.6), (20.0, 38.4), 'Ispanak, sebze ve meyve bölümündedir.', (50.8, 91.1, 55.92)),
       ((42.6, 31.6), (20.0, 38.4), 'Fasulye, sebze ve meyve bölümündedir.', (7.0, 47.3, 58.76)),
       ((57.2, 31.6), (79.0, 38.4), 'Makarna, temel gıdalar bölümündedir.', (50.8, 91.1, 58.76)),
       ((71.8, 31.6), (50.0, 38.4), 'Yumurta, süt ürünleri ve kahvaltılıklar bölümündedir.', (7.0, 47.3, 61.70)),
       ((86.4, 31.6), (50.0, 38.4), 'Peynir, süt ürünleri ve kahvaltılıklar bölümündedir.', (50.8, 91.1, 61.70))]
page(D, 'dk2', 16, [
    act('dk2-16-1', 'Dinleme 1', [5, 15.5, 90, 48.0], audio=AUD('dk2', 16, 'S.097', 'S.098'),
        items=[it for k, (f, t, s, (a, b, y)) in enumerate(L16) for it in (LN(list(f), list(t), g=f'm{k}', dot=list(f)), LB(a, b, y, s, g=f'm{k}'))]),
    act('dk2-16-2', 'Dinleme 2', [5, 64.0, 90, 31.5], [
        B2(16, 71.11, 'muz,'), B2(16, 73.26, 'ıspanak ve fasulye'),
        B2(16, 90.63, 'yumurta ve peynir', x=50), B2(16, 88.48, 'makarna'), B2(16, 90.63, 've un', x=80)]),
], [link([28.5, 5.6, 32.5, 2.6], 'dbt', 93, 'Dil Bilgisi ve Telaffuz Kitabı s.93', {'act': 'dbt95-5b'}, 'dbt93-1')])

page(D, 'dk2', 17, [
    act('dk2-17-3', 'Dinleme 3', [5, 1.5, 90, 26.0], [CK(x, y, 2.4) for x, y in ((38.7, 15.3), (61.0, 15.3), (83.4, 15.3), (16.5, 25.4), (38.7, 25.4), (83.4, 25.4))],
        audio=AUD('dk2', 17, 'S.099'), tiles=[[5, 1.5, 90, 26.0], [5, 27.5, 90, 64.5]], cols=2, nums=False),
    act('dk2-17-4', '4. etkinlik (a)', [5, 28.0, 90, 69.0],
        [NUM(x, y, n, 2.6, 2.4) for x, y, n in ((71.8, 49.2, '2'), (27.9, 68.7, '3'), (71.8, 68.7, '4'), (27.9, 88.7, '5'), (71.8, 88.7, '6'))]),
])

page(D, 'dk2', 18, [
    act('dk2-18-5', '5. etkinlik', [5, 3.0, 90, 45.0], [OPT(36.5, 11.65), OPT(65.6, 25.85), OPT(36.5, 32.1), OPT(65.6, 38.1)]),
    act('dk2-18-6a', '6. etkinlik (a)', [5, 49.0, 90, 44.0], [
        B2(18, 66.41, 'ıspanak', x=30, g='a'), B2(18, 69.22, '7 lira', x=30, g='a'), B2(18, 66.41, 'fasulye', x=50, g='b'), B2(18, 69.22, '5 lira', x=50, g='b'),
        B2(18, 66.41, 'peynir', x=66, g='c'), B2(18, 69.22, '30 lira', x=66, g='c'), B2(18, 66.41, 'makarna', x=85, g='d'), B2(18, 69.22, '4 lira', x=85, g='d'),
        B2(18, 84.45, 'yumurta', x=30, g='e'), B2(18, 87.26, '30 lira', x=30, g='e'), B2(18, 84.45, 'muz', x=85, g='f'), B2(18, 87.26, '12 lira', x=85, g='f')]),
])
page(D, 'dk2', 19, [
    act('dk2-19-6bc', '6. etkinlik (b, c)', [5, 2.5, 90, 29.0]),
    act('dk2-19-7', '7. etkinlik', [5, 38.5, 90, 56.5], [
        B2(19, 71.62, 'Merhaba', x=20), B2(19, 74.02, 'Yardımcı'), B2(19, 78.88, 'Tabii ki', x=25), B2(19, 86.18, 'Rica ederim.', x=25),
        B2(19, 71.62, 'nasıl', x=80), B2(19, 76.47, 'kolay'), B2(19, 78.88, 'peynir', x=65), B2(19, 86.18, 'koli', x=65),
        B2(19, 91.04, 'Hayırlı'), B2(19, 93.44, 'teşekkür ederim.')]),
])

page(D, 'dk2', 20, [
    act('dk2-20-1', '1. etkinlik', [5, 9.0, 90, 21.0], audio=AUD('dk2', 20, 'S.100')),
    act('dk2-20-2', '2. etkinlik', [5, 30.0, 90, 31.0], audio=AUD('dk2', 20, 'S.101')),
    act('dk2-20-3', '3. etkinlik', [5, 63.0, 90, 31.5], [
        B2(20, 92.98, 'Terazide beş yüz gram çilek var.', x=20), B2(20, 92.98, 'Terazide iki kilo elma var.', x=50), B2(20, 92.98, 'Terazide beş kilo karpuz var.', x=80)]),
])
P21 = ['beş yüz gram şeker,', 'bir litre ayran,', 'bir paket çikolata,', 'iki şişe su,', 'bir paket bisküvi,', 'bir demet maydanoz', 've bir koli yumurta']
R21 = [('Yoğurt', '30 lira'), ('Salatalık', '20 lira'), ('Yumurta', '80 lira'), ('Zeytin', '50 lira'), ('Reçel', '35 lira'), ('Simit', '6 lira'), ('İncir', '60 lira'), ('Tavuk', '85 lira')]
Y21 = [75.91, 78.31, 80.76, 83.21, 85.61, 88.07, 90.52, 92.97]
S21 = ['bir kilo', 'salatalık, bir koli yumurta,', 'bir kilo yoğurt,', 'bir kilo zeytin,', 'bir paket reçel,', 'bir adet simit,', 'bir kilo incir ve', 'bir kilo tavuk', 'almak istiyorum.']
page(D, 'dk2', 21, [
    act('dk2-21-4', '4. etkinlik', [5, 2.0, 90, 32.5], [
        LN([52.5, 9.6], [27.6, 21.7], dot=[52.5, 9.6]), LN([32.4, 9.8], [70.4, 21.6], dot=[32.4, 9.8]),
        LN([84.2, 9.8], [43.9, 21.6], dot=[84.2, 9.8]), LN([66.6, 9.6], [83.7, 21.7], dot=[66.6, 9.6])]),
    act('dk2-21-5', '5. etkinlik', [4, 35.0, 92, 28.0],
        [LB(75.2 if k == 0 else 70.1, 93.1 if k == 0 else 93.0, y, t, g='p') for k, (y, t) in enumerate(zip([42.44, 44.59, 46.74, 48.88, 51.03, 53.17, 55.32], P21))]
        + [B2(21, 61.76, 'altmış')]),
    act('dk2-21-6', '6. etkinlik', [4, 64.0, 92, 31.0],
        [it for k, ((n, p), y) in enumerate(zip(R21, Y21)) for it in (LB(35.9, 50.5, y, n, g=f'r{k}'), LB(52.9, 67.5, y, p, g=f'r{k}'))]
        + [LB(84.8 if k == 0 else 71.3, 93.9 if k == 0 else 94.2, y, t, g='s') for k, (y, t) in enumerate(zip([70.34, 72.49, 74.64, 76.78, 78.93, 81.07, 83.22, 85.37, 87.51], S21))]
        + [B2(21, 91.80, '366')]),
])

# ---- s.22: Dil Bilgisi → s.96–98, song, Telaffuz → s.99–100
page(D, 'dk2', 22, [
    act('dk2-22-s', 'Şarkı Zamanı', [5, 17.5, 90, 65.5], audio=AUD('dk2', 22, 'M.017')),
], [link([27.6, 9.3, 32.5, 2.6], 'dbt', 96, 'Dil Bilgisi ve Telaffuz Kitabı s.96', {'act': 'dbt98-5b'}, 'dbt96-1'),
    link([27.2, 85.4, 32.5, 2.6], 'dbt', 99, 'Dil Bilgisi ve Telaffuz Kitabı s.99', {'act': 'dbt100-5b'}, 'dbt99-1')])

L23 = [('Su', '1 lira 50 kuruş', 'Bir şişe su 1 lira 50 kuruş.'), ('Yumurta', '30 lira', 'Bir koli yumurta 30 lira.'), ('Bisküvi', '2 lira', 'Bir paket bisküvi 2 lira.'),
       ('Elma', '10 lira', 'Bir kilo elma 10 lira.'), ('Üzüm', '10 lira', 'Bir kilo üzüm 10 lira.'), ('Ayran', '5 lira', 'Bir litre ayran 5 lira.')]
page(D, 'dk2', 23, [
    act('dk2-23-1a', '1. etkinlik (a)', [5, 7.0, 90, 22.0], [
        B2(23, 12.81, '1', x=20), B2(23, 12.81, '4', x=36), B2(23, 12.81, '2', x=50), B2(23, 12.81, '7', x=63), B2(23, 12.81, '5, 6', x=77), B2(23, 12.81, '3', x=91)]),
    act('dk2-23-1b', '1. etkinlik (b)', [5, 30.0, 90, 27.0],
        [it for k, ((n, p, s), y, y2) in enumerate(zip(L23, [39.48, 42.09, 44.69, 47.30, 49.90, 52.51], [37.54, 40.55, 43.62, 46.63, 49.65, 52.71]))
         for it in (LB(8.6, 14.6, y, n, g=f'r{k}'), LB(16.4, 30.6, y, p, g=f'r{k}'), LB(38.6, 92.5, y2, s, g=f'r{k}'))]),
    act('dk2-23-2', '2. etkinlik', [5, 58.0, 90, 37.0], [
        B2(23, 76.02, 'Markette Alışveriş'),
        B2(23, 79.34, 'Süt ürünleri', x=35), B2(23, 81.48, 'nerede', x=20), B2(23, 81.48, 'olur musunuz', x=40),
        B2(23, 83.60, 'Görevli', x=12), B2(23, 83.63, 'Süt ürünleri bölümü', x=35), B2(23, 85.77, 'on metre ileride, solda.', x=25),
        B2(23, 87.92, 'Teşekkür ederim.', x=30), B2(23, 92.18, 'Görevli', x=12),
        B2(23, 79.34, 'Size nasıl', x=80), B2(23, 81.48, 'yardımcı olabilirim', x=70), B2(23, 83.63, 'Merhaba, kolay gelsin', x=70),
        B2(23, 85.77, 'Sağ olun. Ne almak istersiniz?', x=70), B2(23, 87.92, 'Bir litre süt almak istiyorum.', x=70),
        B2(23, 90.07, 'Buyurun, 3 lira.', x=70), B2(23, 92.21, 'Teşekkür ederim. Hayırlı işler.', x=70)]),
])
page(D, 'dk2', 24, [act('dk2-24-3', '3. etkinlik', [5, 2.0, 90, 90.5])])

M25 = [((17.0, 15.5), (25.5, 24.3), '2 adet ekmek', 19.45), ((17.0, 22.7), (25.5, 14.7), '500 gram un', 22.41), ((17.0, 29.3), (25.5, 17.9), '3 demet maydanoz', 25.38),
       ((17.0, 36.2), (25.5, 34.0), '5 paket makarna', 28.29), ((47.3, 15.5), (38.7, 37.2), '2 litre süt', 31.25), ((47.3, 22.5), (38.7, 27.5), '1 kutu meyve suyu', 34.22),
       ((47.3, 36.2), (38.7, 30.8), '1 koli yumurta', 37.13)]
page(D, 'dk2', 25, [
    act('dk2-25-1', '1. etkinlik', [5, 8.0, 90, 31.0],
        [it for k, (f, t, s, y) in enumerate(M25) for it in (LN(list(f), list(t), g=f'm{k}', dot=list(f)), LB(65.4, 88.7, y, s, g=f'm{k}'))]),
    act('dk2-25-2', '2. etkinlik', [5, 40.0, 90, 56.0], [
        B2(25, 83.07, 'bir adet ekmek,', g='m'), B2(25, 85.21, 'bir litre ayran, bir koli yumurta', g='m'), B2(25, 87.36, 've bir paket bisküvi', g='m'),
        B2(25, 89.51, 'almak isterim.', g='m'), B2(25, 93.80, 'otuz', g='m'),
        B2(25, 82.96, 'bir kilo peynir', g='s'), B2(25, 85.11, 've bir şişe limonata', g='s'), B2(25, 87.26, 'almak isterim.', g='s'), B2(25, 93.70, 'on sekiz', g='s')]),
])

# ---- B. Kahvaltı Zamanı
page(D, 'dk2', 26, [
    act('dk2-26-1a', '1. etkinlik (a)', [5, 16.0, 90, 61.5], audio=AUD('dk2', 26, 'S.102')),
    act('dk2-26-1b', '1. etkinlik (b)', [5, 78.5, 90, 16.5], [
        B2(26, 87.56, 'Peynir ve çay.', x=20),
        B2(26, 87.56, 'Simit, menemen, yumurta, domates,', x=70, g='f'), B2(26, 89.71, 'salatalık, zeytin, meyve suyu,', x=70, g='f'), B2(26, 91.86, 'su böreği ve reçel.', x=70, g='f')]),
])
C27 = [(24.8, 39.7, 'İzo Türkiye’yi ve', 'yemeklerini çok seviyor.'), (42.3, 57.3, 'Onlar', 'lokantadalar.'), (60.0, 74.9, 'Onlar kahvaltı', 'ediyorlar.'), (77.5, 92.5, 'Menüde üç çeşit', 'kahvaltı var.')]
page(D, 'dk2', 27, [
    act('dk2-27-2', '2. etkinlik', [5, 2.0, 90, 74.0], audio=AUD('dk2', 27, 'S.103')),
    act('dk2-27-3', '3. etkinlik', [5, 76.5, 90, 20.0],
        [it for k, (a, b, t1, t2) in enumerate(C27) for it in (LB(a, b, 88.94, t1, g=f'c{k}'), LB(a, b, 91.50, t2, g=f'c{k}'))] + [B2(27, 94.87, '37')]),
])
N28 = [('su', 'böreği'), ('mene-', 'men'), ('peynir', ''), ('zeytin', ''), ('doma-', 'tes'), ('sala-', 'talık'), ('yumur-', 'ta'), ('reçel', ''), ('çay', ''), ('meyve', 'suyu')]
X28 = [25.2, 32.1, 39.1, 46.1, 53.0, 60.0, 67.0, 73.9, 80.9, 87.9]
CX28 = [20.7, 27.6, 34.6, 41.6, 48.5, 55.5, 62.5, 69.4, 76.4, 83.5, 90.4]
page(D, 'dk2', 28, [
    act('dk2-28-4ab', '4. etkinlik (a, b)', [5, 2.0, 90, 30.5],
        [it for k, ((a, b), x) in enumerate(zip(N28, X28)) for it in ([LB(x, x + 5.0, 13.62, a, g=f'n{k}')] + ([LB(x, x + 5.0, 15.77, b, g=f'n{k}')] if b else []))]
        + [LB(7.0, 16.1, 23.79, 'Klasik', g='k'), LB(7.0, 16.1, 25.94, 'kahvaltı', g='k'), LB(7.0, 16.1, 28.95, 'Hızlı', g='h'), LB(7.0, 16.1, 31.10, 'kahvaltı', g='h')]
        + [CK(CX28[i], 19.2, 2.2, g='c1') for i in (0, 2, 3, 9)]
        + [CK(CX28[i], 24.4, 2.2, g='c2') for i in (1, 3, 4, 5, 7, 8, 9)]
        + [CK(CX28[i], 29.6, 2.2, g='c3') for i in (3, 4, 5, 6, 9, 10)]),
    act('dk2-28-4c', '4. etkinlik (c)', [5, 33.0, 90, 62.5], [
        B2(28, 84.24, 'menemen,', x=31, g='g'), B2(28, 86.39, 'peynir ve çay', x=20, g='g'), B2(28, 90.68, 'Zeytin ve tost', x=20, g='gy'),
        B2(28, 82.10, 'Klasik kahvaltı ikinci menü.', x=50, g='k'), B2(28, 84.24, 'Bu menüde zeytin, peynir,', x=50, g='k'), B2(28, 86.39, 'yumurta, çay ve tost', x=50, g='k'),
        B2(28, 90.68, 'Domates ve salatalık', x=50, g='ky'),
        B2(28, 82.10, 'Hızlı kahvaltı üçüncü menü.', x=80, g='h'), B2(28, 84.24, 'Bu menüde zeytin, peynir,', x=80, g='h'), B2(28, 86.39, 'domates, salatalık, çay', x=80, g='h'),
        B2(28, 88.53, 've meyve suyu', x=80, g='h'), B2(28, 90.68, 'Yumurta ve simit', x=80, g='hy')]),
])
page(D, 'dk2', 29, [
    act('dk2-29-5a', '5. etkinlik (a)', [5, 2.5, 90, 24.5], [
        LN([71.0, 7.9], [22.4, 14.8], g='h', dot=[71.0, 7.9]), B2(29, 22.67, 'Hızlı kahvaltı en ucuz.', g='h'),
        LN([44.7, 7.9], [72.0, 14.8], g='k', dot=[44.7, 7.9]), B2(29, 25.89, 'Klasik kahvaltı diğer menülerden daha çeşitli.', g='k')]),
    act('dk2-29-5b', '5. etkinlik (b)', [5, 28.0, 90, 29.5], [
        B2(29, 41.63, 'diğer menülerden daha çeşitli.', g='k'), B2(29, 45.92, 'menüyü seçelim.', g='k'),
        B2(29, 50.98, 'en ucuz menü.', g='h'), B2(29, 55.27, 'üçüncü menüyü seçelim.', g='h')]),
    act('dk2-29-6', '6. etkinlik', [5, 63.5, 90, 28.5],
        [LB(7.0, 16.1, 74.64, 'Serpme', g='a'), LB(7.0, 16.1, 76.78, 'kahvaltı', g='a')]
        + [CK(CX28[i], 75.4, 2.2, g='a') for i in (0, 2, 3, 4, 5, 6, 8, 9)]
        + [B2(29, 85.06, 'Serpme kahvaltı.', g='b'), B2(29, 87.21, 'simit, menemen, peynir, zeytin, salatalık,', g='b'), B2(29, 89.35, 'domates, reçel ve çay', g='b')]),
])
page(D, 'dk2', 30, [
    act('dk2-30-1', '1. etkinlik', [5, 9.0, 90, 50.5], audio=AUD('dk2', 30, 'S.104')),
    act('dk2-30-2', '2. etkinlik', [5, 60.0, 90, 35.0], [
        B2(30, 81.58, 'meyvesi şeftalidir.'), B2(30, 88.74, 'dondurması meşhurdur.'), B2(30, 92.37, 'çayı meşhurdur.')]),
])
page(D, 'dk2', 31, [
    act('dk2-31-3', '3. etkinlik', [5, 4.0, 90, 33.0], audio=AUD('dk2', 31, 'S.105')),
    act('dk2-31-4', '4. etkinlik', [5, 40.0, 90, 48.0], [
        B2(31, 55.47, 'lezzetlidir'), B2(31, 59.25, 'sıcak'), B2(31, 67.33, 'pahalı'), B2(31, 71.11, 'ucuz'),
        B2(31, 79.95, 'ünlü'), B2(31, 82.45, 'ünlü'), B2(31, 85.72, 'soğuk')]),
])

# ---- s.32: 5. etkinlik, Dil Bilgisi → s.101–103, Dinleme
page(D, 'dk2', 32, [
    act('dk2-32-5', '5. etkinlik', [5, 3.0, 90, 13.0], [B2(32, 8.00, 'Ben sütü soğuk içerim.')]),
    act('dk2-32-d', 'Dinleme 1–2', [5, 30.0, 90, 34.0], audio=AUD('dk2', 32, 'S.106', 'S.107')),
    act('dk2-32-3', 'Dinleme 3', [5, 64.5, 90, 31.0], [
        B2(32, 87.36, 'Sarı masada kurabiye ve simit var.'), B2(32, 90.22, 'Mavi masada tavuk ve börek var.', x=20), B2(32, 93.08, 'Beyaz masada köfte ve kek var.', x=20),
        B2(32, 90.22, 'mavi masadakiler.', x=85), B2(32, 93.08, 'kırmızı masadakiler.', x=80)]),
], [link([28.0, 19.2, 31.5, 2.6], 'dbt', 101, 'Dil Bilgisi ve Telaffuz Kitabı s.101', {'act': 'dbt103-4c'}, 'dbt101-1')])
page(D, 'dk2', 33, [
    act('dk2-33-4', 'Dinleme 4', [5, 2.0, 90, 94.0], [CK(x, y, 2.0) for x, y in (
        (24.0, 48.8), (18.2, 53.2), (81.5, 39.9), (84.4, 46.0), (65.5, 47.5), (28.5, 88.5), (34.5, 90.0), (29.6, 93.0), (79.5, 85.1), (87.1, 89.7))],
        audio=AUD('dk2', 33, 'S.108')),
])
N34 = [('tavuk', ''), ('köfte', ''), ('börek', ''), ('kek', ''), ('kura-', 'biye'), ('biber', ''), ('meyve', 'suyu'), ('ekmek', ''), ('bakla-', 'va'), ('simit', '')]
X34 = [25.2, 32.2, 39.2, 46.2, 53.2, 60.1, 67.1, 74.1, 81.0, 88.0]
CX34 = [20.8, 27.8, 34.7, 41.7, 48.6, 55.6, 62.6, 69.6, 76.5, 83.5, 90.5]
page(D, 'dk2', 34, [
    act('dk2-34-5ab', '5. etkinlik (a, b)', [5, 2.5, 90, 46.5],
        [B2(34, 7.24, 'Balık, ekmek, tavuk, börek, köfte, limon, kek, kurabiye, simit, biber ve meyve suyu.', g='a')]
        + [it for k, ((a, b), x) in enumerate(zip(N34, X34)) for it in ([LB(x, x + 5.0, 27.52, a, g=f'n{k}')] + ([LB(x, x + 5.0, 29.67, b, g=f'n{k}')] if b else []))]
        + [CK(CX34[i], 32.9, 2.2, g='kr') for i in (0, 6, 8)] + [CK(CX34[i], 37.8, 2.2, g='mv') for i in (1, 3, 7)]
        + [CK(CX34[i], 42.6, 2.2, g='by') for i in (2, 4, 8, 9)] + [CK(CX34[i], 47.3, 2.2, g='sr') for i in (5, 10)]
        + [B2(34, 17.81, '60')]),
    act('dk2-34-5c', '5. etkinlik (c)', [5, 50.0, 90, 21.5], [
        B2(34, 58.33, 'Baklava ve havuçlu kek.'), B2(34, 61.35, 'Kurabiye ve simit.'), B2(34, 64.31, 'Meyve suyu mavi masada var.'),
        B2(34, 67.28, 'Limon ekşi.'), B2(34, 70.29, 'Biber acı.')]),
    act('dk2-34-6', '6. etkinlik', [5, 72.0, 90, 23.5], [
        LN([47.65, 79.36], [72.57, 86.74], dot=[47.65, 79.36]), LN([22.28, 79.76], [41.84, 88.55], dot=[22.28, 79.76]), LN([67.79, 79.77], [28.54, 88.55], dot=[67.79, 79.77])]),
])
page(D, 'dk2', 35, [
    act('dk2-35-7', '7. etkinlik', [5, 4.0, 90, 24.0], [
        CK(57.6, 15.0, 2.2, g='a'), B2(35, 15.76, 'Köfteler çok tuzsuz.', g='a'),
        CK(54.0, 18.3, 2.2, g='b'),
        CK(57.6, 20.6, 2.2, g='c'), B2(35, 21.28, 'Kıtır, kırmızı masadaki yiyeceklerden almak istiyor.', g='c'),
        CK(57.6, 23.3, 2.2, g='d'), B2(35, 24.09, 'Pıtır, mavi masadaki yiyeceklerden almak istiyor.', g='d'),
        CK(54.0, 26.2, 2.2, g='e')]),
    act('dk2-35-8', '8. etkinlik', [5, 35.5, 90, 20.0], [
        B2(35, 44.84, 'baklava'), B2(35, 47.40, 'börek', x=45), B2(35, 47.40, 'baklavadan', x=55), B2(35, 47.40, 'lezzetli', x=75),
        B2(35, 49.95, 'tavuk, domates ve', x=50), B2(35, 49.95, 'biber', x=72)]),
    act('dk2-35-sv', 'Söz Varlığı 1', [5, 64.0, 90, 27.5], audio=AUD('dk2', 35, 'S.109')),
])
Q36 = [('limon', 45.9, 14.8, 'Limon ekşi mi?', 'Evet, limon ekşi.'), ('börek', 54.2, 20.9, 'Börek tatlı mı?', 'Hayır, börek tatlı değil, tuzlu.'),
       ('kek', 29.1, 26.8, 'Kek tatlı mı?', 'Evet, kek tatlı.'), ('biber', 37.5, 32.3, 'Biber acı mı?', 'Evet, biber acı.')]
Q36b = [('Simit', 55.6, 42.5, 'Simit tuzlu mu?', 'Evet, simit tuzlu.'), ('Balık', 55.6, 48.2, 'Balık acı mı?', 'Hayır, balık acı değil, tuzlu.'),
        ('Meyve suyu', 30.2, 54.1, 'Meyve suyu tatlı mı?', 'Evet, meyve suyu tatlı.')]
page(D, 'dk2', 36, [
    act('dk2-36-2a', '2. etkinlik (a)', [5, 2.0, 90, 33.0],
        [it for k, ((n, cx, cy, q, a), y) in enumerate(zip(Q36, [15.41, 21.29, 27.16, 33.04])) for it in (
            LB(15.2, 23.0, y, n, g=f'r{k}'), CK(cx, cy, 2.2, g=f'r{k}'), LB(59.5, 91.5, [13.78, 19.70, 25.58, 31.35][k], q, g=f'r{k}'), LB(59.6, 92.9, [16.49, 22.41, 28.29, 34.06][k], a, g=f'r{k}'))]),
    act('dk2-36-2b', '2. etkinlik (b)', [5, 35.5, 90, 21.5],
        [it for k, ((n, cx, cy, q, a), y) in enumerate(zip(Q36b, [42.65, 48.52, 54.40])) for it in (
            LB(7.8, 24.3, y, n, g=f'r{k}'), CK(cx, cy, 2.2, g=f'r{k}'), LB(60.8, 92.8, [41.37, 46.89, 52.36][k], q, g=f'r{k}'), LB(60.9, 94.2, [43.93, 49.39, 54.91][k], a, g=f'r{k}'))]),
    act('dk2-36-s', 'Şarkı Zamanı', [5, 62.5, 90, 29.5], audio=AUD('dk2', 36, 'M.018')),
], [link([27.6, 58.5, 31.8, 2.6], 'dbt', 104, 'Dil Bilgisi ve Telaffuz Kitabı s.104', {'act': 'dbt105-4b'}, 'dbt104-1'),
    link([30.4, 92.6, 31.8, 2.6], 'dbt', 106, 'Dil Bilgisi ve Telaffuz Kitabı s.106', {'act': 'dbt107-5b'}, 'dbt106-1')])

page(D, 'dk2', 37, [
    act('dk2-37-1ab', '1. etkinlik (a, b)', [5, 8.0, 90, 59.5]),
    act('dk2-37-1c', '1. etkinlik (c)', [5, 70.0, 90, 25.5], [
        B2(37, 82.61, 'En ucuz içecekler su ve çay.'), B2(37, 84.75, 'Süt ayrandan daha pahalı.'), B2(37, 86.90, 'En pahalı yiyecek cevizli baklava.'),
        B2(37, 89.05, 'Çay sıcak, limonata soğuk.'), B2(37, 91.19, 'Bence çikolatalı kek çok lezzetli.'), B2(37, 93.34, 'Ispanaklı börek tuzlu, baklava tatlı.')]),
])
F38 = [('Havuçlu kek', '20 TL'), ('Kurabiye', '15 TL'), ('Baklava', '100 TL'), ('Börek', '50 TL'), ('Simit', '10 TL')]
I38 = [('Çay', '15 TL'), ('Kahve', '40 TL'), ('Su', '10 TL'), ('Meyve suyu', '35 TL')]
Y38 = [68.53, 70.73, 72.98, 75.17, 77.42]
page(D, 'dk2', 38, [
    act('dk2-38-1a', '1. etkinlik (a)', [5, 8.0, 90, 48.5], [
        B2(38, 22.72, 'Affedersiniz'), B2(38, 27.01, 'ne çeşit'), B2(38, 33.45, 'Hangisinden'), B2(38, 37.74, 'tatlı'), B2(38, 42.03, 'cevizli'),
        B2(38, 48.47, 'Ne'), B2(38, 50.62, 'Sütlü'), B2(38, 52.77, 'Afiyet olsun.')]),
    act('dk2-38-1b', '1. etkinlik (b)', [5, 57.0, 90, 38.0],
        [B2(38, 62.07, 'MENÜ', g='m')]
        + [it for k, ((n, p), y) in enumerate(zip(F38, Y38)) for it in (LB(13.6, 28.0, y, n, g='m'), LB(33.0, 41.3, y, p, g='m'))]
        + [it for k, ((n, p), y) in enumerate(zip(I38, Y38)) for it in (LB(57.2, 71.7, y, n, g='m'), LB(76.7, 85.0, y, p, g='m'))]
        + [LB(10.0, 90.0, y, t, g='d') for y, t in zip([83.73, 85.88, 88.02, 90.17, 92.32], [
            'Müşteri: Merhaba!', 'Garson: Merhaba, hoş geldiniz.', 'Müşteri: Bir simit ve bir çay, lütfen.',
            'Garson: Tabii. Simit 10 TL, çay 15 TL. Toplam 25 TL.', 'Müşteri: Buyurun.  Garson: Teşekkürler. Afiyet olsun!'])]),
])

# ---- C. Köfte Tarifi (video V.006 not in the slides yet)
page(D, 'dk2', 39, [
    act('dk2-39-1', '1. etkinlik', [5, 8.0, 90, 17.5], [CK(67.5, 23.7, 2.6)], audio=AUD('dk2', 39, 'V.006')),
    act('dk2-39-2', '2. etkinlik', [5, 26.0, 90, 46.0],
        [it for k, ((x, y), t, ly) in enumerate(zip(((43.3, 38.1), (13.2, 49.1), (28.2, 49.1), (43.3, 59.4), (58.3, 59.6)), ('ekmek', 'tuz', 'domates', 'biber', 'yağ'),
                                                       (35.44, 38.36, 41.22, 44.13, 46.99))) for it in (CK(x, y, 2.4, g=f'i{k}'), CK(69.7, ly - 0.55, 2.2, g=f'i{k}'), LB(72.0, 92.1, ly, t, g=f'i{k}'))]),
    act('dk2-39-3', '3. etkinlik', [5, 74.0, 90, 12.5], [NUM(x, 84.9, n, 2.6, 2.4) for x, n in ((13.2, '3'), (42.6, '5'), (57.4, '4'), (72.0, '6'), (86.9, '2'))]),
    act('dk2-39-4', '4. etkinlik', [5, 87.0, 62, 8.5]),
])
page(D, 'dk2', 40, [
    act('dk2-40-g', 'Maarif Türkçe Grubu', [5, 2.0, 90, 94.0], tiles=[[5, 2.0, 90, 94.0], {'r': [5, 2.0, 90, 75.0], 'page': 41}], cols=2, nums=False),
])
page(D, 'dk2', 41, [
    dict(act('dk2-41-g', 'Maarif Türkçe Grubu', [5, 2.0, 90, 75.0], skip=True), alias={'page': 40, 'act': 'dk2-40-g'}),
    act('dk2-41-1', '1. etkinlik', [5, 77.0, 90, 18.0]),
])
page(D, 'dk2', 42, [act('dk2-42-p', 'Proje Zamanı', [3, 2.0, 94, 94.0])])

# =================================================================== DİL BİLGİSİ VE TELAFFUZ (6. Ünite)
page(T, 'dbt', 92)
page(T, 'dbt', 93, [
    act('dbt93-1', '1. etkinlik', [8, 22.5, 84, 57.0], audio=AUD('dbt', 93, 'S.083')),
    act('dbt93-2', '2. etkinlik', [8, 79.5, 84, 15.0]),
])
page(T, 'dbt', 94, [
    act('dbt94-3', '3. etkinlik', [8, 7.0, 86, 35.0], [
        BT(94, 39.51, 'üzüm', x=20), BT(94, 39.51, 'bir kilo', x=40), BT(94, 39.51, 'Bir kilo üzüm almak istiyorum.', x=70)]),
    act('dbt94-4', '4. etkinlik', [8, 42.5, 86, 47.5], [
        BT(94, 56.43, 'İzo limon almak istiyor.', x=30, g='a'),
        BT(94, 52.2, 'Temel hangi meyveyi almak istiyor?', g='b'), BT(94, 56.43, 'elma', x=65, g='b'), BT(94, 56.43, 'mak istiyor.', x=82, g='b'),
        BT(94, 65.31, 'Temel kaç kilo havuç almak istiyor?', x=30, g='c'), BT(94, 69.59, 'Temel üç kilo havuç almak istiyor.', x=30, g='c'),
        BT(94, 65.31, 'İzo hangi meyveyi istiyor?', x=70, g='d'), BT(94, 69.59, 'İzo incir istiyor.', x=70, g='d'),
        BT(94, 78.17, 'İzo şeftali almak istiyor mu?', x=30, g='e'), BT(94, 82.4, 'İzo şeftali almak istiyor.', x=30, g='e'), BT(94, 86.63, 'İzo şeftali almak istemiyor.', g='e'),
        BT(94, 78.17, 'İzo kaç kilo domates almak istiyor?', x=70, g='f'), BT(94, 82.4, 'İzo beş kilo domates almak istiyor.', x=70, g='f')]),
])
page(T, 'dbt', 95, [
    act('dbt95-5a', '5. etkinlik (a)', [8, 2.5, 84, 51.0], [
        BT(95, 26.65, 'armut', x=38, g='a'), BT(95, 31.7, '1 kilo', x=38, g='a'), BT(95, 31.7, '3 kilo', x=58, g='b'),
        BT(95, 26.65, 'havuç', x=78, g='c'), BT(95, 31.7, '2 kilo', x=78, g='c'),
        BT(95, 51.44, '1 kilo', x=28, g='d'), BT(95, 46.39, 'maydanoz', x=48, g='e'), BT(95, 51.44, '1 demet', x=48, g='e'),
        BT(95, 46.39, 'marul', x=68, g='f'), BT(95, 51.44, '1 tane', x=68, g='f')]),
    act('dbt95-5b', '5. etkinlik (b)', [8, 54.0, 84, 41.0], [
        BT(95, 63.54, 'Üzüm almak istiyorum.', g='1'),
        BT(95, 68.07, 'Limon almak ister misin?', g='2'), BT(95, 70.53, 'Hayır, limon istemiyorum.', g='2'),
        BT(95, 75.06, 'Salatalık mı domates mi? Hangisinden almak istiyorsun?', g='3'), BT(95, 77.47, 'Domates istiyorum.', g='3'),
        BT(95, 81.99, 'Kaç kilo üzüm almak istiyorsun?', g='4'), BT(95, 84.46, '2 kilo üzüm almak istiyorum.', g='4'),
        BT(95, 88.98, 'Bir kilo limon kaç lira?', g='5'), BT(95, 91.39, 'Bir kilo limon 20 lira.', g='5')]),
])
page(T, 'dbt', 96, [
    act('dbt96-1', '1. etkinlik', [8, 17.0, 84, 49.0], audio=AUD('dbt', 96, 'S.084')),
    act('dbt96-2', '2. etkinlik', [8, 67.0, 84, 27.5]),
])
def half(t):
    """split a sentence over two dotted lines at the word nearest the middle"""
    w = t.split(); best = min(range(1, len(w)), key=lambda k: abs(len(' '.join(w[:k])) - len(' '.join(w[k:]))))
    return ' '.join(w[:best]), ' '.join(w[best:])
def S5(n, y, a, b, g, prod):
    """İstek kipi table row: products, then 've/ile ... istiyoruz' and 've/ile ... alalım', each sentence on two lines"""
    L = (46.65, 62.07, 69.07, 84.49) if n == 97 else (49.16, 64.58, 71.59, 87.0)
    py, pa, pb = prod
    out = [LB(10.34 if n == 97 else 13.17, 24.55 if n == 97 else 25.95, py, pa, g=g), LB(28.33 if n == 97 else 29.91, 41.85 if n == 97 else 42.64, py, pb, g=g)]
    for x0, x1, tail in ((L[0], L[1], 'almak istiyoruz.'), (L[2], L[3], 'alalım.')):
        for k, c in enumerate(('ve', 'ile')):
            l1, l2 = half(f'{a} {c} {b} {tail}')
            yy = y + 5.7 * k
            out += [LB(x0, x1, yy, l1, g=g), LB(x0, x1, yy + 2.65, l2, g=g)]
    return out
# 5a runs from s.97 onto s.98; each sentence fills two dotted lines
page(T, 'dbt', 97, [
    act('dbt97-3', '3. etkinlik', [8, 7.5, 84, 25.0]),
    act('dbt97-4', '4. etkinlik', [8, 33.5, 84, 17.5], [NUM(x, y, n, 2.8, 2.4) for x, y, n in (
        (12.6, 38.1, '8'), (54.9, 38.1, '7'), (39.3, 41.8, '4'), (12.6, 45.5, '5'), (43.9, 45.5, '2'), (12.6, 49.3, '3'), (58.9, 49.3, '6'))]),
    act('dbt97-5a', '5. etkinlik (a)', [8, 52.5, 84, 41.0],
        S5(97, 80.52, 'Bir paket makarna', 'iki şişe su', 'r', prod=(91.58, 'bir paket makarna', 'iki şişe su'))
        + ON(98, *[it for y, a, b, g in ((10.31, 'Bir koli yumurta', 'bir paket bisküvi', 'r1'), (28.47, 'Bir kilo domates', 'üç kutu meyve suyu', 'r2'),
                                           (45.8, 'Bir kilo peynir', 'üç tane ekmek', 'r3'))
                   for it in S5(98, y, a, b, g, prod=(y + 10.4, a[0].lower() + a[1:], b))]),
        tiles=[[8, 52.5, 84, 41.0], {'r': [10, 6.0, 82, 51.5], 'page': 98}], cols=2, nums=False),
])
page(T, 'dbt', 98, [
    dict(act('dbt98-5a', '5. etkinlik (a)', [10, 6.0, 82, 51.5], skip=True), alias={'page': 97, 'act': 'dbt97-5a'}),
    act('dbt98-5b', '5. etkinlik (b)', [10, 59.0, 82, 22.0]),
])
page(T, 'dbt', 99, [
    act('dbt99-1', '1. etkinlik', [8, 13.0, 84, 17.5], audio=AUD('dbt', 99, 'S.085')),
    act('dbt99-2', '2. etkinlik', [8, 30.5, 84, 44.0], audio=AUD('dbt', 99, 'S.086')),
    act('dbt99-3', '3. etkinlik', [8, 74.5, 84, 19.5], audio=AUD('dbt', 99, 'S.087')),
])
page(T, 'dbt', 100, [
    act('dbt100-4', '4. etkinlik', [10, 6.5, 82, 47.0], audio=AUD('dbt', 100, 'S.088')),
    act('dbt100-5a', '5. etkinlik (a)', [10, 54.5, 41, 23.0], [LB(19.82, 42.56, 71.47, 'Nar')], audio=AUD('dbt', 100, 'S.089')),
    act('dbt100-5b', '5. etkinlik (b)', [51, 54.5, 41, 23.0], [
        LB(54.7, 88.2, 66.8, 'Küçük, siyah ya da yeşil,', g='b'), LB(54.7, 88.2, 68.63, 'Tabağımda sabah gelir.', g='b'), LB(54.7, 88.2, 70.48, 'Bil bakalım ne? – Zeytin', g='b')]),
])
page(T, 'dbt', 101, [
    act('dbt101-1', '1. etkinlik', [8, 22.0, 84, 50.5], audio=AUD('dbt', 101, 'S.090')),
    act('dbt101-2', '2. etkinlik', [8, 74.0, 84, 19.5], ON(102, LB(53.35, 74.05, 21.77, 'Bence en lezzetli tatlı sütlaç.')),
        tiles=[[8, 74.0, 84, 19.5], {'r': [10, 6.0, 84, 18.5], 'page': 102}], cols=1, nums=False),
])
page(T, 'dbt', 102, [
    dict(act('dbt102-2', '2. etkinlik', [10, 6.0, 84, 18.5], skip=True), alias={'page': 101, 'act': 'dbt101-2'}),
    act('dbt102-3', '3. etkinlik', [10, 25.5, 84, 47.0]),
    act('dbt102-4a', '4. etkinlik (a)', [10, 74.0, 84, 19.5], ON(103,
        LB(51.32, 84.63, 10.37, 'En ucuz menü 1. menü.'), LB(51.32, 84.63, 15.25, 'En pahalı menü 3. menü.'),
        LB(51.32, 84.63, 20.18, '2. ve 3. menüler 1. menüden daha pahalı.'), LB(51.32, 84.63, 25.06, '3. menü 2. menüden daha pahalı.'),
        LB(51.32, 84.63, 29.99, '1. ve 2. menüler 3. menüden daha ucuz.')),
        tiles=[[10, 74.0, 84, 19.5], {'r': [8, 6.0, 86, 31.5], 'page': 103}], cols=1, nums=False),
])
page(T, 'dbt', 103, [
    dict(act('dbt103-4a', '4. etkinlik (a)', [8, 6.0, 86, 31.5], skip=True), alias={'page': 102, 'act': 'dbt102-4a'}),
    act('dbt103-4b', '4. etkinlik (b)', [8, 38.0, 86, 33.0], [
        BT(103, 57.61, 'Menemen', x=20, g='n'), BT(103, 57.61, 'Tavuk', x=48, g='n'), BT(103, 57.61, 'Börek', x=75, g='n'),
        BT(103, 63.31, 'Börek'), BT(103, 66.72, 'Menemen'), BT(103, 70.12, 'Tavuk')]),
    act('dbt103-4c', '4. etkinlik (c)', [8, 73.0, 86, 20.5], [
        BT(103, 82.46, 'en lezzetli 3. menü.', x=40), BT(103, 82.46, 'yiyecek tavuk.', x=75),
        BT(103, 90.1, 'Bana göre en sağlıklı 3. menü.', x=40), BT(103, 90.1, 'Bence 2. menüyü yiyelim.', x=70)]),
])
page(T, 'dbt', 104, [
    act('dbt104-1', '1. etkinlik', [10, 15.0, 82, 44.0], audio=AUD('dbt', 104, 'S.091')),
    act('dbt104-2', '2. etkinlik', [10, 59.5, 82, 34.0], [
        BT(104, 91.98, 'Evet, cevizli baklava yemek isterim.', x=30), BT(104, 91.98, 'çayımı şekersiz içerim.', x=70)]),
])
W105 = ['ıspanak', 'çilek', 'havuç', 'üzüm', 'elma']
X105 = [34.19, 45.24, 56.34, 67.4, 78.46]
page(T, 'dbt', 105, [
    act('dbt105-3', '3. etkinlik', [8, 7.5, 84, 37.0]),
    act('dbt105-4a', '4. etkinlik (a)', [8, 45.5, 84, 17.5],
        [LB(23.13, 30.57, 61.43, 'şekersiz', g='s')]
        + [it for k, (w, x) in enumerate(zip(W105, X105)) for it in (
            LB(x, x + 7.45, 56.26, w, g=f'w{k}'), LB(x, x + 7.45, 58.84, w + ('lı' if w == 'ıspanak' else 'li' if w == 'çilek' else 'lu' if w == 'havuç' else 'lü' if w == 'üzüm' else 'lı'), g=f'w{k}'),
            LB(x, x + 7.45, 61.43, w + ('sız' if w in ('ıspanak', 'elma') else 'siz' if w == 'çilek' else 'suz' if w == 'havuç' else 'süz'), g=f'w{k}'))]),
    act('dbt105-4b', '4. etkinlik (b)', [8, 63.5, 84, 30.0], [
        LB(45.24, 52.69, 74.06, 'börek', g='n'), LB(56.34, 63.79, 74.06, 'tavuk', g='n'), LB(67.4, 74.85, 74.06, 'köfte', g='n'),
        LB(53.26, 84.45, 77.29, 'Köfte acı mı?', g='k'), LB(53.26, 84.45, 79.88, 'Hayır, köfte acı değil, tuzlu.', g='k'),
        LB(53.26, 84.45, 82.34, 'Tavuk sıcak mı?', g='t'), LB(53.26, 84.45, 84.93, 'Evet, tavuk sıcak.', g='t'),
        LB(12.78, 44.14, 87.46, 'Bu börek ıspanaklı mı', g='b'), LB(13.0, 44.14, 90.04, 'Evet, bu börek ıspanaklı.', g='b'),
        LB(53.04, 84.41, 87.46, 'Bu kek havuçlu mu', g='e'), LB(53.26, 84.41, 90.04, 'Evet, bu kek havuçlu.', g='e')]),
])
page(T, 'dbt', 106, [
    act('dbt106-1', '1. etkinlik', [10, 13.0, 82, 21.0], audio=AUD('dbt', 106, 'S.092')),
    act('dbt106-2', '2. etkinlik', [10, 34.0, 82, 30.5], audio=AUD('dbt', 106, 'S.093')),
    act('dbt106-3', '3. etkinlik', [10, 66.0, 82, 27.5], audio=AUD('dbt', 106, 'S.094')),
])
page(T, 'dbt', 107, [
    act('dbt107-4', '4. etkinlik', [8, 6.0, 84, 57.5], audio=AUD('dbt', 107, 'S.095')),
    act('dbt107-5a', '5. etkinlik (a)', [8, 65.0, 41, 23.0], audio=AUD('dbt', 107, 'S.096')),
    act('dbt107-5b', '5. etkinlik (b)', [50, 65.0, 39, 23.0], [LB(52.07, 85.55, y, t, g='b') for y, t in zip(
        [76.62, 78.44, 80.26, 82.08, 83.96, 85.78], ['Sabah oldu kalktım ben,', 'Sofrada peynir, zeytin hemen.', 'Ekmek geldi tabağıma,', 'Çay da doldu bardağıma.',
                                                     'Afiyetle yedim hepsini,', 'Başladım güzel bir güne.'])]),
])

U6 = lambda a, b: [{'no': 6, 'title': 'Alışveriş Zamanı', 'from': a, 'to': b}]
dump('dk2', D, 0.7826, 'Ders Kitabı 2', U6(7, 42))
dump('dbt-u6', T, 0.6669, 'Dil Bilgisi ve Telaffuz Kitabı', U6(92, 107))
print('ok', len(D), len(T), sum(len(p['activities']) for p in D.values()), sum(len(p['activities']) for p in T.values()))
