# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        def dfs(node1, node2):
            if not ((node1 == None and node2 == None) or ((node1 and node2) and node1.val == node2.val)):
                self.same = False
            if node1 and node2:
                dfs(node1.left, node2.left)
                dfs(node1.right, node2.right)
        dfs(p, q)
        return self.same
