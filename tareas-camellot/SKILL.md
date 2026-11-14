---
name: "tareas-camellot"
description: "Crear fichas de tareas/ejercicios de fútbol en formato Camellot (ficha 'Entrega Ejercicio' de la plataforma del curso RFEF/UEFA B) con su dibujo sobre los fondos y fichas oficiales."
---

# Tareas en formato Camellot

El usuario (entrenador/a en un curso RFEF, p. ej. UEFA B) entrega sus tareas de entrenamiento en la plataforma "Camellot", que exporta cada ejercicio como un PDF A4 llamado **"Entrega Ejercicio"** (y cada sesión como **"Entrega Sesión"**). Cuando pida "hacer tareas en formato Camellot", hay que reproducir ese PDF **idéntico**: misma geometría, mismos grises/blancos, misma tipografía (lo más cerca posible) y el dibujo hecho sobre los fondos y con las fichas de la aplicación.

## Reglas previas (comprobar SIEMPRE antes de generar nada)

1. **¿Sesión o tarea?** Leer lo que pide el enunciado o los criterios:
   - Si piden una **sesión** (p. ej. "1 sesión de entrenamiento con mínimo cuatro tareas", microciclos, "sesiones") → formato **"Entrega Sesión"**: cabecera ENTREGA SESIÓN, banda Detalles de la sesión (título, tiempo, nº jugadoras, materiales, objetivos, lesionados/ausencias), una banda Detalles de la sección por parte (Calentamiento, Parte Principal…) y dentro los ejercicios. Nunca como fichas sueltas "Entrega Ejercicio".
   - Si piden **tareas/ejercicios** sueltos ("8 tareas", "1 tarea condicional", "graba una tarea") → formato **"Entrega Ejercicio"**, una ficha por tarea.
   - Si hay duda, preguntar al usuario antes de hacer nada.
2. **¿Ya está entregada y aprobada?** Si la tarea o la sesión viene de un trabajo anterior ya aprobado (p. ej. en el proyecto final, todo lo que lleva "(PROYECTO ÁREA ENTRENADOR / ENTRENAMIENTO / JUGADOR Y ENTORNO / PARTIDO)"), **no se rehace**: se insertan directamente las páginas originales de ese PDF tal como se entregaron (mismo texto, mismo dibujo, mismo formato), para que el tribunal no vea diferencias. Lo mismo para el texto de esos apartados (p. ej. ejercicios preventivos): copiarlo con la misma estructura con la que se entregó.
3. **Dentro de un documento**, las fichas Camellot van **a página completa**, como si se hubieran juntado dos PDFs: página A4 propia, sin cabecera/pie/márgenes del documento ni número visible, nunca como una captura pegada dentro de una página con texto. En un Word (plantilla RFEF) se hace con una sección propia de márgenes 0 y cabecera/pie vacíos (imagen 21×29,7 cm), y en el PDF final se sustituyen esas páginas por las páginas vectoriales originales con `fitz.insert_pdf`. Fichas seguidas van en la misma sección, sin páginas de texto en medio.
4. **Vídeos**: en los proyectos los vídeos van **adjuntos**, no como enlaces: citar "Vídeo adjunto: Vídeo N – descripción".

## 0. Material necesario (pedirlo si no está)

Los ficheros no se guardan entre sesiones. Al empezar, comprueba si están en los adjuntos o en una carpeta del ordenador (si la sesión está vinculada, busca una carpeta tipo `Camellot`). Si faltan, pídelos en un solo mensaje y sugiere que los guarde todos juntos en una carpeta `Camellot` para reutilizarlos:

1. **Un PDF de ejemplo exportado de la plataforma** (p. ej. "Jugadores y Entorno - Salida de balón"; para sesiones, un "Entrega Sesión"). De él se copian en vectorial la cabecera roja con logo y las bandas rojas de sección, para que salgan exactas.
2. **Los 3 fondos** (capturas PNG de la app): campo entero, medio campo (portería a la izquierda) y cuadrado libre (con cruz central).
3. **Las fichas** (capturas PNG sobre el verde de la app): jugadora roja, amarilla, azul y negra (portera), balón, cono pequeño (naranja), cono grande (salmón), pica, valla, escalera, miniportería y portería grande. Si las hay, también flechas (pase, movimiento, conducción) y maniquí.
4. **La tarea**: captura/PDF de la otra app o descripción, y si es posible espacio y tiempo.

## 1. Formato de la ficha (no improvisar)

Orden: cabecera "ENTREGA EJERCICIO" → banda **DETALLES DEL EJERCICIO** → tabla 1 → tabla 2 → tabla 3 → banda **DESCRIPCIÓN GRÁFICA** + dibujo → banda **CONSIGNA / EXPLICACIÓN** + texto. Nada más (sin filas extra de Complejidad/Dinámica).

Geometría en puntos (A4 595.28×841.89), medida del PDF real:
- Cabecera roja `#E4002A` 0–50 pt; logo en (20,10,50,40); título en fuente ancha (LaRoja Ancha Bold 16 pt). Se copia del PDF de ejemplo.
- Bandas rojas: x 20–575.28, alto 30.69, esquinas superiores redondeadas, texto LaRoja Ancha 8 pt blanco en mayúsculas. Se copian del ejemplo.
- **Tabla 1** (pegada bajo la banda): columna de etiquetas **gris `#F4F4F4`** de x 21 a 131.66; valores en **blanco**. Filas de 25 pt; Objetivos = 12·n + 10 pt. Texto etiqueta en x=31, valor en x=142.66, baseline fila +15.39 (Objetivos: valores +14.39, etiqueta +15.89).
- **Tabla 2** (6 pt debajo): 4 columnas iguales; fila de etiquetas **gris** (25 pt): Espacio · Tiempo · Situación de Juego · Coordinación; fila de valores **blanca** (25 pt). Texto en x = columna + 10, baseline +15.89.
- **Tabla 3** (6 pt debajo): 2 columnas; etiquetas grises Habilidades Coordinativas · Intención / Acción Táctica; valores en blanco.
- Líneas negras finas (1 pt), solo las **esquinas inferiores** de cada bloque redondeadas (r=4).
- 11 pt hasta la banda de Descripción gráfica; imagen centrada, máximo **440×400 pt**, 2 pt bajo la banda, marco cerrando 3 pt por debajo.
- 10 pt hasta la banda de Consigna; texto x=31, ancho 535.7, 10 pt, interlineado 12, padding superior 10 e inferior 11.
- Si el texto no cabe con al menos 2 líneas, pasa **entero** a la página siguiente (marco lateral abierto hasta el pie, nueva cabecera, el texto continúa desde y=60). La ficha puede ocupar 2 páginas.
- Tipografía del texto: la plataforma usa *Intrum Sans* (no disponible completa). Usar **Figtree Regular 10 pt** (la más parecida). Descargar de `https://raw.githubusercontent.com/google/fonts/main/ofl/figtree/Figtree%5Bwght%5D.ttf` e instanciar a wght=400 con `fontTools.varLib.instancer`.

## 2. Contenido de los campos

- **Título**: "<Bloque> - <nombre de la tarea>" (estilo "Jugadores y Entorno - Salida de balón"; para microciclos se usó "Microciclo - …"). Confirmar el prefijo con el usuario si no está claro.
- **Objetivos**: en **MAYÚSCULAS**, uno por línea, frases cortas, sin guiones.
- **Tiempo** con apóstrofo: `20'`. **Espacio** como `40x30` (estimar por el dibujo si no lo da y avisar).
- Campos de lista cerrada (uno solo por campo; si nada encaja, se puede dejar vacío como en sus ejemplos):
  - Estrategia: Acciones a Balón Parado, Acciones combinadas, Circuito, Conservación, Juego Adaptado al Futbol, Juego de Posición, Juego de Posición Específico, Oleadas, Partido, Posesión, Rueda de Pases, Situaciones Reducidas, Trabajo de líneas.
  - Situación de Juego: Estructura Completa, Intersectorial, Sectorial.
  - Coordinación: Coordinación equipo, Coordinación Jugador/a, Coordinación Jugadores/as.
  - Habilidades Coordinativas: Actuación por Desmarcación, Arrancar/Frenar, Cambiar de Dirección, Conducción, Control, Despejes, Desplazamientos, Disparos, Entrada, Equilibrarse, Giros, Intercepción, Pase, Protección, Regate, Saltos.
  - Intención / Acción Táctica: 1v1, 2v1, 2v2, 3v3, 4v4, ABP Defensiva, ABP Ofensiva, Amplitud, Apoyos, Ataque Organizado, Cobertura, Conservar, Contraataque, Defensa Inicio de Juego, Defensa de Juego Directo, Defensa Organizada, Desmarques, Dividir, Evitar Progresión, Fase Defensiva, Fase Ofensiva, Fijar, Finalizar, Inicio de Juego, Juego Directo, Mantener, Marcaje, Orientar, Permuta, Presionar, Primer Atacante, Primer Defensor, Profundidad, Progresar, Proteger Portería, Recuperar, Reinicio de Juego, Replegar, Segundo Atacante, Segundo Defensor, Temporizar, Tercer Atacante, Tercer Defensor.
  - (La plataforma también tiene Complejidad: Baja/Media/Alta/Muy Alta y Dinámica: ADM, Extensiva, Fuerza, Intensiva (acción), Extensiva (interacción), Recuperación, Resistencia, Velocidad, pero **no salen en el PDF**.)
- **Consigna / Explicación**: descripción de la tarea en castellano, en femenino si el equipo es femenino (jugadoras, compañera), preguntando si no está claro, con párrafos separados por salto de línea; consignas ofensivas/defensivas al final.

## 3. El dibujo

Siempre sobre **uno de los 3 fondos completos** (no recortes): cuadrado libre (rondos, micro, posesiones), medio campo (finalización, oleadas, defensa de área, juegos de situación), campo entero (partidos 11c11). El medio campo tiene la portería a la izquierda: si la tarea viene con la portería arriba, girarla 90°. Las fichas se pegan como sprites recortados de sus capturas; flechas: pase = continua, movimiento = discontinua, conducción = ondulada (colores negro/rojo/naranja/blanco según el original). Transcribir posiciones del gráfico original en coordenadas normalizadas y comparar lado a lado antes de entregar. Porterías: la red (roja) mira hacia fuera del campo y el palo (blanco) hacia el juego.

### 3a. Recortar las fichas (sobre verde)
```python
from PIL import Image; import numpy as np
def recortar(src, dst):
    im = np.asarray(Image.open(src).convert('RGB')).astype(float)
    bg = np.median(np.concatenate([im[0], im[-1], im[:,0], im[:,-1]]), axis=0)
    a = np.clip((np.sqrt(((im-bg)**2).sum(-1)) - 10) / 40, 0, 1)
    fg = np.clip((im - (1-a[...,None])*bg) / np.maximum(a[...,None], 1e-3), 0, 255)
    out = Image.fromarray(np.dstack([fg, a*255]).astype(np.uint8), 'RGBA')
    out.crop(out.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()).save(dst)
# nombres: rojo, amarillo, azul, negro, balon, cono, cono_grande, pica, valla, escalera, mini, porteria
```

### 3b. Lienzo (matplotlib)
Medir en cada fondo la caja de líneas (px) buscando columnas/filas con muchos píxeles blancos y recortar el marco no verde (verde ≈ RGB 128,187,59). Valores de referencia (capturas de ejemplo; medir siempre en las del usuario): full (43,27,1081,682), square (37,37,674,675), half (48,37,685,675).
```python
import numpy as np, os, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from PIL import Image
S = 2
ACOL = {'negro':'#1A1A1A','rojo':'#E0322B','naranja':'#F4B26A','blanco':'#FFFFFF','azul':'#2457D6'}
class Lienzo:
    # base: 'square' (x,y 0..1), 'full' (x a lo largo, 0 = portería izq.), 'half' (escrito en vertical: x ancho, y 0 = gol .. 1 = medio campo)
    def __init__(self, base, fondo_png, box, sprites_dir):
        self.base, self.sd = base, sprites_dir
        im = Image.open(fondo_png).convert('RGB'); a = np.asarray(im).astype(int)
        g = (abs(a[...,0]-128)<12)&(abs(a[...,1]-187)<12)&(abs(a[...,2]-59)<14); ys, xs = np.where(g)
        x0, y0 = xs.min(), ys.min(); im = im.crop((x0, y0, xs.max()+1, ys.max()+1))
        self.box = (box[0]-x0, box[1]-y0, box[2]-x0, box[3]-y0)
        w, h = im.size; im = im.resize((w*S, h*S), Image.LANCZOS); self.W, self.H = w*S, h*S
        self.fig = plt.figure(figsize=(self.W/100, self.H/100), dpi=100); self.ax = self.fig.add_axes([0,0,1,1])
        self.ax.imshow(im, extent=(0, self.W, self.H, 0)); self.ax.axis('off')
        self.r = 17*S if base != 'full' else 13*S; self.tf = None; self._lim()
    def _lim(self): self.ax.set_xlim(0, self.W); self.ax.set_ylim(self.H, 0)
    def P(self, x, y):
        if self.tf: x, y = self.tf(x, y)
        u, v = (y, 1-x) if self.base == 'half' else (x, y)
        b = self.box; return (b[0]+u*(b[2]-b[0]))*S, (b[1]+v*(b[3]-b[1]))*S
    def _paste(self, name, cx, cy, w=None, h=None, rot=0, z=6):
        im = Image.open(os.path.join(self.sd, name+'.png')).convert('RGBA')
        if rot: im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
        iw, ih = im.size; w = w or h*iw/ih; h = h or w*ih/iw
        self.ax.imshow(np.asarray(im), extent=(cx-w/2, cx+w/2, cy+h/2, cy-h/2), zorder=z); self._lim()
    def j(self, x, y, c='rojo', k=1.0): self._paste(c, *self.P(x, y), w=2*self.r*k)
    def b(self, x, y): self._paste('balon', *self.P(x, y), w=self.r, z=11)
    def cono(self, x, y): self._paste('cono', *self.P(x, y), w=self.r*.85, z=4)
    def cono_grande(self, x, y): self._paste('cono_grande', *self.P(x, y), w=self.r*1.7, z=4)
    def pica(self, x, y): self._paste('pica', *self.P(x, y), h=self.r*2, z=4)
    def valla(self, x, y, vertical=False): self._paste('valla', *self.P(x, y), w=None if vertical else self.r*2, h=self.r*2 if vertical else None, rot=90 if vertical else 0, z=4)
    def mini(self, x, y, orient='h', k=1.0, name='mini', ancho=3.6):
        horiz = (orient == 'h') != (self.base == 'half'); w = self.r*ancho*k
        self._paste(name, *self.P(x, y), w=w if horiz else None, h=None if horiz else w, rot=0 if horiz else 90, z=4)
    def porteria(self, x, y, orient='h', k=1.0): self.mini(x, y, orient, k, 'porteria', 7)
    def escalera(self, x0, y0, x1, y1):
        a, c = np.array(self.P(x0, y0)), np.array(self.P(x1, y1)); v = c-a; n = np.linalg.norm(v)
        im = Image.open(os.path.join(self.sd, 'escalera.png')).convert('RGBA'); ih = im.size[1]; th = self.r*1.1
        im = im.resize((max(2, int(n/th*ih)), ih)).rotate(np.degrees(np.arctan2(-v[1], v[0])), expand=True)
        m = (a+c)/2; s = th/ih; rw, rh = im.size
        self.ax.imshow(np.asarray(im), extent=(m[0]-rw*s/2, m[0]+rw*s/2, m[1]+rh*s/2, m[1]-rh*s/2), zorder=4); self._lim()
    def zona(self, x0, y0, x1, y1, lw=2.0):
        a, c = self.P(x0, y0), self.P(x1, y1)
        self.ax.add_patch(FancyBboxPatch((min(a[0],c[0]), min(a[1],c[1])), abs(c[0]-a[0]), abs(c[1]-a[1]), boxstyle=f'round,pad=0,rounding_size={3*S}', fill=False, edgecolor='#1A1A1A', lw=lw*S, zorder=3))
    def linea(self, x0, y0, x1, y1, c='negro', lw=1.6):
        a, d = self.P(x0, y0), self.P(x1, y1); self.ax.plot([a[0], d[0]], [a[1], d[1]], color=ACOL.get(c, c), lw=lw*S, zorder=3)
    def _arrow(self, a, d, c, ls='-', lw=1.5):
        self.ax.add_patch(FancyArrowPatch(a, d, arrowstyle='-|>', mutation_scale=9*S, lw=lw*S, ls=ls, color=ACOL.get(c, c), zorder=13, shrinkA=0, shrinkB=0))
    def pase(self, x0, y0, x1, y1, c='negro'): self._arrow(self.P(x0, y0), self.P(x1, y1), c)
    def mov(self, x0, y0, x1, y1, c='negro'): self._arrow(self.P(x0, y0), self.P(x1, y1), c, ls=(0, (3, 2)))
    def cond(self, x0, y0, x1, y1, c='negro'):
        a, d = np.array(self.P(x0, y0)), np.array(self.P(x1, y1)); v = d-a; n = np.linalg.norm(v); u = v/n; p = np.array([-u[1], u[0]])
        t = np.linspace(0, 1, 300); k = max(2, int(n/(self.r*1.4)))
        pts = a + np.outer(t*n*.88, u) + np.outer(self.r*.38*np.sin(t*k*2*np.pi), p)
        self.ax.plot(pts[:,0], pts[:,1], color=ACOL.get(c, c), lw=1.4*S, zorder=13); self._arrow(tuple(pts[-1]), tuple(d), c, lw=1.4)
    def texto(self, x, y, s, k=1.0):
        cx, cy = self.P(x, y); self.ax.text(cx, cy, s, ha='center', va='center', fontsize=self.r*1.9*k*.72, fontweight='bold', color='#1A1A1A', zorder=14)
    def guardar(self, path): self.fig.savefig(path, dpi=100); plt.close(self.fig)
```
Para tareas que en el original ocupan solo una esquina del cuadrado, ampliarlas con `L.tf = lambda x, y: (.05 + 1.8*x, .05 + 1.8*y)`.

## 4. Generar la ficha PDF (PyMuPDF)
`pip install --break-system-packages pymupdf` si falta. La cabecera y las bandas se copian con `show_pdf_page(..., clip=...)` del PDF de ejemplo (recortes de la página 0 del ejemplo "Salida de balón": cabecera (0,0,595.28,50); bandas detalles (20,60,575.28,90.688), gráfica (20,321.7,575.28,352.4), consigna (20,767.4,575.28,798.1); si el ejemplo es otro, localizar las bandas con `page.get_drawings()` buscando rects rellenos de rojo (0.894,0,0.165) de alto 30.69). Para "Entrega Sesión" se usa la misma maquetación con la cabecera y las bandas (Detalles de la sesión, Detalles de la sección, Detalles del ejercicio, Descripción gráfica, Consigna) copiadas de un PDF "Entrega Sesión" real; las páginas de continuación empiezan en y=65.
```python
import fitz
GREY=(0.95686,)*3; BLACK=(0,0,0); X0,X1=20.0,575.28; LH=12.0; FS=10.0; BAND_H=30.688; BOT=841.89-10
class Ficha:
    def __init__(self, template_pdf, font_ttf, clips):
        self.doc=fitz.open(); self.tpl=fitz.open(template_pdf); self.ff=font_ttf; self.font=fitz.Font(fontfile=font_ttf); self.clips=clips; self.new_page()
    def new_page(self):
        self.page=self.doc.new_page(width=595.28, height=841.89); self.page.insert_font(fontname='FIG', fontfile=self.ff)
        self.page.show_pdf_page(self.clips['header'], self.tpl, 0, clip=self.clips['header']); self.y=60.0
    def text(self, x, bl, s): self.page.insert_text((x, bl), s, fontname='FIG', fontsize=FS, color=BLACK)
    def wrap(self, s, width):
        out=[]
        for para in s.split('\n'):
            cur=''
            for w in para.split(' '):
                t=(cur+' '+w) if cur else w
                if self.font.text_length(t, fontsize=FS)<=width: cur=t
                else:
                    if cur: out.append(cur)
                    cur=w
            out.append(cur)
        return out
    def outline(self, top, bottom):
        sh=self.page.new_shape(); r=4.0; L=X0+.5; R=X1-.5; B=bottom-.5
        sh.draw_line((R,top),(R,B-r)); sh.draw_bezier((R,B-r),(R,B-r+2.209),(R-1.791,B),(R-r,B)); sh.draw_line((R-r,B),(L+r,B))
        sh.draw_bezier((L+r,B),(L+1.791,B),(L,B-1.791),(L,B-r)); sh.draw_line((L,B-r),(L,top)); sh.finish(color=BLACK, width=1.0, closePath=False); sh.commit()
    def hline(self, x0, x1, y): self.page.draw_line((x0,y),(x1,y), color=BLACK, width=1.0)
    def vline(self, x, y0, y1): self.page.draw_line((x,y0),(x,y1), color=BLACK, width=1.0)
    def grey(self, x0, y0, x1, y1): self.page.draw_rect(fitz.Rect(x0,y0,x1,y1), color=None, fill=GREY, width=0)
    def band(self, key):
        self.page.show_pdf_page(fitz.Rect(X0, self.y, X1, self.y+BAND_H), self.tpl, 0, clip=self.clips[key]); self.y+=BAND_H
    def detalles(self, titulo, estrategia, objetivos):
        self.band('detalles'); top=self.y; LX=131.656
        rows=[([titulo],25.0,15.39), ([estrategia],25.0,15.39), (objetivos, max(25.0, LH*len(objetivos)+10), 14.39 if len(objetivos)>1 else 15.39)]
        bottom=top+sum(h for _,h,_ in rows)+1; self.outline(top, bottom); self.grey(21.0, top, LX, bottom-1); y=top
        for k,((vals,h,b0),lab) in enumerate(zip(rows, ['Título','Estrategia','Objetivos'])):
            if k: self.hline(21.0, LX, y); self.hline(LX, X1-1, y)
            self.vline(LX, y, y+h); self.text(31.0, y+(15.89 if lab=='Objetivos' and len(vals)>1 else 15.39), lab)
            for i,v in enumerate(vals): self.text(142.656, y+b0+i*LH, v)
            y+=h
        self.y=y
    def tabla(self, headers, values):
        top=self.y+6; n=len(headers); w=(574.28-21.0)/n
        self.grey(21.0, top, 574.28, top+25); self.outline(top, top+51)
        self.page.draw_line((21.0, top+.5), (574.28, top+.5), color=BLACK, width=1.0); self.hline(21.0, 574.28, top+25)
        for i,(hd,v) in enumerate(zip(headers, values)):
            x0=21.0+i*w
            if i<n-1: self.vline(x0+w, top, top+50)
            self.text(x0+10, top+15.89, hd)
            if v: self.text(x0+10, top+40.89, v)
        self.y=top+50
    def grafica(self, img, maxw=440.0, maxh=400.0):
        self.y+=11; pix=fitz.Pixmap(img); s=min(maxw/pix.width, maxh/pix.height); iw, ih = pix.width*s, pix.height*s
        if self.y+BAND_H+ih+5>BOT: self.new_page()
        self.band('grafica'); it=self.y+2
        self.page.insert_image(fitz.Rect((595.28-iw)/2, it, (595.28+iw)/2, it+ih), filename=img)
        self.outline(self.y, it+ih+3); self.y=it+ih+3
    def consigna(self, texto):
        self.y+=10; lines=self.wrap(texto, 535.7)
        if self.y+BAND_H+33>BOT: self.new_page()
        self.band('consigna'); first=True
        while lines:
            top=self.y; pad=10 if first else 0; avail=int((BOT-11-(top+pad))//LH)
            if avail<2:
                self.vline(X0+.5, top, BOT); self.vline(X1-.5, top, BOT); self.new_page(); first=False; continue
            chunk, lines = lines[:avail], lines[avail:]
            for i,l in enumerate(chunk): self.text(31.0, top+pad+9.42+i*LH, l)
            if lines: self.vline(X0+.5, top, BOT); self.vline(X1-.5, top, BOT); self.new_page(); first=False
            else: self.outline(top, top+pad+LH*len(chunk)+11); self.y=top+pad+LH*len(chunk)+11
    def save(self, out): self.doc.save(out, garbage=3, deflate=True)

def ficha(t, img, out, template_pdf, font_ttf, clips):
    f=Ficha(template_pdf, font_ttf, clips)
    f.detalles(t['titulo'], t['estrategia'], t['objetivos'])
    f.tabla(['Espacio','Tiempo','Situación de Juego','Coordinación'], [t['espacio'], t['tiempo'], t['situacion'], t['coordinacion']])
    f.tabla(['Habilidades Coordinativas','Intención / Acción Táctica'], [t['habilidades'], t['intencion']])
    f.grafica(img); f.consigna(t['explicacion']); f.save(out)
```

## 5. Flujo de trabajo
1. Aplicar las **reglas previas**: decidir sesión o tarea según el enunciado y comprobar si ya existe una versión entregada y aprobada (si existe, usar sus páginas originales y no seguir con los pasos siguientes).
2. Reunir el material (sección 0) y la información de las tareas.
3. Si hay varias tareas, hacer **primero una** y enseñarla para validar formato y dibujo antes de hacer el resto.
4. Para cada tarea: dibujo (sección 3) → comparar con el gráfico original lado a lado → ficha (sección 4) → renderizar con `pdftoppm` y revisar junto a un ejemplo real de la plataforma.
5. Si van dentro de un documento (microciclo, proyecto final UEFA B), intercalarlas a **página completa** con `fitz.insert_pdf` (páginas originales de cada sesión tal cual y detrás sus ejercicios; informes en su sitio), nunca como capturas dentro de una página de texto.
6. Entregar el PDF y decir en una línea qué campos se han decidido (lista cerrada, espacio estimado) para que los revise.
