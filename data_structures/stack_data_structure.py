from _collections import deque
from queue import LifoQueue


class Stack:
    """
    Creating Stack class
    """
    def __init__(self):
        """
        Initialize attributes of class
        """
        self.data = deque()




    def push(self, element):
        """
        Add elements to Stack
        :param element:
        :return:
        """
        self.data.append(element)


    def pop(self):
        """
        delete element
        :return:
        """
        try:
            return self.data.pop()
        except IndexError:
            return 'Sorry but stack is empty'

    def peek(self):
        """
        take the argument from stack
        :return:
        """
        return self.data[-1]
    def is_empty(self):
        """
        Check if Stack is empty
        :return:
        """
        if self.data:
            return False
        return True

    def length(self):
        """
        find length of Stack
        :return:
        """
        count = 0
        for _ in self.data:
            count += 1
        return count

    def is_balanced(self, expression):
        exist_braces = {'{': '}', '[': ']', '(': ')'}
        queue = []
        for brace in expression:
            if brace in exist_braces.keys():
                queue.append(exist_braces[brace])
            elif brace in exist_braces.values():
                if not queue or brace != queue.pop():
                    return False
        return not queue




my_stack = Stack()
# my_stack.push(12)
# print(my_stack.peek())
# print(my_stack.is_empty())
# my_stack.push(48)
# print(my_stack.peek())
# print(my_stack.peek())
# print(my_stack.length())
# print(my_stack.is_empty())
# print(my_stack.data)
assert my_stack.is_balanced('(()()())') is True
assert my_stack.is_balanced('())') is False
assert my_stack.is_balanced('[](){({}{[]})}') is True
assert my_stack.is_balanced('[{]}') is False
