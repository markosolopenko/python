class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    a = 0
    while node:
        if a == index:
            break
        else:
            node = node.next
    if node is None:
        raise ValueError
    return node.data




print(get_nth(Node(1), 0))