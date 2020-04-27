from typing import List
class Solution:
    def max_profit(self, prices: List[int]) -> int:
        arr_profit = []
        for j in range(0, len(prices) + 2):
            if j == len(prices) - 1:
                break
            if prices[j + 1] > prices[j]:
                arr_profit.append(prices[j + 1] - prices[j])

        if arr_profit:
            return sum(arr_profit)
        return 0

if __name__ == '__main__':
    my_class=Solution()
    print(my_class.max_profit([1,23,4,5,67,9]))