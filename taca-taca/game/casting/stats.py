from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score_p1 = 0
        self._score_p2 = 0

    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_LIVES:
            self._lives += 1 

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

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        return self._lives
  
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
    
    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score_p1 = 0