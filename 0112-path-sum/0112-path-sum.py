# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False 
        stack =[]
        stack.append((root,targetSum-root.val))
        while stack:
            node,curr = stack.pop()
            if not node.left and not node.right and curr == 0:
                return True
            if node.right:
                stack.append((node.right,curr-node.right.val))
            if node.left:
                stack.append((node.left,curr-node.left.val))
        return False