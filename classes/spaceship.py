__author__ = 'Erick'
import pygame


class SpaceShip(pygame.sprite.Sprite):
    """
    Class Spaceship represents the spaceship controlled by the player. Consists of the image and coordinates.
    """
    def __init__(self, img, x, y, health=100):
        """
        Spaceship constructor.
        :param img: Spaceship image.
        :param x: Spaceship x position.
        :param y: Spaceship y position.
        :return: none
        """
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.explode_pos_x = 0
        self.explode_pos_y = 0
        self.exploded = False
        self.health = health

    def get_x(self):
        """
        Getter for the x position.
        :return: x position
        """
        return self.rect.x

    def get_y(self):
        """
        Getter for the y position.
        :return: y position
        """
        return self.rect.y

    def set_x(self, new_x):
        """
        Setter for the x position
        :param new_x: new X position for spaceship
        :return:
        """
        self.rect.x = new_x

    def set_y(self, new_y):
        """
        Setter for the y position
        :param new_y: new Y position for spaceship
        :return:
        """
        self.rect.y = new_y

    def draw(self, surface):
        """
        Draw the spaceship object on screen
        :param surface: Pygame display object
        :return:
        """
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, surface, y, vx):
        """
        Moves the spaceship object by setting the rect pos for the spaceship. Also checks for collision with screen
        edges.
        :param surface: pygame display object.
        :param y: desired y position
        :param vx: desired x position
        :return:
        """
        l_collide = self.rect.x + vx + self.image.get_width() > surface.get_width()
        r_collide = self.rect.x + vx < 0
        t_collide = self.rect.y < 0
        b_collide = self.rect.y + self.image.get_height() > surface.get_height()

        # Check collision on right and left sides of screen
        if l_collide:
            self.rect.x = surface.get_width() - self.image.get_width()
        if r_collide:
            self.rect.x = 0
        # Check collision on top and bottom sides of screen
        if t_collide:
            self.rect.y = 0
        if b_collide:
            self.rect.y = surface.get_height() - self.image. get_height()
        self.rect.y += y
        self.rect.x += vx

    def explode(self, explosion):
        """
        Explosion animation. Triggered upon player death.
        :param explosion: explosion animation image.
        :return:
        """
        self.explode_pos_x += 64
        if self.explode_pos_x > 320:
            self.explode_pos_x = 0
            self.explode_pos_y += 64
        self.image = explosion.image_at((self.explode_pos_x, self.explode_pos_y, 64, 64), colorkey=(0, 0, 0))
        if self.explode_pos_x >= 320 and self.explode_pos_y >= 320:
            self.exploded = True
