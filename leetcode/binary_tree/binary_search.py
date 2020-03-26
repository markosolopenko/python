from bisect import bisect_left
from typing import List

def binary_search(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        return -1
    # i = bisect_left(a, x)
    # if i != len(a) and a[i] == x:
    #     return i
    # else:
    #     return -1


if __name__ == '__main__':
    print(binary_search([-1,0,3,5,9,12], 2))