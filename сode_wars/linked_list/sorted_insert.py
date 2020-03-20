from сode_wars.linked_list.push_buld_one_two_three import push, build_one_two_three

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None



def sorted_insert(head, data):
    new_node = Node(data)
    previous_node = head
    if head is None:
        head = new_node
        new_node.next = None
        return new_node
    else:
        current_node = head.next

        while current_node is not None:
            if new_node.data > previous_node.data and new_node.data < current_node.data:
                previous_node.next = new_node
                new_node.next = current_node
                break
            elif current_node.next is None:
                current_node.next = new_node
                new_node.next = None
                break
            elif new_node.data < head.data:
                new_node.next = head
                new_node.head = new_node
                return new_node
            else:
                previous_node = current_node
                current_node = current_node.next
        return head






#
# s = sorted_insert(build_one_two_three(), 0.5)
# print(s.data)
# print(s.next.data)



