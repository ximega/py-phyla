from typing import Self, Literal
from .units.classes import _Unit, _Composite, _Dimensional, _Measurable


__all__ = [
    '_Constant',
    'Variable'
]


class _Constant:
    __instances: list[Self] = []
    __slots__ = ['__name', '__description', '__value', '__measured_in']
    
    def __new__(cls, *args, **kwargs) -> Self:
        instance = super().__new__(cls)
        cls.__instances.append(instance)
        return instance
    
    def __init__(self, name: str, description: str, value: int | float, measured_in: _Measurable) -> None:
        self.__name = name
        self.__description = description
        self.__value = value
        self.__measured_in = measured_in
        
    def __str__(self) -> str:
        return f"{self.__value} {self.__measured_in}"
    
    @property
    def name(self) -> str:
        return self.__name
    @property
    def description(self) -> str:
        return self.__description
    @property
    def value(self) -> int | float:
        return self.__value
    @property
    def measured_in(self) -> _Measurable:
        return self.__measured_in

class Variable:
    __instances: list[Self] = []
    
    def __new__(cls, *args, **kwargs) -> Self:
        instance = super().__new__(cls)
        cls.__instances.append(instance)
        return instance
    
    def __init__(self, name: str, description: str, measured_in: _Measurable, param_type: type[int] | type[float], *, value: int | float | None = None) -> None:
        """
        `value param_type`: Can be either `int` or `float`
        """
        if param_type not in [int, float]:
            raise TypeError(f"The parameter {name} can't be of type anything than int or float")
        
        self.name = name
        self.description = description
        self.measured_in = measured_in
        self.value = value
        self.param_type = param_type
        
    def __str__(self) -> str:
        return f"{self.value} {self.measured_in}"
    
    def describe(self) -> str:
        return f"{self.name} = {self.__str__()}"