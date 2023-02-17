import pygame


class Screen:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Minesweeper")
        self.bg = (98, 150, 186)

    def draw(self):
        end = False

        # rect = pygame.Rect(100, 100, 50, 50)

        while not end:
            self.screen.fill(self.bg)
            # self.screen.fill((100, 50, 50), rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
            pygame.display.update()

