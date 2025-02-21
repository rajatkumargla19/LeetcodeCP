# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        freq={}
        def dfs(root,parent,flag):
            nonlocal freq
            if not(root):
                return 
            if parent==-1:
                root.val=0
                parent=root.val
                freq[parent]=True
            else:
                if flag==1:
                    root.val=2*parent+1
                    parent=root.val
                    freq[parent]=True

                elif flag==2:
                    root.val=2*parent+2
                    parent=root.val
                    freq[parent]=True
            dfs(root.left,parent,1)
            dfs(root.right,parent,2)
            return root
        dfs(root,-1,0)
        # print(root)
        self.freq=freq
        

    def find(self, target: int) -> bool:
        # print(self.freq)
        if target in self.freq:
            return True
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)