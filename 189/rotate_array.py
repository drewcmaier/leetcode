from typing import List

class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        for i in range(0, int((end-start)/2)):
            nums[start+i], nums[end-i-1] = nums[end-i-1], nums[start+i]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        if l == 0 or k == 0:
            return
        
        k_clamped = (k % l)

        # algorithm: reverse, then reverse sub-lists from 0 to k-1 then k to end
        self.reverse(nums, 0, l)
        self.reverse(nums, 0, k_clamped)
        self.reverse(nums, k_clamped, l)

        print(nums)
        
        
solution = Solution()
inputs = [
    ([1,2,3,4,5,6,7], 3),
    ([-1,-100,3,99], 2),
    ([1,2], 1),
    ([1,2,3], 2),
]
for input in inputs:
    solution.rotate(input[0], input[1])