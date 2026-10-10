# Render pages of one book for a unit and auto-extract audio codes, cross references, dotted blanks and row gaps.
# usage: prep_unit.py WORK BOOK PDF MARGIN_PT FIRST LAST [PDF_OFFSET]
#   page n (printed) is PDF page n + PDF_OFFSET. Writes WORK/png/BOOK-NNN-c.png, img/BOOK/NNN.jpg (+ t/ thumbs), WORK/auto-BOOK.json
import subprocess, re, json, sys, os, cv2, numpy as np
from html import unescape
from PIL import Image
W, book, pdf, m, a, b = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
off = int(sys.argv[7]) if len(sys.argv) > 7 else 0
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(f'{W}/png', exist_ok=True); os.makedirs(f'{ROOT}/img/{book}/t', exist_ok=True)
DPI = 180
out = {}
for n in range(a, b + 1):
    q = n + off
    c = f'{W}/png/{book}-{n:03d}-c.png'
    if not os.path.exists(c):
        subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(q), '-l', str(q), '-png', '-singlefile', pdf, f'{W}/png/{book}-{n:03d}'], check=True)
        im = Image.open(f'{W}/png/{book}-{n:03d}.png').convert('RGB'); px = round(m / 72 * DPI)
        im = im.crop((px, px, im.width - px, im.height - px)); im.save(c)
    im = Image.open(c)
    im.save(f'{ROOT}/img/{book}/{n:03d}.jpg', quality=80, optimize=True)
    t = im.resize((220, round(im.height * 220 / im.width)), Image.LANCZOS); t.save(f'{ROOT}/img/{book}/t/{n:03d}.jpg', quality=72)
    x = subprocess.run(['pdftotext', '-f', str(q), '-l', str(q), '-bbox-layout', pdf, '-'], capture_output=True, text=True).stdout
    pw, ph = map(float, re.search(r'<page width="([\d.]+)" height="([\d.]+)"', x).groups())
    TW, TH = pw - 2 * m, ph - 2 * m
    P = lambda a_, c_, d_, e_: [round((a_ - m) / TW * 100, 2), round((c_ - m) / TH * 100, 2), round((d_ - a_) / TW * 100, 2), round((e_ - c_) / TH * 100, 2)]
    lines = []
    for lm in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', x, re.S):
        t_ = unescape(' '.join(re.findall(r'<word[^>]*>(.*?)</word>', lm.group(5)))).strip()
        if t_: lines.append({'t': t_, 'r': P(*map(float, lm.groups()[:4]))})
    audio = []
    for wm in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([SVM]\.\d{3})</word>', x):
        a_, c_, d_, e_ = map(float, wm.groups()[:4]); h = e_ - c_
        audio.append({'code': wm.group(5), 'r': P(a_ - h * 2.0, c_ - h * .25, d_ + h * .35, e_ + h * .25)})
    links = [l for l in lines if 'bölümüne bak' in l['t']]
    g = cv2.imread(c, cv2.IMREAD_GRAYSCALE); H, Wd = g.shape
    bw = (g < 170).astype(np.uint8)
    k, lab, st, cen = cv2.connectedComponentsWithStats(bw, 8)
    dots = [(cen[i][0], cen[i][1]) for i in range(1, k) if st[i][2] <= 6 and st[i][3] <= 6 and st[i][4] >= 2]
    rows = {}
    for px_, py in dots: rows.setdefault(round(py / 3), []).append((px_, py))
    blanks = []
    for kk in sorted(rows):
        pts = sorted(rows[kk]); run = [pts[0]]; rs = []
        for p_ in pts[1:]:
            if p_[0] - run[-1][0] > 14: rs.append(run); run = [p_]
            else: run.append(p_)
        rs.append(run)
        for r in rs:
            if len(r) >= 6 and np.median(np.diff([q_[0] for q_ in r])) < 9:
                blanks.append([round(r[0][0] / Wd * 100, 2), round(r[-1][0] / Wd * 100, 2), round(float(np.mean([q_[1] for q_ in r])) / H * 100, 2)])
    ink = (g < 235).sum(axis=1) / Wd; gaps = []; s = None
    for y, bb in enumerate(ink < 0.004):
        if bb and s is None: s = y
        if not bb and s is not None:
            if y - s >= H * 0.005: gaps.append([round(s / H * 100, 1), round(y / H * 100, 1)])
            s = None
    out[f'{book}{n}'] = {'lines': lines, 'audio': audio, 'links': links, 'blanks': blanks, 'gaps': gaps, 'size': [Wd, H], 'aspect': round(TW / TH, 4)}
    print(book, n, 'audio', [a_['code'] for a_ in audio], 'links', len(links), 'blanks', len(blanks))
f = f'{W}/auto-{book}.json'
old = json.load(open(f)) if os.path.exists(f) else {}
old.update(out); json.dump(old, open(f, 'w'), ensure_ascii=False)
