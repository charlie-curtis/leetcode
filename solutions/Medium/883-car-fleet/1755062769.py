class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        C=Counter()
        A=list(zip(position,speed))
        A.sort(reverse=True)
        t=0
        for p,s in A:
            t1=(target-p)/s
            t=max(t,t1)
            C[t]+=1
        return len(C.keys())
        