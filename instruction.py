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
      COLORS["title"],
      font=FONTS["big"],
      shadow=True,
      shadow_color=(255,255,255),
      pos_mode="center"
    )

    ui.draw_text(
      self.surface,
      CONTENT1,
      (SCREEN_WIDTH//2, 210),
      COLORS["instruction"],
      font=FONTS["medium"],
      shadow=False,
      shadow_color=(255,255,255),
      pos_mode="center"
    )
    ui.draw_text(
      self.surface,
      CONTENT2,
      (SCREEN_WIDTH//2, 260),
      COLORS["instruction"],
      font=FONTS["medium"],
      shadow=False,
      shadow_color=(255,255,255),
      pos_mode="center"
    )
    ui.draw_text(
      self.surface,
      CONTENT3,
      (SCREEN_WIDTH//2, 310),
      COLORS["instruction"],
      font=FONTS["medium"],
      shadow=False,
      shadow_color=(255,255,255),
      pos_mode="center"
    )
    ui.draw_text(
      self.surface,
      CONTENT4,
      (SCREEN_WIDTH//2, 360),
      COLORS["instruction"],
      font=FONTS["medium"],
      shadow=False,
      shadow_color=(255,255,255),
      pos_mode="center"
    )
    ui.draw_text(
      self.surface,
      CONTENT6,
      (SCREEN_WIDTH//2, 410),
      COLORS["instruction"],
      font=FONTS["medium"],
      shadow=False,
      shadow_color=(255,255,255),
      pos_mode="center"
    )
    ui.draw_text(
      self.surface,
      CONTENT7,
      (SCREEN_WIDTH//2, 460),
      COLORS["instruction"],
      font=FONTS["medium"],
      shadow=False,
      shadow_color=(255,255,255),
      pos_mode="center"
    )
    ui.draw_text(
      self.surface,
      CONTENT8,
      (SCREEN_WIDTH//2, 510),
      COLORS["instruction"],
      font=FONTS["medium"],
      shadow=False,
      shadow_color=(255,255,255),
      pos_mode="center"
    )

  def update(self):
    self.draw()

    if ui.button(self.surface, 5, "Back", click_sound=self.sound, pos_x=5):
      
      return state_value.menu
