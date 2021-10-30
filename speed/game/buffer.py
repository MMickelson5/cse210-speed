from game import constants
from game.actor import Actor
from game.point import Point


class Buffer(Actor):
    def __init__(self):
        super().__init__()
        self.BUFFER_X = 0
        self.BUFFER_Y = 1
        self._buffer = ""
        self.set_position(Point(self.BUFFER_X, self.BUFFER_Y))
        self.set_velocity(Point(0, 0))
        self.set_text(f"Buffer: {self._buffer}")

    def get_buffer(self):
        return self._buffer

    def add_letter(self, letter):
        self._buffer += letter
        self.set_text(f"Buffer: {self._buffer}")

    def backspace(self):
        self._buffer = self._buffer[:-1]

    def clear(self):
        self._buffer = ""
