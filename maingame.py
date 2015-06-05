__author__ = 'Erick'
import sys
import pygame
import random

from pygame.locals import *
from classes.Star import Star
from classes.Background import Background
from classes.spaceship import SpaceShip
from classes.Tree import Tree
from classes.Weapon import Weapon
from classes.spritesheet import SpriteSheet
from classes import constants
from classes.enemy import Enemy

# TODO: Rewrite Menu Interface to start game

class MainGame:
    def __init__(self, level):
        pygame.mixer.pre_init()
        pygame.init()
        pygame.display.set_caption("EX-54: Dead of Night")
        info = pygame.display.Info()
        constants.window_w = info.current_w - 200
        constants.window_h = info.current_h - 200
        constants.load_sounds()
        constants.load_images()
        if level == 'mars':
            constants.GROUND = (255, 255, 102)
            constants.SKY = (128, 0, 0)
            constants.tree = pygame.image.load('images/rock.png')
        if level == 'ocean':
            constants.GROUND = (255, 255, 102)
            constants.SKY = (0, 0, 50)
            constants.tree = pygame.image.load('images/fish.png')
        run_game()

def run_game():
    fps_clock = pygame.time.Clock()
    surface = pygame.display.set_mode((constants.window_w, constants.window_h))
    main_bg = draw_background(surface)
    # Create player ship and enemy
    main_ship = SpaceShip(pygame.image.load("images\spaceship.png"), 100, 100)
    cannon = Enemy(pygame.image.load("images\cannon.gif"))
    explosion_img = SpriteSheet('images\explosion.png')
    # Start music
    pygame.mixer.music.load('sounds\music.ogg')
    pygame.mixer.music.play()
    # Set variables
    enemy_munitions = []
    enemy_hits = []
    difficulty = constants.difficulty['easy']
    distance = 0
    font = pygame.font.SysFont('Calibri', 20, True, False)
    distance_text = font.render("Distance", True, constants.WHITE)

    while True:
        # TODO: What the heck does weapon_cnt do??
        weapon_cnt = 0
        if distance > constants.goal:
            ending(surface, main_bg, main_ship, cannon, explosion_img, fps_clock)
            menu(surface)
            main_ship = SpaceShip(pygame.image.load("images\spaceship.png"), 100, 100)
            cannon.reset()
            enemy_munitions = []
            distance = 0

        for event in pygame.event.get():
            vy = 0
            vx = 0
            pressed = pygame.key.get_pressed()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if pressed[K_w] or pressed[K_UP]:
                vy -= 5
            elif pressed[K_s] or pressed[K_DOWN]:
                vy += 5
            elif pressed[K_a] or pressed[K_LEFT]:
                vx -= 5
            elif pressed[K_d] or pressed[K_RIGHT]:
                vx += 5
            elif pressed[K_SPACE]:
                menu(surface)

# Generate randomized missiles

        if random.randint(0, difficulty) == 1:
            if not len(enemy_munitions) > 9:
                enemy_boom = Weapon(constants.window_w, random_loc(constants.window_h), constants.enemy_missile_img,
                                    'enemy')
                enemy_munitions.append(enemy_boom)
                enemy_hits.append(enemy_boom)

# Check for hits and update health

        if len(enemy_munitions) > 1:
            ship_hit_list = pygame.sprite.spritecollide(main_ship, enemy_hits, False)
            if len(ship_hit_list) > 0:
                for weapon in ship_hit_list:
                    if not weapon.exploded:
                        weapon.exploded = True
                        weapon.explode(explosion_img)
                        main_ship.health -= 10
                if main_ship.health <= 0:
                    main_ship.explode(explosion_img)
                    menu(surface)
# TODO: Write reset function

                    main_ship = SpaceShip(pygame.image.load("images\spaceship.png"), 100, 100)
                    enemy_munitions = []
                    distance = 0

# Redraw all relevant elements

        main_ship.move(surface, vy, vx)
        move_bg(main_bg, surface)

        for weapon in enemy_munitions:
            weapon.fall()
            weapon.draw(surface, explosion_img)
            if weapon.exploded:
                enemy_munitions.pop(weapon_cnt)
            weapon_cnt += 1

        main_ship.draw(surface)
        cannon.draw(surface)

        text = font.render("Health: " + str(main_ship.health) + "/ 100", True, constants.WHITE)
        surface.blit(text, [200, 10])
        surface.blit(distance_text, (10, 10))
        draw_distance(surface, distance, goal)

# Update Screen and increase the distance the player has traveled

        pygame.display.update()
        fps_clock.tick(constants.fps)
        distance += 1


def draw_background(surface):
    """
    Creates an instance of Background, and defines the properties of the class.
    :param surface: Pygame display object
    :return: instance of Background.
    """
    stars = draw_stars(surface)
    draw_ground(surface)
    trees = draw_trees(surface)
    return Background(stars, trees)


def draw_distance(surface, distance, goal):
    progress = 100 * (distance / goal)
    pygame.draw.rect(surface, (0, 0, 0, 0), (85, 14, 100, 10))
    pygame.draw.rect(surface, constants.WHITE, (86, 14, progress, 10))
    pygame.draw.rect(surface, constants.GROUND, (85, 14, 100, 10), 2)


def draw_stars(surface):
    """
    Creates multiple star objects using the provided image and displays them on the screen.
    :param surface: Pygame display object
    :return:
        star_list: a list of all the star created by the function, to be set as a property of Background.
    """
    height_with_buffer = (constants.window_h / 2) - 10
    star_list = []
    for i in range(1, 100):
        s = Star((random_loc(constants.window_w)), random_loc(height_with_buffer))
        star_list.append(s)
        pygame.draw.circle(surface, constants.WHITE, (s.get_x(), s.get_y()), 1, 0)
    return star_list


def draw_ground(surface):
    """
    Draws a simple green rectangle which acts as the ground.
    :param surface: Pygame display object
    :return:
    """
    pygame.draw.rect(surface, constants.GROUND, (0, constants.window_h / 2, constants.window_w,
                                                 constants.window_h / 2), 0)


def random_loc(constraint, x=0):
    """
    random_loc is used to randomly place elements in the background
    :param constraint: Upper limit for randint()
    :param x: Lower limit for randint(). Defaults to zero.
    :return: random value based on random.randint()
    """
    return random.randint(x, constraint)


def move_bg(main_bg, surface):
    """
    move_bg creates the illusion of movement by shifting all elements of class Background to the left 5 pixels.
    :param main_bg: The single background instance responsible for all elements drawn in the background.
    :param surface: Pygame display object
    :return: Nothing is returned
    """
    surface.fill(constants.SKY)
    draw_ground(surface)
    for s in main_bg.get_stars():
        s.move(surface)
    for t in main_bg.get_trees():
        t.move(surface)
    font = pygame.font.SysFont('Calibri', 14, True, False)
    text = font.render("WASD to Move", True, constants.WHITE)
    surface.blit(text, [constants.window_w - 210, 10])


def draw_trees(surface):
    """
    Creates multiple tree objects using the provided image and displays them on the screen.
    :param surface: Pygame display object
    :return:
        tree_list: a list of all the trees created by the function, to be set as a property of Background.
    """
    height_buffer = constants.window_h / 2
    tree_list = []
    for i in range(1, 10):
        t = Tree(constants.tree, random_loc(constants.window_w),
                 random_loc(constants.window_h, height_buffer))
        tree_list.append(t)
        t.draw_tree(surface)
    return tree_list


def pause(surface):
    font = pygame.font.SysFont('Calibri', 14, True, False)
    font_text = font.render('Paused', True, constants.WHITE)
    surface.blit(font_text, (constants.window_w / 2, constants.window_h / 2))
    pygame.display.update()
    paused = True
    while paused:
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif pressed[K_ESCAPE]:
                paused = False


def menu(surface):
    font_menu = pygame.font.SysFont('Helvetica', 32, True, False)
    font_title = pygame.font.SysFont('Helvetica', 64, True, False)

    txt_title = 'EX-54: Dead of Night'
    txt_play = 'PLAY'
    txt_exit = 'EXIT'

    size_title = font_title.size(txt_title)
    size_play = font_menu.size(txt_play)

    txt_play_pos = (constants.window_w - size_play[0] - 10, constants.window_h - 40)
    txt_exit_pos = (10, txt_play_pos[1])
    txt_title_pos = (constants.window_w / 2 - (size_title[0] / 2), constants.window_h / 2 - (size_title[1] / 2))

    rndr_title = font_title.render(txt_title, True, constants.WHITE)
    rndr_play = font_menu.render(txt_play, True, constants.WHITE)
    rndr_exit = font_menu.render(txt_exit, True, constants.WHITE)

    surface.blit(rndr_play, txt_play_pos)
    surface.blit(rndr_exit, txt_exit_pos)
    surface.blit(rndr_title, txt_title_pos)
    pygame.display.update()
    pygame.mixer.music.pause()
    paused = True
    while paused:
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif pressed[K_SPACE]:
                paused = False
                pygame.mixer.music.unpause()


def ending(surface, main_bg, main_ship, cannon, explosion_img, fps_clock):
    end_running = True
    bombs_away = False
    cannon_moving = True
    pos_x = constants.window_w
    while end_running:
        move_bg(main_bg, surface)
        main_ship.draw(surface)
        if not main_ship.get_x() >= constants.window_w / 2:
            main_ship.move(surface, -5, 5)
        else:
            if not cannon_moving:
                if not bombs_away:
                    bomb = Weapon(main_ship.get_x(), main_ship.get_y(), constants.bomb_img, 'bomb')
                    bombs_away = True
                else:
                    if not bomb.exploded:
                        cannon.end_draw(surface, pos_x)
                        pos_x -= 5
                    bomb.draw(surface, explosion_img)
                    bomb.fall()
            else:
                cannon.end_draw(surface, pos_x)
                pos_x -= 5
                if cannon.get_x() < constants.window_w / 2 + 300:
                    cannon_moving = False
        if bombs_away and bomb.exploded:
            if main_ship.get_x() >= constants.window_w - 150:
                end_running = False
            main_ship.move(surface, 0, 5)
        fps_clock.tick(constants.fps)
        pygame.display.update()


MainGame('ocean')
