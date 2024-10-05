# file: ignore

from phyla.units import *
from phyla.collection import Collection
from phyla.methods import Method
from phyla.storage import Variable

def main() -> None:
    dim.m2 = dim.squared(std.m)
    
    find_area = Method(
        Variable('l', 'length of rectangle', std.m, int),
        Variable('w', 'width of rectangle', std.m, int)
    ).returns(
        Variable('A', 'Area of rectangle', dim.m2, int)
    ).define_formula(
        'l * w'
    )
    
    print(find_area.call(10, 20))

if __name__ == '__main__':
    main()