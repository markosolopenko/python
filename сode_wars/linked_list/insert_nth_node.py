class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def insert_nth(head, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.next = head
            new_node.head = new_node
            return new_node
        else:
            new_node = Node(data)


            previous_node = head
            current_node = head.next
            index_of_el = 1

            while current_node is not None and index_of_el <= index - 1:
                previous_node = current_node
                current_node = current_node.next
                index_of_el += 1
            previous_node.next = new_node
            new_node.next = current_node
            if index > index_of_el:
                raise ValueError
            return head


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


s = insert_nth(build_one_two_three(), 5, 23)
print(s.data)
print(s.next.data)
print(s.next.next.data)
print(s.next.next.next.data)
print(s.next.next.next.next)

