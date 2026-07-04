class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:

        a = n*(n+1)//2
        if a < abs(target) or (a-target) % 2 == 1:
            return []
        
        out = [i for i in range(1,n+1)]

        need = (a - target)
        for i in range(len(out)-1, -1, -1):
            if not need:
                break
            if 2*out[i] > need:
                continue
            need-=2*out[i]
            out[i]*=-1

            
        out.sort()
        return out