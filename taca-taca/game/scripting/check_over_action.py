from ast import Pass
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self, audio_service):
        self._audio_service = audio_service  
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        if stats.get_score_p1() == 5 or stats.get_score_p2() == 5:
            callback.on_next(GAME_OVER)
            self._audio_service.play_sound(Sound(OVER_SOUND))
        