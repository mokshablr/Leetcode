# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def get_root(postorder_list):
    # The root is always the last element in the postorder list
    return postorder_list.pop()

def build_tree(inorder_inp, postorder_inp, lbound, rbound):
    if lbound > rbound:
        return None

    # Get the root value and find its index in the inorder list
    root_val = get_root(postorder_inp)
    root = TreeNode(root_val)
    root_index = inorder_inp.index(root_val)

    # Recursively build the right subtree first (important due to postorder traversal)
    root.right = build_tree(inorder_inp, postorder_inp, root_index + 1, rbound)

    # Recursively build the left subtree
    root.left = build_tree(inorder_inp, postorder_inp, lbound, root_index - 1)

    return root

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Make a copy of postorder so it can be used destructively
        postorder_copy = postorder[:]
        return build_tree(inorder, postorder_copy, 0, len(inorder) - 1)

