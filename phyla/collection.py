from .units.classes import _Unit



__all__ = [
    'Collection'
]


class Collection:
    def __init__(self, prompted: list[_Unit] | None = None) -> None:
        self.prompted = prompted