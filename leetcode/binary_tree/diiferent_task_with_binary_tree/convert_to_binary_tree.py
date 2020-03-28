from leetcode.binary_tree.diiferent_task_with_binary_tree.diameter_of_binary_tree import TreeNode
from typing import List


class Solution:
    def sorted_array_to_bst(self, nums: List[int]) -> TreeNode:
        if nums:
            middle = len(nums) // 2
            root = TreeNode(nums[middle])
            nums.pop(middle)
            nums.reverse()
            for a in nums:
                self.insert_element(root, a)
            return root

    def insert_element(self, root: TreeNode, value):
        if root.val > value:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                self.insert_element(root.left, value)
        elif root.val < value:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                self.insert_element(root.right, value)
        return root


if __name__ == '__main__':
    my_class = Solution()
    s = my_class.sorted_array_to_bst([-10, -3, 0, 5, 9])
    print(s.val, s.left.val, s.right.val)
