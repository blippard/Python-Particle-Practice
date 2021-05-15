class Map:

    def __init__ (self, width, height):
        self.map = [[" " for _ in range(width)] for _ in range(height)]

    def print_map(self):
        for row in range(len(self.map)):
            print("".join(self.map[row])
