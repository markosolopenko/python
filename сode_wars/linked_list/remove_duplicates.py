from сode_wars.linked_list.push_buld_one_two_three import push,build_one_two_three
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    temp = head
    if temp is None:
        return
    while temp.next is not None:
        if temp.data == temp.next.data:
            new = temp.next.next
            temp.next = None
            temp.next = new
        else:
            temp = temp.next
    return head


s = remove_duplicates(build_one_two_three())
print(s.data)
print(s.next.data)
print(s.next.next.data)
print(s.next.next.next)
# print(s.next.next.next.next)