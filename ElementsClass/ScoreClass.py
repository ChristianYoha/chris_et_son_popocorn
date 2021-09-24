from ElementsClass.CustomClass import CustomClass
class ScoreClass():
    def __init__(self, pos, screen, score, text_rgb):
        custom_function = CustomClass
        self.screen = screen
        self.score = score
        self.msg = "Score: "+str(self.score)+"/10"
        self.font_size = 30
        self.text_rgb = text_rgb
        # self.text = customText(text=self.msg, font_size=self.font_size, text_rgb=self.text_rgb)
        self.text = custom_function.customText(text=self.msg, font_size=self.font_size, text_rgb=self.text_rgb)
        self.pos = self.text.get_rect(center=pos)

    def render(self):
        self.screen.blit(self.text, self.pos)

    def hide(self):
        transparent = (0, 0, 0, 0)
        self.text.fill(transparent)