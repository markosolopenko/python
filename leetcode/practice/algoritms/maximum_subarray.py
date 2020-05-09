from typing import List


def maxSubArray(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i - 1] + nums[i], nums[i])
    return max(nums)


if __name__ == '__main__':
    print(maxSubArray([-2, 1, -1, 1, -3, 4, -5, 4]))