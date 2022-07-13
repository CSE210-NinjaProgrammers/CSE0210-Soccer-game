from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):
    """An action that sets the formats of the HUD of the game and how it displays"""

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        self._draw_label(cast, SCORE_P1_GROUP, SCORE_P1_FORMAT, stats.get_score_p2())
        self._draw_label(cast, SCORE_P2_GROUP, SCORE_P2_FORMAT, stats.get_score_p1())

    def _draw_label(self, cast, group, format_str, data):
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)