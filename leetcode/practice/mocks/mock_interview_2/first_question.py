from typing import List


class Solution:
    def rotateString(self, string_a: str, string_b: str) -> bool:
        is_b = False
        i = 0
        string_a = [i for i in string_a]
        if len(string_a) == 0 and len(string_b) == 0:
            return True
        elif len(string_a) == 0 or len(string_b) == 0:
            return False
        while i != len(string_a) - 1:
            prev = 0
            while prev != len(string_a) - 1:
                string_a[prev], string_a[prev + 1] = string_a[prev + 1], string_a[prev]
                prev += 1
            if ''.join(string_a) == string_b:
                is_b = True
                break
            i += 1
        return is_b


if __name__ == '__main__':
    new_class = Solution()
    print(new_class.rotateString("", ""))
                                # cmbfg, mbfgc, bfgcm, fgcmb