from typing import List
from string import ascii_lowercase

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alphabet = ascii_lowercase
        integers = '0123456789'
        copy_logs = logs[:]
        for i in range(len(logs)):
            prev = i
            while prev != len(logs) - 1:
                if logs[prev].split(' ')[1:][0] > logs[prev+1].split(' ')[1:][0]:
                    logs[prev], logs[prev+1] = logs[prev+1], logs[prev]
                    prev += 1
                elif ''.join(logs[prev].split(' ')[1:]) == ''.join(logs[prev+1].split(' ')[1:]):
                    if ''.join(logs[prev].split(' ')) > ''.join(logs[prev+1].split(' ')):
                        logs[prev], logs[prev + 1] = logs[prev + 1], logs[prev]
                        prev += 1
                    else:
                        prev += 1
                else:
                    prev += 1
        result = [i for i in logs if i[-1] in alphabet]

        for i in copy_logs:
            if i[-1] in integers:
                result.append(i)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reorderLogFiles(["j mo", "5 m w", "g 07", "o 2 0", "t q h"]))