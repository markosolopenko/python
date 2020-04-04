class Solution:
    def is_palindrome(self, x) -> bool:
        if len(str(x)) <= 1:
            return True
        if str(x)[0] != str(x)[-1]:
            return False
        else:
            return self.is_palindrome(str(x)[1:-1])


if __name__ == '__main__':
    some = Solution()
    print(some.is_palindrome(123))