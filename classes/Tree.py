__author__ = 'Erick'
import pygame
from classes import constants


class Tree(pygame.sprite.Sprite):
    """
    Class Tree represents every tree in-game. Consists of the image object, an x position, and y position.
    """

    def __init__(self, img, x, y):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_tree(self):
        return self.image

    def draw_tree(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, surface):
        new_x = self.rect.x - 7
        if new_x <= -133:
            new_x = constants.window_w
        self.rect.x = new_x
        surface.blit(self.image, (self.rect.x, self.rect.y))
