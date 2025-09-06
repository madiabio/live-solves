from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxMap = dict()
        for i, node in enumerate(inorder):
            idxMap[node] = i

        preorder = deque(preorder)

        def helper(start, end):
            if start > end:
                return None
            
            root = preorder.popleft()
            rootIdx = idxMap[root]
            root = TreeNode(root)

            root.left = helper(start, rootIdx - 1)
            root.right = helper(rootIdx+1, end)
        
            return root
        
        return helper(0, len(preorder) - 1)
