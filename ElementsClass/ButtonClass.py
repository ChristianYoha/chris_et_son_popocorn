from pygame.sprite import Sprite
from ElementsClass.CustomClass import CustomClass
class ButtonClass(Sprite):

    def __init__(self, center_position, text, font_size, text_rgb, action=None):
        custom_function = CustomClass
        self.mouse_over = False 
        # create the default btn
        default_btn = custom_function.customButton(
            text=text, font_size=font_size, text_rgb=text_rgb
        )

        # create the btn that shows when mouse is over the element
        highlighted_btn = custom_function.customButton(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb
        )

        # add both btn type and their rects to lists
        self.btns = [default_btn, highlighted_btn]
        self.rects = [
            default_btn.get_rect(center=center_position),
            highlighted_btn.get_rect(center=center_position),
        ]

        # assign button action
        self.action = action

        # calls the init method of the parent sprite class
        super().__init__()

    # properties that vary the image and its rect when the mouse is over the element
    @property
    def btn(self):
        return self.btns[1] if self.mouse_over else self.btns[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def render(self, screen):
        """ Rebnder btn onto a screen """
        screen.blit(self.btn, self.rect)