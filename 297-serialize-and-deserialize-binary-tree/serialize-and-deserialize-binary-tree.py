# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res=[]
        def preorder(node):
            if not node:
                res.append("null")
            else:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        if data=="null":
            return None
        nodes=data.split(",")
        self.i=0
        def construct():
            n=nodes[self.i]
            self.i+=1
            if n=="null":
                return None
            node=TreeNode(int(n))
            node.left=construct()
            node.right=construct()
            return node
        return construct()