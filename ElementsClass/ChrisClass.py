class ChrisClass:
    def __init__(self, screen, pygame):
        self.screen = screen
        self.screen_largeur = self.screen.get_width()
        self.screen_hauter = self.screen.get_height()
        self.image = pygame.transform.scale(pygame.image.load("assets/chris.png"),(170,350))
        self.position=[10, 110]

    def render(self):
        self.screen.blit(self.image, self.position)