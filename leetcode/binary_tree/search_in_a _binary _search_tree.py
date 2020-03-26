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
        if root and root.val != val:
            if root.val > val:
                return self.search_bst(root.left, val)
            else:
                return self.search_bst(root.right, val)
        return root


if __name__ == '__main__':
    root = Solution()
    print(root.search_bst(TreeNode(12), 12).val)

