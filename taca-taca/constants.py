import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "TACA-TACA"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "taca-taca/assets/fonts/Proline.otf"
FONT_FILE_SCORE = "taca-taca/assets/fonts/WoodenLog.ttf"
FONT_SMALL = 40
FONT_LARGE = 50

# SOUND
KICK_SOUND = "taca-taca/assets/sounds/kick.wav"
WELCOME_SOUND = "taca-taca/assets/sounds/whistle.wav"
GOAL_SOUND = "taca-taca/assets/sounds/goal.wav"
OVER_SOUND = "taca-taca/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
GREEN = Color(0,100,0)

# KEYS
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
W = "w"
S = "s"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4


# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"

# HUD
HUD_MARGIN = 15
SCORE_P1_GROUP = "Red Team"
SCORE_P2_GROUP = "Black Team"
SCORE_P1_FORMAT = "Red Team: {}"
SCORE_P2_FORMAT = "Black Team: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "taca-taca/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# TEAM
TEAM_GROUP = "team"
TEAM_IMAGES = [f"taca-taca/assets/images/{n:03}.png" for n in range(101, 103)]
TEAM_WIDTH = 28
TEAM_HEIGHT = 106
TEAM_RATE = 6
TEAM_VELOCITY = 7

TEAM_TWO_GROUP = "teamtwo"
TEAM_TWO_IMAGES = [f"taca-taca/assets/images/{n:03}.png" for n in range(103, 106)]


# GOAL
GOAL_GROUP = "goals"
GOAL_IMAGES = "taca-taca/assets/images/goalLeft.png"
GOAL_RIGHT = "taca-taca/assets/images/goalright.png"
GOAL_WIDTH = 50
GOAL_HEIGHT = 300
GOALR_WIDTH = 80
GOALR_HEIGHT = 300  
GOAL_DELAY = 0.5
GOAL_RATE = 4
GOAL_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
PREP_TO_LAUNCH = "PREPARING TO PLAY"
ENTER_TO_START = "PRESS ENTER TO START"
PLAYER_ONE_WIN = "RED TEAM IS THE WINNER!"
PLAYER_TWO_WIN = "BLACK TEAM IS THE WINNER!"