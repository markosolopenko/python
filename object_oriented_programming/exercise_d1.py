

#@logget
def func_log(*args, **kwargs):
    arg_dict = {}
    arg_list = []
    for k, v in kwargs.items():
        arg_dict[k] = v

    for a in args:
        arg_list.append(a)

    print(arg_list)
    print(arg_dict)

func_log(12,1212, a = 3, b = 4)
