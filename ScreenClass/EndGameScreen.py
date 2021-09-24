# from GameState import GameState
from ElementsClass.ChrisClass import ChrisClass
from ElementsClass.IntroText import IntroText
from ElementsClass.ButtonClass import ButtonClass
from ElementsClass.FinalScoreClass import FinalScoreClass

class EndGameScreen:
    def __init__(self):
        pass

    def end_game_screen(screen, SCORE, pygame, SCREEN, BLACK_BLUE, BLACK, RED, GameState):
        # Create Chris
        chris = ChrisClass(screen, pygame)
        # Create Intro Text
        introText1 = IntroText(
            msg="Fin de la partie!",
            pos = (400, 50), 
            text_rgb=BLACK_BLUE,
            screen = screen
        )
        introText2 = IntroText(
            msg="Merci d'avoir aidé Chris à retrouver ses dents.",
            pos = (400, 80), 
            text_rgb=BLACK_BLUE,
            screen = screen
        )

        final_score = FinalScoreClass(
            msg="Score: "+str(SCORE[0])+"/10",
            pos = (400, 140), 
            text_rgb=BLACK_BLUE,
            screen = screen
        )

        
        # Create Buttons
        startButton = ButtonClass(
            center_position=(400, 250),
            font_size=40,
            text_rgb=BLACK,
            text="Rejouer",
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
            final_score.render()


            for button in buttons:
                btn_action = button.update(pygame.mouse.get_pos(), mouse_up)
                if btn_action is not None:
                    return btn_action
                button.render(screen)


            pygame.display.flip()