# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val 
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue=[root]
        level=0
        while queue:
            n=len(queue)
            for i in range(n):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)                
                queue=queue[1:]
            if level%2==0:
                i=0
                j=len(queue)-1
                while i<=j:
                    queue[i].val,queue[j].val=queue[j].val,queue[i].val
                    i+=1
                    j-=1
            level+=1
        return root
                
        