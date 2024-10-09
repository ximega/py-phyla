from phyla.units import *
from phyla.collection import Collection, CollectionMethod
from phyla.methods import Method
from phyla.storage import Variable
from typing import Self

from phyla.units.classes import _Unit


class Main:
    class Rectangle(Collection):
        def __new__(cls, *args, **kwargs) -> Self:
            return super().__new__(cls)
        
        def __init__(self, **values: int | float) -> None:            
            var_input = [
                Variable('l', 'length', std.m, float),
                cnst.g,
                Variable('w', 'width', std.m, float),
            ]
            
            super().__init__(var_input, **values)
            
            self.findPerimeter = CollectionMethod(self, '2 * (l + w)', std.m)
            self.findArea = CollectionMethod(self, 'l * w / g', dim.squared(std.m))
    
    def run(self) -> None:
        print(self.Rectangle().findArea())
        print(self.Rectangle(l=10, w=15).findPerimeter())
    

if __name__ == '__main__':
    Main().run()