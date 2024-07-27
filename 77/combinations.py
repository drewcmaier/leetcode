class Solution(object):
    def combinations(self, subset, result, n, k, i):
        if len(subset) == k:
            result.append(subset[:])
            return

        for num in range(i, n+1):
            subset.append(num);
            self.combinations(subset, result, n, k, num+1)
            subset.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        subset = []
        i = 1
        self.combinations(subset, result, n, k, i)

        return result
        

print(Solution().combine(4, 2))