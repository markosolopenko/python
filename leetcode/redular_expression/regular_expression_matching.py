import re


class Solution:
    def is_match(self, s: str, p: str) -> bool:
        return True if re.fullmatch(p, s) else False


if __name__ == '__main__':
    class_my = Solution()
    print(class_my.is_match('aa', 'a'))
