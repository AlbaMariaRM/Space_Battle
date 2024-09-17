
from variables import BOARD_SIZE
import random

def generate_random_coordinates():
    return random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)