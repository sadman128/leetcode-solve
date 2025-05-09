class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit = + profit + prices[i+1] - prices[i]

        return profit




prices = [7,1,5,3,6,4]
res = Solution().maxProfit(prices)
print(res)
