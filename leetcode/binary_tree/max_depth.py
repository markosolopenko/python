from leetcode.binary_tree.diameter_of_binary_tree import TreeNode
# Definition for a binary tree node.

class Solution:
    def max_depth(self, root: TreeNode) -> int:
        return self.solve(root)

    def solve(self, root, depth=0):
        if root is None:
            return depth
        return min(self.solve(root.left, depth + 1), self.solve(root.right, depth + 1))

if __name__ == '__main__':
    my_class = Solution()
    new_root = TreeNode(-8)
    new_root.insert(-6)
    print(new_root.print_tree())
    s = my_class.max_depth(new_root)
    print(s)