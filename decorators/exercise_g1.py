"""
Write a generator function
"""

def main_function(func):
    def generator_func(new_func):
        def decorator(*args):
            for a in new_func(*args):
                print(a * func, end=" ")
            print()
            my_list = list(new_func(*args))
            my_iter = my_list.__iter__()
            for a in my_iter:
                try:
                    print(my_iter.__next__() * func)
                except StopIteration:
                    print(f'It was last iterator!!!')
        return decorator
    return generator_func

@main_function(2)
def return_values(*args):
    return args


print(return_values(1, 2, 3, 4, 5))
