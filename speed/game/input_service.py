import sys
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

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
        self.reset()
        
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        event = self._screen.get_key()
        
        if not event is None:
            if event == 27:
                sys.exit()
                
            elif event == 10: 
                return False
            
            elif event >= 97 and event <= 122:
                self._result += chr(event)
                return event

    def get_result(self):
        return self._result
    
    def reset(self):
        self._result = ""