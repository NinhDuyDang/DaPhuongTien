from background import Background
import pygame
import ui
import background_type
from settings import *
import state_value

class Instruction:
  def __init__(self, surface):
    self.surface = surface
    self.background = Background(1, background_type.instruction)
    self.sound = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
  
  def draw(self):
    self.background.draw(self.surface)
    ui.draw_text(
      self.surface,
      INSTRUCTION_HEAD,
      (SCREEN_WIDTH//2, 120),
      COLORS["instruction"],
      font=FONTS["big"],
      shadow=True,
      shadow_color=(255,255,255),
      pos_mode="center"
    )
  def update(self):
    self.draw()

    if ui.button(self.surface, 5, "Back", click_sound=self.sound, pos_x=5):
      
      return state_value.menu
