from classes import constants
import pygame


class Star:
    """
    Class star represents every star object in game. Consists of the image and position.
    """
    __num_stars = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Star.__num_stars += 1

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def move(self, surface):
        new_x = self.__x - 1
        if new_x < 0:
            new_x = constants.window_w
        self.__x = new_x
        pygame.draw.circle(surface, constants.WHITE, (self.__x, self.__y), 1, 0)
