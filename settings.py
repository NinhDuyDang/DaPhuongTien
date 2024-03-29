import pygame

WINDOW_NAME = "Nhom Da Phuong Tien "
GAME_TITLE = WINDOW_NAME

INSTRUCTION_HEAD ="Instructions for playing the game"
CONTENT1 ="Players use hand gestures to interact with the screen."
CONTENT2 ="When hands are closed it is counted as catching objects" 
CONTENT3 ="Each time the player successfully catch zombie, the score increases 1 value"
CONTENT4 ="Each time the player successfully catch angel, the score decreases 1 value"
CONTENT5 ="Each time the player successfully catch boom, the score increases 5 value"
CONTENT6 ="Each time the player reach the level's goal score, they game move to a next level"
CONTENT7 ="The number of extra points for the next game will be calculated by dividing "
CONTENT8 = "The number of points exceeding the target in the previous game by 3"

# Người chơi sử dụng cử chỉ của tay để tương tác với các đối tượng trên màn hình.
# Khi tay đóng (hand_tracking.hand_closed), người chơi có thể "vỗ" hoặc thực hiện hành động tương tự để tương tác với các đối tượng trên màn hình.
# Điểm Số:

# Mỗi lần người chơi tương tác thành công với một đối tượng (zombie, thiên thần), điểm số tăng lên.
# Hệ số điểm có thể được tính dựa trên cách người chơi tương tác (vỗ tay hay làm hành động khác).
# Cấp Độ và Mục Tiêu:

# Mỗi khi người chơi vượt qua mục tiêu điểm của một cấp độ, họ chuyển lên cấp độ mới.
# Mục tiêu điểm của cấp độ mới được tính toán theo công thức goal = 100 * level * 2.

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
ZOMBIES_SIZES = (50, 38)
ZOMBIE_SIZE_RANDOMIZE = (1,2) # for each new zombie, it will multiply the size with an random value between X and Y
ANGEL_SIZES = (50, 50)
ANGEL_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 3 # the frame of the zombies will change every X sec

# difficulty
GAME_DURATION = 30 # the game will last X sec
ZOMBIES_SPAWN_TIME = 1
ZOMBIES_MOVE_SPEED = {
  "min": 0.5,
  "max": 2
}
ANGEL_PENALTY = 1 # will remove X of the score of the player (if you kills a angel)

BOOM_BONUS = 5

# colors
COLORS = {
  "title": (38, 61, 39),
  "score": (38, 61, 39),
  "timer": (38, 61, 39),
  "buttons": {
    "default": (56, 67, 209),
    "second":  (87, 99, 255), # second is the color when the mouse is on the button
    "text": (255, 255, 255), "shadow": (46, 54, 163)
  },
  "instruction": (255, 255, 255)
}

# sounds / music
MUSIC_VOLUME = 0.3 # value between 0 and 1
SOUNDS_VOLUME = 0.3 # value between 0 and 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 30)
FONTS["medium"] = pygame.font.Font(None, 40)
FONTS["big"] = pygame.font.Font(None, 60)