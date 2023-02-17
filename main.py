import pygame

from screen import Screen
from game import Game


def start():
    pygame.init()
    current_display = Screen(100, 800)
    game = Game()
    game.generate_mines(10)
    print(game.field)
    current_display.draw()


start()
