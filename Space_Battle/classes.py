
import numpy as np
from variables import BOARD_SIZE, SHIPS
import random

class Board:
    def __init__(self, player_id):
        self.player_id = player_id
        self.dimensions = BOARD_SIZE
        self.ships = SHIPS
        self.board = np.zeros((self.dimensions, self.dimensions), dtype = int)
        self.hit_board = np.zeros((self.dimensions, self.dimensions), dtype = int)
        self.ship_lives = {name: length for name, length in self.ships.items()}
        self.ship_positions = {}
        self.shot_coordinates = set()

    def initialize_board(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for name, length in self.ships.items():
            ship_positions = []
            while True:
                x = random.randint(0, self.dimensions - 1)
                y = random.randint(0, self.dimensions - 1)
                direction = random.choice(directions)
                valid = True
                for i in range(length):
                    new_x = x + direction[0] * i
                    new_y = y + direction[1] * i
                    if not (0 <= new_x < self.dimensions and 0 <= new_y < self.dimensions) or self.board[new_x][new_y] != 0:
                        valid = False
                        break
                if valid:
                    for i in range(length):
                        self.board[new_x - direction[0] * i][new_y - direction[1] * i] = 1
                        ship_positions.append((new_x - direction[0] * i, new_y - direction[1] * i))
                    break
            self.ship_positions[name] = ship_positions

    def fire_coordinate(self, x, y):
        if (x, y) in self.shot_coordinates:
            print("Coordinate already fired! You lose a turn for being distracted.")
            return
        if not (0 <= x < self.dimensions and 0 <= y < self.dimensions):
            print("Coordinates out of bounds! You lose a turn for being clumsy.")
            return
        hit = False
        for ship_name, ship_positions in self.ship_positions.items():
            for pos in ship_positions:
                if pos == (x, y):
                    self.ship_lives[ship_name] -= 1
                    if self.ship_lives[ship_name] == 0:
                        for pos in ship_positions:
                            self.hit_board[pos[0], pos[1]] = 3
                        print(f"Incredible! You have destroyed the ship {ship_name}")
                    else:
                        self.hit_board[x, y] = 2
                        print(f"Hit! Keep aiming at that ship!")
                    hit = True
                    break
            if hit:
                break
        if not hit:
            self.hit_board[x, y] = 1
            print("You missed! Stay focused!")
        self.shot_coordinates.add((x, y))

    def fire_coordinate_machine(self, x, y):
        if (x, y) in self.shot_coordinates:
            print("Coordinate already fired! The enemy loses a turn.")
            return
        if not (0 <= x < self.dimensions and 0 <= y < self.dimensions):
            print("Coordinates out of bounds! The enemy loses a turn.")
            return
        hit = False
        for ship_name, ship_positions in self.ship_positions.items():
            for pos in ship_positions:
                if pos == (x, y):
                    self.ship_lives[ship_name] -= 1
                    if self.ship_lives[ship_name] == 0:
                        for pos in ship_positions:
                            self.hit_board[pos[0], pos[1]] = 3
                        print(f"Meteorites! They destroyed our ship {ship_name}")
                    else:
                        self.hit_board[x, y] = 2
                        print(f"Hit! Watch out for that ship!")
                    hit = True
                    break
            if hit:
                break
        if not hit:
            self.hit_board[x, y] = 1
            print("Great, the enemy missed!")
        self.shot_coordinates.add((x, y))

    def get_ship_name(self, x, y):
        for name, length in self.ships.items():
            if self.player_id == "Player":
                if np.sum(self.board[x:x+length, y]) == length:
                    return name
            else:
                if np.sum(self.board[x:x+length, y]) == length:
                    return name

    def print_board_with_ships(self, is_machine_board=False):
        if is_machine_board:
            player_name = "Enemy Fleet"
            board = self.hit_board
        else:
            player_name = self.player_id
            board = self.board
        # Column header with x-axis values
        print("  ", end = "")
        for i in range(self.dimensions):
            print(f"{i} ", end = "")
        print()
        for i in range(self.dimensions):
            # Row header with y-axis values
            print(f"{i} ", end = "")
            for j in range(self.dimensions):
                if board[i][j] == 0:
                    print("~ ", end = "")
                elif board[i][j] == 1:
                    print("S ", end = "")
                else:
                    print("X ", end = "")
            print()

    def print_board(self):
        # Column header with x-axis values
        print("  ", end = "")
        for i in range(self.dimensions):
            print(f"{i} ", end = "")
        print()
        # Row header with y-axis values + board content
        for i in range(self.dimensions):
            print(f"{i} ", end = "")
            for j in range(self.dimensions):
                if self.hit_board[i][j] == 0:
                    print("~", end = " ")
                elif self.hit_board[i][j] == 1:
                    print("O", end = " ")  # O for misses
                elif self.hit_board[i][j] == 2:
                    print("X", end = " ")  # X for hits
                elif self.hit_board[i][j] == 3:
                    print("D", end = " ")  # D for destroyed
            print()