class Solution:
    def hammingWeight(self, n: int) -> int:
        num_1_bits = 0
        
        for _ in range(0, 32):
            if n & 1 == 1:
                num_1_bits += 1
            n = n >> 1

        return num_1_bits
    
solution = Solution()
inputs = [
    2147483645,
    11,
    128,
]
for input in inputs:
    print(solution.hammingWeight(input))
