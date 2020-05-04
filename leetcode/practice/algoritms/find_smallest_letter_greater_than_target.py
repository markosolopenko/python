from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        switch = True
        a = 1
        while switch:
            suma = alphabet[(alphabet.index(target)+a) % len(alphabet)]
            if suma in letters:
                switch = False
            else:
                a += 1
        return suma
    

if __name__ == '__main__':
    class_my= Solution()
    print(class_my.nextGreatestLetter(['a', 'c', 'f'], 'd'))