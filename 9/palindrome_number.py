class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = len(s)
        for i in range(0, l):
            if s[i] != s[l-i-1]:
                return False
            
        return True
        

solution = Solution()
print(solution.isPalindrome(101))
print(solution.isPalindrome(-101))
print(solution.isPalindrome(10))
print(solution.isPalindrome(2002))