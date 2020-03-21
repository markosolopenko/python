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
    previous = None
    current = head
    while (current):

        next_one = current.next
        current.next = previous

        # print_helper(previous, 'Previous')
        # print_helper(current, 'Current')
        # print_helper(next_one, 'NXT')
        previous = current
        current = next_one
    head = previous
    return head


s = reverse(build_one_two_three())
print(s.data)
print(s.next.data)
print(s.next.next.data)
print(s.next.next.next.data)
print(s.next.next.next.next)