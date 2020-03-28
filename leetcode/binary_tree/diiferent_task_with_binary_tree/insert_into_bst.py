from leetcode.binary_tree.diiferent_task_with_binary_tree.diameter_of_binary_tree import TreeNode


class Solution:
    def insert_into_bst(self, root: TreeNode, value: int) -> TreeNode:
        if root is not None:
            if root.val > value:
                if root.left is None:
                    root.left = TreeNode(value)
                else:
                    self.insert_into_bst(root.left, value)
            elif root.val < value:
                if root.right is None:
                    root.right = TreeNode(value)
                else:
                    self.insert_into_bst(root.right, value)
            return root
        else:
            root.val = value
            return root




if __name__ == '__main__':
    my_class = Solution()
    new_root = TreeNode(1)
    new_root.insert(2)
    new_root.insert(3)
    new_root.insert(4)
    new_root.insert(5)
    print(new_root.print_tree())
