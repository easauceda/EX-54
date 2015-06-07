__author__ = 'Erick'
import pygame


class Weapon(pygame.sprite.Sprite):
    """
    Weapon class. Used to control all missiles on screen, detect collisions, and animate explosion upon collision.
    """

    def __init__(self, x, y, img, weapon_type):
        """
        Constructor.
        :param x: x position for weapon
        :param y: y position for weapon
        :param img: weapon image
        :param weapon_type: generally a missile, but during ending will be used to bomb the enemy.
        :return:
        """
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.explode_pos_x = 0
        self.explode_pos_y = 0
        self.exploded = False
        self.weapon_type = weapon_type

    def draw(self, surface, explosion):
        """
        Draw the weapon on screen.
        :param surface: Pygame Display object
        :param explosion: explosion animation
        :return:
        """
        if not self.weapon_type == 'enemy':
            b_collide = self.rect.y + self.image.get_height() > surface.get_height()
            r_collide = self.rect.x + self.image.get_width() > surface.get_width()

            if b_collide:
                self.rect.y = surface.get_height() - self.image.get_height()
                self.explode(explosion)
            if r_collide:
                self.rect.x = surface.get_width() - self.image.get_width()
        else:
            l_collide = self.rect.x + self.image.get_width() < 0
            if l_collide:
                self.rect.x = 0
                self.exploded = True
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def fall(self):
        """
        Moves the weapon object across the screen by updating the position of the weapon.
        :return:
        """
        if self.weapon_type == 'bomb':
            self.rect.y += 5
            self.rect.x += -1
        if self.weapon_type == 'enemy':
            self.rect.x -= 10
            self.rect.y += 0

    def explode(self, explosion):
        """
        Explosion for weapon object. Triggered upon collision. Flips the exploded boolean to flag the weapon object for
        cleanup in the main game loop.
        :param explosion:
        :return:
        """
        if self.weapon_type == 'bomb':
            self.rect.x += -10
            self.explode_pos_x += 128
            if self.explode_pos_x > 640:
                self.explode_pos_x = 0
                self.explode_pos_y += 128
            self.image = explosion.image_at((self.explode_pos_x, self.explode_pos_y, 128, 128), colorkey=(0, 0, 0))
        else:
            if self.explode_pos_x >= 320 and self.explode_pos_y >= 320:
                self.exploded = True
            self.explode_pos_x += 64
            if self.explode_pos_x > 320:
                self.explode_pos_x = 0
                self.explode_pos_y += 64
            self.image = explosion.image_at((self.explode_pos_x, self.explode_pos_y, 64, 64), colorkey=(0, 0, 0))
        if self.explode_pos_x >= 320 and self.explode_pos_y >= 320:
            self.exploded = True

    def is_exploded(self):
        """
        The main game loop checks this boolean in order to determine whether it is time to clean up the weapon object.
        :return:
        """
        return self.exploded



