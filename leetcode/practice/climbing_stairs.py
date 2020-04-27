class Solution:
    def climbStairs(self, n: int) -> int:
        count = 1
        if n == 1:
            return 1
        else:
            for i in range(1, n):
                for j in range(1, n):
                    print(i + j)
                    if i + j == n:
                        count += 1

            return count


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.climbStairs(4))