from typing import List
from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        all_comb = [''.join(j) for i in range(1, len(tiles) + 1) for j in permutations(tiles, i)]
        return len(set(all_comb))

if __name__ == '__main__':
    new_class = Solution()
    print(new_class.numTilePossibilities("AAB"))
