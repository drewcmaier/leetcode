class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        MAX_VALUE = (10 ** 4) + 1

        min_val = MAX_VALUE
        max_val = 0
        profit = 0
        for i in range(0, len(prices)):
            if prices[i] <= min_val:
                min_val = prices[i]
                max_val = 0
            elif prices[i] >= max_val:
                max_val = prices[i]
                profit = max(profit, max_val - min_val)

        return profit
        
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([2,4,1,1]))
print(solution.maxProfit([2,1,2,1,0,1,2]))
print(solution.maxProfit([3,3,5,0,0,3,1,4]))