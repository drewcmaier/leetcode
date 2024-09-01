from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0] * l
        for i in range(l):
            sum_1 = dp[i-1] if i >= 1 else nums[i]
            sum_2 = nums[i] + dp[i-2] if i >= 2 else nums[i]
            if sum_1 > sum_2:
                dp[i] = sum_1
            else:
                dp[i] = sum_2
                
        return dp[l-1]
        
        
solution = Solution()
inputs = [
    [1,2,3,1],
    [2,7,9,3,1],
    [1,10,11,2,10]
]
for input in inputs:
    print(solution.rob(input))