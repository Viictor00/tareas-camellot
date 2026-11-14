"""Ejemplo completo: Tarea 1 del Proyecto Área Entrenador (ajuste de pase con mensaje).
Ejecutar desde la carpeta scripts:  python ejemplo_tarea.py
Genera dibujo_ejemplo.png y ficha_ejemplo.pdf en la carpeta desde la que se ejecuta
"""
import os
from camellot import Lienzo, ficha

OUT = os.getcwd()   # la carpeta de la skill puede ser de solo lectura: se escribe donde se ejecuta

# --- dibujo (medio campo: x = ancho, y = 0 gol .. 1 medio campo) ---
L = Lienzo('medio')
L.zona(.292, .310, .711, .783)
L.mini(.5, .330, abre='derecha')          # miniportería con la boca hacia el juego
L.j(.501, .515, 'rojo')                     # receptor, de espaldas a la miniportería
L.j(.501, .706, 'rojo')                     # jugador que inicia, de cara
L.j(.636, .433, 'amarillo'); L.j(.367, .433, 'amarillo')   # defensores a los lados
L.b(.476, .542)
L.pase(.512, .677, .512, .544)              # ida
L.pase(.490, .544, .490, .677)              # vuelta
L.mov(.616, .453, .532, .502)               # salta uno de los dos defensores
img = os.path.join(OUT, 'dibujo_ejemplo.png'); L.guardar(img)

# --- ficha ---
datos = dict(
    titulo='Entrenador - Ajuste de pase: pase con mensaje',
    estrategia='Situaciones Reducidas',
    objetivos=['PASE CON TENSIÓN Y DIRECCIÓN QUE INFORME AL RECEPTOR', 'CONTROL ORIENTADO PARA GIRARSE BAJO PRESIÓN',
               'ESCANEAR ANTES DE RECIBIR', 'COMUNICACIÓN NO VERBAL A TRAVÉS DEL PASE'],
    espacio='15x15', tiempo="15'", situacion='Sectorial', coordinacion='Coordinación Jugadores/as',
    habilidades='Pase', intencion='2v1',
    explicacion=(
        "Grupos de cuatro jugadores en varias estaciones a la vez, con rotación de roles. Dos atacantes se colocan uno frente al otro: "
        "el jugador que inicia, de cara a la miniportería, y el receptor, de espaldas a ella. A los lados del receptor se sitúan dos defensores.\n"
        "La acción empieza con un pase de ida y vuelta. Cuando el balón vuelve al jugador que inicia y sale el siguiente pase, uno de los dos "
        "defensores salta a presionar al receptor. Los defensores deciden quién salta solo con señas y pueden hacer fintas para engañar. "
        "El receptor tiene que hacer un control orientado hacia el lado libre, girarse y marcar en la miniportería.\n"
        "Norma principal: está prohibido hablar. Toda la información tiene que ir en el pase. Los defensores no pueden saltar hasta que sale el pase."),
)
pdf = os.path.join(OUT, 'ficha_ejemplo.pdf')
print('páginas:', ficha(datos, img, pdf))
