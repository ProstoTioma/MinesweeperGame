import pygame

from screen import Screen
from game import Game


def start():
    pygame.init()
    current_display = Screen(1000, 800)
    print(current_display.game.field)
    current_display.draw()


start()
