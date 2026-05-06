class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_p=prices[0]

        for i in range(len(prices)):
            if buy_p > prices[i]:
                buy_p = prices[i]
            sell_value = prices[i] - buy_p
            if profit < sell_value:
                profit = sell_value
        return profit
            

        