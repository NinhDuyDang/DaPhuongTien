# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
from settings import *
from game import Game
from menu import Menu
import state_value
from instruction import Instruction

# Setup pygame/window --------------------------------------------- #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,32) # windows position
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

mainClock = pygame.time.Clock()

# Fonts ----------------------------------------------------------- #
fps_font = pygame.font.SysFont("coopbl", 22)

# Music ----------------------------------------------------------- #
pygame.mixer.music.load("Assets/Sounds/y2mate.com - Shiverr  Whize  Nhạc nền kinh dị gây ám ảnh Tiktok.mp3")
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1)
# Variables ------------------------------------------------------- #
state = "menu"

# Creation -------------------------------------------------------- #
game = Game(SCREEN)
menu = Menu(SCREEN)
instruction = Instruction(SCREEN)

# Functions ------------------------------------------------------ #
def user_events():
    """
    Process user events such as quitting the game or pressing the escape key.

    This function iterates over the events in the Pygame event queue and handles
    specific events such as quitting the game when the window is closed or
    pressing the escape key to quit the game.

    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_game()

def update():
    """
    Updates the game state based on the current state value.

    If the current state is 'menu', it checks for menu updates and performs corresponding actions.
    If the current state is 'game', it checks for game updates and performs corresponding actions.
    If the current state is 'instruction', it checks for instruction updates and performs corresponding actions.

    The function also updates the display and controls the frame rate.
    """
    global state
    if state == state_value.menu:
        if menu.update() == state_value.game:
            start_game()
        if menu.update() == state_value.quit_game:
            quit_game()
        if menu.update() == state_value.instruction:
            show_instruction()
    elif state == state_value.game:
        if game.update() == state_value.quit_game:
            quit_game()
        if game.update() == state_value.menu:
            state = state_value.menu
    elif state == state_value.instruction:
        if instruction.update() == state_value.menu:    
            state = state_value.menu
    pygame.display.update()
    mainClock.tick(FPS)

def start_game():
    global state
    game.start() # reset the game to start a new game
    state = state_value.game

def quit_game():
    pygame.quit()
    sys.exit()

def show_instruction():
    global state
    state = state_value.instruction
    instruction.update()

# Loop ------------------------------------------------------------ #
while True:
    # Buttons ----------------------------------------------------- #
    user_events()
    # Update ------------------------------------------------------ #
    update()
    # FPS
    if DRAW_FPS:
        fps_label = fps_font.render(f"FPS: {int(mainClock.get_fps())}", 1, (255,200,20))
        SCREEN.blit(fps_label, (5,5))
