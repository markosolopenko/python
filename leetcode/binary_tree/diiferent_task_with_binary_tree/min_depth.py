from leetcode.binary_tree.diiferent_task_with_binary_tree.diameter_of_binary_tree import TreeNode


class Solution:
    def min_depth(self, root: TreeNode) -> int:
        return self.solve(root)

    def solve(self, root, depth=0):
        if root is None:
            return depth
        if root.right and root.left:
            return min(self.solve(root.left, depth + 1), self.solve(root.right, depth + 1))
        else:
            if root.left:
                return self.solve(root.left, depth + 1)
            else:
                return self.solve(root.right, depth + 1)