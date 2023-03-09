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
        self.sprites = []
        self.flag_image = pygame.image.load(
            r"C:\Users\artio\PycharmProjects\pythonLessons\src\MinesweeperGame\sprites\flag_icon.png")
        self.flag_rect = self.flag_image.get_rect()

        # # Plot Numbers
        # font = pygame.font.SysFont('arial', 150)
        # text = font.render(str(self.game.neighbors_count), True, (0, 0, 0))
        # self.screen.blit(text, rect)
        # pygame.display.update()

    def draw(self):
        end = False
        self.screen.fill(self.bg)

        while not end:

            self.sprites = []
            self.draw_field(self.game.field)

            for event in pygame.event.get():
                self.draw_field(self.game.field)
                # Click
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicked_sprites = [s for s in self.sprites if s.collidepoint(pos)]
                    print(clicked_sprites[0][0] // clicked_sprites[0][2],
                          clicked_sprites[0][1] // clicked_sprites[0][3])

                    self.game.click(event.button, (clicked_sprites[0][1] // clicked_sprites[0][3],
                                                   clicked_sprites[0][0] // clicked_sprites[0][2]))
                    print(self.game.field)
                if event.type == pygame.QUIT:
                    end = True
            pygame.display.update()

    def draw_field(self, field):
        countRaw = 0

        for raw in field:
            countSquare = 0
            for square in raw:
                rect = pygame.Rect(countSquare * self.screen_width // len(raw), countRaw * self.screen_height // len(
                    field), self.screen_width // len(raw), self.screen_height // len(field))
                self.sprites += [rect]
                if square == -1:
                    colour = (200, 0, 0)
                    pygame.draw.rect(self.screen, colour, rect, 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                elif square == 1:
                    colour = (126, 132, 247)
                    pygame.draw.rect(self.screen, colour, rect, 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)


                elif square == 2:
                    colour = (162, 209, 73)
                    pygame.draw.rect(self.screen, colour, rect, 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                    self.screen.blit(self.flag_image, rect)
                    pygame.display.flip()


                else:
                    colour = (162, 209, 73)
                    pygame.draw.rect(self.screen, colour, rect, 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                countSquare += 1
            countRaw += 1
