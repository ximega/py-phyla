from phyla.units import std, dim
from phyla.collection import Collection

def main() -> None:
    print(dim.power(3, std.kg))
    print(dim.fpower(3.2, std.kg))
    print(dim.frctpower((3, 10), std.kg))

if __name__ == '__main__':
    main()