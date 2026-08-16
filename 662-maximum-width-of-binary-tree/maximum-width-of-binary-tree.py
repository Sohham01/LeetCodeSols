# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        q=deque([(root,0)])
        width=0
        while q:
            size=len(q)
            first=q[0][1]
            last=q[-1][1]
            width=max(width,last-first+1)
            for i in range(size):
                node, pos= q.popleft()
                if node.left:
                    q.append((node.left, 2*pos+1))
                if node.right:
                    q.append((node.right, 2*pos+2))
        return width