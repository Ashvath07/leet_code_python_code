# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        first = deque()
        first.append((root,1))
        while first :
            node,depth = first.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                first.append((node.left,depth+1))
            if node.right:
                first.append((node.right,depth+1))
        return 0