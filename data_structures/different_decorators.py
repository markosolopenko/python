# import array
#
# balance = array.array('i', [122, 200, 123])
# balance.insert(1,12)
# balance[1] = 11
# print(balance)



def double_Ii(old_function):
    def new_function(*args):
        some_tuple = []
        for a in old_function(args):
            some_tuple.append(old_function(a*2))
        return some_tuple

    return new_function


@double_Ii
def func(args):
    return args

#####################
#     Generator     #
####################
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwargs):
            if isinstance(multiplier, int):
                return multiplier * old_function(*args, **kwargs)
        return new_function
    return multiply_generator # it returns the new generator


@multiply(int) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num*2
#print(return_num(2))




def type_check(correct_type):
    def generator(some_func):
        def new_func(arg):
            try:
                if not isinstance(arg, correct_type):
                    raise TypeError
            except TypeError:
                print("Bad Type")
            else:
                return some_func(arg)
            finally:
                print("Bad Type")
        return new_func
    return generator

@type_check(int)
def times2(num):
    return num*2

@type_check(str)
def first_letter(word):
    return word[0]
print(times2(12))
print(first_letter("a"))


# def type_check(correct_type):
#     def generator(some_func):
#         def new_func(arg):
#             if isinstance(some_func, int):
#                 return correct_type(arg)
#             else:
#                 return "Not A Number"
#         return new_func
#     return generator
#
# @type_check
# def times2(num):
#     return num*2
# print(times2(2))
#
#
# def type_check(correct_type):
#     def generator(some_func):
#         def new_func(arg):
#             if isinstance(arg, correct_type):
#                 return some_func(arg)
#             else:
#                 print("Bad Type")
#         return new_func
#     return generator
#
# @type_check(int)
# def times2(num):
#     return num*2
#
# print(times2("a"))
# times2('Not A Number')
#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
# print(first_letter(2))
# first_letter(['Not', 'A', 'String'])
#
#
# def type_check(correct_type):
#     def check(old_function):
#         def new_function(arg):
#             if (isinstance(arg, correct_type)):
#                 return old_function(arg)
#             else:
#                 print("Bad Type")
#         return new_function
#     return check
#
# @type_check(int)
# def times2(num):
#     return num*2
#
# print(times2(2))
# times2('Not A Number')
#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
# print(first_letter('Hello World'))
# first_letter(['Not', 'A', 'String'])







