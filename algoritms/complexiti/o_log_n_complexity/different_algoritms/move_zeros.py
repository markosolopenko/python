from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]):
        n = len(nums)
        j = 0
        for i in nums:
            if i != 0:
                nums[j] = i
                j += 1

        for x in range(j, n):
            nums[x] = 0

        return nums


if __name__ == '__main__':
    m = Solution()
    print(m.move_zeroes([0, 1, 0, 12, 3, 0]))