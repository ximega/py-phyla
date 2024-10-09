from typing import Self, Union, Literal


__all__ = [
    'Unknown',
    '_Composite',
    '_Unit',
    '_Dimensional',
    '_Measurable'
]


Unknown = 'Unknown'  

class _Composite:
    __instances: list[Self] = []
    __slots__ = ['__name', 'measurement', 'description', 'parts']
    
    def __new__(cls, *args, **kwargs) -> Self:
        instance = super().__new__(cls)
        cls.__instances.append(instance)
        return instance
    
    def __init__(self, name: str, measurement: str, description: str) -> None:
        self.__name = name
        self.measurement = measurement
        self.description = description
        
    @property
    def name(self) -> str:
        return self.__name
    
    def set_name(self, name: str) -> Self:
        self.__name = name
        return self
        
    def __str__(self) -> str:
        return self.name
        
    def __add__(self, other) -> "_Composite":
        return _Composite(f"{self.name}+{other.name}", Unknown, Unknown)
    
    def __sub__(self, other) -> "_Composite":
        return _Composite(f"{self.name}-{other.name}", Unknown, Unknown)
    
    def __mul__(self, other) -> "_Composite":
        return _Composite(f"{self.name}*{other.name}", Unknown, Unknown)
    
    def __truediv__(self, other) -> "_Composite":
        return _Composite(f"({self.name})/({other.name})", Unknown, Unknown)
    
    def __radd__(self, other) -> "_Composite":
        return _Composite(f"{other.name}+{self.name}", Unknown, Unknown)
    
    def __rsub__(self, other) -> "_Composite":
        return _Composite(f"{other.name}-{self.name}", Unknown, Unknown)
    
    def __rmul__(self, other) -> "_Composite":
        return _Composite(f"{other.name}*{self.name}", Unknown, Unknown)
    
    def __rtruediv__(self, other) -> "_Composite":
        return _Composite(f"({other.name})/({self.name})", Unknown, Unknown)

class _Unit:
    __ALLOWED_NAMES = ['kg', 's', 'm', 'A', 'cd', 'K', 'mol']
    __instances: list[Self] = []
    __slots__ = ['name', 'measurement', 'description']
    
    def __new__(cls, name: str, measurement: str, description: str) -> Self:
        if name not in cls.__ALLOWED_NAMES:
            raise PermissionError("You can't create a unit that is outside of allowed names")
        elif name in [instance.name for instance in cls.__instances]:
            raise PermissionError(f"Can't create a second instance of {name}")
        elif measurement in [instance.measurement for instance in cls.__instances]:
            raise PermissionError(f"Can't create a second of {name} as a same measurement: {measurement}")
        else:
            instance = super().__new__(cls)
            
            cls.__instances.append(instance)
            
            return instance
            
    def __init__(self, name: str, measurement: str, description: str) -> None:
        self.name = name
        self.measurement = measurement
        self.description = description
        
    def __str__(self) -> str:
        return self.name
    
    def describe(self) -> str:
        return f"fullname: {self.description}, and measures: {self.measurement}"
    
    def __add__(self, other) -> _Composite:
        return _Composite(f"{self.name}+{other.name}", Unknown, Unknown)
    
    def __sub__(self, other) -> _Composite:
        return _Composite(f"{self.name}-{other.name}", Unknown, Unknown)
    
    def __mul__(self, other) -> _Composite:
        return _Composite(f"{self.name}*{other.name}", Unknown, Unknown)
    
    def __truediv__(self, other) -> _Composite:
        return _Composite(f"({self.name})/({other.name})", Unknown, Unknown)
    
    def __radd__(self, other) -> _Composite:
        return _Composite(f"{other.name}+{self.name}", Unknown, Unknown)
    
    def __rsub__(self, other) -> _Composite:
        return _Composite(f"{other.name}-{self.name}", Unknown, Unknown)
    
    def __rmul__(self, other) -> _Composite:
        return _Composite(f"{other.name}*{self.name}", Unknown, Unknown)
    
    def __rtruediv__(self, other) -> _Composite:
        return _Composite(f"({getattr(other, 'name', other)})/({self.name})", Unknown, Unknown)

class _Dimensional:
    __ALLOWED_NAMES = ['dim<power>']
    __instances: list[Self] = []
    __slots__ = ['__dname', 'name', 'measurement', 'description']
    
    def __new__(cls, dname: str, name: str, measurement: str, description: str) -> Self:
        if dname not in cls.__ALLOWED_NAMES:
            raise PermissionError("You can't create a unit that is outside of allowed names")
        else:
            instance = super().__new__(cls)
            
            cls.__instances.append(instance)
            
            return instance
    
    def __init__(self, dname: str, name: str, measurement: str, description: str) -> None:
        self.name = name
        self.measurement = measurement
        self.description = description
        
    def __str__(self) -> str:
        return self.name
    
    def describe(self) -> str:
        return f"fullname: {self.description}, and measures: {self.measurement}"
    
    def __add__(self, other) -> _Composite:
        return _Composite(f"{self.name}+{other.name}", Unknown, Unknown)
    
    def __sub__(self, other) -> _Composite:
        return _Composite(f"{self.name}-{other.name}", Unknown, Unknown)
    
    def __mul__(self, other) -> _Composite:
        return _Composite(f"{self.name}*{other.name}", Unknown, Unknown)
    
    def __truediv__(self, other) -> _Composite:
        return _Composite(f"({self.name})/({other.name})", Unknown, Unknown)
    
    def __radd__(self, other) -> _Composite:
        return _Composite(f"{other.name}+{self.name}", Unknown, Unknown)
    
    def __rsub__(self, other) -> _Composite:
        return _Composite(f"{other.name}-{self.name}", Unknown, Unknown)
    
    def __rmul__(self, other) -> _Composite:
        return _Composite(f"{other.name}*{self.name}", Unknown, Unknown)
    
    def __rtruediv__(self, other) -> _Composite:
        return _Composite(f"({other.name})/({self.name})", Unknown, Unknown)

_Measurable = Union[_Unit, _Composite, _Dimensional]