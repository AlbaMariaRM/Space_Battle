
import os
import time
from variables import BOARD_SIZE, SHIPS
from classes import Board
from functions import generate_random_coordinates

def main():
    print("Greetings, brave astronaut! \nI am Zorvax, leader of the planet Zylox, located in the star system of Rytar.")
    time.sleep(5)
    
    print("\nToday, I need your help. \nI invite you to participate in an exciting galactic battle, where cunning and strategy will be our best weapons. \nBefore we dive into this stellar adventure,")
    time.sleep(5)
    player_name = input("\nWhat name do you want the universe to remember you by? ")
    
    os.system("cls")  

    print(f"\nWelcome then, {player_name}, may the force be with you!")
    time.sleep(3)
    
    print("\nThe battlefield is ready for action. \nNow, it's time to position our ships among this sea of stars. \nOur forces and those of the enemy are equal. Each side has: \n4 ships of 1 length \n3 ships of 2 length \n2 ships of 3 length \n1 ship of 4 length")
    time.sleep(8)
    
    print("\nTrust my judgment to place the ships. \nYour responsibility is to defeat the enemy fleet, so focus on directing our ship's fire.")
    time.sleep(5)

    print(f"\nATTENTION, {player_name}! In this turbulent system ~~~ you will see: \nmissed shots as O \nhits as X \ndestroyed ships as D")
    time.sleep(5)
    
    os.system("cls")  

    # Initialize both players' boards
    player_board = Board(player_id = player_name)
    enemy_board = Board(player_id = "Enemy Fleet")
    player_board.initialize_board()
    enemy_board.initialize_board()

     # Print the player's board with the ships placed
    print(f"\nThis is your board with the ships placed, {player_name}:\n")
    player_board.print_board_with_ships()
    
    time.sleep(5)
    os.system("cls")

    while True:
        # Human player's turn
        print("\nYour shots:\n")
        enemy_board.print_board()
        print("\nEnemy's shots:\n")
        player_board.print_board()
        print("\nIt's your turn! Fire at them:")

        try:
            # Player's turn
            x, y = map(int, input("\nEnter the coordinates separated by commas (x, y). \nRemember, numbers between 0 and 9 as shown on the board: ").split(","))

            # Check if the coordinates are within the allowed range
            if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
                print("Coordinates out of range, pay attention! They must be between 0 and 9.")
                continue  # Return to the start of the loop

            # Fire at the entered coordinates
            enemy_board.fire_coordinate(x, y)

            # Check if the player has lost
            if sum(player_board.ship_lives.values()) == 0:
                print("\nWe've lost! The enemy has won.")
                ppp = input("YOUR HELP WAS OF LITTLE USE...PRESS A KEY TO LAUNCH YOUR SHIP AND RETURN TO YOUR PLANET")
                break

            # Machine's turn
            print("\nEnemy Fleet's turn:")
            time.sleep(3)  # Add a timesleep to simulate the machine thinking
            x, y = generate_random_coordinates()
            print(f"The Enemy Fleet fires at coordinates {x}, {y}.")
            player_board.fire_coordinate_machine(x, y)

            # Check if the machine has lost
            if sum(enemy_board.ship_lives.values()) == 0:
                print("\nWe've won! The enemy has been eliminated. Bravo!")
                ppp = input("YOUR HELP WILL BE REMEMBERED...PRESS A KEY TO LAUNCH YOUR SHIP AND RETURN TO YOUR PLANET AMID CHEERS")
                break

            time.sleep(3)
            os.system("cls")
            
        except ValueError:
            print("Error! You must enter integers separated by commas.")
            time.sleep(5)

if __name__ == "__main__":
    main()