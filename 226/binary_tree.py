# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Parse leetcode's format
def readTree(nodes):
    if len(nodes) == 0:
        return None

    root = TreeNode(nodes.pop(0))
    q = [root]
    while len(q) > 0 and len(nodes) > 0:
        cur = q.pop(0)
        if cur == None:
            continue

        left = nodes.pop(0) if len(nodes) > 0 else None
        if left != None:
            cur.left = TreeNode(left)
            q.append(cur.left)

        right = nodes.pop(0) if len(nodes) > 0 else None
        if right != None:
            cur.right = TreeNode(right)
            q.append(cur.right)
    
    return root

def toArray(tree):
    if tree == None:
        return []

    out = []
    q = [tree]
    while len(q) > 0:
        cur = q.pop(0)
        
        if cur == None:
            continue

        out.append(cur.val)

        q.append(cur.left)
        q.append(cur.right)
    
    return out