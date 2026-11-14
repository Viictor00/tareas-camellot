# Tareas Camellot — skill para Claude

Skill para que Claude genere fichas de tareas de fútbol con el formato de la plataforma **Camellot**, la que se usa en los cursos de entrenador RFEF (UEFA C, UEFA B…). Hace la ficha **"Entrega Ejercicio"** (y también la **"Entrega Sesión"**) como un PDF A4 casi idéntico al que exporta la plataforma, con el dibujo de la tarea sobre los fondos y con las fichas de la app.

## Qué hace

- Rellena los campos de la ficha: título, estrategia, objetivos, espacio, tiempo, situación de juego, coordinación, habilidades coordinativas, intención táctica y consigna. Usa las listas cerradas de la plataforma.
- Dibuja la tarea sobre el fondo que toque (campo entero, medio campo o cuadrado libre), con jugadores/as, balones, conos, picas, vallas, porterías y flechas de pase, movimiento y conducción.
- Monta el PDF con la misma geometría, colores y maquetación que el original.
- Puede meter las fichas a página completa dentro de un documento más grande, como un microciclo o un proyecto.

## Qué tienes que aportar tú

Este repositorio **no incluye material de la plataforma** (logos, fondos ni fichas). Cuando uses la skill, Claude te pedirá:

1. Un PDF de ejemplo exportado de Camellot (una "Entrega Ejercicio" y, si vas a hacer sesiones, una "Entrega Sesión").
2. Capturas PNG de los 3 fondos: campo entero, medio campo y cuadrado libre.
3. Capturas PNG de las fichas sobre el verde de la app: jugador/a rojo, amarillo, azul y negro (portero/a), balón, conos, pica, valla, escalera, miniportería y portería.
4. La tarea que quieres pasar al formato: una captura, un dibujo o una descripción.

Consejo: guárdalo todo en una carpeta `Camellot` para reutilizarlo.

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
└── SKILL.md            # instrucciones de la skill
tareas-camellot.zip     # la misma carpeta comprimida, lista para subir a Claude
```

## Aviso

Proyecto personal, sin relación con la RFEF ni con la plataforma Camellot. Los nombres de la plataforma se usan solo para describir el formato. Revisa siempre la ficha antes de entregarla.
