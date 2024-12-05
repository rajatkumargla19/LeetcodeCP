class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n=len(start)
        m=len(target)
        i=0
        j=0
        # checking the respective positions of L and R in each string 
        while i<n or j<m:
            while i<n and start[i]=="_":
                i+=1
            while j<m and target[j]=="_":
                j+=1
            if i<n and j<m and start[i]!=target[j]:
                # print(start[i],target[j])
                print("loop1 false ")
                return False
            i+=1
            j+=1
        # checking whether each L in string start is coming after each L in the string target or not ?
        i=0
        j=0
        L1count=0
        L2count=0
        while i<n or j<m:
            while i<n and start[i]!="L":
                i+=1
            if i<n:
                L1count+=1
            while j<m and target[j]!="L": 
                j+=1
            if j<m:
                L2count+=1
            if i<n and j<m and i<j :
                print(i,j)
                print("loop2 false")
                return False
            i+=1
            j+=1
        if L1count!=L2count:
            print('count checking loop2')
            return False
        # for checking whether each R in string start is coming before each R in string target in both the strings 
        i=0
        j=0
        R1count=0
        R2count=0
        while i<n or j<m:
            while i<n and start[i]!="R":
                i+=1
            if i<n:
                R1count+=1
            while j<m and target[j]!="R":
                j+=1
            if j<m:
                R2count+=1
            if i<n and j<m and i>j:
                print("loop3 false")
                return False
            i+=1
            j+=1
        if R1count!=R2count:
            print(R1count,R2count)
            print("count checking loop 3")
            return False
            
        return True




        