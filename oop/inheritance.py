
class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def eat(self): pass
    def drink(self): pass
    def breath(self): pass

    def __str__(self):
        return f'Human: {self.age} | {self.name} | {self.height}'


class Superhero(Human):

    def __init__(self, superpower, name, age, height):
        super().__init__(name, age, height)
        self.superpower = superpower

    def do_super_stuff(self): print('I`m doing a super stuff')


class Man(Superhero):
    def __init__(self, name, age, height, superpower):
        super(Man, self).__init__(name, age, height, superpower)
        self.gender = 'MALE'

    def __str__(self):
        return f'Human: {self.age} | {self.name} | {self.height} | {self.gender}'


class Woman(Human):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.gender = 'FEMALE'

    def __str__(self):
        return f'Human: {self.age} | {self.name} | {self.height} | {self.gender}'


man = Man('Andrii', 23, 180, 'lift things')
wom = Woman('Olenka', 23, 170)

print(man)

man.do_super_stuff()

print(Man.__mro__)