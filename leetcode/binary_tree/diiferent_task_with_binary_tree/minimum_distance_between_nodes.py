from leetcode.binary_tree.diiferent_task_with_binary_tree.diameter_of_binary_tree import TreeNode


class Solution:
    def min_diff_in_bst(self, root: TreeNode) -> int:
        """
        Searching min distance between each node
        :param root:
        :return:
        """
        list_elements = self.convert_to_list(root)
        new_list = []
        for i in list_elements:
            for j in list_elements:
                if i > j:
                    res = i - j
                    new_list.append(res)
                elif j > i:
                    res = j - i
                    new_list.append(res)
        return min(new_list)

    def convert_to_list(self, root):
        """
        Convert tree to list
        For me it is more easy
        :param root:
        :return:
        """
        res = []
        if root:
            res.append(root.val)
            res = res + self.convert_to_list(root.left)
            res = res + self.convert_to_list(root.right)
        return res



if __name__ == '__main__':
    class_mine = Solution()
    new_node = TreeNode(12)
    new_node.insert(2)
    new_node.insert(3)
    some = class_mine.min_diff_in_bst(new_node)