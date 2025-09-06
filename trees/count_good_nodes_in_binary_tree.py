# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque()
        q.append((root, root.val))
        while q:
            node, maxVal = q.popleft()
            maxVal = max(node.val, maxVal)
            if maxVal <= node.val: count += 1
            if node.left: q.append([node.left, maxVal])
            if node.right: q.append([node.right, maxVal])
        return count
