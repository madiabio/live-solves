# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val == p) and (self.isDescendent(root, q)):
            return p
        elif (root.val == q) and (self.isDescendent(root, p)):
            return q
        elif root.left and ( self.isDescendent(root.left, p) and self.isDescendent(root.left, q) ):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.right and ( self.isDescendent(root.right, p) and self.isDescendent(root.right, q) ):
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
    def isDescendent(self, A, B):
        if not A:
            return False
        elif (A and B) and (A.val == B.val):
            return True
        else:
            return self.isDescendent(A.left, B) or self.isDescendent(A.right, B)

