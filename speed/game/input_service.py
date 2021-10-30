import sys


class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player
    key presses and translate them into a point representing a direction (or velocity).
    Stereotype:
        Service Provider
    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.

        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen

    def get_letter(self):
        """Gets the key that was typed.
        Args:
            self (InputService): An instance of InputService.
        Returns:
            str: A string of the letter.
        """
        event = self._screen.get_key()
        if event is not None:
            if event == -1:
                sys.exit()
            elif event == 10:
                return "ENTER"
            elif 97 <= event <= 122:
                return chr(event)
            elif event == -300:
                return "BACKSPACE"
        return ""
