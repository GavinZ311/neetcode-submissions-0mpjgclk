# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if not node:
                return 0
            leftH = getHeight(node.left)
            if leftH == -1:
                return -1
            rightH = getHeight(node.right)
            if rightH == -1:
                return -1
            if abs(leftH-rightH)>1:
                return -1
            return max(leftH, rightH)+1
        return getHeight(root) != -1

