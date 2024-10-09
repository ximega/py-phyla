from .classes import _Unit, _Composite, _Dimensional, Unknown
from typing import Any, Self
from ..storage import _Constant



__all__ = [
    'std',
    'dim',
    'cmp',
    'cnst',
    'Singleton'
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
    
class _Std(Singleton, ModuleCollection):  
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
      
    def __init__(self) -> None:
        super().__init__()
        # define default units here
        self.kg = _Unit('kg', 'mass', 'kilogram')
        self.s = _Unit('s', 'time', 'second')
        self.m = _Unit('m', 'length', 'meter')
        self.A = _Unit('A', 'electric current', 'Amper')
        self.K = _Unit('K', 'temperature', 'Kelvin')
        self.mol = _Unit('mol', 'amount of substance', 'mole')
        self.cd = _Unit('cd', 'luminous intensity', 'candela')
        
std = _Std()

class _Dim(Singleton, ModuleCollection):
    def __new__(cls, *args, **kwargs) -> Self:
        return super().__new__(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        # define default units here
        self.m2 = self.squared(std.m)
        self.m3 = self.power(3, std.m)
        self.s2 = self.squared(std.s)
        self.s3 = self.power(3, std.s)
        
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
    
dim = _Dim()

class _Cmp(Singleton, ModuleCollection):    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
      
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        # define default units here
        self.N = ((std.kg * std.m) / dim.s2).set_name('N')
        self.J = ((std.kg * dim.m2) / dim.s2).set_name('J')
        self.W = ((std.kg * dim.m2) / dim.s3).set_name('W')
        self.Pa = ((std.kg) / (std.m * dim.s2)).set_name('Pa')
        self.C = (std.s * std.A).set_name('C')
        self.V = ((std.m * dim.m2) / (dim.s3 * std.A)).set_name('V')
        
    def __setattr__(self, name: str, value: _Composite) -> None:
        super().__setattr__(name, value)
                
    def create(self, name: str, composite: _Composite) -> None:
        """
        Will create an instance of _Composite with corr_value = True
        """
        
        instance = _Composite(composite.name, composite.measurement, composite.description)
        
        setattr(self, name, instance)
                        
cmp = _Cmp()

class _Cnst(Singleton, ModuleCollection):
    __instances: list[Self] = []
    __slots__ = [
        'g',
    ]
    
    def __new__(cls, *args, **kwargs) -> Self:
        instance = super().__new__(cls, *args, **kwargs)
        cls.__instances.append(instance)
        return instance
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        # define all constants here
        self.g = _Constant('g', 'gravitational acceleration', 9.80665, std.m * dim.squared(std.s))
        self.c = _Constant('c', 'speed of light', 299792458, std.m / std.s)
        self.G = _Constant('G', 'gravitational constant', 6.674e-11, dim.m3 / (std.kg * dim.s2))
        self.h = _Constant('h', 'Planck\'s constant', 6.626e-34, cmp.J * std.s)
        self.e = _Constant('e', 'elementary charge', 1.602e-19, cmp.C)
        self.k = _Constant('k', 'Boltzmann constant', 1.381e-23, cmp.J / std.K)
        self.Na = _Constant('Na', 'Avogadro\'s number', 6.022e23, 1 / std.mol)
        self.R = _Constant('R', 'gas constant', 8.314, cmp.J / (std.mol * std.K))
        self.me = _Constant('me', 'mass of electron', 9.109e-31, std.kg)
        self.mp = _Constant('mp', 'mass of proton', 1.673e-27, std.kg)
        self.mn = _Constant('mn', 'mass of neutron', 1.675e-27, std.kg)
        
cnst = _Cnst()