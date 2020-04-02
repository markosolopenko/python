from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        must_be = []
        for a in range(len(nums)):
            result = target - nums[a]
            if result in nums and nums.index(result) != a:
                if result == nums[a]:
                    must_be.append(a)
                    nums[a] = -1
                    must_be.append(nums.index(result))
                    return must_be
                return [a, nums.index(target - nums[a])]



if __name__ == '__main__':
    my_class = Solution()
    print(my_class.two_sum([0,4,3,0], 0))