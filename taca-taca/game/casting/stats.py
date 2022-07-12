from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._score_p1 = 0
        self._score_p2 = 0

    def add_point_p1(self):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score_p1 += 1
    
    def add_point_p2(self):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score_p2 += 1

    def get_score_p1(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score_p1
    
    def get_score_p2(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score_p2
    

    def reset(self):
        """Resets the stats back to their default values."""
        self._score_p1 = 0