__author__ = 'Erick'
import pygame
from classes import constants

class Enemy(pygame.sprite.Sprite):
    """
    Class Enemy represents the end goal. Consists of the image and coordinates.
    """
    def __init__(self, img):
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = constants.window_w - self.rect.size[0]
        self.rect.y = constants.window_h - self.rect.size[1] + 10
        self.explode_pos_x = 0
        self.explode_pos_y = 0
        self.exploded = False

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def draw(self, surface):
        pygame.draw.rect(surface, constants.SKY, (constants.window_w - 304, 400, 304, 200), 0)
        pygame.draw.rect(surface, (0, 0, 0), (constants.window_w - 308, 400, 310, 200), 6)
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def end_draw(self, surface, x):
        self.rect.x = x
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def explode(self, explosion):
        self.explode_pos_x += 48
        self.image = explosion.image_at((self.explode_pos_x, 0, 58, 128), colorkey=(0, 0, 0))
        if self.explode_pos_x >= 128:
            self.exploded = True

    def reset(self):
        self.exploded = False
        self.rect.x = constants.window_w - self.rect.size[0]
        self.rect.y = constants.window_h - self.rect.size[1] + 10
