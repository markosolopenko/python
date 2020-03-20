from сode_wars.linked_list.push_buld_one_two_three import push, build_one_two_three
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def insert_nth(head, index, data):
        """
        Append data by index
        :param head:
        :param index:
        :param data:
        :return:
        """
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



s = insert_nth(build_one_two_three(), 2, 23)
print(s.data)
print(s.next.data)
print(s.next.next.data)
print(s.next.next.next.data)
print(s.next.next.next.next)

