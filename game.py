import pygame
import time
import random
from boom import Boom
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from zombie import Zombie
from angel import Angel
import cv2
import ui
import state_value
import background_type

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background(1, background_type.game)

        # Load camera
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["slap"] = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
        self.sounds["slap"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"Assets/Sounds/screaming.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)

    def start (self):
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.animators = []
        self.animators_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()
        self.goal = 100
        self.level = 1

    def reset(self): # reset all the needed variables
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.animators = []
        self.animators_spawn_timer = 0
        self.game_start_time = time.time()
        self.background = Background(self.level, background_type.game)


    def spawn_animators(self):
        t = time.time()
        if t > self.animators_spawn_timer:
            # self.insects_spawn_timer = t + ZOMBIES_SPAWN_TIME

            # increase the probability that the animation will be a angel or a zombie over time
            nb = (GAME_DURATION-self.time_left)/GAME_DURATION * 100  /50  # increase from 0 to 50 during all  the game (linear)
            if random.randint(0, 20) < nb:
                self.animators.append(Angel(self.level))
            elif random.randint(20, 30) < nb:
                self.animators.append(Boom())
            else:
                self.animators.append(Zombie(self.level))

            # spawn a other zombie after the half of the game
            if self.time_left < GAME_DURATION/2:
                self.animators.append(Zombie(self.level + 1))

    def load_camera(self):
        _, self.frame = self.cap.read()


    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)

    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        # draw the animators
        for animator in self.animators:
            animator.draw(self.surface)
        # draw the hand
        self.hand.draw(self.surface)
        # draw the score
        ui.draw_text(
            self.surface,
            f"Score : {self.score}",
            (5, 5),
            COLORS["score"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255,255,255)
        )
        goal = self.goal
        ui.draw_text(
            self.surface,
            f"Goal : {goal} level : {self.level}",
            (SCREEN_WIDTH//1.5 + 10, 5),
            COLORS["score"],
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255,255,255),
        )
        # draw the time left
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] # change the text color if less than 5 s left
        ui.draw_text(
            self.surface,
            f"Time left : {self.time_left}",
            (SCREEN_WIDTH//2, 5),
            timer_text_color,
            font=FONTS["medium"],
            shadow=True,
            shadow_color=(255,255,255)
        )


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)



    def update(self):

        self.load_camera()
        self.set_hand_position()
        self.game_time_update()

        self.draw()

        if self.time_left > 0:
            self.spawn_animators()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            print("Hand closed", self.hand.left_click)
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()
            self.score = self.hand.kill_animators(self.animators, self.score, self.sounds)
            for animator in self.animators:
                animator.move()

        else: # when the game is over
            if ui.button(
                self.surface,
                320,
                "Continue" if self.score >= self.goal else "Retry",
                click_sound=self.sounds["slap"]
            ):
                if (self.score >= self.goal):
                    self.level += 1
                    nextGoal = 100 * self.level * 2
                    bonusPoint = self.score - self.goal
                    while (bonusPoint >= nextGoal):
                        nextGoal *= 2
                    self.goal = nextGoal
                    self.score = int(bonusPoint / 3)
                    self.reset()
                else:
                    self.score = 0
                    self.reset()
            elif ui.button(
                self.surface,
                320+BUTTONS_SIZES[1]*1.5,
                "Back",
                click_sound=self.sounds["slap"]
            ):
                return state_value.menu
            elif ui.button(
                self.surface,
                320+BUTTONS_SIZES[1]*3,
                "Quit",
                click_sound=self.sounds["slap"]
            ):
                return state_value.quit_game


        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
