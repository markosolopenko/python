# from leetcode.binary_tree.diameter_of_binary_tree import TreeNode
from typing import List


class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, element):
        if self.data is not None:
            if self.data > element:
                if self.left is None:
                    self.left = TreeNode(element)
                else:
                    self.left.insert(element)
            elif self.data < element:
                if self.right is None:
                    self.right = TreeNode(element)
                else:
                    self.right.insert(element)
        else:
            self.data = element


class Solution:
    def binary_search_algorithm(self, root: TreeNode, array: List[int], element: int):
        try:
            if root and root.data != element:
                if root.data > element:
                    return self.binary_search_algorithm(root.left, array, element)
                else:
                    return self.binary_search_algorithm(root.right, array, element)
            return array.index(element)
        except ValueError:
            return None



if __name__ == '__main__':
    my_class = Solution()
    new_root = TreeNode(2)
    new_root.insert(5)
    new_root.insert(8)
    new_root.insert(4)
    print(my_class.binary_search_algorithm(new_root, [1, 2, 3, 7], 1))