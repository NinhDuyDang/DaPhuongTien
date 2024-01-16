import pygame
import image
from settings import *

class Background:
    def __init__(self):
        """
        Initialize the Background object.

        This method loads the background image and assigns it to the `image` attribute.

        Parameters:
        None

        Returns:
        None
        """
        self.image = image.load(
            "Assets/background.jpg",
            size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            convert="default"
        )


    def draw(self, surface):
        """
        Draw the background image on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw on.
        """
        image.draw(surface, self.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")
