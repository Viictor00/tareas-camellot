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

## 0. Material: incluido en la skill

La skill lleva todo lo necesario para dibujar y montar las fichas, en su propia carpeta (la ruta base de la skill):

```
tareas-camellot/
├── plantilla/plantilla_entrega_ejercicio.pdf   # cabecera + 3 bandas rojas en su sitio (y=60 / 321.7 / 767.4)
├── plantilla/ejemplo_entrega_ejercicio.pdf     # una exportación real, para comparar
├── fondos/medio_campo.png (+ mascara_medio_campo.png), cuadrado.png, campo_entero.png   # limpios, sin jugadores
├── fichas/rojo, amarillo, azul, negro (portero/a), balon, cono, mini (miniportería).png  # con transparencia
├── fuentes/Figtree-Regular.ttf
└── scripts/camellot.py, extraer_recursos.py, ejemplo_tarea.py
```

Uso: `sys.path.insert(0, '<ruta de la skill>/scripts')` y `from camellot import Lienzo, ficha`; los scripts encuentran solos los fondos, las fichas, la plantilla y la fuente (o los de otra carpeta con la variable de entorno `CAMELLOT_KIT`). Los archivos de salida se escriben en el directorio de trabajo, nunca dentro de la skill. No hace falta pedir capturas ni PDFs al usuario; solo **la tarea**: captura/PDF de la otra app o descripción, y si es posible espacio y tiempo.

**Fichas que faltan** (portería grande, cono grande, pica, valla, escalera, maniquí): pedir una captura sobre el verde de la app o una ficha exportada que la lleve y recortarla con `scripts/extraer_recursos.py` (ver abajo); guardarla junto al resto en la carpeta de trabajo y avisar al usuario para que la añada a la skill. Mientras tanto se puede dibujar con matplotlib imitando el estilo (y avisar).

`scripts/extraer_recursos.py` (para ampliar o regenerar el material desde PDFs exportados de Camellot, sin capturas):
- `plantilla ejemplo.pdf plantilla.pdf` → cabecera y bandas en vectorial (localiza las bandas rojas solo).
- `dibujos carpeta pdf1 pdf2 ...` → los dibujos de cada ficha (y la máscara de esquinas del medio campo).
- `mediana fondo.png dib1 dib2 dib3 ...` → fondo vacío con 3 o más dibujos del mismo fondo; `limpiar dib.png fondo.png` si solo hay uno (inpainting; luego redibujar círculos/arcos ajustando un círculo y repasar líneas copiando su perfil).
- `ficha dib.png x0 y0 x1 y1 salida.png` → recorta un jugador, cono, miniportería… sobre el verde (vigilar que no se cuele una línea negra de zona en el borde ni otra ficha pegada).

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

### 3a. Lienzo (`scripts/camellot.py`)
```python
import sys; sys.path.insert(0, '<ruta de la skill>/scripts')
from camellot import Lienzo
L = Lienzo('medio')                 # 'medio' | 'cuadrado' | 'entero'
L.zona(.29, .31, .71, .78)          # zona de trabajo (línea negra, esquinas redondeadas)
L.mini(.5, .33, abre='derecha')     # miniportería: 'abre' = hacia dónde mira la boca
L.j(.5, .52, 'rojo'); L.j(.64, .43, 'amarillo'); L.b(.48, .54)
L.pase(.51, .68, .51, .54); L.mov(.62, .45, .53, .50); L.cond(...); L.texto(x, y, '1')
L.guardar('dibujo.png')             # en 'medio' aplica la máscara de esquinas transparentes
```
- Coordenadas normalizadas 0–1 dentro de las líneas del campo. `cuadrado`/`entero`: x izquierda→derecha, y arriba→abajo. `medio`: se escribe en vertical, x = ancho, y = 0 en la línea de gol … 1 en el medio campo (la portería queda a la izquierda).
- El diccionario `FONDO` guarda para cada fondo la caja de líneas (px) y el radio de jugador. Si los fondos del usuario tienen otro tamaño, medir la caja (columnas/filas con muchos píxeles blancos) y el diámetro de una ficha en un dibujo real, y actualizarlo.
- Tareas que en el original ocupan solo una esquina: ampliarlas con `L.tf = lambda x, y: (.05 + 1.8*x, .05 + 1.8*y)`.
- `scripts/ejemplo_tarea.py` es un ejemplo completo (dibujo + ficha).

## 4. Generar la ficha PDF (`scripts/camellot.py`)
`pip install --break-system-packages pymupdf` si falta. `Ficha` implementa exactamente la geometría de la sección 1: copia la cabecera y las bandas de `plantilla/plantilla_entrega_ejercicio.pdf` (incluida) con `show_pdf_page(..., clip=...)` (`CLIPS`: cabecera (0,0,595.28,50); detalles (20,60,…,90.688); gráfica (20,321.7,…,352.4); consigna (20,767.4,…,798.1)), dibuja las tablas, mete el dibujo y parte la consigna en páginas si hace falta.
```python
from camellot import ficha
ficha(dict(titulo='Entrenador - …', estrategia='Situaciones Reducidas', objetivos=['…', '…'],
           espacio='15x15', tiempo="15'", situacion='Sectorial', coordinacion='Coordinación Jugadores/as',
           habilidades='Pase', intencion='2v1', explicacion='Párrafo 1\nPárrafo 2'),
      'dibujo.png', 'Entrenador - ….pdf')       # devuelve el nº de páginas
```
Si se cambia la plantilla por otra exportación y las bandas no están en 60 / 321.7 / 767.4, `extraer_recursos.py plantilla` lo avisa: actualizar `CLIPS`. Para "Entrega Sesión" se usa la misma maquetación con la cabecera y las bandas (Detalles de la sesión, Detalles de la sección, Detalles del ejercicio, Descripción gráfica, Consigna) copiadas de un PDF "Entrega Sesión" real; las páginas de continuación empiezan en y=65.

## 5. Flujo de trabajo
1. Aplicar las **reglas previas**: decidir sesión o tarea según el enunciado y comprobar si ya existe una versión entregada y aprobada (si existe, usar sus páginas originales y no seguir con los pasos siguientes).
2. Reunir la información de las tareas (el material gráfico ya va en la skill, sección 0).
3. Si hay varias tareas, hacer **primero una** y enseñarla para validar formato y dibujo antes de hacer el resto.
4. Para cada tarea: dibujo (sección 3) → comparar con el gráfico original lado a lado → ficha (sección 4) → renderizar con `pdftoppm` y revisar junto a un ejemplo real de la plataforma.
5. Si van dentro de un documento (microciclo, proyecto final UEFA B), intercalarlas a **página completa** con `fitz.insert_pdf` (páginas originales de cada sesión tal cual y detrás sus ejercicios; informes en su sitio), nunca como capturas dentro de una página de texto.
6. Entregar el PDF y decir en una línea qué campos se han decidido (lista cerrada, espacio estimado) para que los revise.
