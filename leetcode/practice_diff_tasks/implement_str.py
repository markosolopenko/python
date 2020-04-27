class Solution:
    def string(self, haystack: str, needle: str) -> int:
        find = haystack.find(needle)
        return find
        # res = ''
        # switch = True
        # if needle in haystack:
        #     for i in range(len(haystack) + 1):
        #         print(res)
        #         if needle in res:
        #             switch = False
        #             break
        #         else:
        #             res += haystack[i]
        #     if switch == False:
        #         return len(res) - len(needle)
        #     else:
        #         return 0
        # else:
        #     return -1


if __name__ == '__main__':
    mine = Solution()
    print(mine.string("a", "b"))