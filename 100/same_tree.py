from typing import Optional
from binary_tree import TreeNode, readTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        if p != None and q != None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False

solution = Solution()
inputs = [
    (readTree([1,2,3]), readTree([1,2,3])),
    (readTree([1,2]), readTree([1,None,2])),
    (readTree([1,2,1]), readTree([1,1,2])),
    (readTree([]), readTree([0])),
    (readTree([1,None,2,4,None,None,3]), readTree([1,None,4,2,None,None,3])),
]
for input in inputs:
    print(solution.isSameTree(input[0], input[1]))