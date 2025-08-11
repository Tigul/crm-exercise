from typing import Dict

import numpy as np
from semantic_world.world import World


class MotionDesignator:

    def __init__(self):
        pass

class CartesianMotionDesignator(MotionDesignator):
    """
    A designator for Cartesian motions.
    """

    def __init__(self, goal_pose: np.ndarray, end_effector: str):
        """
        Initializes a CartesianMotionDesignator.
        
        :param goal_pose: The desired pose in the form of a 4x4 transformation matrix.
        :param end_effector: The name of the body that should be moved to the goal pose.
        """
        super().__init__()
        self.goal_pose = goal_pose
        self.target_body = end_effector

    def perform(self, world: World):
        pass

class JointMotionDesignator(MotionDesignator):
    """
    A designator for joint motions.
    """

    def __init__(self, joint_positions: Dict[str, float]):
        """
        Initializes a JointMotionDesignator.

        :param joint_positions: A dictionary mapping joint names to their target positions.
        """
        super().__init__()
        self.joint_positions = joint_positions

    def perform(self, world: World):
        pass
