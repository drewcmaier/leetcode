class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = 1
        while (val*val <= x):
            val += val
        return val-1
        
solution = Solution()
print(solution.mySqrt(8))
print(solution.mySqrt(9))
print(solution.mySqrt(64))