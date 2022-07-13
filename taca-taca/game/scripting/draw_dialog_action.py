from constants import *
from game.scripting.action import Action


class DrawDialogAction(Action):
    """This is an action that applies to the current text that appears in this game display"""

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        dialogs = cast.get_actors(DIALOG_GROUP)
        for dialog in dialogs:
            text = dialog.get_text()
            position = dialog.get_position()
            self._video_service.draw_text(text, position)