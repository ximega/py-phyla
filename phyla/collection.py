from copy import deepcopy
from .units.classes import *
from .storage import Variable, _Constant
from .units import Singleton, cnst
from typing import Any, Self


__all__ = [
    'Collection',
    'CollectionMethod'
]



class Collection(Singleton):
    __slots__ = ['__values']
    
    def __new__(cls, *args, **kwargs) -> Self:
        return super().__new__(cls, *args, **kwargs)
    
    def __init__(self, param_input: list[Variable | _Constant], **values: int | float) -> None:
        self.__values: dict[str, int | float | None] = {}
        
        param_names = [x.name for x in param_input]
        
        for key, value in values.items():
            if key in cnst.__slots__:
                raise TypeError(f"You can't specify value to a constant: {key=}, {value=}")
            
            if key in param_names:
                self.__values[key] = value
                continue
            else:
                raise ValueError(f"Unknown parameter to a collection: {key=}, {value=}")
            
        if len(self.__values) < len(param_input):
            for param in param_input:
                if isinstance(param, _Constant):
                    self.__values[param.name] = param.value
                    continue
                
                if isinstance(param, Variable):
                    if param.name not in self.__values.keys():
                        self.__values[param.name] = param.param_type(input(f"{param.name}: "))
                        continue
                    
    def all(self) -> dict[str, int | float | None]:
        return self.__values
    
    
class CollectionMethod:
    __slots__ = ['name', '__collection', '__formula', '__measured_in']
    
    def __init__(self, collection: Collection, formula: str, measured_in: _Measurable) -> None:
        self.__collection = collection
        self.__formula = formula
        self.__measured_in = measured_in
        
    def describe(self, name: str, description: str) -> Self:
        if not hasattr(self, 'name'):
            self.name = name
        else:
            raise AttributeError(f"Can't overwrite argument 'name' in collection {self.__collection.__class__.__name__}")
        
        if not hasattr(self, 'description'):
            self.description = description
        else:
            raise AttributeError(f"Can't overwrite argument 'description' in collection {self.__collection.__class__.__name__}")
        
        return self

    def __call__(self) -> Variable:
        formula = deepcopy(self.__formula)
        
        for key, val in self.__collection.all().items():
            if val is None:
                raise ValueError(f"value of key in Collection.values can't be equal None")
                
            formula = formula.replace(key, str(val))
        
        return Variable(getattr(self, 'name', Unknown), getattr(self, 'description', Unknown), self.__measured_in, float, value = eval(formula))