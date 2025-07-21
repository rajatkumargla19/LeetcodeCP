class Solution:
    def makeFancyString(self, s: str) -> str:
        stack=[]
        n=len(s)
        i=0
        while i<n:
            if not stack:
                stack.append(s[i])
            else:
                if i+1<n and stack[-1]==s[i] and stack[-1]==s[i+1]:
                    pass
                else:
                    stack.append(s[i])
            i+=1
        print(stack)
        return "".join(stack)

