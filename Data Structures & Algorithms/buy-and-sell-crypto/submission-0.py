class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        sell=0
        for i in range(len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            current_profit=prices[i]-buy
            if profit<current_profit:
                profit=current_profit
        return profit 

        