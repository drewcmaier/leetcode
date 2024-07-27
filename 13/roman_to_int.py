class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(0, len(s)):
            # get current digit and digit to the left
            d = s[i]
            d_next = s[i+1] if i < len(s)-1 else None

            if d == 'I':
                sum += 1 if d_next != 'V' and d_next != 'X' else -1
            elif d == 'V':
                sum += 5
            elif d == 'X':
                sum += 10 if d_next != 'L' and d_next != 'C' else -10
            elif d == 'L':
                sum += 50
            elif d == 'C':
                sum += 100 if d_next != 'D' and d_next != 'M' else -100
            elif d == 'D':
                sum += 500
            elif d == 'M':
                sum += 1000
            
            i -= 1

        return sum
        
solution = Solution()
print(solution.romanToInt("MCMLXXXVIII"))
