class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = []
        while l1 or l2:
            if l1 is None:
                new_list.append(l2.val)
                l2 = l2.next
            elif l2 is None:
                new_list.append(l1.val)
                l1 = l1.next
            else:
                new_list.append(l1.val)
                new_list.append(l2.val)
                l1 = l1.next
                l2 = l2.next
        return self.insert(sorted(new_list))

    def insert(self, some_list):
        """
        Insert data in linked list
        :param new_data:
        :return:
        """
        head = None
        for data in range(len(some_list)):
            new_node = ListNode(some_list[data])
            if head is None:
                head = new_node
            else:
                previous = head
                while previous.next:
                    previous = previous.next
                previous.next = new_node
        return head