# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #fuck
        #same logic as previous problem lol
        #we just use the "is same binary tree" logic when we run into a node that equals the root of the subroot
        #if the outcome is true, keep!
        #else, return false
        #or the left and right results

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p and q:
                if p.val != q.val:
                    return False
                if isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
                    return True

            elif not p and not q:
                return True

            return False

        def isSubtree2(root, subRoot):
            if not subRoot:
                return True
            if not root:
                return False

            res = False
            
            if root.val == subRoot.val:
                res = isSameTree(root, subRoot)
            return res or isSubtree2(root.left, subRoot) or isSubtree2(root.right, subRoot)
            

        return isSubtree2(root, subRoot)

        