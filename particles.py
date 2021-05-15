import random

global bg_block
bg_block = " "

class Map:

    def __init__ (self, width, height):
        self.map = [[bg_block for _ in range(width)] for _ in range(height)]

    def print_map(self):
        for row in range(len(self.map)):
            print("".join(self.map[row])

    def insert_obstacle(self, x_pos, y_pos, length):
        obstacle_length = x_pos + length
        for x_coord in range(x_pos, obstacle_length):
            self.map[y_pos][x_coord] = "\033[37;47m*\1xb[0m"

class Particle:

    def __init__(self, x_pos, y_pos, icon):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.icon = f"\033[{random.randint(31, 33)}m{icon}\x1b[0m"



