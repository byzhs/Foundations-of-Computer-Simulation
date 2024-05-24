import tkinter as tk
import numpy as np

class GameOfLife:
    def __init__(self, master, rows=20, cols=20, cell_size=20):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.running = False
        self.rules = [2, 3, 3]
        self.grid = np.zeros((rows, cols), dtype=bool)
        self.temp_grid = np.zeros((rows, cols), dtype=bool)
        self.setup_gui()

    def setup_gui(self):
        self.canvas = tk.Canvas(self.master, width=self.cols * self.cell_size, height=self.rows * self.cell_size)
        self.canvas.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start_game)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_game)
        self.stop_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_grid)
        self.clear_button.pack(side=tk.LEFT)

        self.random_button = tk.Button(self.master, text="Random", command=self.random_grid)
        self.random_button.pack(side=tk.LEFT)

        self.rule_label = tk.Label(self.master, text="Rules B/S:")
        self.rule_label.pack(side=tk.LEFT)

        self.rule_entry = tk.Entry(self.master)
        self.rule_entry.pack(side=tk.LEFT)
        self.rule_entry.insert(0, "3/23")

        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.update_canvas()

    def start_game(self):
        self.running = True
        self.update_game()

    def stop_game(self):
        self.running = False

    def clear_grid(self):
        self.grid = np.zeros((self.rows, self.cols), dtype=bool)
        self.update_canvas()

    def random_grid(self):
        self.grid = np.random.choice([False, True], size=(self.rows, self.cols))
        self.update_canvas()

    def toggle_cell(self, event):
        row = event.y // self.cell_size
        col = event.x // self.cell_size
        self.grid[row, col] = not self.grid[row, col]
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        for row in range(self.rows):
            for col in range(self.cols):
                color = "black" if self.grid[row, col] else "white"
                self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size,
                                             (col + 1) * self.cell_size, (row + 1) * self.cell_size,
                                             fill=color, outline="gray")

    def update_game(self):
        if not self.running:
            return
        self.parse_rules()
        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = self.count_live_neighbors(row, col)
                if self.grid[row, col]:
                    self.temp_grid[row, col] = live_neighbors in self.rules[1:]
                else:
                    self.temp_grid[row, col] = live_neighbors == self.rules[0]
        self.grid, self.temp_grid = self.temp_grid, self.grid
        self.update_canvas()
        self.master.after(100, self.update_game)

    def count_live_neighbors(self, row, col):
        neighbors = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1),          (0, 1),
                     (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in neighbors:
            r, c = (row + dr) % self.rows, (col + dc) % self.cols
            count += self.grid[r, c]
        return count

    def parse_rules(self):
        rule_text = self.rule_entry.get()
        birth, survival = rule_text.split('/')
        self.rules = [int(b) for b in birth] + [int(s) for s in survival]

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game of Life")
    game = GameOfLife(root)
    root.mainloop()
