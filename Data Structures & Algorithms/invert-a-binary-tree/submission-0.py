# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #intuition: go from the root, swap the left and right
        #move on to the next node for each
        #can do this with a BFS?

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node:
                left = node.left
                right = node.right
                node.left = right
                node.right = left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
        