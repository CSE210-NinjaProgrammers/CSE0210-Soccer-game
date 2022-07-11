from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideTeamAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service


    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        teams = cast.get_actors(TEAM_GROUP)
        
        for team in teams:
            ball_body = ball.get_body()
            team_body = team.get_body()

            if self._physics_service.has_collided(ball_body, team_body):
                ball.bounce_x()
                sound = Sound(KICK_SOUND)
                self._audio_service.play_sound(sound)
        

        teams2 = cast.get_actors(TEAM_TWO_GROUP)
        
        for team2 in teams2:
            ball_body = ball.get_body()
            team2_body = team2.get_body()

            if self._physics_service.has_collided(ball_body, team2_body):
                ball.bounce_x()
                sound = Sound(KICK_SOUND)
                self._audio_service.play_sound(sound)