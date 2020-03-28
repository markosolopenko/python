# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def insert(self, element):
        if self.val:
            if element < self.val:
                if self.left is None:
                    self.left = TreeNode(element)
                else:
                    self.left.insert(element)
            elif element > self.val:
                if self.right is None:
                    self.right = TreeNode(element)
                else:
                    self.right.insert(element)
        else:
            self.val = element

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val, end=' ')
        if self.right:
            self.right.print_tree()


class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:

        self.answer = 0
        self.dfs(root)
        return self.answer

    def dfs(self, node):
        if not node:
            return 0
        left_node = self.dfs(node.left)
        right_node = self.dfs(node.right)
        self.answer = max(self.answer, right_node + left_node)
        return max(left_node + 1, right_node + 1)





if __name__ == '__main__':
     my_class = Solution()
     new_root = TreeNode(1)
     new_root.insert(2)
     new_root.insert(3)
     new_root.insert(4)
     new_root.insert(5)
     print(new_root.print_tree())
     print(my_class.diameter_of_binary_tree(new_root))

