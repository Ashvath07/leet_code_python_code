# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        value = 0
        stack =[]
        stack.append((root,False))
        while stack:
            node,is_left = stack.pop()
            if not node.left and not node.right:
                if is_left:
                    value = value+node.val
            else:
                if node.left:
                    stack.append((node.left,True))
                if node.right:
                    stack.append((node.right,False))
        return value