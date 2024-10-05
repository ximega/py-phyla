# file: ignore

from phyla.units import *
from phyla.collection import Collection
from phyla.methods import Method
from phyla.storage import Variable

def main() -> None:
    cmp.ms2 = std.m * dim.squared(std.s) # type: ignore
    cmp.create('N', std.kg * cmp.ms2) # type: ignore
    dim.m2 = dim.squared(std.m) # type: ignore
    cmp.create('Pa', cmp.N / dim.m2) # type: ignore
            
    p = Method(
        
        Method(
            Variable('m', 'mass', std.kg, float),
            Variable('g', 'gravitational acceleration', cmp.ms2, float)
        ).returns(
            Variable('F', 'weight', cmp.N, float)
        ).define_formula(
            'm * g'
        ).prompted(),
        
        Method(
            Variable('l', 'length', std.m, float),
            Variable('w', 'width', std.m, float)
        ).returns(
            Variable('A', 'Area', dim.m2, float)
        ).define_formula(
            'l * w'
        ).prompted()
        
    ).returns(
        Variable('p', 'pressure', cmp.Pa, float)
    ).define_formula(
        'F / A'
    ).prompted().call()
        
    print(p)

if __name__ == '__main__':
    main()