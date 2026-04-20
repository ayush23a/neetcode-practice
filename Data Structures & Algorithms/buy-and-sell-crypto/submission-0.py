class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_p = 0
        for sell in range(0, len(prices)):
            if sell < len(prices):
                if prices[buy] > prices[sell]:
                    buy = sell
                    sell = sell +1

                else :
                    max_p = max(max_p, (prices[sell] - prices[buy]))

        return max_p

                 