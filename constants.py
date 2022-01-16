from pygame import USEREVENT

# настройки экрана
WIDTH = 960
HEIGHT = 540
FPS = 60

# настройки скорости передвижения
WALK_SPEED = 5
FALLING_SPEED = 0.5
JUMPING_SPEED = 12

# настройки лоцкации
BRICK_SIZE = 20
X_BRICKS = 48
Y_BRICKS = 27

# пользовательские ивенты
ATTACK_END = USEREVENT + 1
PLAYER_IMMORTALITY = USEREVENT + 1
ENEMY_IMMORTALITY = USEREVENT + 1

# размеры игрока
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
