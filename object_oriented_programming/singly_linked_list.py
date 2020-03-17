# class Node(object):
#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next_node = next_node
#
#
#     def get_data(self):
#         return self.data, self.next_node
#
#
#     def get_next(self):
#         return self.get_data
#
#     def set_next(self, new_next):
#         self.data, self.next_node = new_next
#
#
# class SinglyLinkedList(object):
#     def __init__(self, head: Node = None):
#         self.head = head
#         self.linked_list = []
#
#     def insert(self, inx, data):
#         self.linked_list.insert(inx, data)
#         return self.linked_list
#
#     def size(self):
#         return self.linked_list.__len__()
#
#     def search(self, data):
#         if data in self.linked_list:
#             return data
#
#     def delete(self, data):
#         delattr(self.linked_list, data)

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
            NewNode = Node(newdata)
            NewNode.nextval = self.headval
            self.headval = NewNode


list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")

list1.headval.nextval = e4

e2.nextval = e3
# e3.nextval = e4

list1.AtBegining('Sun')
print(list1.listprint())
