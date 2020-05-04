class Solution:
    def roman_to_int(self, s: str) -> int:
        some_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for roman in range(len(s)):
            if roman == len(s) - 1:
                result += some_dict[s[roman]]
                break
            else:
                if  s[roman] == 'I' and s[roman+1] == 'X' or s[roman] == 'I' and s[roman+1] == 'V':
                    result -= 1
                elif s[roman] == 'X' and s[roman+1] == 'L' or s[roman] == 'X' and s[roman+1] == 'C':
                    result -= 10
                elif s[roman] == 'C' and s[roman+1] == 'D' or s[roman] == 'C' and s[roman+1] == 'M':
                    result -= 100
                else:
                    result += some_dict[s[roman]]
        return result