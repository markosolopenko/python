



class Generic:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __str__(self):
        return f'[{self.__class__.__name__}]: ' + \
               ', '.join([
                   f'{k}={v}' for k, v in self.__dict__.items()
               ])



if __name__ == "__main__":
    gen = Generic(a='5', b='5', dfafda='fdfd')

    print(str(gen))