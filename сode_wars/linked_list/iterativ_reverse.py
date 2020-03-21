from сode_wars.linked_list.push_buld_one_two_three import build_one_two_three
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def print_helper(node, name):
    if node is None:
        print(f'{name}: None')
    else:
        print(f'{name}: {node.data}')

def reverse(head):
    linked_list = head
    size_linked_list = 0
    while linked_list is not None:
        size_linked_list += 1
        linked_list = linked_list.next
    for i in range(size_linked_list - 1, 0, -1):
        xcount = 0
        linked_list = head
        while (xcount != i):
            linked_list.data, linked_list.next.data = linked_list.next.data, linked_list.data
            linked_list = linked_list.next
            xcount += 1
    return head



s = reverse(build_one_two_three())
print(s.data)
print(s.next.data)
print(s.next.next.data)
print(s.next.next.next.data)
print(s.next.next.next.next)