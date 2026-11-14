# Tareas Camellot — skill para Claude

Skill para que Claude genere fichas de tareas de fútbol con el formato de la plataforma **Camellot**, la que se usa en los cursos de entrenador RFEF (UEFA C, UEFA B…). Hace la ficha **"Entrega Ejercicio"** (y también la **"Entrega Sesión"**) como un PDF A4 casi idéntico al que exporta la plataforma, con el dibujo de la tarea sobre los fondos y con las fichas de la app.

## Qué hace

- Rellena los campos de la ficha: título, estrategia, objetivos, espacio, tiempo, situación de juego, coordinación, habilidades coordinativas, intención táctica y consigna. Usa las listas cerradas de la plataforma.
- Dibuja la tarea sobre el fondo que toque (campo entero, medio campo o cuadrado libre), con jugadores/as, balones, conos, picas, vallas, porterías y flechas de pase, movimiento y conducción.
- Monta el PDF con la misma geometría, colores y maquetación que el original.
- Puede meter las fichas a página completa dentro de un documento más grande, como un microciclo o un proyecto.

## Qué incluye

La skill lleva todo el material para hacer los gráficos y la ficha: plantilla (cabecera y bandas), fondos limpios (campo entero, medio campo y cuadrado), fichas (jugadores/as rojo, amarillo, azul y negro, balón, cono y miniportería) y la fuente. Solo hay que darle la tarea: una captura, un dibujo o una descripción.

Faltan por recortar la portería grande, el cono grande, la pica, la valla, la escalera y el maniquí: se añaden desde una captura o una ficha exportada con `scripts/extraer_recursos.py`.

## Instalación

### En Claude (web, escritorio o móvil)

1. Descarga [`tareas-camellot.zip`](tareas-camellot.zip) de este repositorio (botón **Download raw file**).
2. En Claude, comprueba que tienes activada la ejecución de código (**Settings → Capabilities → Code execution and file creation**).
3. Ve a **Customize → Skills**, pulsa **+**, **Create skill** y luego **Upload a skill**.
4. Sube el ZIP sin descomprimirlo. La skill aparecerá en tu lista y se puede activar o desactivar.

Después pídele, por ejemplo: *"Hazme esta tarea en formato Camellot"* y adjunta el material.

### En Claude Code

Copia la carpeta `tareas-camellot/` en `~/.claude/skills/` (para todos tus proyectos) o en `.claude/skills/` dentro de un proyecto.

## Estructura

```
tareas-camellot/
├── SKILL.md                    # instrucciones de la skill
├── plantilla/                  # cabecera y bandas rojas + una ficha exportada de ejemplo
├── fondos/                     # campo entero, medio campo (+ máscara) y cuadrado
├── fichas/                     # jugadores/as, balón, cono, miniportería
├── fuentes/                    # Figtree Regular
└── scripts/
    ├── camellot.py             # Lienzo (dibujo sobre los fondos) y ficha() (PDF "Entrega Ejercicio")
    ├── extraer_recursos.py     # amplía el material desde PDFs exportados o capturas
    └── ejemplo_tarea.py        # ejemplo completo: dibujo + ficha
tareas-camellot.zip             # la misma carpeta comprimida, lista para subir a Claude
```

Para usar los scripts fuera de Claude: `pip install pymupdf matplotlib pillow numpy` (y `opencv-python-headless` para `extraer_recursos.py limpiar`).

## Aviso

Proyecto personal y de uso privado, sin relación con la RFEF ni con la plataforma Camellot. El material gráfico incluido pertenece a sus propietarios. Revisa siempre la ficha antes de entregarla.
