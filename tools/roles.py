# Dialogue lines for "Rol yap": speaker labels ("Karagöz:") and their text, read from the PDF word boxes.
# ROLES([(book, page, [x, y, w, h]), ...]) → {'chars': [...], 'lines': [{'sp', 't', 'page', 'r'}]}
# Within each region the speech boxes (columns of labels) are read panel by panel: top to bottom, then left to right.
import re
from words import words
LABEL = re.compile(r"^[A-ZÇĞİÖŞÜ][a-zçğıöşüâ]+:$")
def _region(book, n, rect):
    x, y, w, h = rect
    W = [q for q in words(book, n) if x <= q[1] and q[3] <= x + w + .5 and y <= q[2] and q[4] <= y + h + .5]
    labs = [q for q in W if LABEL.match(q[0])]
    # columns: labels sharing (about) the same left edge and following each other closely
    cols = []
    for q in sorted(labs, key=lambda q: (q[1], q[2])):
        c = next((c for c in cols if abs(c[-1][1] - q[1]) < 1.2 and 0 < q[2] - c[-1][2] < 6), None)
        (c.append(q) if c else cols.append([q]))
    cols.sort(key=lambda c: (round(c[0][2] / 8), c[0][1]))
    out = []
    for c in cols:
        top, bot = c[0][2], c[-1][4] + 6
        right = min([o[0][1] for o in cols if o is not c and o[0][1] > c[0][1] + 3 and not (o[-1][4] < top - 1 or o[0][2] > bot)] + [x + w])
        for k, q in enumerate(c):
            y_end = c[k + 1][2] - .3 if k + 1 < len(c) else bot
            ws = [v for v in W if q[1] - .5 <= v[1] < right - .5 and q[2] - .4 <= v[2] < y_end and v is not q]
            ws = [v for v in ws if not (LABEL.match(v[0]) and v[2] > q[2] + .3) and not re.fullmatch(r"\d+", v[0])]
            if k + 1 == len(c):   # last line of a box: stop at the first big vertical gap
                ws.sort(key=lambda v: (round(v[2], 1), v[1])); keep = []
                for v in ws:
                    if keep and v[2] - max(u[4] for u in keep) > 1.2: break
                    keep.append(v)
                ws = keep
            ws.sort(key=lambda v: (round(v[2] * 2) / 2, v[1]))
            t = ' '.join(v[0] for v in ws).replace(' ,', ',').strip()
            x0 = min([q[1]] + [v[1] for v in ws]); y0 = q[2]; x1 = max([q[3]] + [v[3] for v in ws]); y1 = max([q[4]] + [v[4] for v in ws])
            out.append({'sp': q[0][:-1], 't': t, 'page': n, 'r': [round(x0 - .4, 2), round(y0 - .3, 2), round(x1 - x0 + .8, 2), round(y1 - y0 + .6, 2)]})
    return out
def ROLES(*regions, fix=None):
    lines = [l for b, n, r in regions for l in _region(b, n, r)]
    for i, t in (fix or {}).items(): lines[i]['t'] = t
    chars = []
    for l in lines:
        if l['sp'] not in chars: chars.append(l['sp'])
    return {'chars': chars, 'lines': lines}
