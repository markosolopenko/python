# import functools
# def min_num_taxis(func):
#     @functools.wraps(func)
#     def wrapper(args):
#         key = func(args)
#         print(key)
#         some = 'co'
#         if some in key:
#             wrapper.s += str(key) + ' '
#         print(wrapper.s)
#     wrapper.s = ''
#     return wrapper




# @min_num_taxis
def recurs(indx, string):
    characters = 'co'
    text = "We extend the concept of linked data structures to structure containing nodes \
                   with more than one self-referenced field. A binary tree is made of nodes, \
                   where each node contains a left reference, a right reference, and a data element.\
                    The topmost node in the tree is called the root."
    text = text.split(' ')
    if characters in text[indx]:
        string += f'{ {text[indx]} } \n'
        # print(f'Words with this symbols "{characters}" are { {text[indx]} } ')
    if indx == len(text) - 1:
        return f'Recurse Done!!! \nFound: \n{string}'
    else:
        return recurs(indx + 1, string)

if __name__ == '__main__':
    print(recurs(0, ''))
