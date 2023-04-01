import random

import numpy as np


class Game:
    def __init__(self):
        # -3 closed square w/o mine, -4 opened square w/o mine, -1 mine opened, -2 mine closed, -5 flag
        self.game_over = False
        self.field = np.zeros((6, 6), dtype=Cell)
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                cell = Cell(0)
                self.field[j][i] = cell
        self.generate_mines(6)
        self.flags_number = 7
        self.neighbors_count = 0

    def generate_mines(self, n):
        for i in range(n):
            line = random.randint(0, len(self.field) - 1)
            el_ind = random.randint(0, len(self.field) - 1)

            self.field[el_ind][line].number = -2

    def click(self, button, square_index):
        if not self.game_over:
            self.neighbors_count = 0
            if button == 1:
                if not self.field[square_index].is_flag:
                    if self.field[square_index].number == -2:
                        self.field[square_index].number = -1
                        self.game_over = True
                        print("Game Over!")
                    elif self.field[square_index].number == -3:
                        self.field[square_index].number = -4
                        neighbours = self.get_neighbors(self.field, square_index[0], square_index[1])
                        for neighbour in neighbours:
                            if neighbour.number == -2:
                                self.neighbors_count += 1
                        self.field[square_index].neighbours_count = self.neighbors_count

            elif button == 3:
                if self.field[square_index].is_flag:
                    self.field[square_index].is_flag = False
                    self.flags_number += 1
                elif self.flags_number > 0 and not self.field[square_index].is_flag and (self.field[square_index].number == -3 or self.field[square_index].number == -2):
                    self.field[square_index].is_flag = True
                    self.flags_number -= 1

    def get_neighbors(self, matrix, x, y):
        num_rows, num_cols = len(matrix), len(matrix[0])
        neighbours = []

        for i in range((0 if x - 1 < 0 else x - 1), (num_rows if x + 2 > num_rows else x + 2), 1):
            for j in range((0 if y - 1 < 0 else y - 1), (num_cols if y + 2 > num_cols else y + 2), 1):
                if matrix[x][y] != matrix[i][j]:
                    neighbours.append(matrix[i][j])

        return neighbours


class Cell:
    def __init__(self, neighbours_count):
        self.number = -3
        self.neighbours_count = neighbours_count
        self.is_flag = False


       #index box number 0,1,2,3,4
