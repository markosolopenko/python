from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = []
        for i in nums:
            if i not in majority and nums.count(i) > len(nums) / 3:
                majority.append(i)
        return majority


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([3, 2, 3]))
