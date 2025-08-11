from enum import Enum, auto

from semantic_world.world_entity import Body


class SpatialRelationship(Enum):
    NEXT_TO = auto()
    ONTOP = auto()

class Relationship:

    def __init__(self, relative_body: Body, spatial_relationship: SpatialRelationship):
        self.relative_body = relative_body
        self.spatial_relationship = spatial_relationship