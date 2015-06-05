__author__ = 'Erick'

import pygame
import sys
from pygame.locals import *

NIGHT_SKY_PURPLE = pygame.Color(30, 0, 50)


def main():
    global window_h
    global window_w
    pygame.init()
    # #Frames-per-second for the game
    fps = 30
    fps_clock = pygame.time.Clock()
    font = pygame.font.SysFont('Calibri', 64, True, False)
    info = pygame.display.Info()
    window_w = info.current_w - 200
    window_h = info.current_h - 200
    surface = pygame.display.set_mode((window_w, window_h))
    surface.fill(NIGHT_SKY_PURPLE)
    text = font.render('EX-54: Into the Night', True, (255, 255, 255))
    surface.blit(text, (0, 100))
    rect = pygame.Surface((window_w, window_h), pygame.SRCALPHA)
    rect.fill((70, 70, 70, 128))
    rect.blit(text, (0, 0))
    y = window_h / 4
    x = window_w / 7
    for i in range(0, 10):
        pygame.draw.rect(rect, (0, 0, 0), (x, y, 100, 100), 0)
        x += window_w / 7
        if x >= window_w - window_w / 7:
            x = window_w / 7
            y += window_w / 4
    surface.blit(rect, (0, 0))
    pygame.display.set_caption("Testing Lab")
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        fps_clock.tick(fps)

if __name__ == "__main__":
    main()