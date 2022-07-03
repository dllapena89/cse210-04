from casting.actor import Actor
from shared.point import Point


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.
    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def set_value(self, text):
        """set up for articact as '*' and 'o'
        """
        if text == '*':
            value = 1
            return value
        elif text == 'o':
            value = -1
            return value

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        """
        self._velocity = velocity

    def move_next(self, max_x, max_y):
        """Moves the actor 
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)
        
    def get_position(self):
        """Updates the position to the given one.
        
        """
        return self._position

    def set_position(self, position):
        """Updates the position to the given one.
        """
        self._position = position