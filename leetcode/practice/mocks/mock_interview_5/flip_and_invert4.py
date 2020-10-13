from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for arr in A:
            arr.reverse()
            for ind in range(len(arr)):
                if arr[ind] == 1:
                    arr[ind] = 0
                elif arr[ind] == 0:
                    arr[ind] = 1
        return A


if __name__ == '__main__':
    new_class = Solution()
    print(new_class.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))