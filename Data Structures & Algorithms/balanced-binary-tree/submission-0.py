# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #abs(left - right) <= 1

        def dfs(root):
            if not root:
                return (True, 0)
            left = dfs(root.left)
            right = dfs(root.right)


            if left[0] == False or right[0] == False:
                return (False, 1 + max(right[1], left[1]))

            if abs(left[1] - right[1]) > 1:
                return (False, 1 + max(right[1], left[1]))

            return (True, 1 + max(right[1], left[1]))

        return dfs(root)[0]
        