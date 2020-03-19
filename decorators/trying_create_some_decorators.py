#from object_oriented_programming.decorator_tutorial import debug, do_twice, repeat
import functools
import math

################################
#   Decorators With Arguments   #
################################

def repeat(_func = None, *, num_times = 2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def generator(kwargs):
            for _ in range(num_times):
                print(func(kwargs))
        return generator
    return decorator_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

@repeat
def greet(name):
    return f"Hello {name}"

# print(greet("Marko"))


#########################
#  Stateful Decorators
#########################


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")

# say_whee()
# say_whee()
# say_whee()
# print(say_whee.num_calls)

###########################
#  Classes as Decorators  #
###########################
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")

print(Counter().__call__())
# counter = Counter()
# counter()
# counter()

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func) # instead @functools.wraps
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")




#################################
# Adding Information About Units
#################################

def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit

@set_unit("cm^3")
def volume(radius, height):
    return f'{math.pi * radius**2 * height} {volume.unit}'

# print(volume(2, 21))





