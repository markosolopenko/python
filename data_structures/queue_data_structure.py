class QueueIsFull(Exception):
    """
    Class raise error
    """
    def __init__(self):
        super().__init__()



class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    def push(self, element):
        """
        Add element ot front of Queue
        :param element:
        :return:
        """
        try:
            if self.is_full() is True:
                raise QueueIsFull()
        except QueueIsFull:
            print(f"Queue is full")
        else:
            self.queue.insert(0, element)
    def pop_element(self):
        """
        If queue not empty pop(), the first element
        :return:
        """
        if self.is_empty():
            return f'Can\'t to pop() from empty Queue'
        else:
            return self.queue.pop(0)
    def is_empty(self):
        """
        Check whether queue is empty or not
        :return:
        """
        if self.queue:
            return False
        return True
    def is_full(self):
        """
        Check whether queue is full or not
        :return:
        """
        if self.size == len(self.queue):
            return True
        return False

    def peek(self):
        """
        If queue not empty, peek first element
        :return:
        """
        if not self.is_empty():
            return self.queue[0]

    def __str__(self):
        return self.queue



my_queue = Queue(5)
print(my_queue.is_empty())
my_queue.push(1)
my_queue.push(3)
my_queue.push(12)
my_queue.push(28)
my_queue.push(9)
my_queue.pop_element()
print(my_queue.peek())
print(my_queue.__str__())


