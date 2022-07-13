from pathlib import Path
from game.scripting.action import Action


class LoadAssetsAction(Action):
    """This action loads everything in the assets files of this game that includes sounds, images, and fonts"""

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._audio_service.load_sounds("taca-taca/assets/sounds")
        self._video_service.load_fonts("taca-taca/assets/fonts")
        self._video_service.load_images("taca-taca/assets/images")
        