from addition import Addition
from division import Division
from multiplication import Multiplication
from operation import Operation
from subtraction import Subtraction



class Calculator:
    def __init__(self):
        self.operations: dict[str, Operation] = {
            "add": Addition(),
            "sub": Subtraction(),
            "mul": Multiplication(),
            "div": Division()
        }

    def calculate(self, operation: str, a: float, b: float):
        if (operation := operation.lower().strip()) in self.operations:
            a = float(a)
            b = float(b)
            return self.operations[operation].calculate(a, b)
        else:
            return "Error: Unknown operation"
