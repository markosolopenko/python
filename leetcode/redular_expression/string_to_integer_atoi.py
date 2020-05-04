import re


class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.search(r'^[+-]?\d(\d)*', s.strip())
        if match:
            return min(2**31-1, max(-2**31, int(match.group(0))))
        return 0


if __name__ == '__main__':
    my_class =Solution()
    print(my_class.myAtoi('42'))
