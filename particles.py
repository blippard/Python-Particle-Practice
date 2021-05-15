class Map:

    def __init__ (self, width, height):
        self.map = [[" " for _ in range(width)] for _ in range(height)]

    def print_map(self):
        for row in range(len(self.map)):
            print("".join(self.map[row])

    def insert_obstacle(self, x_pos, y_pos, length):
        obstacle_length = x_pos + length
        for x_coord in range(x_pos, obstacle_length):
            self.map[y_pos][x_coord] = "\033[37;47m*\1xb[0m"
