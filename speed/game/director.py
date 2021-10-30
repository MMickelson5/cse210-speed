from time import sleep
from game import constants
from game.score import Score
from game.word import Word
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        word (Word): The users target to write.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._words = []
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        for i in range(constants.STARTING_WORDS):
            word = Word()
            self._words.append(word)
            
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        event = self._input_service.get_letter()
        if event is False:
            self._reset()
            self._output()
        self._buffer.set_word(event)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._check_word()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output()

    def _check_word(self):
        
        for i in self._words:
            word = i.get_text()
        
            if self._input_service.get_result() == word:
                points = i.get_points()
                self._score.add_points(points)
                i.reset()
                self._reset()
    
    def _reset(self):
        self._buffer.reset()
        self._input_service.reset()
    
    def _output(self):
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._words)
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()