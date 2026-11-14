"""Saca los recursos del kit (fondos limpios, fichas, plantilla) de PDFs exportados de Camellot.

No hace falta tener capturas de la app: cada "Entrega Ejercicio" lleva el dibujo como imagen,
así que con varias exportaciones se reconstruye el fondo vacío.

    python extraer_recursos.py dibujos  carpeta_salida  pdf1.pdf pdf2.pdf ...   # extrae los dibujos de los PDFs
    python extraer_recursos.py mediana  fondo.png  dibujo1.png dibujo2.png ...  # fondo limpio (>=3 dibujos del mismo fondo)
    python extraer_recursos.py limpiar  dibujo.png fondo.png                    # fondo limpio desde 1 dibujo (inpainting)
    python extraer_recursos.py ficha    dibujo.png x0 y0 x1 y1 salida.png       # recorta una ficha (jugador, cono...) con transparencia
    python extraer_recursos.py plantilla ejemplo_exportado.pdf plantilla.pdf    # cabecera + bandas rojas en un PDF limpio

Requisitos: pip install pymupdf pillow numpy  (y opencv-python-headless para 'limpiar')
"""
import sys, os, hashlib
import numpy as np
from PIL import Image

G = np.array([128, 187, 59.])            # verde de la app
WT = np.array([255, 255, 255.])


def _a_paleta(rgb):
    """Proyecta cada píxel sobre la recta verde-blanco: devuelve t (0 = verde, 1 = línea blanca) y el residuo."""
    d = WT - G
    t = np.clip(((rgb - G) @ d) / (d @ d), 0, 1)
    resid = np.sqrt((((G + t[..., None] * d) - rgb) ** 2).sum(-1))
    return t, resid


def dibujos(outdir, pdfs):
    import pymupdf as fitz
    os.makedirs(outdir, exist_ok=True); vistos = set()
    for src in pdfs:
        doc = fitz.open(src)
        for pn, page in enumerate(doc):
            for im in page.get_images(full=True):
                if im[2] < 500:          # logos y bandas son pequeños
                    continue
                pix = fitz.Pixmap(doc, im[0])
                if pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                h = hashlib.md5(pix.samples).hexdigest()
                if h in vistos:
                    continue
                vistos.add(h)
                fn = os.path.join(outdir, f'{os.path.splitext(os.path.basename(src))[0][:40]}_p{pn + 1}_{pix.width}x{pix.height}.png')
                pix.save(fn); print(fn)
                if im[1]:                 # máscara de transparencia (esquinas del medio campo)
                    fitz.Pixmap(doc, im[1]).save(fn.replace('.png', '_mascara.png'))


def mediana(out, pngs):
    A = np.stack([np.asarray(Image.open(p).convert('RGB')).astype(float) for p in pngs])
    M = np.median(A, 0)
    t, resid = _a_paleta(M)
    t[resid > 40] = 0                    # restos de objetos que se repiten en varios dibujos
    Image.fromarray((G + t[..., None] * (WT - G)).astype(np.uint8)).save(out)
    print(out, '-> revisa que las líneas estén completas; si falta algún trozo, repásalo copiando el perfil de la línea')


def limpiar(src, out, zonas=()):
    import cv2
    rgb = np.asarray(Image.open(src).convert('RGB')).astype(float)
    t, resid = _a_paleta(rgb)
    obj = (resid > 25).astype(np.uint8)
    for (x0, y0, x1, y1) in zonas:       # objetos blancos (porterías, balones) que hay que borrar a mano
        obj[y0:y1, x0:x1] = 1
    obj = cv2.dilate(obj, np.ones((5, 5), np.uint8), iterations=2)
    img = (G + t[..., None] * (WT - G)).astype(np.uint8)[:, :, ::-1].copy()
    res = cv2.inpaint(img, obj * 255, 5, cv2.INPAINT_TELEA)[:, :, ::-1].astype(float)
    t2, _ = _a_paleta(res)
    Image.fromarray((G + t2[..., None] * (WT - G)).astype(np.uint8)).save(out)
    print(out, '-> los círculos y arcos pueden quedar borrosos donde había jugadores: redibújalos ajustando un círculo')


def ficha(src, box, out):
    im = np.asarray(Image.open(src).convert('RGB').crop(box)).astype(float)
    a = np.clip((np.sqrt(((im - G) ** 2).sum(-1)) - 10) / 40, 0, 1)
    fg = np.clip((im - (1 - a[..., None]) * G) / np.maximum(a[..., None], 1e-3), 0, 255)
    res = Image.fromarray(np.dstack([fg, a * 255]).astype(np.uint8), 'RGBA')
    res = res.crop(res.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()); res.save(out)
    print(out, res.size, '-> comprueba que no se ha colado una línea negra de zona en el borde')


def plantilla(src, out):
    import pymupdf as fitz
    ej = fitz.open(src); p0 = ej[0]
    rojos = [d['rect'] for d in p0.get_drawings()
             if d.get('fill') and abs(d['fill'][0] - 0.894) < .03 and d['fill'][1] < .05 and 29 < d['rect'].height < 32]
    rojos = sorted({(round(r.y0, 1), r) for r in rojos}, key=lambda k: k[0])
    clips = [fitz.Rect(0, 0, 595.28, 50)] + [fitz.Rect(20, r.y0, 575.28, r.y0 + 30.688) for _, r in rojos]
    doc = fitz.open(); pg = doc.new_page(width=595.28, height=841.89)
    for c in clips:
        pg.show_pdf_page(c, ej, 0, clip=c)
    doc.save(out, garbage=3, deflate=True)
    print(out, 'bandas en y =', [round(c.y0, 1) for c in clips[1:]], '(si no son 60 / 321.7 / 767.4, actualiza CLIPS en camellot.py)')


if __name__ == '__main__':
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == 'dibujos': dibujos(args[0], args[1:])
    elif cmd == 'mediana': mediana(args[0], args[1:])
    elif cmd == 'limpiar': limpiar(args[0], args[1])
    elif cmd == 'ficha': ficha(args[0], tuple(int(v) for v in args[1:5]), args[5])
    elif cmd == 'plantilla': plantilla(args[0], args[1])
    else: print(__doc__)
