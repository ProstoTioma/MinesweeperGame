import pygame
import random


class Game:
    def __init__(self):
        # 0 closed square w/o mine, 1 opened square w/o mine, -1 mine, 2 flag
        self.game_over = False
        self.field = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

    def generate_mines(self, n):
        for i in range(n):
            line = random.randint(0, 4)
            el_ind = random.randint(0, 4)

            self.field[line][el_ind] = -1


