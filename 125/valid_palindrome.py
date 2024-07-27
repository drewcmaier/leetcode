import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        formatted = re.sub(r'[^a-z0-9]', '', s.lower())
        print(formatted)
        return formatted[::-1] == formatted
        
        
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("0P"))