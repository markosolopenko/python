from сode_wars.linked_list.push_buld_one_two_three import push, build_one_two_three


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sorted_list_to_bst(self, head: ListNode) -> TreeNode:
        list_of_elements = self.linked_list_to_list(head)
        return self.binary_tree(list_of_elements)

    def linked_list_to_list(self, head: ListNode):
        new_list = []
        while head is not None:
            new_list.append(head.data)
            head = head.next
        return new_list

    def binary_tree(self, some_list):
        if not some_list:
            return None
        mid = len(some_list) // 2
        root = TreeNode(some_list[mid])
        root.left = self.binary_tree(some_list[:len(some_list) // 2])
        root.right = self.binary_tree(some_list[len(some_list) // 2 + 1:])
        return root


if __name__ == '__main__':
    my_class = Solution()
    # s = my_class.linked_list_to_list(build_one_two_three())
    # print(s)
    result = my_class.sorted_list_to_bst(build_one_two_three())
    print(result.val, result.left.val, result.right.val)
