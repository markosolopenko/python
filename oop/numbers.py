

class Numbers:

    MULTIPLIER = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER * a

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return self.x, self.y

    @value.setter
    def value(self, val):
        self.x, self.y = val

    @value.deleter
    def value(self):
        del self.x
        del self.y

    def __str__(self):
        return f'{self.x} | {self.y}'


if __name__ == "__main__":

    obj = Numbers(1, 2)

    print(obj.x)
    obj.x = 4


    print(obj.value)
    obj.value = 12




