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
    s = my_class.sorted_array_to_bst([1, 2, 3, 4, 5, 6])
    print(s.val, s.left.val, s.right.val, s.left.right.val, s.right.left.val)
    
    
    



def res(arr):
    if not arr:
        return
    mis = arr[len(arr) // 2]
    root = TreeNode(mis)
    root.left = res(arr[:len(arr) // 2])
    root.right = res(arr[len(arr) // 2+1:])
    return root

new = res([1, 2, 3, 4, 5, 6])


print(f'       {new.val}       ')
print(f'    /     \\')
print(f'   {new.left.val}        {new.right.val}')
print(f'  /  \     / \\')
print(f'{new.left.left.val}      {new.left.right.val}  {new.right.left.val}  {new.right.right}')


