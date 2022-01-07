from pygame import USEREVENT

# настройки экрана
WIDTH = 960
HEIGHT = 540

# настройки скорости передвижения
WALK_SPEED = 5
FALLING_SPEED = 0.5
JUMPING_SPEED = 12
ENEMY_WALK_SPEED = 3

# настройки лоцкации
BRICK_SIZE = 20

# пользовательские ивенты
ATTACK_END = USEREVENT + 1
PLAYER_IMMORTALITY = USEREVENT + 1
