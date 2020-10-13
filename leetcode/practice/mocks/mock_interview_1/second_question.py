from typing import List
import collections

class Solution:
    def gardenNoAdj(self, num: int, paths: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in paths:
            graph[a].append(b)
            graph[b].append(a)
        colors = [0] * num
        for node in range(1, num + 1):
            nei_colors = []
            for nei in graph[node]:
                nei_colors.append(colors[nei - 1])
            for k in range(1, 5):
                if k not in nei_colors:
                    colors[node - 1] = k
                    break
        return colors

if __name__ == '__main__':
    new_class = Solution()
    print(new_class.gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))