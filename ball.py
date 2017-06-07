import numpy as np
import matplotlib as plt

class Ball:
    """Stores information about a particle with mass, position, and velocity."""

    def __init__(self, coordinate, x_velocity, y_velocity):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.ball = circle
        self.center = coordinate   # Sets x position
        self.x_pos, self.y_pos = self.center
        self.x_vel = x_velocity
        self.y_vel = y_velocity
