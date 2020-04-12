from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        switch = True
        indx = 0
        prefix = ''
        if not strs:
            return ''
        for i in strs[0]:
            check = i
            for j in strs:
                if len(j) <= indx or j[indx] != check:
                    switch = False
            if switch == False:
                return prefix
            else:
                prefix += check
                indx += 1
        return prefix


if __name__ == '__main__':
    may = Solution()
    print(may.longest_common_prefix(["aa","a"]))