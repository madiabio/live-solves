# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mps = -float('inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.getMPS(root)
        return self.mps
    
    def getMPS(self, root):
        if not root:
            return -float('inf')    

        leftPS = self.getMPS(root.left)
        rightPS = self.getMPS(root.right)
        self.mps = max(
            self.mps,
            root.val,
            root.val + leftPS,
            root.val + rightPS,
            leftPS + root.val + rightPS,
            leftPS,
            rightPS
            )

        return max( root.val, leftPS + root.val, rightPS + root.val )        
