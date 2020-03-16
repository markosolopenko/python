
import functools


def func_log(func):
    @functools.wraps(func)
    def log_wrapper(*args, **kwargs):
        print(f'args:    {args}')
        print(f'kwargs:  {kwargs}')
        return_value = func(*args, **kwargs)
        print(f'returns: {return_value}')
        return return_value
    return log_wrapper


@func_log
def some_function(*args, **kwargs):
    print('[INSIDE FUNCTION] Doing some boring stuff...')


if __name__ == "__main__":

    some_function(1, 2, 3, a=5, b=6, c=7)
