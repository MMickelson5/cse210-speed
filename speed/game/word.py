from game import constants
from game.actor import Actor
from game.point import Point
import random

class Word(Actor):
    """A word. The responsibility of Word is keep track of its the text. 
    It contains methods for setting itself and getting its worth.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _points (List): The points it is worth
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Word): An instance of word.
        """
        super().__init__()
        self.reset()
    
    def reset(self):
        self.set_text(random.choice(constants.LIBRARY))
        self.set_position(Point(random.randint(1, constants.MAX_X - 2), random.randint(1, constants.MAX_Y - 2)))
        self._points = random.randint(1, 5)
    
    def get_points(self):
        return self._points