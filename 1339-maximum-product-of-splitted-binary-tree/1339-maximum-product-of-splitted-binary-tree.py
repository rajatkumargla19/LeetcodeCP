# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        res=0
        total_sum=0
        def total(root):
            nonlocal total_sum
            if not(root):
                return 
            total_sum+=root.val
            total(root.left)
            total(root.right)
            return 
        total(root)
        def dfs(root):
            nonlocal res
            nonlocal total_sum
            if not(root):
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            current_sum=((root.val+left+right)*(total_sum-(root.val+left+right)))
            res=max(res,current_sum)
            # res=res%(10**9+7)
            
            
            return root.val+left+right
        dfs(root)
        return res%(10**9+7)
        