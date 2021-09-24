from ElementsClass.ChrisClass import ChrisClass
from ElementsClass.IntroText import IntroText
from ElementsClass.ButtonClass import ButtonClass

class HomeScreenClass:
    def __init__(self):
        pass
    def home_screen(screen, pygame, SCREEN, BLACK_BLUE, BLACK, RED, GameState):
        # Create Chris
        # chris = ChrisClass(screen)
        chris = ChrisClass(screen, pygame)
        # Create Intro Text
        introText1 = IntroText(
            msg="Chris a perdu ses dents en mangeant du popcorn.",
            pos = (400, 60), 
            text_rgb=BLACK_BLUE,
            screen = screen
        )
        introText2 = IntroText(
            msg="Aidez-le à les retrouver!",
            pos = (400, 90), 
            text_rgb=BLACK_BLUE,
            screen = screen
        )
        
        # Create Buttons
        startButton = ButtonClass(
            center_position=(400, 250),
            font_size=40,
            text_rgb=BLACK,
            text="Commencer",
            action=GameState.NEWGAME,
        )
        exitButton = ButtonClass(
            center_position=(400, 350),
            font_size=40,
            text_rgb=RED,
            text="Quitter",
            action=GameState.QUIT,
        )
        buttons = [startButton, exitButton]
        while True:
            mouse_up = False
            for event in pygame.event.get():
                # pass
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True

            screen.fill(SCREEN)

            # show Chris, întro text and buttons 
            chris.render()
            introText1.render()
            introText2.render()


            for button in buttons:
                btn_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if btn_action is not None:
                    return btn_action
                button.render(screen)

            pygame.display.flip()