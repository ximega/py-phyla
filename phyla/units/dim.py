from .std import __Unit
from typing import Self


class __Dimensional:
    __ALLOWED_NAMES = ['dim<squared>', 'dim<power>']
    __instances: list[Self] = []
    
    def __new__(cls, dname: str, name: str, measurement: str, description: str) -> Self:
        if dname not in cls.__ALLOWED_NAMES:
            raise PermissionError("You can't create a unit that is outside of allowed names")
        elif name in [instance.__name for instance in cls.__instances]:
            raise PermissionError(f"Can't create a second instance of {name}")
        else:
            instance = super().__new__(cls)
            
            cls.__instances.append(instance)
            
            return instance
    
    def __init__(self, dname: str, name: str, measurement: str, description: str) -> None:
        self.__dname = dname
        self.__name = name
        self.__measurement = measurement
        self.__description = description
        
    def __str__(self) -> str:
        return self.__name
    
    @property
    def name(self) -> str:
        return self.__name
    @property
    def measurement(self) -> str:
        return self.__measurement
    @property
    def description(self) -> str:
        return self.__description
    
    def describe(self) -> str:
        return f"fullname: {self.__description}, and measures: {self.__measurement}"

def power(power: int, unit: __Unit) -> __Dimensional:
    return __Dimensional('dim<power>', f'{unit.name}^{power}', unit.measurement, f'{unit.description} to the power {power}')

def fpower(fpower: float, unit: __Unit) -> __Dimensional:
    return __Dimensional('dim<power>', f'{unit.name}^{fpower}', unit.measurement, f'{unit.description} to the power {fpower}')

def frctpower(fraction: tuple[int, int], unit: __Unit) -> __Dimensional:
    return __Dimensional('dim<power>', f'{unit.name}^({fraction[0]}/{fraction[1]})', unit.measurement, f'{unit.description} to the power {fraction[0]}/{fraction[1]}')

def squared(unit: __Unit) -> __Dimensional:
    return power(2, unit)