from сode_wars.linked_list.push_buld_one_two_three import push, build_one_two_three
from сode_wars.linked_list.sorted_insert import sorted_insert
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_sort(head):
    """
    Sort
    :param h: head
    :return:
    """
    if head == None:
        return None
    # Just for check how sort work
    # new_node = Node(5)
    # new_node.next = head
    # new_node.head = new_node
    ####################


    sorted_list = head
    head = head.next
    sorted_list.next = None
    while head != None:
        current = head
        head = head.next
        if current.data < sorted_list.data:
            # Advance the nodes
            current.next = sorted_list
            sorted_list = current
        else:
            # Search list for correct position of current
            search = sorted_list
            while search.next != None and current.data > search.next.data:
                search = search.next
            # current goes after search
            current.next = search.next
            search.next = current
    return sorted_list
s = insert_sort(build_one_two_three())
print(s.data)
print(s.next.data)
print(s.next.next.data)
print(s.next.next.next)
