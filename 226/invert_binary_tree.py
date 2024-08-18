from typing import Optional
from binary_tree import *

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or (root.left is None and root.right is None):
            return root
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

solution = Solution()
print(toArray(
    solution.invertTree(
        readTree([4,2,7,1,3,6,9])
    )
))
print(toArray(
    solution.invertTree(
        readTree([2,3,1])
    )
))
print(toArray(
    solution.invertTree(
        readTree([])
    )
))