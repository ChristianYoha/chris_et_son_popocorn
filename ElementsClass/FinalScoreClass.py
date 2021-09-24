from ElementsClass.CustomClass import CustomClass
class FinalScoreClass:

    def __init__(self,msg, pos, screen, text_rgb):
        custom_function = CustomClass
        self.screen = screen
        self.msg = msg
        self.font_size = 60
        self.text = custom_function.customText(text=self.msg, font_size=self.font_size, text_rgb=text_rgb)
        self.pos = self.text.get_rect(center=pos)

    def render(self):
        self.screen.blit(self.text, self.pos)