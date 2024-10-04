from typing import Self

class __Unit:
    __ALLOWED_NAMES = ['kg', 's', 'm']
    __instances: list[Self] = []
    
    def __new__(cls, name: str, measurement: str, description: str) -> Self:
        if name not in cls.__ALLOWED_NAMES:
            raise PermissionError("You can't create a unit that is outside of allowed names")
        elif name in [instance.__name for instance in cls.__instances]:
            raise PermissionError(f"Can't create a second instance of {name}")
        elif measurement in [instance.__measurement for instance in cls.__instances]:
            raise PermissionError(f"Can't create a second of {name} as a same measurement: {measurement}")
        else:
            instance = super().__new__(cls)
            
            cls.__instances.append(instance)
            
            return instance
            
    def __init__(self, name: str, measurement: str, description: str) -> None:
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

kg = __Unit('kg', 'mass', 'kilogram')
s = __Unit('s', 'time', 'second')
m = __Unit('m', 'length', 'meter')