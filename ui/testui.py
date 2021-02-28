
import pygame
import sys
import ui

class UICanvas:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,800))
        pygame.display.set_caption('Alien')
        self.bg_color = (230, 230, 230)
        self.text = ui.Text(self.screen, 'hello', 20, (255,0,0))

    def run(self):
        while True:
            self._handle_events()
            self._update()
            self._draw()
            
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.text.pos = pos

    def _update(self):
        pos = pygame.mouse.get_pos()
        self.text.pos = pos

    def _draw(self):
        self.screen.fill(self.bg_color)
        self.text.draw()
        pygame.display.flip()

game = UICanvas()
game.run()
