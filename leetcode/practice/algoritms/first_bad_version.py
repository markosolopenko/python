import math


class Solution:
    def first_bad_version(self, n) -> int:
        left = 0
        right = n
        while left < right:
            mid = math.floor(left + (right - left) / 2)
            print(mid)

            if is_bad_version(mid) is False:
                left = mid + 1

            else:
                right = mid

        return left


def is_bad_version(n):
    bad = 4
    if n == bad:
        return True
    else:
        return False


if __name__ == '__main__':
    my_class = Solution()
    print(my_class.first_bad_version(5))