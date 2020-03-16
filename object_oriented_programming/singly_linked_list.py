class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def get_data(self):
        return self.data, self.next_node


    def get_next(self):
        return self.get_data

    def set_next(self, new_next):
        self.data, self.next_node = new_next


class SinglyLinkedList(object):
    def __init__(self, head: Node = None):
        self.head = head
        self.linked_list = []

    def insert(self, inx, data):
        self.linked_list.insert(inx, data)
        return self.linked_list

    def size(self):
        return self.linked_list.__len__()

    def search(self, data):
        if data in self.linked_list:
            return data

    def delete(self, data):
        delattr(self.linked_list, data)

some = Node()
print(some.get_data)

a = SinglyLinkedList(Node(3))
print(a.head.get_data)
# print(a.insert(1, '3'))
# print(a.size())
# print(a.delete('3'))
# print(a.size())

