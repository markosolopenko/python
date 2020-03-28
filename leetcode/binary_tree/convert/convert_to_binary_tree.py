from leetcode.binary_tree.diiferent_task_with_binary_tree.diameter_of_binary_tree import TreeNode
from typing import List


class Solution:
    def sorted_array_to_bst(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = nums[len(nums) // 2]
        root = TreeNode(mid)
        root.left = self.sorted_array_to_bst(nums[:len(nums) // 2])
        root.right = self.sorted_array_to_bst(nums[len(nums) // 2 + 1:])
        return root


if __name__ == '__main__':
    my_class = Solution()
    s = my_class.sorted_array_to_bst([-10, -3, 0, 5, 9])
    print(s.val, s.left.val, s.right.val)
