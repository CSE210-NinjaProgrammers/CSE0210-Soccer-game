from constants import *
from game.scripting.action import Action


class DrawTeamAction(Action):
    """An action that sets the teams displays with it movement and positions including how the players appears in the game
    and settings"""

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        teams = cast.get_actors(TEAM_GROUP)
        
        for team in teams:
            body = team.get_body()

            if team.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle)
               
                
          
            animation = team.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
        
        teams2 = cast.get_actors(TEAM_TWO_GROUP)
        
        for team2 in teams2:
            body = team2.get_body()

            if team2.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle)
                
          
            animation = team2.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)