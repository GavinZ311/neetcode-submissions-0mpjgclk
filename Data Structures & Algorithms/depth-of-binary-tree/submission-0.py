# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        lists = []
        def search(root, count):
            if not root:
                lists.append(count)
                count = 0
                return None
            else:
                count+=1
            search(root.left, count)
            search(root.right, count)
        
        search(root, count)
        return max(lists)
