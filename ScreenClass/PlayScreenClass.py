import random
from ElementsClass.ButtonClass import ButtonClass
from ElementsClass.TeethClass import TeethClass
from ElementsClass.PopcornClass import PopcornClass
from ElementsClass.ScoreClass import ScoreClass
from ElementsClass.TimerClass import TimerClass

class PlayScreenClass:
    def __init__(self):
        pass

    # # # Timer function # # #
    def timer_run(self, new_countdown, timer_instances, screen, BLACK_BLUE):
        for timer in timer_instances:
            timer.hide()
        new_timer = TimerClass(
            second = new_countdown,
            pos = (screen.get_width()-(screen.get_width()/10), 25), 
            text_rgb=BLACK_BLUE,
            screen = screen
        )
        timer_instances.append(new_timer)

    def play_screen(self, screen, pygame, clock, SCREEN, BLACK_BLUE, BLACK, SCORE, GameState):
        back_btn = ButtonClass(
            center_position=(55, 20),
            font_size=18,
            text_rgb=BLACK,
            text="<- Retour",
            action=GameState.HOME,
        )

        array_of_pops=[]
        array_of_teeth=[]
        cpt = 0
        loop = 0
        loop2 = 0

        while loop2 < 10:
            teeth = TeethClass(
                screen = screen,
                pos_x= random.randint(20, (screen.get_width()-30)),
                pos_y= random.randint(50, (screen.get_height()-20)),
            )
            if teeth.pos_x < (screen.get_width()-20) and teeth.pos_y < (screen.get_height()-20):
                array_of_teeth.append(
                    teeth
                )
                loop2 = loop2 +1


        while loop < 200:
            cpt = cpt+1
            popcorn = PopcornClass(
                screen = screen,
                pos_x= random.randint(20, (screen.get_width()-30)),
                pos_y= random.randint(50, (screen.get_height()-20)),
                imgId= cpt
            )
            if cpt == 10:
                cpt = 0
            if popcorn.pos_x < (screen.get_width()-20) and popcorn.pos_y < (screen.get_height()-20):
                array_of_pops.append(
                    popcorn
                )
                loop = loop +1

        # Score
        score_instances = []
        new_score = 0
        score = ScoreClass(
            score=new_score,
            pos = (screen.get_width()-(screen.get_width()/2), 25), 
            text_rgb=BLACK_BLUE,
            screen = screen
        )
        score_instances.append(score)

        # Timer
        timer_instances = []
        countdown = 30
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        timer = TimerClass(
            second = str(countdown),
            pos = (screen.get_width()-(screen.get_width()/10), 25), 
            text_rgb=BLACK_BLUE,
            screen = screen
        )
        timer_instances.append(timer)

        while True:
            screen.fill(SCREEN)
            mouse_up = False

            # Show Score
            for score in score_instances:
                score.render()
            
            # Show Timer
            for timer in timer_instances:
                timer.render()
    
            # Show teeth
            for teeth in array_of_teeth:
                if not teeth.is_selected:
                    teeth.update(pygame.mouse.get_pos())
                teeth.render()

            # Show popcorns
            for pop in array_of_pops:
                pop.render()
            
            for event in pygame.event.get():
                # Run Timer
                if event.type == pygame.USEREVENT: 
                    if countdown > 0 :
                        new_countdown = countdown - 1
                    if new_countdown > 9:
                        self.timer_run((str(new_countdown)), timer_instances, screen, BLACK_BLUE)
                    else:
                        self.timer_run("0"+str(new_countdown), timer_instances, screen, BLACK_BLUE)
                    countdown = new_countdown
                # End - Run Timer

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
                    # Handle teeth selected
                    for teeth in array_of_teeth:
                        #  This function return the new score value
                        new_score = teeth.select(pygame.mouse.get_pos(), mouse_up, score_instances, new_score, BLACK_BLUE)
                    
                    # Handle pop selected
                    for pop in array_of_pops:
                        # This function return .......
                        pass

            # Action for go back
            btn_action = back_btn.update(pygame.mouse.get_pos(), mouse_up)
            if btn_action is not None:
                return btn_action
            back_btn.render(screen)

            # Action for stop game by good score
            if new_score == 10 :
                SCORE.append(new_score)
                return GameState.ENDGAME
            
            #Action for stop game by times'up
            if countdown == 0 :
                SCORE.append(new_score)
                return GameState.ENDGAME
                
            pygame.display.flip()
            clock.tick(60)