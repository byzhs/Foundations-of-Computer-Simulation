import numpy as np

class GameRules:
    def __init__(self, survival_rules, birth_rules):
        self.survival_rules = np.zeros(10, dtype=int)
        self.birth_rules = np.zeros(10, dtype=int)

        for c in survival_rules:
            i = int(c)
            if i <= 8:
                self.survival_rules[i] = 1

        for c in birth_rules:
            j = int(c)
            if j <= 8:
                self.birth_rules[j] = 1

    def should_survive(self, neighbor_count):
        return 1 if self.survival_rules[neighbor_count] > 0 else 0

    def should_be_born(self, neighbor_count):
        return 1 if self.birth_rules[neighbor_count] > 0 else 0

    def update_rules(self, new_survival, new_birth):
        self.survival_rules = np.zeros(10, dtype=int)
        self.birth_rules = np.zeros(10, dtype=int)

        for c in new_survival:
            i = int(c)
            if i <= 8:
                self.survival_rules[i] = 1

        for c in new_birth:
            j = int(c)
            if j <= 8:
                self.birth_rules[j] = 1

class GameOfLife:
    def __init__(self, grid_size, game_rules):
        self.size = grid_size
        self.game_rules = game_rules
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.new_grid = np.zeros((grid_size, grid_size), dtype=int)

    def initialize_grid(self, x, y):
        self.grid[x][y] = 1

    def print_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                print('■' if self.grid[i][j] == 1 else '0', end=' ')
            print()

    def iterate(self):
        for x in range(self.size):
            for y in range(self.size):
                current_x, current_y = np.meshgrid(
                    np.mod(np.arange(x - 1, x + 2), self.size),
                    np.mod(np.arange(y - 1, y + 2), self.size),
                    indexing="ij",
                )
                neighbor_values = np.sum(self.grid[current_x, current_y]) - self.grid[x, y]

                if self.grid[x][y] == 1:
                    self.new_grid[x][y] = self.game_rules.should_survive(neighbor_values)
                else:
                    self.new_grid[x][y] = self.game_rules.should_be_born(neighbor_values)

        self.grid = np.copy(self.new_grid)

def main():
    grid_size = int(input("Grid size: "))
    survival_rules = input("Rules for survival: ")
    birth_rules = input("Rules for birth: ")
    game_rules = GameRules(survival_rules, birth_rules)
    game = GameOfLife(grid_size, game_rules)

    print("Enter initial live cell coordinates (format: x,y). Finish by typing 'q'.")
    while True:
        input_coords = input("Coordinates: ")
        if input_coords == 'q':
            break
        x, y = map(int, input_coords.split(','))
        game.initialize_grid(x, y)

    while True:
        game.print_grid()
        game.iterate()
        user_input = input("Next iteration (n), change rules (c), quit (q): ")
        if user_input == "q":
            break
        elif user_input == "c":
            new_survival = input("New rules for survival: ")
            new_birth = input("New rules for birth: ")
            game.game_rules.update_rules(new_survival, new_birth)

if __name__ == "__main__":
    main()
