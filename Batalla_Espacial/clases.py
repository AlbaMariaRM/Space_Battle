
import numpy as np
from variables import TAMANO_TABLERO, NAVES
import random

class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.dimensiones = TAMANO_TABLERO
        self.naves = NAVES
        self.tablero = np.zeros((self.dimensiones, self.dimensiones), dtype = int)
        self.tablero_impactos = np.zeros((self.dimensiones, self.dimensiones), dtype = int)
        self.nave_vidas = {nombre: eslora for nombre, eslora in self.naves.items()}
        self.posiciones_naves = {}
        self.coordenadas_disparadas = set()

    def inicializar_tablero(self):
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for nombre, eslora in self.naves.items():
            posiciones_naves = []
            while True:
                x = random.randint(0, self.dimensiones - 1)
                y = random.randint(0, self.dimensiones - 1)
                direccion = random.choice(direcciones)
                valido = True
                for i in range(eslora):
                    nuevo_x = x + direccion[0] * i
                    nuevo_y = y + direccion[1] * i
                    if not (0 <= nuevo_x < self.dimensiones and 0 <= nuevo_y < self.dimensiones) or self.tablero[nuevo_x][nuevo_y] != 0:
                        valido = False
                        break
                if valido:
                    for i in range(eslora):
                        self.tablero[nuevo_x - direccion[0] * i][nuevo_y - direccion[1] * i] = 1
                        posiciones_naves.append((nuevo_x - direccion[0] * i, nuevo_y - direccion[1] * i))
                    break
            self.posiciones_naves[nombre] = posiciones_naves

    def disparo_coordenada(self, x, y):
        if (x, y) in self.coordenadas_disparadas:
            print("¡Coordenada ya disparada! Pierdes turno por despistado.")
            return
        if not (0 <= x < self.dimensiones and 0 <= y < self.dimensiones):
            print("¡Coordenadas fuera del tablero! Pierdes turno por torpe.")
            return
        impacto = False
        for nombre_nave, posiciones_nave in self.posiciones_naves.items():
            for pos in posiciones_nave:
                if pos == (x, y):
                    self.nave_vidas[nombre_nave] -= 1
                    if self.nave_vidas[nombre_nave] == 0:
                        for pos in posiciones_nave:
                            self.tablero_impactos[pos[0], pos[1]] = 3
                        print(f"¡Increíble! Has derrotado la nave {nombre_nave}")
                    else:
                        self.tablero_impactos[x, y] = 2
                        print(f"¡Tocado! ¡Sigue afinando tu puntería contra esa nave!")
                    impacto = True
                    break
            if impacto:
                break
        if not impacto:
            self.tablero_impactos[x, y] = 1
            print("¡No impactaste en ninguna nave, espabila!")
        self.coordenadas_disparadas.add((x, y))

    def disparo_coordenada_maquina(self, x, y):
        if (x, y) in self.coordenadas_disparadas:
            print("¡Coordenada ya disparada! El enemigo pierde turno.")
            return
        if not (0 <= x < self.dimensiones and 0 <= y < self.dimensiones):
            print("¡Coordenadas fuera del tablero! El enemigo pierde turno.")
            return
        impacto = False
        for nombre_nave, posiciones_nave in self.posiciones_naves.items():
            for pos in posiciones_nave:
                if pos == (x, y):
                    self.nave_vidas[nombre_nave] -= 1
                    if self.nave_vidas[nombre_nave] == 0:
                        for pos in posiciones_nave:
                            self.tablero_impactos[pos[0], pos[1]] = 3
                        print(f"¡Meteoritos! Han derrotado nuetra nave {nombre_nave}")
                    else:
                        self.tablero_impactos[x, y] = 2
                        print(f"¡Tocados! ¡Cuidado con esa nave!")
                    impacto = True
                    break
            if impacto:
                break
        if not impacto:
            self.tablero_impactos[x, y] = 1
            print("¡Genial, el enemigo no impactó en ninguna nave!")
        self.coordenadas_disparadas.add((x, y))
            
    def obtener_nombre_nave(self, x, y):
        for nombre, eslora in self.naves.items():
            if self.id_jugador == "Jugador":
                if np.sum(self.tablero[x:x+eslora, y]) == eslora:
                    return nombre
            else:
                if np.sum(self.tablero[x:x+eslora, y]) == eslora:
                    return nombre
                
    def imprimir_tablero_con_naves(self, es_tablero_maquina = False):
        if es_tablero_maquina:
            nombre_jugador = "Flota enemiga"
            tablero = self.tablero_impactos
        else:
            nombre_jugador = self.id_jugador
            tablero = self.tablero
        # Encabezado de columnas con valores de los ejes x
        print("  ", end = "")
        for i in range(self.dimensiones):
            print(f"{i} ", end = "")
        print()        
        for i in range(self.dimensiones):
            # Encabezado de filas con valores del eje y
            print(f"{i} ", end = "")
            for j in range(self.dimensiones):
                if tablero[i][j] == 0:
                    print("~ ", end = "")
                elif tablero[i][j] == 1:
                    print("N ", end = "")
                else:
                    print("X ", end = "")
            print()

    def imprimir_tablero(self):
        # Encabezado de columnas con valores de los ejes x
        print("  ", end = "")
        for i in range(self.dimensiones):
            print(f"{i} ", end = "")
        print()
        # Encabezado de filas con valores del eje y + contenido del tablero
        for i in range(self.dimensiones):
            print(f"{i} ", end = "")
            for j in range(self.dimensiones):
                if self.tablero_impactos[i][j] == 0:
                    print("~", end = " ")
                elif self.tablero_impactos[i][j] == 1:
                    print("O", end = " ")  # O para no-impactos
                elif self.tablero_impactos[i][j] == 2:
                    print("X", end = " ")  # X para tocado
                elif self.tablero_impactos[i][j] == 3:
                    print("D", end = " ")  # D para derrotado
            print()