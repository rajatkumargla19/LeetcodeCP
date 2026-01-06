# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum=root.val
        que=[root]
        level=1
        res=1
        curr_sum=0
        while que:
            n=len(que)
            while n:
                if que[0].left:
                    que.append(que[0].left)
                if que[0].right:
                    que.append(que[0].right)
                curr_sum+=que[0].val
                que=que[1:]
                n-=1
            print(curr_sum,maxSum)
            if curr_sum>maxSum:
                maxSum=curr_sum
                res=level
            level+=1
            curr_sum=0
        return res


        