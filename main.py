import pygame
import pygame.freetype

from ElementsClass.GameState import GameState
from ScreenClass.HomeScreenClass import HomeScreenClass
from ScreenClass.PlayScreenClass import PlayScreenClass
from ScreenClass.EndGameScreen import EndGameScreen

SCREEN = (192, 198, 200)
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACK_BLUE = (3, 34, 76)
RED = (255,0,0)
SCORE = []

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    # For Timer
    clock = pygame.time.Clock()

    game_state = GameState.HOME

    home_screen = HomeScreenClass
    play_screen = PlayScreenClass()
    end_game_screen = EndGameScreen

    while True:
        if game_state == GameState.HOME:
            game_state = home_screen.home_screen(screen, pygame, SCREEN, BLACK_BLUE, BLACK, RED, GameState)

        if game_state == GameState.NEWGAME:
            game_state = play_screen.play_screen(screen, pygame, clock, SCREEN, BLACK_BLUE, BLACK, SCORE, GameState)

        if game_state == GameState.ENDGAME:
            game_state = end_game_screen.end_game_screen(screen, SCORE, pygame, SCREEN, BLACK_BLUE, BLACK, RED, GameState)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

# call main when the script is run
if __name__ == "__main__":
    main()