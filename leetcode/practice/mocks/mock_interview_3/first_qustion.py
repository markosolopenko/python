from typing import List


class TreeNode:
    def __init__(self):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

            # Could be a larger subtree to the right
        if root.val < L:
            return self.trimBST(root.right, L, R)

            # Could have a smaller subtree to the left
        if root.val > R:
            return self.trimBST(root.left, L, R)

            # Recursively trim
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


if __name__ == '__main__':
    solution = Solution()
    print(solution.trimBST())


