from __future__ import annotations

import numpy as np
from semantic_world.world import World


class LocationDesignator:

    def __init__(self, target: np.ndarray, world: World):
        self.target = target  # Target location in world coordinates
        self.world = world  # Reference to the world object

class Costmap:
    def __init__(self, resolution: float, width: int, height: int, origin: np.ndarray, world: World):
        """
        Initializes a Costmap.

        :param resolution: The resolution of the costmap in meters per pixel.
        :param width: The width of the costmap in pixels.
        :param height: The height of the costmap in pixels.
        :param origin: The origin of the costmap as a 2D numpy array [x, y].
        """
        self.resolution = resolution
        self.width = width
        self.height = height
        self.origin = origin
        self.world = world
        self.data = np.zeros((height, width), dtype=np.float32)

    def merge(self, other: Costmap):
        """
        Merges another costmap into this one.

        :param other: The other costmap to merge.
        """
        if self.resolution != other.resolution or self.width != other.width or self.height != other.height:
            raise ValueError("Costmaps must have the same resolution and dimensions to merge.")

        self.data = np.maximum(self.data, other.data)

    def sample(self, n: int) -> np.ndarray:
        """
        Samples n random points from the costmap.

        :param n: The number of points to sample.
        :return: An array of shape (n, 2) containing the sampled points in world coordinates.
        """
        indices = np.argpartition(self.data, -n)[-n:]
        y_indices, x_indices = np.unravel_index(indices, (self.height, self.width))
        points = np.column_stack((x_indices * self.resolution + self.origin[0],
                                  y_indices * self.resolution + self.origin[1]))
        return points

class OccupancyCostmap(Costmap):
    """
    A costmap that represents occupancy information.
    """

    def __init__(self, resolution: float, width: int, height: int, origin: np.ndarray, world: World):
        super().__init__(resolution, width, height, origin, world)
        self.occupancy_threshold = 0.5  # Default threshold for occupancy
        self.data = np.zeros((height, width), dtype=np.float32)  # Occupancy values between 0 and 1

class ReachabilityCostmap(Costmap):
    """
    A costmap that represents reachability information.
    """

    def __init__(self, resolution: float, width: int, height: int, origin: np.ndarray, world: World):
        super().__init__(resolution, width, height, origin, world)
        self.reachability_threshold = 0.5  # Default threshold for reachability
        self.data = np.zeros((height, width), dtype=np.float32)  # Reachability values between 0 and 1