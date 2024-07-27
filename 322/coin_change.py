class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX_VALUE = 10**4 +1

        dp = [MAX_VALUE] * (amount+1)

        dp[0] = 0
        for i in range(0, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c]+1)

        return -1 if dp[amount] == MAX_VALUE else dp[amount]


        
solution = Solution()
print(solution.coinChange([186,419,83,408], 6249))
print(solution.coinChange([2147483647], 2))
# print(solution.coinChange([1, 2, 5], 11))
# print(solution.coinChange([2], 3))
# print(solution.coinChange([1], 0))