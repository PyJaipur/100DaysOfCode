# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

final_root = None


def drop(node):
    if node.parent is None:
        global final_root
        final_root = None
        return
    if node.parent.left == node:
        node.parent.left = None
    if node.parent.right == node:
        node.parent.right = None


def is_insufficient(node, limit):
    if node is None:
        return True
    if node.left is None and node.right is None:
        if node.sum_from_root < limit:
            drop(node)
            return True
    else:
        if node.left is not None:
            node.left.parent = node
            node.left.sum_from_root = node.left.val + node.sum_from_root
        if node.right is not None:
            node.right.parent = node
            node.right.sum_from_root = node.right.val + node.sum_from_root
        l = is_insufficient(node.left, limit)
        r = is_insufficient(node.right, limit)
        if l and r:
            drop(node)
            return True
    return False


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        global final_root
        root.sum_from_root = root.val
        root.parent = None
        final_root = root
        is_insufficient(root, limit)
        return final_root
