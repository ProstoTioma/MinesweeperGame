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
            r"sprites/flag_icon.png")
        self.flag_rect = self.flag_image.get_rect()

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
                if square.number == -1:
                    colour = (200, 0, 0)
                    pygame.draw.rect(self.screen, colour, rect, 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                elif square.number == -4:
                    colour = (126, 132, 247)
                    pygame.draw.rect(self.screen, colour, rect, 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                    # Plot Numbers
                    if square.neighbours_count > 0:
                        rect.x += 50
                        font = pygame.font.SysFont('arial', 120)
                        text = font.render(str(square.neighbours_count), True, (162, 209, 73))
                        self.screen.blit(text, rect)
                        pygame.display.update()


                elif square.number == -5:
                    colour = (162, 209, 73)
                    pygame.draw.rect(self.screen, colour, rect, 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
                    rect.x += 30

                    self.screen.blit(self.flag_image, rect)
                    pygame.display.flip()




                else:
                    colour = (162, 209, 73)
                    pygame.draw.rect(self.screen, colour, rect, 0)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                countSquare += 1
            countRaw += 1
