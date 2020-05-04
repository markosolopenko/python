from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for a in range(len(nums)):
            prev = a
            while prev > 0 and nums[prev] < nums[prev-1]:
                nums[prev], nums[prev-1] = nums[prev-1], nums[prev]
                prev -= 1


if __name__ == '__main__':
    my_class=Solution()
    print(my_class.sortColors([1, 3, 4, 5, 5]))