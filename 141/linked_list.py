# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Parse leetcode's format
def readList(nodes):
    if len(nodes) == 0:
        return None

    root = ListNode(nodes.pop(0))
    prev = root
    while len(nodes) > 0:
        node = ListNode(nodes.pop(0))
        prev.next = node
        prev = node
    
    return root

def getTail(head):
    while head.next != None:
        head = head.next
    return head