# Word boxes straight from the PDF text layer (in % of the trimmed page), for circling/underlining printed words.
import subprocess, re
from html import unescape
PDF = {'dk2': ('/mnt/user-data/uploads/ORTA_A1_DK02_2.pdf', 14.17), 'dbt': ('/mnt/user-data/uploads/ORTA_A1_DBT.pdf', 8.5),
       'dk': ('/mnt/user-data/uploads/Ortaokul_A1_-_1_DK.pdf', 14.17)}
_C = {}
def words(b, n):
    if (b, n) not in _C:
        pdf, m = PDF[b]
        x = subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), '-bbox', pdf, '-'], capture_output=True, text=True).stdout
        pw, ph = map(float, re.search(r'<page width="([\d.]+)" height="([\d.]+)"', x).groups()); TW, TH = pw - 2 * m, ph - 2 * m
        _C[(b, n)] = [(unescape(t), (a - m) / TW * 100, (c - m) / TH * 100, (d - m) / TW * 100, (e - m) / TH * 100)
                      for a, c, d, e, t in ((*map(float, g[:4]), g[4]) for g in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', x))]
    return _C[(b, n)]
def clean(t): return t.strip('.,!?:;’\'"“”()').lower()
def WB(b, n, w, near):
    """box (x0,y0,x1,y1) of word w on page n nearest to point near=(x,y)"""
    c = [q for q in words(b, n) if clean(q[0]) == w.lower()]
    if not c: raise SystemExit(f'word {w!r} not on {b}{n}')
    q = min(c, key=lambda q: ((q[1] + q[3]) / 2 - near[0]) ** 2 + ((q[2] + q[4]) / 2 - near[1]) ** 2)
    return q[1:]
