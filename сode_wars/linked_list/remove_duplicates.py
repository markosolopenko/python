from сode_wars.linked_list.push_buld_one_two_three import push,build_one_two_three
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head, element):
    current_el = head
    if current_el.data == element:
        current_el = current_el.next
        return current_el
    else:


s = remove_duplicates(build_one_two_three(), 1)
print(s.data)
print(s.next.data)
print(s.next.next.data)
# print(s.next.next.next.data)
