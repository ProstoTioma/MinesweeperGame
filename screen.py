import pygame
from game import Game


class Screen:
    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Minesweeper")
        self.bg = (98, 150, 186)
        self.game = Game()

    def draw(self):
        end = False

        # rect = pygame.Rect(100, 100, 50, 50)

        while not end:
            self.screen.fill(self.bg)
            self.draw_field(self.game.field)
            # self.screen.fill((100, 50, 50), rect)
            for event in pygame.event.get():
                # Click

                if event.type == pygame.QUIT:
                    end = True
            pygame.display.update()

    def draw_field(self, field):
        countRaw = 0

        for raw in field:
            countSquare = 0
            for square in raw:
                pygame.draw.rect(self.screen, (162, 209, 73),
                                 (countSquare * self.screen_width // len(raw),
                                  countRaw * self.screen_height // len(field),
                                  self.screen_width // len(raw), self.screen_height // len(field)), 0)
                pygame.draw.rect(self.screen, (0, 0, 0), (
                countSquare * self.screen_width // len(raw), countRaw * self.screen_height // len(field),
                self.screen_width // len(raw), self.screen_height // len(field)), 1)

                countSquare += 1
            countRaw += 1
