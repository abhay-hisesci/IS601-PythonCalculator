class calculator:
    result = 0
    def __init__(self):
        self.result = 1;
        pass

    def add(self, a, b):
        c = a + b
        return c

    def subtract(self, a, b):
        c = b - a
        return c

    def multiply(self, a, b):
        c = b * a
        return c

    def divide(self, a, b):
        c = b / a
        return c

    def square(self, a):
        b = a ** 2
        return b

    def square_root(self, a):
        b = a**(float(1)/2)
        return b