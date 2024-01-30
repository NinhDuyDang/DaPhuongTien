import pygame

def load(img_path, size="default", convert="alpha", flip=False):
    """
    Load an image from the given file path and perform optional transformations.

    Args:
        img_path (str): The path to the image file.
        size (str, optional): The size of the image. Defaults to "default".
        convert (str, optional): The conversion mode for the image. Defaults to "alpha".
        flip (bool, optional): Whether to flip the image horizontally. Defaults to False.

    Returns:
        pygame.Surface: The loaded and transformed image.
    """
    if convert == "alpha":
        img = pygame.image.load(img_path).convert_alpha()
    else:
        img = pygame.image.load(img_path).convert()

    if flip:
        img = pygame.transform.flip(img, True, False)

    if size != "default":
        img = scale(img, size)

    return img

def scale(img, size):
    return pygame.transform.smoothscale(img, size)

def draw(surface, img, pos, pos_mode="top_left"):
    if pos_mode == "center":
        pos = list(pos)
        pos[0] -= img.get_width()//2
        pos[1] -= img.get_height()//2
    surface.blit(img, pos)
