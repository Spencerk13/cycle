import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    INHERITS ACTION, ONE INSTANCE OF POLYMORPHISM

    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
        _directionp1: direction of snake 1 (default going right)
        _directionp2: direction of snake 2 (default going right)
        
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._directionp1 = Point(constants.CELL_SIZE, 0)
        self._directionp2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script): # Polymorphism
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a'):
            self._directionp1 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._directionp1 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._directionp1 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._directionp1 = Point(0, constants.CELL_SIZE)
        
        player1 = cast.get_first_actor("p1")
        player1.turn_head(self._directionp1)

        if self._keyboard_service.is_key_down('j'):
            self._directionp2 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._directionp2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._directionp2 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._directionp2 = Point(0, constants.CELL_SIZE)
        

        player2 = cast.get_first_actor("p2")
        player2.turn_head(self._directionp2)