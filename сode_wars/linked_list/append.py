from сode_wars.linked_list.push_buld_one_two_three import build_one_two_three


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def append(list_a, list_b):
    if list_a == None:
        return list_b
    elif list_b == None:
        return list_a
    else:
        current = list_a
        while current.next is not None:
            current = current.next
        current.next = list_b
        return list_a
s = append(build_one_two_three(), build_one_two_three())
print(s.data)
print(s.next.data)
print(s.next.next.data)
print(s.next.next.next.data)
print(s.next.next.next.next.data)
print(s.next.next.next.next.next.data)




