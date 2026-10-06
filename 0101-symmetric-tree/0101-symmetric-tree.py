# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        stack=deque()
        stack.append((root.left,root.right))
        while stack:
            lnode,rnode = stack.popleft()
            if not lnode and not rnode:
                continue
            if not lnode or not rnode or lnode.val !=  rnode.val:
                return False
            stack.append((lnode.left,rnode.right))
            stack.append((lnode.right,rnode.left))
        return True