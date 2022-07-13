from constants import *
from game.scripting.action import Action


class DrawGoalAction(Action):
    """The action that display the Goal object of the game"""

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        goals = cast.get_actors(GOAL_GROUP)
        
        for goal in goals:
            body = goal.get_body()

            if goal.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                

            image = goal.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
