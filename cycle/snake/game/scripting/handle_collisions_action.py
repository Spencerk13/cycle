import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import pyray

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_player_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_player_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_head()
        segments = snake.get_segments()[1:]
        p2 = cast.get_first_actor("p2")
        head2 = p2.get_head()
        segments2 = p2.get_segments()[1:]
        for segment in segments:
            rect1 = p2.create_rect(head2)
            rect2 = snake.create_rect(segment)
            if pyray.check_collision_recs(rect1,rect2):
                self._is_game_over = True
                self._winner=1
        for segment in segments2:
            rect1 = snake.create_rect(head)
            rect2 = p2.create_rect(segment)
            if pyray.check_collision_recs(rect1,rect2):
                self._is_game_over = True
                self._winner=0
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        
        p2 = cast.get_first_actor("p2")
        head2 = p2.get_segments()[0]
        segments2 = p2.get_segments()[1:]

        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner=0
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner=1
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            p2 = cast.get_first_actor("p2")
            segments2 = p2.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)
            if self._winner == 0:
                for segment in segments:
                    segment.set_color(constants.WHITE)
            else:
              for segment in segments2:
                    segment.set_color(constants.WHITE)