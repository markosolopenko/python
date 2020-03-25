# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def search_bst(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        res = []
        if root:
            if val < root.val:
                res = res + self.search_bst(root.left, val)
                res.append(root.val)
            if val > root.val:
                res = res + self.search_bst(root.right, val)
                res.append(root.val)
            return res


if __name__ == '__main__':
    root = Solution()

