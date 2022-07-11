class Point:
    """A distance from a relative origin (0, 0)."""
    
    def __init__(self, x = 0, y = 0):
        """Constructs a new Point using the specified x and y values.
        
        Args:
            x: An int representing the horizontal distance from the origin.
            y: An int representing the vertical distance from the origin.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other: An instance of Point.

        Returns:
            A new instance of Point containing the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)


    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            An integer containing the x value or horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            An integer containing the y value or vertical distance.
        """
        return self._y

