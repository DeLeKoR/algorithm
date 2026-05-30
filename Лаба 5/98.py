class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        def check(node, left_limit, right_limit):
            if node is None:
                return True

            if node.val <= left_limit or node.val >= right_limit:
                return False

            return check(node.left, left_limit, node.val) and check(node.right, node.val, right_limit)

        return check(root, float("-inf"), float("inf"))