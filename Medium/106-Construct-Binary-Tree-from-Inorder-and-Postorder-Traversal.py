import json
from typing import final

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_root(inorder_inp, postorder_list, lbound, rbound):
    if lbound != rbound:
        subtree = inorder_inp[lbound:rbound]
    else:
        subtree = [inorder_inp[lbound],]

    print("SUB", subtree)
    for i in postorder_list[::-1]:
        if i in subtree:
            index = 0
            for j in inorder_inp:
                if j == i:
                    return (i, index)
                index += 1

def get_left_tree(root, inorder_inp, lbound, rbound):
    index = lbound-1
    for i in range(lbound, rbound):
        index += 1
        if inorder_inp[i] == root:
            print("LEFT TREE IN", inorder_inp[lbound:index])
            return (inorder_inp[lbound:index], index) 

def get_right_tree(root, inorder_inp, lbound, rbound):
    index = lbound-1
    for i in range(lbound, rbound):
        index += 1
        if inorder_inp[i] == root:
            print("RIGHT TREE IN", inorder_inp[index:rbound])
            return (inorder_inp[index+1:rbound], index) 

def build_tree(inorder_inp, postorder_inp, lbound, rbound):
    root_val, root_index = get_root(inorder_inp, postorder_inp, lbound, rbound)
    root = TreeNode(root_val)
    print("ROOT:", root.val, root_index)
    # left_subtree, lbound_new = get_left_tree(root, inorder_inp, lbound, rbound)
    # left_subtree, root_index = get_left_tree(root.val, inorder_inp, lbound, rbound)
    left_subtree = inorder_inp[lbound:root_index]
    print("LEFT TREE LIST:", left_subtree, root_index)
    # right_subtree, rbound_new = get_right_tree(root, inorder_inp, l_rbound_new, rbound)
    # right_subtree = inorder_inp[root_index+1:rbound]
    right_subtree = inorder_inp[root_index+1:rbound]

    print("RIGHT TREE LIST:", right_subtree)
    
    if left_subtree == []:
        left_root = TreeNode(None)
        print("LEFT NONED")
    else:
        left_root = build_tree(inorder_inp, postorder_inp, lbound, root_index-1)
        print("LEFT TREE", left_root.val)

    if right_subtree == []:
        right_root = TreeNode(None)
        print("RIGHT NONED")
    else:
        right_root = build_tree(inorder_inp, postorder_inp, root_index+1, rbound)
        print("RIGHT TREE", right_root.val)

    # tree = TreeNode(root, left_root, right_root)
    root.left = left_root
    root.right = right_root
    
    return root

def levelOrderRec(root, level, res):
    if not root:
        return

    # Add a new level to the result if needed
    if len(res) <= level:
        res.append([])

    # Add current node's data to its corresponding level
    res[level].append(root.val)

    # Recur for left and right children
    levelOrderRec(root.left, level + 1, res)
    levelOrderRec(root.right, level + 1, res)

# Function to perform level order traversal
def levelOrder(root):
    res = []
    levelOrderRec(root, 0, res)
    l = len(res)
    for i in res[::-1]:
        print("AIAIAI",i)
        if i != None:
            break
        l -= 1
    return res[:-1]

with open("testcase.txt", "r") as file:
    testcases = [line.strip() for line in file]

inorder_inp = json.loads(testcases[0])
postorder_inp = json.loads(testcases[1])

final_tree = build_tree(inorder_inp, postorder_inp, 0, len(inorder_inp))

print("TREE BUILT")


res = levelOrder(final_tree)

output_list = []
# Print the result
for level in res:
    for data in level:
        print(data, end=" ")
        if data == None:
            data = "null"
        output_list.append(data)

print(output_list)