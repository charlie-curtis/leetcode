class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        
        v1=v1.split(".")
        v2=v2.split(".")
        n=max(len(v1),len(v2))
        
        if len(v1) < n:
            v1+=["0"]*(n-len(v1))
            
        if len(v2) < n:
            v2+=["0"]*(n-len(v2))
        
        for i in range(n):
            x,y= int(v1[i]), int(v2[i])
            if x > y:
                return 1
            if y > x:
                return -1
        return 0