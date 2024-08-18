class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = ""
        for i in range(0, len(strs[0])+1):
            cur_prefix = strs[0][0:i]
            for s in strs:
                if not s.startswith(cur_prefix):
                    return prefix
            
            prefix = cur_prefix    

        return prefix

solution = Solution()
inputs = [
    ["flower","flow","flight"],
    ["dog","racecar","car"],
    [],
    ["", ""],
    ["a"]
]
for input in inputs:
    print(solution.longestCommonPrefix(input))
