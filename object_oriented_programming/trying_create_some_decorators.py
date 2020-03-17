#from object_oriented_programming.decorator_tutorial import do_twice, decorator
import math
from object_oriented_programming.decorator_tutorial import debug

#@do_twice
def say_whee():
    print(f'Hello')

#@do_twice
def greet(name):
    print(f'Hello {name}')

#@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f'Hi {name}'

# hi_adam = return_greeting("Adam")
# print(hi_adam)

# say = do_twice(say_whee)
# print(help(say))
# say()

# other = do_twice(greet)
# other("Marko")


# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)
def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

print(approximate_e(5))