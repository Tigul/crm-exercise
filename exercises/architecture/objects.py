from semantic_world.world_entity import Body


class ObjectDesignator:

    def __init__(self, name: str, relationships = None):
        self.name = name
        self.relationships = relationships if relationships is not None else []

    def __iter__(self) -> Body:
        pass