from semantic_world.world import World


class ActionDesignator:

    def __init__(self):
        pass

class PickUpActionDesignator(ActionDesignator):
    """
    A designator for pick-up actions.
    """

    def __init__(self):
        super().__init__()
        pass

    def perform(self, world: World):
        pass

class PlaceActionDesignator(ActionDesignator):
    """
    A designator for place actions.
    """

    def __init__(self):
        super().__init__()
        pass

    def perform(self, world: World):
        pass

class NavigateActionDesignator(ActionDesignator):
    """
    A designator for navigate actions.
    """

    def __init__(self):
        super().__init__()
        pass

    def perform(self, world: World):
        pass