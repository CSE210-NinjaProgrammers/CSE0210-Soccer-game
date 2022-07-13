from game.scripting.action import Action


class EndDrawingAction(Action):
    """An action which transfer data to the memory of the device as all data are 
    changed and runs. """

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        self._video_service.flush_buffer()