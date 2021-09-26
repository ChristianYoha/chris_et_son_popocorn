import pygame
from pygame.sprite import Sprite
from ElementsClass.ScoreClass import ScoreClass

class TeethClass(Sprite):
    def __init__(self, screen, pos_x, pos_y):
        self.screen = screen
        self.screen_largeur = self.screen.get_width()
        self.screen_hauter = self.screen.get_height()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = (pos_x, pos_y)

        self.mouse_over = False
        self.is_selected = False

        default_teeth_image = pygame.transform.scale(pygame.image.load("assets/dent.png"),(40,50))
        selected_teeth_image = pygame.transform.scale(pygame.image.load("assets/dent_hallo.png"),(45,55))

        self.teeth_images = [default_teeth_image, selected_teeth_image]
        self.rects = [
            default_teeth_image.get_rect(center=self.position),
            selected_teeth_image.get_rect(center=self.position),
        ]

    @property
    def image(self):
        return self.teeth_images[1] if self.mouse_over else self.teeth_images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    

    def update(self, mouse_pos):
        if self.is_selected == False:
            if self.rect.collidepoint(mouse_pos):
                self.mouse_over = True
            else:
                self.mouse_over = False

    def select(self, score_instances, score_value, BLACK_BLUE):
        new_score_value = score_value
        new_score_value += 1
        transparent = (0, 0, 0, 0)
        self.image.fill(transparent)
        self.is_selected = True

        # Handle score up
        for score_ in score_instances:
            score_.hide()
        
        new_score = ScoreClass(
            score = new_score_value,
            pos = (self.screen.get_width()-(self.screen.get_width()/2), 25), 
            text_rgb=BLACK_BLUE,
            screen = self.screen
        )
        score_instances.append(new_score)

        return new_score_value 
            
    def render(self):
        self.screen.blit(self.image, self.rect)