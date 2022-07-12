from game.casting.actor import Actor


class Goal(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, image, player, debug = False):
        """Constructs a new Goal.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image 
        self._points = 0
        self._player = player

    def get_player(self):
        """Gets the player.
        
        Returns:
            An instance of PLayer.
        """
        return self._player

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the Goal's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the Goal's points.
        
        Returns:
            A number representing the Goal's points.
        """
        return self._points