# from _collections import deque
class Stack:
    """
    Creating Stack class
    """
    def __init__(self, size, default_value=None):
        """
        Initialize attributes of class and fill the list by default values
        :param size:
        :param default_value:
        """
        self.size = size
        self.default_value = default_value
        self.data = []
        for _ in range(size):
            self.data.append(default_value)




    def push(self, element):
        """
        Add elements to Stack
        :param element:
        :return:
        """
        for el in range(len(self.data)):
            if self.data[el] is None:
                self.data[el] = element
                break


    def pop(self):
        """
        delete element
        :return:
        """
        if self.data:
            top = -1
            while self.data[top] is None:
                top -= 1
            delete = self.data.pop()
            return delete
        else:
            return "Stack is empty"


    def peek(self):
        """
        take the argument from stack
        :return:
        """
        top = -1
        if self.data:
            while self.data[top] is None:
                top -= 1
            return self.data[top]
        else:
            return None

    def is_empty(self):
        """
        Check if Stack is empty
        :return:
        """
        for a in self.data:
            if a is not None:
                return False
        return True

    def length(self):
        """
        find length of Stack
        :return:
        """
        count = 0
        for a in self.data:
            if a is not None:
                count += 1
        return count


my_stack = Stack(3)
my_stack.push(12)
print(my_stack.peek())
print(my_stack.is_empty())
# assert my_stack.data == deque([12, None, None])
# my_stack.push(13)
# assert my_stack.data == deque([12, 13, None])
# my_stack.push(48)
# print(my_stack.peek())
# print(my_stack.peek())
# print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack.pop())
print(my_stack.data)
