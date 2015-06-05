__author__ = 'Erick'
from classes import constants
import pygame

class Menu:

    def __init__(self, surface):
        self.__choice = 3
        surface.fill(constants.SKY)

        font_menu = pygame.font.SysFont('Helvetica', 32, True, False)
        font_title = pygame.font.SysFont('Helvetica', 64, True, False)

        txt_title = 'EX-54: Dead of Night'
        txt_play = 'PLAY'
        txt_exit = 'EXIT'

        size_title = font_title.size(txt_title)
        size_play = font_menu.size(txt_play)

        self.__txt_play_pos = (constants.window_w - size_play[0] - 10, constants.window_h - 40)
        self.__txt_exit_pos = (10, self.__txt_play_pos[1])
        txt_title_pos = (constants.window_w / 2 - (size_title[0] / 2), constants.window_h / 2 - (size_title[1] / 2))

        rndr_title = font_title.render(txt_title, True, constants.WHITE)
        rndr_play = font_menu.render(txt_play, True, constants.WHITE)
        rndr_exit = font_menu.render(txt_exit, True, constants.WHITE)

        surface.blit(rndr_play, self.__txt_play_pos)
        surface.blit(rndr_exit, self.__txt_exit_pos)
        surface.blit(rndr_title, txt_title_pos)

    def select(self, surface, choice):
        if choice == 0:
            pos = self.__txt_exit_pos
        if choice == 1:
            pos = self.__txt_play_pos

        pygame.draw.line(surface, constants.GROUND, (pos[0], pos[1] + 30), (pos[0] + 55, pos[1] + 30), 10)
