class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_of_s = []
        a = 1
        if s == '':
            return 0
        elif s == ' ' or len(s) == 1:
            return 1
        else:
            for i in s:
                string = i
                for j in range(a, len(s)):
                    if s[j] not in string:
                        string += s[j]
                    else:
                        a += 1
                        break
                list_of_s.append(len(string))
            return max(list_of_s)