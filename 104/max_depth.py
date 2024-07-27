from binary_tree import readTree

class Solution(object):
    def findMaxDepth(self, root, depth):
        if root == None:
            return depth
        
        depth += 1

        if root.left == None and root.right == None:
            return depth

        left = right = 0
        if root.left:
            left = self.findMaxDepth(root.left, depth)
        if root.right:
            right = self.findMaxDepth(root.right, depth)

        return max(left, right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findMaxDepth(root, 0)
        
solution = Solution()

print(solution.maxDepth(
    readTree([3,9,20,None,None,15,7])
))
print(solution.maxDepth(
    readTree([])
))
print(solution.maxDepth(
    readTree([1,None,2])
))
print(solution.maxDepth(
    readTree([1,2,None,3,None,4,5])
))