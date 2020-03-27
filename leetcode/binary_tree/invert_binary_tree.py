from leetcode.binary_tree.diameter_of_binary_tree import TreeNode
# Definition for a binary tree node.

class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invert_tree(root.left)
            self.invert_tree(root.right)
            return root
        else:
            return






if __name__ == '__main__':
    my_class = Solution()
    new_root = TreeNode(-8)
    new_root.insert(-6), new_root.insert(7), new_root.insert(6), new_root.insert(5)
    new_root.insert(3), new_root.insert(9)
    print(new_root.print_tree())
    s = my_class.invert_tree(new_root)
    print(s.val, s.left.val, s.right.val,
          s.left.left.val, s.left.right.val,
          s.right.left.val, s.right.right.val)