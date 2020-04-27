class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = -1
        k = 0
        if digits[-1] + 1 >= 10:
            if len(digits) > 1:
                while k != len(digits):
                    if digits[a] + 1 < 10:
                        digits[a] += 1
                        break
                    else:
                        digits[a] = 0
                        k += 1
                        a -= 1
                if k == len(digits):
                    digits.append(1)
                    digits.reverse()
            else:
                digits[a] = 1
                digits.append(0)
        else:
            digits[-1] = digits[-1] + 1
        return digits