from binary_tree import readTree

class Solution(object):
    def traverse (self, root, out, depth):
        if root == None:
            return out

        # new depth; set this as the depth's value
        if len(out) <= depth:
            out.append(root.val)

        depth += 1

        # traverse right, then left
        if root.right:
            self.traverse(root.right, out, depth)

        if root.left:
            self.traverse(root.left, out, depth)

        return out

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        self.traverse(root, out, 0)
        return out
        
solution = Solution()
print(solution.rightSideView(readTree([1,2,3,None,5,None,4])))
print(solution.rightSideView(readTree([1,None,3])))
print(solution.rightSideView(readTree([])))
