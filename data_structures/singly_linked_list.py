class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = next

    # def get_data(self):
    #     """
    #     This method like -> @property
    #     :return:
    #     """
    #     return self.data
    #
    #
    # def get_next(self):
    #     """
    #     getter
    #     :return:
    #     """
    #     return self.next_node

    # def set_next(self, new_next):
    #     """
    #     setter
    #     :param new_next:
    #     :return:
    #     """
    #     self.next_node = new_next


class SinglyLinkedList(object):
    def __init__(self, head: Node = None):
        self.head = head

    def insert(self, new_data):
        """
        Insert data in linked list
        :param new_data:
        :return:
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


        # current = self.head
        # if
        # new_node = Node(new_data)
        # new_node.next = self.head
        # self.head =



    def size(self):
        """
        Find length of linked list
        :return:
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        """
        Searching data in linked list
        :param data:
        :return:
        """
        current = self.head
        while current:
            if current.get_data() == data:
                break
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data_to_remove):
        """
        Removing data from linked list
        :param data_to_remove:
        :return:
        """
        current_value = self.head
        previous = None
        while current_value:
            if current_value.get_data() == data_to_remove:
                break
            else:
                previous = current_value
                current_value = current_value.get_next()
        if current_value is None:
            raise ValueError("Data is not in list")
        if previous is None:
            self.head = current_value.get_next()
        else:
            previous.set_next(current_value.get_next())

    def print_list(self):
        """
        Traversing the list
        :return:
        """
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next





# linked_list = SinglyLinkedList()
# linked_list.head = Node('Hello')
# e1 = Node('Mi')
# e2 = Node('Si')
#
# linked_list.head.set_next(e1)
# e1.set_next(e2)
# print(linked_list.search("Mi").get_data())
# print(linked_list.delete("Hello"))
# print(linked_list.size())
# print(linked_list.print_list())

a = SinglyLinkedList()
a.insert(12)
a.insert(2)
a.insert(48)
a.print_list()

