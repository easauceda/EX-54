__author__ = 'Erick'
import pygame

WHITE = pygame.Color(255, 255, 255)
GROUND = pygame.Color(2, 74, 0)
SKY = pygame.Color(30, 0, 50)
laser = pygame.mixer.Sound
rocket = pygame.mixer.Sound
missile_ammo = 50
bomb_ammo = 50
window_h = 800
window_w = 800
fps = 120
bomb_img = pygame.image
missile_img = pygame.image
enemy_missile_img = pygame.image
difficulty = {'easy': 50, 'medium': 20, 'hard': 10, 'death': 2}
bg_sprite = pygame.image
goal = 300
selected_difficulty = {}


def load_sounds():
    """
    Since pygame must be initialized before any sounds can be loaded, this function sets the laser and impact sounds
    for the game.
    :return:
    """
    global laser
    global impact
    laser = pygame.mixer.Sound('sounds/rocket.ogg')
    impact = pygame.mixer.Sound('sounds/laser.ogg')


def load_images():
    """
    Since pygame must be initialized before any sounds can be loaded, this function loads and sets images
    for the game.
    :return:
    """
    global bomb_img
    global missile_img
    global enemy_missile_img
    global bg_sprite
    bomb_img = pygame.image.load("images/boom.png")
    missile_img = pygame.image.load("images/bomb.gif")
    enemy_missile_img = pygame.image.load("images/enemy.gif")
    bg_sprite = pygame.image.load("images/tree_alt.png")
