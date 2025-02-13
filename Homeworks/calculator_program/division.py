from operation import Operation

class Division(Operation):
    def calculate(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b