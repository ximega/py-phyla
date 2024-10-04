from typing import Any


class Foo:
    def __init__(self, value: int) -> None:
        super().__setattr__('value', value)
        
    def __setattr__(self, name: str, value: Any) -> None:
        raise PermissionError("You can't change any value of this object")
    
foo = Foo(10)

print(foo.value)

foo.value = 10