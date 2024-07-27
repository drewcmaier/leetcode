class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # int[] --> string
        s = "".join(str(i) for i in digits)
        # string --> number, add 1
        n = int(s)+1
        # number --> string --> int[]
        a = [int(i) for i in str(n)]
        return a


solution = Solution()
print(solution.plusOne([8] * 100))