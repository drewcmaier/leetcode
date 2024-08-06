class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_num = int(a, 2)
        b_num = int(b, 2)
        sum_binary = bin(a_num+b_num)
        return sum_binary[2:]


solution = Solution()
print(solution.addBinary("11", "1"))
print(solution.addBinary("1010", "1011"))