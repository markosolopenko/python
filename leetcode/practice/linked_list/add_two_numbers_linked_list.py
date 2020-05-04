class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        array_with_numbers = []
        additional = 0
        while l1 or l2:
            if l1 is None:
                combine = l2.val + additional
                if combine > 9 and combine < 20:
                    si = str(combine)
                    array_with_numbers.append(int(si[1]))
                    if l2.next:
                        additional = 1
                        l2 = l2.next
                    else:
                        additional = 0
                        array_with_numbers.append(int(si[0]))
                        l2 = l2.next
                else:
                    additional = 0
                    array_with_numbers.append(combine)
                    l2 = l2.next
            elif l2 is None:
                combine = l1.val + additional
                if combine > 9 and combine < 20:
                    si = str(combine)
                    array_with_numbers.append(int(si[1]))
                    if l1.next:
                        additional = 1
                        l1 = l1.next
                    else:
                        additional = 0
                        array_with_numbers.append(int(si[0]))
                        l1 = l1.next
                else:
                    additional = 0
                    array_with_numbers.append(combine)
                    l1 = l1.next
            else:
                result = l1.val + l2.val + additional
                additional = 0
                if result > 9 and result < 20:
                    si = str(result)
                    array_with_numbers.append(int(si[1]))
                    if l1.next is not None or l2.next is not None:
                        additional = 1
                        l1 = l1.next
                        l2 = l2.next
                    else:
                        si = str(result)
                        array_with_numbers.append(int(si[0]))
                        l1 = l1.next
                        l2 = l2.next
                else:
                    array_with_numbers.append(result)
                    l1 = l1.next
                    l2 = l2.next
        return self.insert(array_with_numbers)

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

if __name__ == '__main__':
    some_class = Solution()
    s = some_class.insert([18])
    print(s.val)