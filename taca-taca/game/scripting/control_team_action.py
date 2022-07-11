from constants import *
from game.scripting.action import Action


class ControlTeamAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    # def execute(self, cast, script, callback):
    #     racket = cast.get_first_actor(RACKET_GROUP)
    #     if self._keyboard_service.is_key_down(UP): 
    #         racket.swing_up()
    #     elif self._keyboard_service.is_key_down(DOWN): 
    #         racket.swing_down()  
    #     else: 
    #         racket.stop_moving()  


    def execute(self, cast, script, callback):
        teams = cast.get_actors(TEAM_GROUP)
        for team in teams:

            if self._keyboard_service.is_key_down(W): 
                team.swing_up()
            elif self._keyboard_service.is_key_down(S): 
                team.swing_down()  
            else: 
                team.stop_moving()


        teams2 = cast.get_actors(TEAM_TWO_GROUP)
        for team2 in teams2:

            if self._keyboard_service.is_key_down(UP): 
                team2.swing_up()
            elif self._keyboard_service.is_key_down(DOWN): 
                team2.swing_down()  
            else: 
                team2.stop_moving()       