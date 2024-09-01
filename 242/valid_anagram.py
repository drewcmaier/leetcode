class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
solution = Solution()
inputs = [
    ("anagram","nagaram"),
    ("rat","car")
]
for input in inputs:
    print(solution.isAnagram(input[0], input[1]))
    