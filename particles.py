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

    def move_to_available(self, Map):
        if (self.y_pos == len(Map) - 1) or (self.x_pos == len(Map[0]) - 1) or self.x_pos == 0:
            pass
        elif Map[self.y_pos + 1][self.x_pos] == bg_block:
            self.y_pos += 1
        elif Map[self.y_pos + 1][self.x_pos - 1] == bg_block and Map[self.y_pos][self.x_pos - 1] == bg_block:
            self.y_pos += 1
            self.x_pos -= 1
        elif Map[self.y_pos + 1][self.x_pos + 1] == bg_block and Map[self.y_pos][self.x_pos + 1] == bg_block:
            self.y_pos += 1
            self.x_pos += 1

class Game:

    def __init__(self):
        self.game_map = Map(30, 30)
        self.particle_list = []

    def generate_particle(self, icon):
        self.particle_list.append(Particle(random.randint(5, 15), 0, icon))

    def position_particles(self):
        for particle in self.particle_list:
            self.game_map.map[particle.y_pos][particle.x_pos] = bg_block
            particle.move_to_available(self.game_map.map)
            self.game_map.map[particle.y_pos][particle.x_pos] = particle.icon

    def generate_obstacles(self, amount):
        for _ in range(amount):
            x_pos = random.randint(0, 20)
            y_pos = random.randint(0, 20)
            length = random.randint(5, 10)
            self.game_map.insert_obstacle(x_pos, y_pos, length)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def refresh(self):
        self.position_particles()
        self.game_map.print_map()

    def game_loop(self):
        while True:
            self.generate_particles("█")
            self.clear_screen()
            self.refresh()
            time.sleep(0.05)

    def run_game(self):
        self.generate_obstacles(5)
        self.game_loop()

