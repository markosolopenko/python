from typing import List


def third_max(nums: List[int]) -> int:
    nums = set(nums)
    if len(nums) == 2:
        return max(nums)
    else:
        count = 0
        max_num = 0
        length = len(nums)
        for _ in range(length):
            if count >= 2:
                max_num = max(nums)
                break
            max_num = max(nums)
            nums.remove(max_num)
            count += 1
        return max_num


if __name__ == '__main__':
    print(third_max([3, 2, 1]))
