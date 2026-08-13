# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev=None
        self.valid=True
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        if self.prev is None:
            self.prev=root
        elif root.val <= self.prev.val:
            self.valid=False
        else:
            self.prev=root
        self.inorder(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev=None
        self.valid=True
        self.inorder(root)
        return self.valid