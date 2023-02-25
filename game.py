import pygame
import random
import numpy as np


class Game:
    def __init__(self):
        # 0 closed square w/o mine, 1 opened square w/o mine, -1 mine, 2 flag
        self.game_over = False
        self.field = np.zeros([6, 6])
        self.generate_mines(10)

    def generate_mines(self, n):
        for i in range(n):
            line = random.randint(0, len(self.field) - 1)
            el_ind = random.randint(0, len(self.field) - 1)

            self.field[el_ind][line] = -1





    def click(self, square_index):
        if self.field[square_index] == -1:
            self.game_over = True
            print("Game Over!")
        elif self.field[square_index] == 0:
            self.field[square_index] = 1
