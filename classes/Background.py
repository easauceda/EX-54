__author__ = 'Erick'


class Background:
    """
    Class Background is the container for all elements in the background of the game. This class utilizes two
    lists, one for stars, and one for trees. Each list is then traversed through by the function move_bg in order to
    create the illusion of movement.
    """

    def __init__(self, stars, trees):
        self.__stars = stars
        self.__trees = trees

    def get_stars(self):
        return self.__stars

    def get_trees(self):
        return self.__trees