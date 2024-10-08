from phyla.units import *
from phyla.methods import Method
from phyla.storage import Variable

def main() -> None:
    cmp.ms2 = std.m * dim.squared(std.s) # type: ignore
    cmp.create('N', std.kg * cmp.ms2) # type: ignore
    dim.m2 = dim.squared(std.m) # type: ignore
    cmp.create('Pa', cmp.N / dim.m2) # type: ignore
            
    p = Method(
        Variable('m', 'mass', std.kg, float),
        cnst.g,
        Variable('A', 'Area', dim.m2, float),
    ).returns(
        Variable('p', 'pressure', cmp.Pa, float)
    ).define_formula(
        '(m * g) / A'
    ).call(10, 20)
        
    print(p)

if __name__ == '__main__':
    main()