import os

import numpy as np
from semantic_world.world import World
from semantic_world.adapters.urdf import URDFParser

def setup_world() -> World:
    apartment = URDFParser(os.path.join(__file__, "..", "..", "resources")).parse()
    pr2 = URDFParser(os.path.join(__file__, "..", "..", "resources", "pr2.urdf")).parse()

    merge_pose = np.eye(4)
    merge_pose[:3, 3] = [1.0, 2.0, 0.0]
    apartment.merge_world_at_pose(pr2, merge_pose)

    return apartment