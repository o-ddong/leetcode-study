"""
TC - O(n)
    ㄴ 주어진 배열을 끝까지 탐색하므로 O(n)이라고 생각합니다.
SC - O(1)
    ㄴ 추가적으로 사용하는 공간이 상수 크기이므로 O(1)이라고 생각합니다.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
            
        return max_profit
