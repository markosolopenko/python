# class Numbers:
#     MULTIPLIER = 12
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self):
#         return self.x + self.y
#
#     @classmethod
#     def multiply(cls, some):
#         return cls.MULTIPLIER * some
#
#     @staticmethod
#     def subtract(b, c):
#         return b - c
#
#     @property
#     def value(self):
#         return self.x, self.y
#
#     @value.setter
#     def value(self, some_value):
#         self.x, self.y = some_value
#
#     @value.deleter
#     def value(self):
#         del self.x
#         del self.y
#
#     def __dict__(self):
#         reload = {
#             'x': self.x,
#             'y': self.y,
#             'b': self.MULTIPLIER
#         }
#         return reload
#
#
# a = Numbers(12, 13)
# b = Numbers(21, 22)





# def say_hello(name):
#     return f"Hello {name}"
#
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
#
#
# def some_func(sarname_func):
#     return sarname_func('Solopenko')
# print(greet_bob(say_hello))
# print(some_func(be_awesome))



# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()
# parent()

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
# print(parent(2)())
# second = parent(1)
# #print(first())



def my_decorator(func):

    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say = my_decorator(say_whee)
print(say)


from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say = not_during_the_night(say_whee)
print(say())