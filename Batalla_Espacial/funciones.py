
from variables import TAMANO_TABLERO
import random

def generar_coordenadas_aleatorias():
    return random.randint(0, TAMANO_TABLERO - 1), random.randint(0, TAMANO_TABLERO - 1)