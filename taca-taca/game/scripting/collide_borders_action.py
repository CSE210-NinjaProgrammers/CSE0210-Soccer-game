from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(KICK_SOUND)
        goal_sound = Sound(GOAL_SOUND)

        if x < FIELD_LEFT:
          ball.bounce_x()
          self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
           ball.bounce_y()
           self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        teams = cast.get_actors(TEAM_GROUP)
        for team in teams:
            team_body = team.get_body()
            team_position = team_body.get_position()
               
            if team_position.get_y() < FIELD_TOP:
                team.swing_down()
                print(team_position.get_y())

            elif team_position.get_y() >= (FIELD_BOTTOM - BALL_WIDTH):
                team.swing_up()
