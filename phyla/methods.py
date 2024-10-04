from typing import Self
from .storage import Variable


class Method:
    def __init__(self, *params: Variable) -> None:
        self.needs_prompt = False
        self.returned_param: Variable | None = None
        self.params = params
        self.formula: str | None = None
    
    def prompted(self) -> Self:
        if self.returned_param is None:
            raise TypeError(f"Can't run a function without a type of return instanced")
        if self.formula is None:
            raise TypeError(f"Can't run a function without a type of formula defined")
        self.needs_prompt = True
        return self
    
    def returns(self, param: Variable) -> Self:
        self.returned_param = param
        return self
    
    def define_formula(self, formula_text: str) -> Self:
        self.formula = formula_text
        return self
    
    def call(self) -> Variable:
        pass