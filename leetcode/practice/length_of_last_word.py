class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        print(s)
        if not s[-1]:
            return 0
        else:
            return len(s[-1])


if __name__ == '__main__':
    mine = Solution()
    print(mine.lengthOfLastWord(""))