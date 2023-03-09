import pygame
import random
import numpy as np


class Game:
    def __init__(self):
        # 0 closed square w/o mine, 1 opened square w/o mine, -1 mine opened, -2 mine closed, 2 flag
        self.game_over = False
        self.field = np.zeros([6, 6])
        self.generate_mines(10)
        self.flags_number = 10
        self.neighbors_count = 0

    def generate_mines(self, n):
        for i in range(n):
            line = random.randint(0, len(self.field) - 1)
            el_ind = random.randint(0, len(self.field) - 1)

            self.field[el_ind][line] = -2

    def click(self, button, square_index):
        self.neighbors_count = 0
        if button == 1:
            if self.field[square_index] == -2:
                self.field[square_index] = -1
                self.game_over = True
                print("Game Over!")
            elif self.field[square_index] == 0:
                self.field[square_index] = 1
                neighbours = self.get_neighbors(self.field, square_index[0], square_index[1])
                print(neighbours)
                for neighbour in neighbours:
                    if neighbour == -2:
                        self.neighbors_count += 1
                print(self.neighbors_count)

        elif button == 3:
            if self.flags_number > 0:
                self.field[square_index] = 2
                self.flags_number -= 1

    def get_neighbors(self, matrix, x, y):
        num_rows, num_cols = len(matrix), len(matrix[0])
        neighbours = []

        for i in range((0 if x - 1 < 0 else x - 1), (num_rows if x + 2 > num_rows else x + 2), 1):
            for j in range((0 if y - 1 < 0 else y - 1), (num_cols if y + 2 > num_cols else y + 2), 1):
                if matrix[x][y] != matrix[i][j]:
                    neighbours.append(matrix[i][j])

        return neighbours
