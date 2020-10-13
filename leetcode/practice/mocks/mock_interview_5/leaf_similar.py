
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, data):
        if self.val:
            if self.val > data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif self.val < data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        pass


if __name__ == '__main__':
    node = TreeNode()
    node.insert(3)
    node.insert(5)
    node.insert(1)
    node.insert(6)
    node.insert(2)
    node.insert(7)
    node.print_tree()

    solution = Solution()
    print(solution.leafSimilar(node, node))

