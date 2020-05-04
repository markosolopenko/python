class Solution:
    def reverse(self, x: int) -> int:
        result = ''
        minus = ''
        for a in str(x):
            if a is not "-":
                result = a + result
            else:
                minus = a
        result = minus + result
        if (int(result) > (2**31)-1) or (int(result) <- (2**31)):
            return 0
        else:
            return int(result)


if __name__ == '__main__':
    clas = Solution()
    print(clas.reverse(-123))