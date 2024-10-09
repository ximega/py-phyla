from phyla.units import *
from phyla.collection import Collection, CollectionMethod
from phyla.storage import Variable
from typing import Self
from math import sqrt

class Main:
    class EscapeVelocity(Collection):
        def __new__(cls, *args, **kwargs) -> Self:
            return super().__new__(cls)
        
        def __init__(self, **values: int | float) -> None:            
            var_input = [
                cnst.G,
                Variable('M', 'Mass of black hole', std.kg, float),
                Variable('r', 'radial distance from hole', std.m, float),
                Variable('a', 'angular momentum of hole', (std.kg * dim.m2) / std.s, float),
                cnst.c
            ]
            
            super().__init__(var_input, **values)
            
            self.find = CollectionMethod(self, '''
                (((2 * G * M) / (r)) + ((a * a * c * c) / (r * r))) ** (1/2)
            ''', std.m / std.s)
            
    def run(self) -> None:
        print(self.EscapeVelocity().find())
    

if __name__ == '__main__':
    Main().run()