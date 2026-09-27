# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxcount = 0
        stack = []
        if root:
            stack.append([root,1])
        while stack:
            node = stack.pop()
            if node[0]:
                if node[1] > maxcount:
                    maxcount = node[1]
                if node[0].left:
                    stack.append([node[0].left, node[1]+1])
                if node[0].right:
                    stack.append([node[0].right, node[1]+1])

        return maxcount
 