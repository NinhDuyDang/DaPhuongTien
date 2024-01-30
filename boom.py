import random
from settings import *
from zombie import Zombie
import image

# Inheritance from Zombie
class Boom(Zombie):
  def __init__(self):
    random_size_value = random.uniform(ZOMBIE_SIZE_RANDOMIZE[0], ZOMBIE_SIZE_RANDOMIZE[1])
    size = (int(ZOMBIES_SIZES[0] * random_size_value), int(ZOMBIES_SIZES[1] * random_size_value))
    moving_direction, start_pos = self.define_spawn_pos(size)
    self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
    self.images = [image.load("Assets/boom.png", size=size, flip=moving_direction=="right")]
    self.current_frame = 0
    self.animation_timer = 0
  
  def kill(self, zombies):
    zombies.remove(self)
    return BOOM_BONUS