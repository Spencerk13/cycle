import constants

from game.casting.cast import Cast
from game.casting.snake import Snake
from game.casting.food import Food
from game.casting.score import Score
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("p1", Snake("GREEN"))
    cast.add_actor("p2", Snake("RED"))
    cast.add_actor("scores", Score(player=1,pos_x=0))
    cast.add_actor("scores", Score(player=2,pos_x=constants.MAX_X-150))

    cast.add_actor("foods", Food())

   
    # set up script
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    # start the game
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()