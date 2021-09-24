import pygame
class CustomClass:
    def __init__(self):
        None

    def customText(text,font_size, text_rgb):
        font = pygame.freetype.SysFont("Chalkboard", font_size, bold=True)
        custom_text, _ = font.render(text=text, fgcolor=text_rgb)
        return custom_text.convert_alpha()

    def customButton(text,font_size, text_rgb):
        font = pygame.freetype.SysFont("Chalkboard", font_size, bold=True)
        surface, _ = font.render(text=text, fgcolor=text_rgb)
        return surface.convert_alpha()