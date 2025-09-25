class Calc:

    def add(self, a, b):
        return a+b

    def div(self, a, b):
        if b != 0:
            return a/b
        return "ZeroDivisionError"

