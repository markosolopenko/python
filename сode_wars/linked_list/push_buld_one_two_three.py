class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None




def push(head, data):
    linked_list = Node()
    linked_list.head = Node(data)
    linked_list.head.next = head
    return linked_list.head

def build_one_two_three():
    head = None
    new_node = Node()
    first = push(head, 1)
    second = push(head, 2)
    third = push(head, 3)
    new_node.head = first
    first.next = second
    second.next = third
    return new_node.head





# change = push(None, 1)
# print(change.data)
# print(push(None, 1).next)
# print(push(Node(1), 2).data)
# print(push(Node(1), 2).next.data)

print(build_one_two_three().data)
print(build_one_two_three().next.data)
print(build_one_two_three().next.next.data)
print(build_one_two_three().next.next.next)
