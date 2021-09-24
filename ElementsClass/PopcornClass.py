import pygame
from pygame.sprite import Sprite
class PopcornClass(Sprite):
    def __init__(self, screen, pos_x, pos_y, imgId):
        self.screen = screen
        self.screen_largeur = self.screen.get_width()
        self.screen_hauter = self.screen.get_height()
        self.image = pygame.transform.scale(pygame.image.load("assets/pop"+str(imgId) +".png"),(50,50))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = (pos_x, pos_y)

    def render(self):
        self.screen.blit(self.image, self.position)