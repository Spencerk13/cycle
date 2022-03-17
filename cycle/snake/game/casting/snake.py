import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point

class Snake(Actor):
    """
    INHERITS ACTOR, TWO INSTANCES OF POLYMORPHISM

    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, color):
        """Create an instance of a snake.
        Parameters:
        color: the color of the snake
        """
        super().__init__()
        self._segments = []
        self._color = color
        self._prepare_body()

    def get_segments(self):
        """Get all of the segments of the snake in a list."""
        return self._segments

    def move_next(self): # Polymorphism
        """Move each individual segment of snake and update their velocities."""
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Return the segment comprising the head."""
        return self._segments[0]

    def grow_tail(self): # Polymorphism
        """Make snake grow up to 150 segments long"""
        if constants.SNAKE_LENGTH <= 150:
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position() + offset
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            eval(f"segment.set_color(constants.{self._color})")
            self._segments.append(segment)
            constants.SNAKE_LENGTH+=1

    def turn_head(self, velocity):
        """Change direction
        Args:
        velocity: the direction of the snake.
        """
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self):
        """
        Create the snake with its position, color, velocity, and graphics.
        """
        x = random.randint(0,900)
        y = random.randint(0,600)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = eval(f"constants.YELLOW if i == 0 else constants.{self._color}")
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)