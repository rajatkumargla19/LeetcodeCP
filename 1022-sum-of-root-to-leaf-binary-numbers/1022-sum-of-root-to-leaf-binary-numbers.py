# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root,p,res):
            if not(root.left) and not(root.right):
                p+=str(root.val)
                res.append(p)
                return 
            if root.left:
                dfs(root.left,p+str(root.val),res)
            if root.right:
                dfs(root.right,p+str(root.val),res)
            return res
             
        
        arr= dfs(root,'',[])
        # print(res)
        res=0
        if not(arr):return root.val
        for i in range(len(arr)):
            res+=int(arr[i],2)
        return res

        # # print(res)
        return 1

        
        