from .classes import _Unit, _Composite, _Dimensional
from typing import Self



__all__ = [
    'std',
    'dim',
    'cmp'
]



class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Ensure the initialization only happens once
            self.value = value
            self.initialized = True

class ModuleCollection:
    def __new__(cls, *args, **kwargs) -> Self: return super().__new__(cls)
    def __init__(self, *args, **kwargs) -> None: pass
    
class Std(Singleton, ModuleCollection):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
      
    def __init__(self) -> None:
        super().__init__()
        # define default units here
        self.kg = _Unit('kg', 'mass', 'kilogram')
        self.s = _Unit('s', 'time', 'second')
        self.m = _Unit('m', 'length', 'meter')
        
std = Std()

class Dim(Singleton, ModuleCollection):
    def __new__(cls, *args, **kwargs) -> Self:
        return super().__new__(cls, *args, **kwargs)
    
    def __init__(self):
        super().__init__()
        # define default units here
        
    def power(self, power: int | float | tuple[int, int], unit: _Unit | _Dimensional | _Composite) -> _Dimensional:
        power_text = str()
        
        if isinstance(power, int) or isinstance(power, float):
            power_text = str(power)
        elif isinstance(power, tuple):
            power_text = f"{power[0]}/{power[1]}"
            
        ARITHEMTIC_CHARS = list('*/+-')
        final_name = str()
        for char in ARITHEMTIC_CHARS:
            if char in unit.name:
                final_name = f'({unit.name})^{power}'
                break
        else:
            final_name = f'{unit.name}^{power}'
            
        return _Dimensional('dim<power>', f'{final_name}', unit.measurement, f'{unit.description} to the power {power_text}')

    def squared(self, unit: _Unit | _Dimensional | _Composite) -> _Dimensional:
        return self.power(2, unit)
    
dim = Dim()

class Cmp(Singleton, ModuleCollection):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
      
    def __init__(self) -> None:
        super().__init__()
        # define default units here
        
cmp = Cmp()