from game.actor import Actor
from game import constants
from game.point import Point
import random


class Word(Actor):
    """A floating collection of letters. The responsibility of Word is keep track of its segments. 
    It contains methods for moving and growing among others.
    Attributes:
    """
    def __init__(self):
        """The class constructor.
        """
        super().__init__()
        self._word = ""
        self.reset()

    def get_word(self):
        """Gets all the actor's words.
        Args:
            self (Word): An instance of word.
        pass
        """
        return self._word

    def check_guess(self, current_buffer):
        """Prepares the word guess by adding letters.
        Args:
            current_buffer:
            self (Word): an instance of Word.
        Returns:
            list: The word's letters.
        """
        if self._word == current_buffer:
            return True
        return False

    def reset(self):
        """Resets the words by moving them to random positions within the boundaries of the
        screen and reassigning a new random list of five words.
        Args:
            self (Word): an instance of Word.
        """
        self._word = random.choice(constants.LIBRARY)
        self.set_position(Point(random.randint(1, constants.MAX_X - 55), random.randint(2, constants.MAX_Y - 10)))
        self.set_velocity(Point(1, 0))
        self.set_text(self._word)
