class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self, ):
        self.head = None
    def addTwoNumbers(self, l1, l2):
        first = self.convert_to_list_1(l1)
        second = self.convert_to_list_2(l2)


        add_two_lists = int(''.join(first)) + int(''.join(second))
        final_list = [int(i) for i in str(add_two_lists)]
        result = self.convert_to_linked_list(final_list)

        return result

    def convert_to_linked_list(self, arr):
        for i in arr:
            new_node = ListNode(i)
            new_node.next = self.head
            self.head = new_node
        return self.head


    def convert_to_list_1(self, node1):
        arr = []
        while node1:
            arr.append(str(node1.val))
            node1 = node1.next
        return arr

    def convert_to_list_2(self, node2):
        arr = []
        while node2:
            arr.append(str(node2.val))
            node2 = node2.next
        return arr


if __name__ == '__main__':
    solution = Solution()
    print(solution.addTwoNumbers())