def _validated_data(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operators must be numbers and not str")

class Calc:
    def add(self, a, b):
        _validated_data(a,b)
        return a + b

    def minus(self, a, b):
        _validated_data(a, b)
        return a - b

    def div(self, a, b):
        _validated_data(a, b)
        if b != 0:
            return a / b
        return "ZeroDivisionError"

    def mult(self, a, b):
        _validated_data(a, b)
        return a * b
