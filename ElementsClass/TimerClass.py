from ElementsClass.CustomClass import CustomClass
class TimerClass():

    def __init__(self, pos, screen, second, text_rgb):
        custom_function = CustomClass
        self.screen = screen
        self.second = second
        self.msg = "Temps: 00:"+self.second
        self.font_size = 20
        self.text_rgb = text_rgb
        # self.text = customText(text=self.msg, font_size=self.font_size, text_rgb=self.text_rgb)
        self.text = custom_function.customText(text=self.msg, font_size=self.font_size, text_rgb=self.text_rgb)
        self.pos = self.text.get_rect(center=pos)

    def render(self):
        self.screen.blit(self.text, self.pos)

    def hide(self):
        transparent = (0, 0, 0, 0)
        self.text.fill(transparent)