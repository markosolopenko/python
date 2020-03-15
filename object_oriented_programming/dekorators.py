class Numbers:
    MULTIPLIER = 12

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, some):
        return cls.MULTIPLIER * some

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return self.x, self.y

    @value.setter
    def value(self, some_value):
        self.x, self.y = some_value

    @value.deleter
    def value(self):
        del self.x
        del self.y

    def __dict__(self):
        reload = {
            'x': self.x,
            'y': self.y,
            'b': self.MULTIPLIER
        }
        return reload
a = Numbers(12, 13)
b = Numbers(21,22)