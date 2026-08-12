# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapping={a:i for i,a in enumerate(inorder)}
        def build(i,j):
            if i>j:
                return
            a=postorder.pop()
            mid=mapping[a]
            root=TreeNode(a)
            root.right=build(mid+1,j)
            root.left=build(i,mid-1)
            return root
        return build(0,len(postorder)-1)