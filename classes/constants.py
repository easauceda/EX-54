__author__ = 'Erick'
import pygame
from classes.spritesheet import SpriteSheet

WHITE = pygame.Color(255, 255, 255)
GROUND = pygame.Color(2, 74, 0)
SKY = pygame.Color(30, 0, 50)
laser = pygame.mixer.Sound
rocket = pygame.mixer.Sound
missile_ammo = 50
bomb_ammo = 50
window_h = 800
window_w = 800
fps = 60
bomb_img = pygame.image
missile_img = pygame.image
enemy_missile_img = pygame.image
difficulty = {'easy': 70, 'medium': 40, 'hard': 20, 'death': 5}
tree = pygame.image
goal = 3000


def load_sounds():
    global laser
    global impact
    laser = pygame.mixer.Sound('sounds/rocket.ogg')
    impact = pygame.mixer.Sound('sounds/laser.ogg')


def load_images():
    global bomb_img
    global missile_img
    global enemy_missile_img
    global tree
    bomb_img = pygame.image.load("images/boom.png")
    missile_img = pygame.image.load("images/bomb.gif")
    enemy_missile_img = pygame.image.load("images/enemy.gif")
    tree = pygame.image.load("images/tree_alt.png")
