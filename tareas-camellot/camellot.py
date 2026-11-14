"""Kit Camellot: dibujo de la tarea (Lienzo) y ficha PDF "Entrega Ejercicio" (Ficha).

Uso rápido (ver ejemplo_tarea.py):
    from camellot import Lienzo, ficha
    L = Lienzo('medio')            # 'medio' | 'cuadrado' | 'entero'
    L.j(.5, .3, 'rojo'); L.pase(.5, .3, .5, .6); L.guardar('dibujo.png')
    ficha(datos, 'dibujo.png', 'salida.pdf')

Requisitos: pip install pymupdf matplotlib pillow numpy
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from PIL import Image

# Los recursos se buscan en la carpeta del kit (variable de entorno CAMELLOT_KIT o la carpeta padre de scripts/),
# tanto en subcarpetas (fondos/, fichas/, plantilla/, fuentes/) como todos sueltos en la misma carpeta que este script.
_AQUI = os.path.dirname(os.path.abspath(__file__))
KIT = os.environ.get('CAMELLOT_KIT') or os.path.dirname(_AQUI)


def ruta(sub, nombre):
    for d in (os.path.join(KIT, sub), KIT, os.path.join(_AQUI, sub), _AQUI, os.path.join(os.path.dirname(_AQUI), sub)):
        p = os.path.join(d, nombre)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f'No encuentro {nombre} (buscado en {KIT} y {_AQUI}, con y sin la subcarpeta {sub}/)')


PLANTILLA = ruta('plantilla', 'plantilla_entrega_ejercicio.pdf')
FUENTE = ruta('fuentes', 'Figtree-Regular.ttf')

# Fondos del kit: archivo, caja de líneas (px), radio de jugador (px) y máscara de esquinas.
FONDO = {
    'medio':    dict(png='medio_campo.png',  box=(100, 82, 1198, 1181), r=26, mask='mascara_medio_campo.png'),
    'cuadrado': dict(png='cuadrado.png',     box=(59, 59, 1334, 1333),  r=30, mask=None),
    'entero':   dict(png='campo_entero.png', box=(76, 41, 2152, 1353),  r=24, mask=None),
}
ACOL = {'negro': '#1A1A1A', 'rojo': '#E0322B', 'naranja': '#F4B26A', 'blanco': '#FFFFFF', 'azul': '#2457D6'}


class Lienzo:
    """Coordenadas normalizadas 0..1 dentro de la caja de líneas.
    - 'cuadrado' y 'entero': x de izquierda a derecha, y de arriba abajo (en 'entero', x=0 es la portería izquierda).
    - 'medio': se escribe en vertical, como en las apps de pizarra: x = ancho del campo (0 izq. .. 1 der.),
      y = 0 en la línea de gol .. 1 en el medio campo. La portería queda a la izquierda del dibujo.
    """

    def __init__(self, fondo='medio'):
        cfg = FONDO[fondo]
        self.base, self.cfg = fondo, cfg
        im = Image.open(ruta('fondos', cfg['png'])).convert('RGB')
        self.W, self.H = im.size
        self.box, self.r, self.tf = cfg['box'], cfg['r'], None
        self.fig = plt.figure(figsize=(self.W / 100, self.H / 100), dpi=100)
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.imshow(im, extent=(0, self.W, self.H, 0)); self.ax.axis('off'); self._lim()

    def _lim(self):
        self.ax.set_xlim(0, self.W); self.ax.set_ylim(self.H, 0)

    def P(self, x, y):
        if self.tf:
            x, y = self.tf(x, y)
        u, v = (y, 1 - x) if self.base == 'medio' else (x, y)
        b = self.box
        return b[0] + u * (b[2] - b[0]), b[1] + v * (b[3] - b[1])

    def _paste(self, name, cx, cy, w=None, h=None, rot=0, z=6):
        im = Image.open(ruta('fichas', name + '.png')).convert('RGBA')
        if rot:
            im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
        iw, ih = im.size
        w = w or h * iw / ih
        h = h or w * ih / iw
        self.ax.imshow(np.asarray(im), extent=(cx - w / 2, cx + w / 2, cy + h / 2, cy - h / 2), zorder=z); self._lim()

    # fichas
    def j(self, x, y, c='rojo', k=1.0):            # c: rojo, amarillo, azul, negro (portero/a)
        self._paste(c, *self.P(x, y), w=2 * self.r * k)
    def b(self, x, y):
        self._paste('balon', *self.P(x, y), w=self.r * 1.1, z=11)
    def cono(self, x, y):
        self._paste('cono', *self.P(x, y), w=self.r * 1.05, z=4)
    def mini(self, x, y, abre='derecha', k=1.0):
        """Miniportería. 'abre' = hacia dónde mira la boca (la red queda detrás)."""
        rot = {'derecha': 0, 'izquierda': 180, 'arriba': 90, 'abajo': 270}[abre]
        self._paste('mini', *self.P(x, y), h=self.r * 2.8 * k, rot=rot, z=4)

    # líneas y flechas
    def zona(self, x0, y0, x1, y1, lw=3.2):
        a, c = self.P(x0, y0), self.P(x1, y1)
        self.ax.add_patch(FancyBboxPatch((min(a[0], c[0]), min(a[1], c[1])), abs(c[0] - a[0]), abs(c[1] - a[1]),
                                         boxstyle='round,pad=0,rounding_size=6', fill=False, edgecolor='#1A1A1A', lw=lw, zorder=3))
    def linea(self, x0, y0, x1, y1, c='negro', lw=3.0):
        a, d = self.P(x0, y0), self.P(x1, y1)
        self.ax.plot([a[0], d[0]], [a[1], d[1]], color=ACOL.get(c, c), lw=lw, zorder=3)
    def _arrow(self, a, d, c, ls='-', lw=2.6):
        self.ax.add_patch(FancyArrowPatch(a, d, arrowstyle='-|>', mutation_scale=20, lw=lw, ls=ls,
                                          color=ACOL.get(c, c), zorder=13, shrinkA=0, shrinkB=0))
    def pase(self, x0, y0, x1, y1, c='negro'):
        self._arrow(self.P(x0, y0), self.P(x1, y1), c)
    def mov(self, x0, y0, x1, y1, c='negro'):
        self._arrow(self.P(x0, y0), self.P(x1, y1), c, ls=(0, (4, 3)))
    def cond(self, x0, y0, x1, y1, c='negro'):
        a, d = np.array(self.P(x0, y0)), np.array(self.P(x1, y1)); v = d - a; n = np.linalg.norm(v)
        u = v / n; p = np.array([-u[1], u[0]]); t = np.linspace(0, 1, 300); k = max(2, int(n / (self.r * 1.4)))
        pts = a + np.outer(t * n * .88, u) + np.outer(self.r * .38 * np.sin(t * k * 2 * np.pi), p)
        self.ax.plot(pts[:, 0], pts[:, 1], color=ACOL.get(c, c), lw=2.4, zorder=13)
        self._arrow(tuple(pts[-1]), tuple(d), c, lw=2.4)
    def texto(self, x, y, s, k=1.0):
        cx, cy = self.P(x, y)
        self.ax.text(cx, cy, s, ha='center', va='center', fontsize=self.r * 1.2 * k, fontweight='bold', color='#1A1A1A', zorder=14)

    def guardar(self, path):
        self.fig.savefig(path, dpi=100); plt.close(self.fig)
        if self.cfg['mask']:   # esquinas transparentes, como exporta la plataforma el medio campo
            im = Image.open(path).convert('RGB').resize((self.W, self.H))
            im.putalpha(Image.open(ruta('fondos', self.cfg['mask'])).convert('L')); im.save(path)


# ---------------------------------------------------------------- ficha PDF
import pymupdf as fitz

GREY = (0.95686,) * 3; BLACK = (0, 0, 0); X0, X1 = 20.0, 575.28; LH = 12.0; FS = 10.0; BAND_H = 30.688; BOT = 841.89 - 10
CLIPS = {'header': fitz.Rect(0, 0, 595.28, 50), 'detalles': fitz.Rect(20, 60, 575.28, 90.688),
         'grafica': fitz.Rect(20, 321.7, 575.28, 352.4), 'consigna': fitz.Rect(20, 767.4, 575.28, 798.1)}


class Ficha:
    def __init__(self, template_pdf=PLANTILLA, font_ttf=FUENTE, clips=CLIPS):
        self.doc = fitz.open(); self.tpl = fitz.open(template_pdf); self.ff = font_ttf
        self.font = fitz.Font(fontfile=font_ttf); self.clips = clips; self.new_page()
    def new_page(self):
        self.page = self.doc.new_page(width=595.28, height=841.89); self.page.insert_font(fontname='FIG', fontfile=self.ff)
        self.page.show_pdf_page(self.clips['header'], self.tpl, 0, clip=self.clips['header']); self.y = 60.0
    def text(self, x, bl, s):
        self.page.insert_text((x, bl), s, fontname='FIG', fontsize=FS, color=BLACK)
    def wrap(self, s, width):
        out = []
        for para in s.split('\n'):
            cur = ''
            for w in para.split(' '):
                t = (cur + ' ' + w) if cur else w
                if self.font.text_length(t, fontsize=FS) <= width: cur = t
                else:
                    if cur: out.append(cur)
                    cur = w
            out.append(cur)
        return out
    def outline(self, top, bottom):
        sh = self.page.new_shape(); r = 4.0; L = X0 + .5; R = X1 - .5; B = bottom - .5
        sh.draw_line((R, top), (R, B - r)); sh.draw_bezier((R, B - r), (R, B - r + 2.209), (R - 1.791, B), (R - r, B)); sh.draw_line((R - r, B), (L + r, B))
        sh.draw_bezier((L + r, B), (L + 1.791, B), (L, B - 1.791), (L, B - r)); sh.draw_line((L, B - r), (L, top))
        sh.finish(color=BLACK, width=1.0, closePath=False); sh.commit()
    def hline(self, x0, x1, y): self.page.draw_line((x0, y), (x1, y), color=BLACK, width=1.0)
    def vline(self, x, y0, y1): self.page.draw_line((x, y0), (x, y1), color=BLACK, width=1.0)
    def grey(self, x0, y0, x1, y1): self.page.draw_rect(fitz.Rect(x0, y0, x1, y1), color=None, fill=GREY, width=0)
    def band(self, key):
        self.page.show_pdf_page(fitz.Rect(X0, self.y, X1, self.y + BAND_H), self.tpl, 0, clip=self.clips[key]); self.y += BAND_H
    def detalles(self, titulo, estrategia, objetivos):
        self.band('detalles'); top = self.y; LX = 131.656
        rows = [([titulo], 25.0, 15.39), ([estrategia], 25.0, 15.39),
                (objetivos, max(25.0, LH * len(objetivos) + 10), 14.39 if len(objetivos) > 1 else 15.39)]
        bottom = top + sum(h for _, h, _ in rows) + 1; self.outline(top, bottom); self.grey(21.0, top, LX, bottom - 1); y = top
        for k, ((vals, h, b0), lab) in enumerate(zip(rows, ['Título', 'Estrategia', 'Objetivos'])):
            if k: self.hline(21.0, LX, y); self.hline(LX, X1 - 1, y)
            self.vline(LX, y, y + h); self.text(31.0, y + (15.89 if lab == 'Objetivos' and len(vals) > 1 else 15.39), lab)
            for i, v in enumerate(vals): self.text(142.656, y + b0 + i * LH, v)
            y += h
        self.y = y
    def tabla(self, headers, values):
        top = self.y + 6; n = len(headers); w = (574.28 - 21.0) / n
        self.grey(21.0, top, 574.28, top + 25); self.outline(top, top + 51)
        self.page.draw_line((21.0, top + .5), (574.28, top + .5), color=BLACK, width=1.0); self.hline(21.0, 574.28, top + 25)
        for i, (hd, v) in enumerate(zip(headers, values)):
            x0 = 21.0 + i * w
            if i < n - 1: self.vline(x0 + w, top, top + 50)
            self.text(x0 + 10, top + 15.89, hd)
            if v: self.text(x0 + 10, top + 40.89, v)
        self.y = top + 50
    def grafica(self, img, maxw=440.0, maxh=400.0):
        self.y += 11; pix = fitz.Pixmap(img); s = min(maxw / pix.width, maxh / pix.height); iw, ih = pix.width * s, pix.height * s
        if self.y + BAND_H + ih + 5 > BOT: self.new_page()
        self.band('grafica'); it = self.y + 2
        self.page.insert_image(fitz.Rect((595.28 - iw) / 2, it, (595.28 + iw) / 2, it + ih), filename=img)
        self.outline(self.y, it + ih + 3); self.y = it + ih + 3
    def consigna(self, texto):
        self.y += 10; lines = self.wrap(texto, 535.7)
        if self.y + BAND_H + 33 > BOT: self.new_page()
        self.band('consigna'); first = True
        while lines:
            top = self.y; pad = 10 if first else 0; avail = int((BOT - 11 - (top + pad)) // LH)
            if avail < 2:
                self.vline(X0 + .5, top, BOT); self.vline(X1 - .5, top, BOT); self.new_page(); first = False; continue
            chunk, lines = lines[:avail], lines[avail:]
            for i, l in enumerate(chunk): self.text(31.0, top + pad + 9.42 + i * LH, l)
            if lines:
                self.vline(X0 + .5, top, BOT); self.vline(X1 - .5, top, BOT); self.new_page(); first = False
            else:
                self.outline(top, top + pad + LH * len(chunk) + 11); self.y = top + pad + LH * len(chunk) + 11
    def save(self, out): self.doc.save(out, garbage=3, deflate=True)


def ficha(t, img, out, **kw):
    """t: dict con titulo, estrategia, objetivos (lista), espacio, tiempo, situacion, coordinacion,
    habilidades, intencion, explicacion (párrafos separados por \\n)."""
    f = Ficha(**kw)
    f.detalles(t['titulo'], t['estrategia'], t['objetivos'])
    f.tabla(['Espacio', 'Tiempo', 'Situación de Juego', 'Coordinación'], [t['espacio'], t['tiempo'], t['situacion'], t['coordinacion']])
    f.tabla(['Habilidades Coordinativas', 'Intención / Acción Táctica'], [t['habilidades'], t['intencion']])
    f.grafica(img); f.consigna(t['explicacion']); f.save(out)
    return len(f.doc)
