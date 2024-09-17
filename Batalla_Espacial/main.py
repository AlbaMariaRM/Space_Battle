
import os
import time
from variables import TAMANO_TABLERO, NAVES
from clases import Tablero
from funciones import generar_coordenadas_aleatorias

def main():
    print("¡Saludos, astronauta intrépido! \nSoy Zorvax, líder del planeta Zylox, que se encuentra en el sistema estelar de Rytar.")
    time.sleep(5)
    
    print("\nHoy necesito tu ayuda. \nTe invito a participar en una emocionante batalla galáctica, donde la astucia y la estrategia serán nuestras mejores armas. \nAntes de adentrarnos en esta aventura estelar,")
    time.sleep(5)
    nombre_jugador = input("\n¿Con qué nombre quieres que te recuerde el universo? ")
    
    os.system("cls")  

    print(f"\nBienvenidx pues, {nombre_jugador}, ¡que la fuerza te acompañe!")
    time.sleep(3)
    
    print("\nEl campo de batalla está listo para la acción. \nAhora, es momento de posicionar nuestras naves entre este mar de estrellas. \nNuestras fuerzas y las del enemigo son parejas. Cada bando cuenta con: \n4 naves de 1 posición de eslora \n3 naves de 2 posiciones de eslora \n2 naves de 3 posiciones de eslora \n1 nave de 4 posiciones de eslora")
    time.sleep(8)
    
    print("\nConfía en mi criterio para la colocación de las naves. \nTu responsabilidad es derrotar la flota enemiga, así que céntrate en dirigir los disparos de nuestras naves.")
    time.sleep(5)

    print(f"\n¡ATENTX, {nombre_jugador}! En este sistema turbulento ~~~ veras: \nlos disparos fallidos como O \nlos aciertos como X \nlas naves derrotadas como D")
    time.sleep(5)
    
    os.system("cls")  

    # Inicializamos los tableros de ambos jugadores
    tablero_jugador = Tablero(id_jugador = nombre_jugador)
    tablero_maquina = Tablero(id_jugador = "Flota enemiga")
    tablero_jugador.inicializar_tablero()
    tablero_maquina.inicializar_tablero()

     # Imprimimos el tablero del jugador con las naves colocadas
    print(f"\nEstos son tu tablero y tus naves posicionadas, {nombre_jugador}:\n")
    tablero_jugador.imprimir_tablero_con_naves()
    
    time.sleep(5)
    os.system("cls")

    while True:
        # Turno del jugador humano
        print("\nTus disparos:\n")
        tablero_maquina.imprimir_tablero()
        print("\nDisparos del enemigo:\n")
        tablero_jugador.imprimir_tablero()
        print("\n¡Es tu turno! Disparales:")

        try:
            # Turno del jugador
            x, y = map(int, input("\nIntroduce las coordenadas separadas por comas (x, y). \nRecuerda, números entre el 0 y el 9 según muestra el tablero: ").split(","))
            
            # Verificar si las coordenadas están dentro del rango permitido
            if not (0 <= x < TAMANO_TABLERO and 0 <= y < TAMANO_TABLERO):
                print("¡Coordenadas fuera del rango, despistado! Deben estar entre 0 y 9.")
                continue  # Vuelve al inicio del bucle

            # Disparar en las coordenadas introducidas
            tablero_maquina.disparo_coordenada(x, y)

            # Verificamos si el jugador ha perdido
            if sum(tablero_jugador.nave_vidas.values()) == 0:
                print("\n¡Hemos perdido! El enemigo ha ganado.")
                ppp = input("DE POCO SIRVIÓ TU AYUDA...PULSA UNA TECLA PARA DESPEGAR TU NAVE Y VOLVER A TU PLANETA")
                break

            # Turno de la máquina
            print("\nTurno de la Flota enemiga:")
            time.sleep(3)  # Añadimos un timesleep para hacer como que la máquina piensa
            x, y = generar_coordenadas_aleatorias()
            print(f"La Flota enemiga dispara a las coordenadas {x}, {y}.")
            tablero_jugador.disparo_coordenada_maquina(x, y)

            # Verificamos si la máquina ha perdido
            if sum(tablero_maquina.nave_vidas.values()) == 0:
                print("\n¡Hemos ganado! El enemigo ha sido eliminado. ¡Bravo!")
                ppp = input("TU AYUDA SERÁ RECORDADA...PULSA UNA TECLA PARA DESPEGAR TU NAVE Y VOLVER A TU PLANETA ENTRE VÍTORES")
                break

            time.sleep(3)
            os.system("cls")
            
        except ValueError:
            print("¡Error! Debes introducir números enteros separados por comas.")
            time.sleep(5)

if __name__ == "__main__":
    main()