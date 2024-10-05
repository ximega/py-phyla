from typing import Self
from .storage import Variable
from copy import deepcopy


class Method:
    def __init__(self, *params: Variable) -> None:
        if len(set(params)) < len(params):
            raise TypeError("You have specified the same variable two or more times")
        
        self.needs_prompt = False
        self.returned_param: Variable | None = None
        self.params = set(params)
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
    
    def call(self, *param_values: int | float) -> Variable:
        if self.returned_param is None:
            raise TypeError(f"Can't run a function without a type of return instanced")
        if self.formula is None:
            raise TypeError(f"Can't run a function without a type of formula defined")
        
        if self.needs_prompt:
            if len(param_values) > 0:
                raise ValueError("Length of params in Method.call() can't be more than 0")
            
            values: dict[str, int | float] = {}
            
            for param in self.params:
                if param.param_type == int:
                    values[param.name] = int(input(param.name + ': '))
                elif param.param_type == float:
                    values[param.name] = float(input(param.name + ': '))
              
            formula = deepcopy(self.formula)      
            for key, value in values.items():
                formula = formula.replace(key, str(value))
                                    
            return Variable(self.returned_param.name, self.returned_param.description, self.returned_param.measured_in, self.returned_param.param_type, value = eval(formula))
        else:
            if len(param_values) > len(self.params):
                raise ValueError(f"Specified {set(param_values) - {x.value for x in self.params}} is not associated to any of method's parameter. Check parameters and types of them of method before putting values.")
            if len(param_values) < len(self.params):
                raise ValueError(f"Not specified value for one of parameters")
            
            formula = deepcopy(self.formula)    
            keys = [variable.name for variable in self.params]  
            for index, value in enumerate(param_values):
                formula = formula.replace(keys[index], str(value))
                                    
            return Variable(self.returned_param.name, self.returned_param.description, self.returned_param.measured_in, self.returned_param.param_type, value = eval(formula))