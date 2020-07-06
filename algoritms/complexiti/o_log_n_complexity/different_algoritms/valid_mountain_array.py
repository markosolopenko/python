from typing import List


class Solution:
    def valid_mountain_array(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        i = 1
        while i < len(A) and A[i] > A[i - 1]:
            i += 1

        if i == 1 or i == len(A):
            return False

        while i < len(A) and A[i] < A[i - 1]:
            i += 1

        return i == len(A)


if __name__ == '__main__':
    class_s = Solution()
    print(class_s.valid_mountain_array([1, 3, 2]))
