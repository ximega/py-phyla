from .units.std import __Unit

class Collection:
    def __init__(self, prompted: list | None = None) -> None:
        self.prompted = prompted