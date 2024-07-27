class Solution(object):
    # map item to ordinal, eg abba --> 0110
    def createIndexMap(self, iterable):
        map = {}
        cur_index = 0
        for i in range(0, len(iterable)):
            if iterable[i] not in map:
                map[iterable[i]] = cur_index
                cur_index += 1

        return map

    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        
        word_index = self.createIndexMap(words)
        pattern_index = self.createIndexMap(pattern)

        # check if mapping is equivalent at each index
        for i in range(0, len(words)):
            if word_index[words[i]] != pattern_index[pattern[i]]:
                return False
            
        return True
        
solution = Solution()
# print(solution.wordPattern("abba", "dog cat cat dog"))
# print(solution.wordPattern("abba", "dog cat cat fish"))
# print(solution.wordPattern("aaaa", "dog cat cat dog"))
print(solution.wordPattern("e", "eureka"))