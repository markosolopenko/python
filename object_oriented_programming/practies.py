class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self): # instance method
        # instance object accessible through self
        return "%s %s" % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
        # class or instance object accessible through cls
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith): # static method
        # no parameter for class or instance object
        # we have to use Person directly
        return [t for t in Person.TITLES if t.endswith(endswith)]


class Some(Person):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.name = name

    def some(self):
        return self.allowed_titles_ending_with('Mr')

# abc = Some("Marko", 'Solopenko')
# print(abc.some())

class Person:
    def __init__(self, height):
        self.height = height


    def get_height(self):
        return self.height


    def set_height(self, height):
        self.height = height


# some = Person(123)


# jane = Person("Jane", "Smith")
#
# print(jane.fullname())
#
# print(jane.allowed_titles_starting_with("M"))
# print(Person.allowed_titles_starting_with("M"))
#
# print(jane.allowed_titles_ending_with("s"))
# print(Person.allowed_titles_ending_with("s"))

class Sentetic:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __str__(self):
        return f'[{self.__class__.__name__}] ' + \
            ', '.join([
                f' {k}: {v}' for k, v in self.__dict__.items()
            ])


obj = Sentetic(a=2, b=3, c=2)
print(obj)




# class Person:
#     MAN = "Ivan"
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def fullname(self):
#         return "%s %s" % (self.name, self.surname)
#
# jane = Person("Jane", "Smith")
#
# print(dir(Person))

