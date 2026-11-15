# Builds data/dk-u2.json (Ders Kitabı 1, 2. Ünite s.39–64) and data/dbt-u2.json (telaffuz s.22–38).
# usage: build_u2.py WORK   (WORK holds auto-dk.json / auto-dbt.json from prep_unit.py)
# Answers: the official "dijital kitap" slides, checked against the book; book cross references
# ("Dil Bilgisi ve Telaffuz Kitabı … bölümüne bak") decide where the telaffuz book opens, never the slide notes.
import sys
from kit import *
W = sys.argv[1]
load(f'{W}/auto-dk.json', f'{W}/auto-dbt.json')
D, T = {}, {}
B1 = lambda n, y, text, **k: BL(f'dk{n}', y, text, **k)
BT = lambda n, y, text, **k: BL(f'dbt{n}', y, text, **k)
def OPT(x, y, w=12.8, h=3.6, g=None):
    """circle a word centred at x,y"""
    return EL([round(x - w / 2, 2), round(y - h / 2, 2), w, h], g=g)
def half(t):
    """split a sentence over two dotted lines at the word nearest the middle"""
    w = t.split(); best = min(range(1, len(w)), key=lambda k: abs(len(' '.join(w[:k])) - len(' '.join(w[k:]))))
    return ' '.join(w[:best]), ' '.join(w[best:])
def TWO(n, y1, y2, t, x=None, g=None, B=None):
    a, b = half(t); B = B or B1
    return [B(n, y1, a, x=x, g=g), B(n, y2, b, x=x, g=g)]
def LET(cx, cy, ch, g=None, s=3.0):
    return NUM(cx, cy, ch, s, s, g=g)

# =================================================================== DERS KİTABI 1 — 2. ÜNİTE
page(D, 'dk', 39, [act('dk39-h', 'Üniteye Hazırlık', [8, 86.0, 84, 10.5])])

# 4. etkinlik: the story runs over s.40 (panels 1–2) and s.41 (panels 3–6)
page(D, 'dk', 40, [
    act('dk40-1', '1. ve 2. etkinlik', [5, 16.5, 91.0, 16.0], audio=AUD('dk', 40, 'S.024') + AUD('dk', 40, 'S.025')),
    act('dk40-3', '3. etkinlik', [4, 32.5, 93, 18.0], [
        OPT(59.1, 38.9, g='y'), OPT(59.1, 43.3, w=14.5, g='y'),
        OPT(90.3, 38.9, g='p'), OPT(90.3, 43.3, g='p'), OPT(90.3, 47.6, g='p')]),
    act('dk40-4', '4. etkinlik', [4, 51.0, 93, 44.5],
        [UL([68.1, 90.2], [75.9, 90.2]), UL([66.9, 93.4], [70.9, 93.4]), UL([72.0, 93.4], [76.0, 93.4]), UL([77.1, 93.3], [81.1, 93.3])]
        + ON(41, UL([22.2, 8.55], [27.4, 8.55]), UL([20.8, 13.05], [26.0, 13.05]), UL([26.7, 13.2], [31.9, 13.2]),
             UL([33.8, 13.15], [39.0, 13.15]), UL([71.7, 7.15], [76.9, 7.15]), UL([19.1, 41.05], [30.3, 41.05])),
        audio=AUD('dk', 40, 'S.026'), tiles=[[4, 51.0, 93, 44.5], {'r': [6, 2.5, 88, 58.0], 'page': 41}], cols=2, nums=False),
])
page(D, 'dk', 41, [
    dict(act('dk41-4', '4. etkinlik', [6, 2.5, 88, 58.0], skip=True), alias={'page': 40, 'act': 'dk40-4'}),
    act('dk41-5', '5. etkinlik', [5, 60.0, 90, 34.0], audio=AUD('dk', 41, 'S.027')),
])

# crossword cells (centres in %): rows 3.33 apart
XC = [22.7, 26.9, 31.4, 35.5, 39.7, 43.9, 48.0, 52.2, 56.4, 60.6, 65.0, 69.4]
X = dict(zip('S İ K A L E M T I R a Ş'.split(), XC))
def row(y, start, word, g):
    i = XC.index(start)
    return [LET(XC[i + k], y, ch, g=g) for k, ch in enumerate(word) if ch != ' ']
def col(x, y0, word, g):
    return [LET(x, round(y0 + 3.33 * k, 2), ch, g=g) for k, ch in enumerate(word) if ch != ' ']
page(D, 'dk', 42, [
    act('dk42-6', '6. etkinlik', [5, 2.5, 90, 52.0],
        row(14.9, 31.4, 'KALEMTIR Ş', 'kalemtıraş')
        + col(43.9, 11.55, 'D FTER', 'defter')
        + col(31.4, 18.23, 'ALEMLİK', 'kalemlik')
        + row(31.5, 22.7, 'Sİ Gİ', 'silgi')
        + row(38.2, 35.5, 'İTAP', 'kitap')
        + col(48.0, 41.53, 'AKET', 'paket')
        + row(48.2, 31.4, 'NOTD FTERİ', 'not defteri')
        + [LET(x, 38.5, ch, g='şifre') for x, ch in zip([70.1, 74.3, 78.5, 82.7, 86.9], 'FENER')]),
    act('dk42-7', '7. etkinlik', [5, 55.0, 90, 41.0], [
        B1(42, 72.89, 'Ali'), B1(42, 92.47, 'cetvel'), B1(42, 92.48, 'Zeynep', x=45),
        B1(42, 73.50, 'silgi,', g='k'), LB(65.5, 84.7, 75.6, 'kalemtıraş ve cetvel', g='k'),
        B1(42, 93.03, 'defter', g='ç'), B1(42, 95.15, 've kalemtıraş var', g='ç')]),
])
page(D, 'dk', 43, [
    act('dk43-8', '8. etkinlik', [5, 5.5, 90, 16.0], [
        B1(43, 14.68, 'kitap, defter,', x=30, g='a'), B1(43, 17.20, 'kalem, silgi, kalemtıraş', x=20, g='a'), LB(11.9, 44.1, 19.72, 've cetvel', g='a'),
        B1(43, 14.68, 'kalemler, silgi,', x=75, g='b'), B1(43, 17.20, 'kalemtıraş ve cetvel', x=60, g='b')]),
    act('dk43-gy', 'Gizemli Yolculuk', [5, 21.5, 90, 30.0], [B1(43, 41.12, 'Fener burada!', g='ş'), B1(43, 43.23, 'Peki yol nerede?', g='ş')]),
    act('dk43-sv1', 'Söz Varlığı 1', [5, 57.0, 90, 16.0], audio=AUD('dk', 43, 'S.028')),
    act('dk43-sv2', 'Söz Varlığı 2', [5, 73.0, 90, 17.5],
        TWO(43, 85.98, 88.09, 'Bu sarı kalem.', x=30) + TWO(43, 85.98, 88.10, 'Bu siyah makas.', x=50)
        + TWO(43, 85.98, 88.09, 'Bu yeşil çanta.', x=65) + TWO(43, 85.98, 88.10, 'Bu kırmızı paket.', x=85)),
], [link([28.6, 93.0, 30.8, 2.0], 'dbt', 23, 'Dil Bilgisi ve Telaffuz Kitabı s.23', {'act': 'dbt25-7'}, 'dbt23-1')])

# ---- Dinleme (listening scripts from the teacher's guide decide the answers)
C44 = [17.1, 39.4, 61.4, 83.5]
page(D, 'dk', 44, [
    act('dk44-1', '1. ve 2. etkinlik', [5, 8.0, 91.0, 32.0], audio=AUD('dk', 44, 'S.029') + AUD('dk', 44, 'S.030')),
    act('dk44-3', '3. etkinlik', [5, 40.5, 90, 20.5], [B1(44, 59.69, 'sıra', x=15), B1(44, 59.70, 'sandalye', x=40)]),
    act('dk44-4', '4. etkinlik', [5, 61.0, 90, 34.5],
        [CK(C44[2], 79.4, 2.4), CK(C44[3], 79.4, 2.4), CK(C44[1], 93.7, 2.4), CK(C44[2], 93.7, 2.4), CK(C44[3], 93.7, 2.4)],
        audio=AUD('dk', 44, 'S.031')),
])
Y45 = [63.3, 67.4, 71.5, 75.6, 79.7, 83.8, 87.9]
page(D, 'dk', 45, [
    act('dk45-5', '5. etkinlik', [5, 57.0, 90, 39.0], [
        LN([36.1, 67.4], [42.1, 63.3], g='q2'), B1(45, 63.78, 'kitap, defter ve kalemlik', g='q2'),
        B1(45, 67.86, 'on kalem', g='q1'),
        LN([36.1, 75.7], [42.0, 71.4], g='q4'), B1(45, 71.88, 'sıralar kahverengi', g='q4'),
        LN([36.1, 71.7], [42.1, 75.6], g='q3'), B1(45, 75.91, 'on iki', g='q3'),
        LN([35.4, 88.1], [42.1, 79.8], g='q7'), B1(45, 79.99, 'bir', g='q7'),
        LN([36.1, 84.2], [42.1, 83.9], g='q6'), LB(45.0, 79.8, 84.07, 'Sınıfta on beş', g='q6'),
        LN([36.1, 79.5], [42.8, 87.9], g='q5'), B1(45, 88.15, 'sıra, tahta, masa, pano ve dolap', g='q5')]
        + [LET(x, 93.0, ch, g='şifre', s=3.2) for x, ch in zip([44.0, 49.2, 54.5, 59.7, 64.9, 70.2], 'IRALAR')]),
])
page(D, 'dk', 46, [
    act('dk46-6', '6. etkinlik', [5, 7.0, 90, 15.5], [
        B1(46, 14.48, 'tahta, sıra, masa,'), LB(16.5, 83.1, 17.0, 'sandalye, pano, çöp kovası, klima'), B1(46, 19.51, 've kitaplık')]),
    act('dk46-sv1', 'Söz Varlığı 1', [5, 29.0, 90, 31.0], audio=AUD('dk', 46, 'S.032')),
    act('dk46-sv2', 'Söz Varlığı 2', [4, 61.0, 92, 27.0], [
        B1(46, 69.87, 'bir çanta var'), B1(46, 74.05, 'Sınıfta bir cetvel'),
        B1(46, 78.28, 'Sınıfta bir', x=75), B1(46, 78.27, 'var', x=88),
        B1(46, 82.46, 'bir kalemtıraş var'), B1(46, 86.64, 'Sınıfta altı defter')]),
    act('dk46-sv3', 'Söz Varlığı 3', [5, 88.5, 90, 7.5], [B1(46, 93.69, 'on kalemim var')]),
])
page(D, 'dk', 47, [
    act('dk47-s', 'Şarkı Zamanı', [5, 13.5, 90, 76.0], audio=AUD('dk', 47, 'M.006', 'M.007')),
], [link([29.3, 6.0, 30.8, 2.0], 'dbt', 26, 'Dil Bilgisi ve Telaffuz Kitabı s.26', {'act': 'dbt28-6'}, 'dbt26-1'),
    link([29.3, 90.9, 30.8, 2.0], 'dbt', 29, 'Dil Bilgisi ve Telaffuz Kitabı s.29', {'act': 'dbt30-5'}, 'dbt29-1')])

page(D, 'dk', 48, [
    act('dk48-1', 'Konuşma 1', [5, 9.0, 90, 32.0]),
    act('dk48-2', 'Konuşma 2', [5, 42.0, 90, 26.5]),
    act('dk48-3', 'Konuşma 3', [5, 69.0, 90, 26.5]),
])
page(D, 'dk', 49, [
    act('dk49-1a', 'Yazma 1 (a)', [5, 9.0, 90, 71.0], [
        B1(49, 60.15, 'bu kitaplık'),
        B1(49, 66.34, 'nerede', x=30, g='n'), B1(49, 69.11, 'sınıfta', x=30, g='n'),
        B1(49, 66.34, 'öğrenci', x=75, g='ö'), B1(49, 69.12, 'Evet', x=70, g='ö'), B1(49, 69.11, 'o öğrenci', x=80, g='ö'),
        B1(49, 75.51, 'defter', x=32, g='d'), LB(20.9, 38.6, 78.33, 'Sınıfta beş defter var', g='d'),
        B1(49, 75.51, 'kaç sıra', x=78)]),
    act('dk49-1b', 'Yazma 1 (b)', [5, 81.0, 90, 15.0], [
        B1(49, 88.60, 'Sınıfta kaç tahta var', x=30, g='t'), B1(49, 91.42, 'Sınıfta bir tahta var', x=30, g='t'),
        B1(49, 88.60, 'Sınıfta kaç öğretmen var', x=75, g='ö'), B1(49, 91.42, 'Sınıfta bir öğretmen var', x=75, g='ö')]),
])

# ---- B. Okulu Tanıyalım
page(D, 'dk', 50, [
    act('dk50-1', '1. ve 2. etkinlik', [5, 18.5, 91.0, 15.5], audio=AUD('dk', 50, 'S.033') + AUD('dk', 50, 'S.034')),
    act('dk50-3', '3. etkinlik', [5, 34.0, 90, 26.0], [CK(62.8, 45.8, 2.4), CK(92.8, 45.8, 2.4), CK(32.7, 51.3, 2.4), CK(62.8, 58.2, 2.4), CK(92.8, 54.8, 2.4)]),
    act('dk50-4', '4. etkinlik', [4, 60.5, 92, 35.0], [UL([29.0, 85.3], [32.7, 85.3]), UL([68.6, 86.9], [82.2, 86.9])]
        + ON(51, UL([36.4, 21.7], [44.3, 21.7]), UL([21.6, 23.3], [30.5, 23.3]), UL([31.8, 23.2], [39.7, 23.2]),
             UL([76.4, 42.7], [84.3, 42.7]), UL([78.4, 44.4], [86.3, 44.4])),
        audio=AUD('dk', 50, 'S.035'), tiles=[[4, 60.5, 92, 35.0], {'r': [6, 2.0, 88, 47.0], 'page': 51}], cols=2, nums=False),
])
page(D, 'dk', 51, [
    dict(act('dk51-4', '4. etkinlik', [6, 2.0, 88, 47.0], skip=True), alias={'page': 50, 'act': 'dk50-4'}),
    act('dk51-5', '5. etkinlik', [5, 49.5, 90, 15.5], [
        B1(51, 63.82, 'Öğretmenler odası', x=15), B1(51, 63.82, 'Sınıf', x=38), B1(51, 63.83, 'Laboratuvar', x=60), B1(51, 63.82, 'Kantin', x=82)]),
    act('dk51-6', '6. etkinlik', [5, 65.0, 90, 30.5], [
        B1(51, 71.33, 'tuvalet', g='t'), B1(51, 74.15, 'Tuvalet birinci katta', g='t'),
        B1(51, 80.54, 'Burası sınıf', x=30, g='s'), B1(51, 83.36, 'Sınıf ikinci', x=30, g='s'),
        B1(51, 80.54, 'Burası laboratuvar', x=80, g='l'), B1(51, 83.36, 'Laboratuvar birinci katta', x=80, g='l'),
        B1(51, 89.85, 'Burası öğretmenler odası', x=30, g='ö'), B1(51, 92.63, 'Öğretmenler odası ikinci katta', x=30, g='ö'),
        B1(51, 89.86, 'Burası kantin', x=80, g='k'), B1(51, 92.63, 'Kantin birinci katta', x=80, g='k')]),
])
page(D, 'dk', 52, [
    act('dk52-8a', '8. etkinlik (a)', [5, 4.0, 90, 72.0], [CK(48.3, 64.9, 2.6)]),
    act('dk52-8b', '8. etkinlik (b)', [5, 76.5, 90, 19.5], [
        B1(52, 82.21, 'üç', x=67, g='o'), B1(52, 82.21, 'Bahçede', x=80, g='o'),
        B1(52, 84.72, 'futbol sahası ve kantin var. Birinci katta müdür odası,', g='o'),
        B1(52, 87.29, 'spor salonu, tuvalet ve sınıflar var. İkinci katta sınıflar,', g='o'),
        LB(12.5, 87.7, 89.81, 'tuvalet, kütüphane, dil sınıfı ve öğretmenler odası var.', g='o'),
        B1(52, 92.32, 'Üçüncü katta konferans salonu, müzik odası ve resim odası var.', g='o')]),
])
R53 = [(34.5, 55.1), (50.2, 55.1), (66.0, 55.1), (73.8, 55.1), (34.2, 76.6), (49.8, 76.6), (57.8, 76.6), (65.5, 76.6), (73.5, 76.6)]
page(D, 'dk', 53, [
    act('dk53-1', 'Söz Varlığı 1', [5, 8.5, 90, 34.5], audio=AUD('dk', 53, 'S.036')),
    act('dk53-2', 'Söz Varlığı 2', [5, 45.0, 90, 42.0], [FL([round(x - 3.0, 2), round(y - 2.4, 2), 6.0, 4.8]) for x, y in R53]),
], [link([27.9, 90.6, 30.6, 2.0], 'dbt', 31, 'Dil Bilgisi ve Telaffuz Kitabı s.31', {'act': 'dbt33-7'}, 'dbt31-1')])

# word search: column centres and row centres
WX = lambda c: round(17.4 + 4.35 * (c - 1), 2)
WY = [72.5, 75.9, 79.2, 82.6, 86.0, 89.4]
def WORD(r, c0, c1, g): return FL([round(WX(c0) - 2.1, 2), round(WY[r - 1] - 1.6, 2), round(WX(c1) - WX(c0) + 4.2, 2), 3.2], g=g)
page(D, 'dk', 54, [
    act('dk54-1', '1. ve 2. etkinlik', [5, 12.0, 91.0, 28.0], audio=AUD('dk', 54, 'S.037') + AUD('dk', 54, 'S.038')),
    act('dk54-3', '3. etkinlik', [5, 41.0, 90, 51.0], [
        WORD(1, 4, 13, 'spor'), CK(79.9, 52.1, 2.4, g='spor'),
        WORD(2, 4, 10, 'tuvalet'), CK(57.9, 63.1, 2.4, g='tuvalet'),
        WORD(3, 1, 16, 'öğretmen'), CK(79.7, 63.1, 2.4, g='öğretmen'),
        WORD(4, 5, 11, 'koridor'), CK(58.1, 52.1, 2.4, g='koridor'),
        WORD(5, 4, 14, 'bahçe'), CK(34.5, 52.1, 2.4, g='bahçe'),
        WORD(6, 1, 16, 'bilgisayar'), CK(34.5, 63.1, 2.4, g='bilgisayar')]),
])
page(D, 'dk', 55, [
    act('dk55-4', '4. etkinlik', [5, 2.0, 90, 88.5], [
        CK(29.8, 38.7, 2.0), CK(22.2, 44.7, 2.0), CK(27.0, 73.2, 2.0), CK(24.1, 80.8, 2.0), CK(73.9, 73.2, 2.0)],
        audio=AUD('dk', 55, 'S.039')),
])
page(D, 'dk', 56, [
    act('dk56-5', '5. etkinlik', [5, 3.5, 90, 66.0], [
        TX([37.5, 21.8, 25.0, 2.6], 'Zeynep’in okulu kaç katlı?', g='a'), CK(85.0, 30.5, 2.4, g='a'),
        TX([62.6, 33.6, 25.4, 2.8], 'Okulda kaç sınıf var?', g='b'), CK(57.4, 45.6, 2.4, g='b'),
        TX([62.2, 49.1, 25.2, 2.8], 'Okulda kaç öğretmen var?', g='c'), CK(94.0, 61.9, 2.4, g='c')]),
    act('dk56-6', '6. etkinlik', [5, 73.0, 90, 23.0], [
        B1(56, 85.12, 'beş', x=26), B1(56, 85.12, 'elli', x=46), B1(56, 85.12, 'doksan', x=70),
        B1(56, 87.64, 'sınıflar ve tuvalet', x=35), B1(56, 87.64, 'katta kütüphane ve', x=70), B1(56, 90.16, 'laboratuvar var', x=15),
        B1(56, 90.16, 'yüzme havuzu', x=45)]),
])
page(D, 'dk', 57, [
    act('dk57-1', 'Söz Varlığı 1', [5, 8.5, 90, 52.0], audio=AUD('dk', 57, 'S.040')),
    act('dk57-2', 'Söz Varlığı 2', [5, 61.0, 90, 35.0], [
        B1(57, 78.63, 'Lütfen, kitabı aç.', x=38), B1(57, 78.63, 'Lütfen, kitabı kapat.', x=60), B1(57, 78.63, 'Lütfen, çöpü at.', x=82),
        B1(57, 95.40, 'Lütfen, kalk.', x=38), B1(57, 95.39, 'Lütfen, otur.', x=60)]),
])
page(D, 'dk', 58, [
    act('dk58-s', 'Şarkı Zamanı', [5, 13.0, 90, 70.0], audio=AUD('dk', 58, 'M.008')),
], [link([28.4, 6.0, 30.6, 2.0], 'dbt', 34, 'Dil Bilgisi ve Telaffuz Kitabı s.34', {'act': 'dbt36-8'}, 'dbt34-1'),
    link([28.4, 84.0, 30.6, 2.0], 'dbt', 37, 'Dil Bilgisi ve Telaffuz Kitabı s.37', {'act': 'dbt38-5b'}, 'dbt37-1')])
page(D, 'dk', 59, [act('dk59-1', 'Konuşma 1', [5, 9.0, 90, 75.0])])
page(D, 'dk', 60, [
    act('dk60-2', 'Konuşma 2', [5, 4.0, 90, 40.0]),
    act('dk60-1a', 'Yazma 1 (a)', [5, 54.5, 90, 22.0], [
        B1(60, 61.31, '20', x=42), B1(60, 64.27, 'on', x=28), B1(60, 64.29, 'otuz', x=56), B1(60, 61.31, '40', x=70), B1(60, 64.27, 'elli', x=85),
        B1(60, 70.42, '60', x=21), B1(60, 73.39, 'yetmiş', x=35), B1(60, 70.40, '80', x=49), B1(60, 73.39, 'doksan', x=63), B1(60, 70.42, '100', x=77)]),
    act('dk60-1b', 'Yazma 1 (b)', [5, 76.5, 90, 12.0], [
        B1(60, 82.95, '20.', x=33), B1(60, 85.93, 'otuzuncu', x=49), B1(60, 82.94, '40.', x=66), B1(60, 85.93, 'ellinci', x=82)]),
])
C61 = [69.4, 77.7, 86.1]; R61 = [13.6, 16.5, 19.4, 22.2, 25.1]
ECE = ['Merhaba! Ben Ece. Benim okulum dört katlı. Bahçede basket sahası var.', 'Birinci katta spor salonu, yüzme havuzu ve kantin var.',
       'İkinci katta müdür odası, sınıflar, tuvalet ve kütüphane var.', 'Üçüncü katta öğretmenler odası, sınıflar, tuvalet ve müzik odası var.',
       'Dördüncü katta kantin, tuvalet ve konferans salonu var.']
page(D, 'dk', 61, [
    act('dk61-2a', 'Yazma 2 (a)', [5, 4.0, 90, 23.5],
        [CK(C61[0], R61[0], 2.2), CK(C61[1], R61[1], 2.2), CK(C61[2], R61[1], 2.2), CK(C61[1], R61[2], 2.2), CK(C61[0], R61[3], 2.2), CK(C61[2], R61[4], 2.2)]),
    act('dk61-2b', 'Yazma 2 (b)', [5, 29.5, 90, 61.5], [LB(10.1, 89.5, y, t, g='e') for y, t in zip([73.30, 75.41, 77.53, 79.64, 81.76], ECE)]),
])
page(D, 'dk', 62, [
    act('dk62-1', 'C. Pırıl’ın Sınıfı 1', [5, 12.0, 90, 73.0], [
        B1(62, 35.53, 'Pırıl’ın okulu', x=25), B1(62, 35.53, 'Pırıl’ın sınıfı', x=75),
        B1(62, 59.55, 'kalem', x=14), B1(62, 59.54, 'defter', x=28), B1(62, 59.55, 'çanta', x=42), B1(62, 59.50, 'öğretmen', x=63), B1(62, 59.49, 'tahta', x=82),
        B1(62, 83.61, 'defter', x=14), B1(62, 83.62, 'çanta', x=28), B1(62, 83.62, 'kalemlik', x=42), B1(62, 83.62, 'Deha', x=63), B1(62, 83.61, 'Cesur', x=80)],
        audio=AUD('dk', 62, 'V.002')),
    act('dk62-2', 'C. Pırıl’ın Sınıfı 2', [33, 87.0, 62, 9.0]),
])
page(D, 'dk', 63, [act('dk63-g', 'Maarif Türkçe Grubu', [19, 4.0, 63, 90.0])])
page(D, 'dk', 64, [act('dk64-p', 'Proje Zamanı', [3, 4.0, 94, 92.0])])

# =================================================================== DİL BİLGİSİ VE TELAFFUZ — 2. ÜNİTE
page(T, 'dbt', 22)
page(T, 'dbt', 23, [
    act('dbt23-1', '1. etkinlik', [8, 24.0, 84, 52.5], audio=AUD('dbt', 23, 'S.017')),
    act('dbt23-2', '2. etkinlik', [8, 77.0, 84, 16.5]),
])
page(T, 'dbt', 24, [
    act('dbt24-3', '3. etkinlik', [10, 7.0, 82, 26.0], [
        BT(24, 15.66, 'Bu Esma', x=60), BT(24, 15.66, 'Bu defter', x=80), BT(24, 20.59, 'Bu Emre', x=60), BT(24, 20.59, 'Bu kalem', x=80),
        BT(24, 25.53, 'Bu Zeynep', x=60), BT(24, 25.53, 'Bu makas', x=80), BT(24, 30.46, 'Bu Ali', x=60), BT(24, 30.46, 'Bu çanta', x=80)]),
    act('dbt24-4', '4. etkinlik', [10, 38.5, 82, 19.0], audio=AUD('dbt', 24, 'S.018')),
    act('dbt24-5', '5. etkinlik', [10, 58.5, 82, 30.5], [
        BT(24, 74.24, 'Şu', x=38), BT(24, 74.24, 'O', x=68), BT(24, 87.81, 'Bu', x=18), BT(24, 87.81, 'Şu', x=36), BT(24, 87.81, 'O', x=67)]),
])
E25 = lambda x, y, g=None: EL([round(x - 8.6, 2), round(y - 1.3, 2), 17.2, 2.6], g=g)
page(T, 'dbt', 25, [
    act('dbt25-6', '6. etkinlik', [8, 7.0, 84, 26.5], audio=AUD('dbt', 25, 'S.019')),
    act('dbt25-7', '7. etkinlik', [8, 34.0, 84, 58.0], [
        E25(77.6, 48.2), E25(77.6, 53.4), E25(58.7, 58.5), E25(77.6, 63.8), E25(58.7, 68.9)]),
])
page(T, 'dbt', 26, [
    act('dbt26-1', '1. etkinlik', [10, 19.5, 82, 53.5], audio=AUD('dbt', 26, 'S.020')),
    act('dbt26-2', '2. etkinlik', [10, 73.5, 82, 20.5]),
])
page(T, 'dbt', 27, [
    act('dbt27-3', '3. etkinlik', [8, 16.0, 84, 40.0], audio=AUD('dbt', 27, 'S.021')),
    act('dbt27-4', '4. etkinlik', [8, 58.0, 84, 31.5], [
        BT(27, 64.95, 'üç cetvel', x=75), BT(27, 70.77, 'cetveller', x=75),
        BT(27, 80.46, 'iki sıra', x=35), BT(27, 86.28, 'sıralar', x=35),
        BT(27, 80.46, 'iki kalemtıraş', x=75), BT(27, 86.28, 'kalemtıraşlar', x=75)]),
])
page(T, 'dbt', 28, [
    act('dbt28-5', '5. etkinlik', [10, 16.0, 82, 16.5], audio=AUD('dbt', 28, 'S.022')),
    act('dbt28-6', '6. etkinlik', [10, 33.0, 82, 60.5], [
        BT(28, 63.17, 'Sıra burada.', x=20), BT(28, 63.17, 'Sıra şurada.', x=50), BT(28, 63.17, 'Sıra orada.', x=75),
        BT(28, 77.23, 'Masa burada.', x=20), BT(28, 77.23, 'Masa şurada.', x=50), BT(28, 77.23, 'Masa orada.', x=75),
        BT(28, 91.69, 'Askı burada.', x=20), BT(28, 91.69, 'Askı şurada.', x=50), BT(28, 91.69, 'Askı orada.', x=75)]),
])
page(T, 'dbt', 29, [
    act('dbt29-1', '1. etkinlik', [8, 11.5, 84, 21.5], audio=AUD('dbt', 29, 'S.023')),
    act('dbt29-2', '2. etkinlik', [8, 34.0, 84, 22.5], audio=AUD('dbt', 29, 'S.024')),
    act('dbt29-3', '3. etkinlik', [8, 57.5, 84, 35.0], audio=AUD('dbt', 29, 'S.025')),
])
page(T, 'dbt', 30, [
    act('dbt30-4', '4. etkinlik', [10, 6.0, 82, 59.5], audio=AUD('dbt', 30, 'S.026')),
    act('dbt30-5', '5. etkinlik', [10, 66.5, 82, 22.0], [BT(30, 83.93, 'Kitap')], audio=AUD('dbt', 30, 'S.027')),
])
page(T, 'dbt', 31, [
    act('dbt31-1', '1. etkinlik', [8, 23.5, 84, 45.5], audio=AUD('dbt', 31, 'S.028')),
    act('dbt31-2', '2. etkinlik', [8, 69.5, 84, 22.5]),
])
page(T, 'dbt', 32, [
    act('dbt32-3', '3. etkinlik', [10, 16.0, 82, 16.0], audio=AUD('dbt', 32, 'S.029')),
    act('dbt32-4', '4. etkinlik', [10, 32.0, 82, 14.5], [
        BT(32, 45.33, 'Burası sınıf.', x=20), BT(32, 45.33, 'Şurası sınıf.', x=45), BT(32, 45.33, 'Orası sınıf.', x=75)]),
    act('dbt32-5', '5. etkinlik', [8, 54.0, 85, 38.5], audio=AUD('dbt', 32, 'S.030')),
])
page(T, 'dbt', 33, [
    act('dbt33-6', '6. etkinlik', [8, 7.0, 84, 34.5], [
        BT(33, 32.81, 'Kantin birinci katta.', x=70), BT(33, 36.57, 'Kütüphane ikinci katta.', x=30), BT(33, 36.57, 'Sınıflar üçüncü katta.', x=70),
        BT(33, 40.16, 'Spor salonu birinci katta.', x=30), BT(33, 40.16, 'Tuvalet üçüncü katta.', x=70)]),
    act('dbt33-7', '7. etkinlik', [8, 43.5, 84, 48.5], [
        NUM(49.4, 74.6, '2.', 3.0, 2.2), NUM(32.4, 72.5, '3.', 3.0, 2.2), NUM(24.9, 67.6, '4.', 3.0, 2.2), NUM(37.0, 62.6, '5.', 3.0, 2.2), NUM(46.4, 61.4, '6.', 3.0, 2.2)]),
])
page(T, 'dbt', 34, [
    act('dbt34-1', '1. etkinlik', [10, 18.5, 82, 32.5], audio=AUD('dbt', 34, 'S.031')),
    act('dbt34-2', '2. etkinlik', [10, 51.0, 82, 42.5]),
])
page(T, 'dbt', 35, [
    act('dbt35-3', '3. etkinlik', [8, 15.0, 84, 18.0]),
    act('dbt35-4', '4. etkinlik', [8, 33.0, 84, 32.5], [
        BT(35, 57.90, 'Evet, kantin birinci katta.'), BT(35, 61.08, 'Hayır, ikinci katta sınıf yok.'), BT(35, 64.25, 'Üçüncü katta sınıflar ve tuvalet var.')]),
    act('dbt35-5', '5. etkinlik', [8, 65.5, 84, 28.0], [
        BT(35, 85.58, 'Okulda sınıflar var mı?', g='a'), BT(35, 87.69, 'Evet, sınıflar ikinci katta.', g='a'),
        BT(35, 90.33, 'Kantin kaçıncı katta?', x=25, g='b'), BT(35, 92.45, 'Kantin birinci katta.', x=25, g='b'),
        BT(35, 90.33, 'Tuvalet kaçıncı katta?', x=65, g='c'), BT(35, 92.45, 'Tuvalet birinci katta.', x=65, g='c')]),
])
page(T, 'dbt', 36, [
    act('dbt36-6', '6. etkinlik', [10, 15.0, 82, 18.5], audio=AUD('dbt', 36, 'S.032')),
    act('dbt36-7', '7. etkinlik', [10, 34.5, 82, 14.0], audio=AUD('dbt', 36, 'S.033')),
    act('dbt36-8', '8. etkinlik', [10, 49.5, 82, 43.0], [
        BT(36, 70.53, 'Pencereyi', x=50), BT(36, 70.53, 'Tahtayı', x=75), BT(36, 90.51, 'Çantayı', x=35), BT(36, 90.51, 'Topu', x=62)]),
])
page(T, 'dbt', 37, [
    act('dbt37-1', '1. etkinlik', [8, 11.5, 84, 21.5], audio=AUD('dbt', 37, 'S.034')),
    act('dbt37-2', '2. etkinlik', [8, 34.0, 84, 22.5], audio=AUD('dbt', 37, 'S.035')),
    act('dbt37-3', '3. etkinlik', [8, 57.5, 84, 35.0], audio=AUD('dbt', 37, 'S.036')),
])
page(T, 'dbt', 38, [
    act('dbt38-4', '4. etkinlik', [10, 6.0, 82, 61.0], audio=AUD('dbt', 38, 'S.037')),
    act('dbt38-5a', '5. etkinlik (a)', [10, 67.5, 41, 23.0], [BT(38, 87.16, 'Birinci olur.')], audio=AUD('dbt', 38, 'S.038')),
    act('dbt38-5b', '5. etkinlik (b)', [51, 67.5, 41, 23.0], [
        LB(54.9, 87.8, 80.1, 'Siler, temizler, izleri yok eder,', g='b'), LB(54.9, 87.8, 81.9, 'Kalemin yanında hep bekler!', g='b'),
        LB(54.9, 87.8, 83.8, 'Bil bakalım ne?', g='b'), BT(38, 85.63, '– Silgi.', g='b')]),
])

U2 = lambda a, b: [{'no': 2, 'title': 'Haydi Okula', 'from': a, 'to': b}]
dump('dk-u2', D, 0.7855, 'Ders Kitabı 1', U2(39, 64))
dump('dbt-u2', T, 0.6669, 'Dil Bilgisi ve Telaffuz Kitabı', U2(22, 38))
print('ok', len(D), len(T), sum(len(p['activities']) for p in D.values()), sum(len(p['activities']) for p in T.values()))
