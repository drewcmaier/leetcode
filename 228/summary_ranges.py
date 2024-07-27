class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        head = 0
        tail = 0
        result = []
        l = len(nums)

        for i in range(1, l+1):
            if i == l or nums[i] - nums[i-1] != 1:
                run = tail - head
                str = "{}".format(nums[head]) if run < 1 else "{}->{}".format(nums[head], nums[tail])
                result.append(str);
                head = tail = i
            else:
                tail = i
        
        return result

solution = Solution()
print(solution.summaryRanges([0,1,2,4,5,7]))
print(solution.summaryRanges([0,2,3,4,6,8,9]))