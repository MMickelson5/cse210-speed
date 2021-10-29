import random
from game.actor import Actor
from game.point import Point

class Buffer(Actor):
    """Points earned. The responsibility of Buffer is to keep track of the player's guessed letters.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._word = ""
        position = Point(1, 1)
        self.set_position(position)
        self.set_text(f"Buffer: {self._word}")
        
    def set_word(self, event):
        
        if not event is None:
            self._word += chr(event)
            self.set_text(f"Buffer: {self._word}")
    
    def reset(self):
        self._word = ""
        self.set_text(f"Buffer: {self._word}")