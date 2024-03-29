import image
from settings import *
import background_type

class Background:
    def __init__(self, level, type: background_type):
        """
        Initialize the Background object.

        This method loads the background image and assigns it to the `image` attribute.

        Parameters:
        None

        Returns:
        None
        """
        if (type == background_type.game):
            background_number = level if level <= 7 else (level % 7) + 1
            self.image = image.load(
                f"Assets/background/background{background_number}.jpg",
                size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                convert="default"
            )

        elif (type == background_type.instruction):
            self.image = image.load(
                f"Assets/background/instruction_background.jpg",
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
