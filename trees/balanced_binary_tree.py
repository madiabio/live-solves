# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def dfs(node):
            if not node or (not node.left and not node.right):
                return 0
            l = dfs(node.left) + 1 if node.left else 0
            r = dfs(node.right) + 1 if node.right else 0
            if abs(l-r) > 1:
                self.isBalanced = False
            return max(l,r)
        dfs(root)
        return self.isBalanced
