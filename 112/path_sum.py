from binary_tree import readTree

class Solution(object):
    def dfs(self, root, sum, targetSum):
        if root == None:
            return False
        
        sum += root.val

        if root.left == None and root.right == None:
            return sum == targetSum

        if root.left != None and self.dfs(root.left, sum, targetSum):
            return True
        
        if root.right != None and self.dfs(root.right, sum, targetSum):
            return True

        return False

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.dfs(root, 0, targetSum)
        
solution = Solution()
print(
    solution.hasPathSum(
        readTree([5,4,8,11,None,13,4,7,2,None,None,None,1]),
        18
    )
)
# print(
#     solution.hasPathSum(
#         readTree([1,2,3]),
#         5
#     )
# )
# print(
#     solution.hasPathSum(
#         readTree([]),
#         0
#     )
# )