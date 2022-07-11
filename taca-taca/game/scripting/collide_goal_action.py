from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideGoalAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        bricks = cast.get_actors(GOAL_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for brick in bricks:
            ball_body = ball.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                ball.bounce_y()
                sound = Sound(GOAL_SOUND)
                self._audio_service.play_sound(sound)
                if brick.get_player() == 1:
                    stats.add_point_p1()
                
                if brick.get_player() == 2:
                    stats.add_point_p2()
                callback.on_next(TRY_AGAIN) 