import pygame

from screen import Screen
from game import Game


def start():
    pygame.init()
    current_display = Screen(1000, 800)
    game = Game()
    print(game.field)
    current_display.draw()


start()
