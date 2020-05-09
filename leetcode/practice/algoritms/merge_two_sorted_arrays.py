from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    index = 0
    for i in range(len(nums1)):
        if index == len(nums2):
            break
        if nums1[i] == 0:
            nums1[i] = nums2[index]
            index += 1
    return sorted(nums1)


if __name__ == '__main__':
    print(merge([1, 2, 3, 4, 5, 0, 0, 0,], 8, [2, 3, 5], 3))
