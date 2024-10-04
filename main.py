from phyla.units import *
from phyla.collection import Collection

def main() -> None:
    cmp.kgm = dim.squared(std.kg * dim.squared(std.m))
    
    print(cmp.kgm)

if __name__ == '__main__':
    main()