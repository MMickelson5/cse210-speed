from game import constants
from game.point import Point


class Actor:
    """
    A visible, move-able thing that participates in the game.
    The responsibility of Actor is to keep track of its appearance, position
    and velocity in 2d space.
    Stereotype:
        Information Holder
    Attributes:
        _text (string): word representing the actor
        _position (Point): actors location on the screen
        _velocity (Point): speed and direction of actor
    """

    def __init__(self):
        """
        Class constructor.
        Args:
            self (Actor): an instance of Actor
        """
        self._text = ''
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_position(self):
        """
        Gets the actor's position on the screen
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Point: actors position
        """

        return self._position

    def get_text(self):
        """
        Gets the word of the actor
        Args:
            self (Actor): an instance of Actor.
        Returns:
            string: what the actor looks like
        """

        return self._text

    def get_velocity(self):
        """
        Gets the speed and direction of the actor
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Point: the actors speed and direction (movement)
        """

        return self._velocity

    def move(self):
        """
        Moves the actor to its next position according to the velocity.
        Args:
            self (Actor): an instance of Actor
        """
        x1 = self._position.get_x()
        y1 = self._position.get_y()
        x2 = self._velocity.get_x()
        y2 = self._velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        self._position = Point(x, y)

    def set_position(self, position):
        """
        Updates the actors position to the given one.
        Args:
            self (Actor): an instance of Actor
            position (Point): the given position
        """

        self._position = position

    def set_text(self, text):
        """
        Updates actor text to given value
        Args:
            self (Actor): an instance of Actor
            text (string): given value
        """

        self._text = text

    def set_velocity(self, velocity):
        """
        Sets the new velocity.
        Args:
            velocity:
            self (Actor): an instance of Actor
        """
        self._velocity = velocity
