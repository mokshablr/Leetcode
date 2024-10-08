# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        out = postOrderTraversal(root)
        return out

def postOrderTraversal(root):
    if root == None:
        return root
    left = postOrderTraversal(root.left)
    right = postOrderTraversal(root.right)
    root.left = right
    root.right = left
    return root
