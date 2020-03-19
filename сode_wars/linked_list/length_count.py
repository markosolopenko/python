class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def length(node):
    current = node
    length_of_list = 0
    while current:
        length_of_list += 1
        current = current.next
    return length_of_list

def count(node, data):
    amount_of_element = 0
    while node is not None:
        if node.data == data:
            amount_of_element += 1
            node = node.next
        else:
            node = node.next
    return amount_of_element

print(count(Node(2), 2))
