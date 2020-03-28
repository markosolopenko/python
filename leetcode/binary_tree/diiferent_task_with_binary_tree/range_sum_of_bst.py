from leetcode.binary_tree.diiferent_task_with_binary_tree.diameter_of_binary_tree import TreeNode

class Solution:
    def range_sum_bst(self, root: TreeNode, left_node: int, right_node: int) -> int:
        """
        passing the loop and just sum all elements with certain rules
        :param root:
        :param left_node:
        :param right_node:
        :return:
        """
        if root:
            list_with_nodes = self.in_order_traversal(root)
            sum_of_elements = 0
            for a in range(1, len(list_with_nodes)):
                if list_with_nodes[a] >= left_node and list_with_nodes[a] <= right_node:
                    sum_of_elements += list_with_nodes[a]
            return sum_of_elements


    def in_order_traversal(self, root: TreeNode):
        """
        Add elements to list for more convenient
        :param root:
        :return:
        """
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.val)
            res = res + self.in_order_traversal(root.right)
        return res








if __name__ == '__main__':
    my_class = Solution()
    new_root = TreeNode(1)
    new_root.insert(2)
    new_root.insert(3)
    new_root.insert(4)
    new_root.insert(5)
    print(new_root.print_tree())
    print(my_class.range_sum_bst(new_root, 2, 5))