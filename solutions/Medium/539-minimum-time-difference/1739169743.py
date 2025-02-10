class Solution:
    def findMinDifference(self, t: List[str]) -> int:
        
        def toi(s):
            return int(s[:2])*60 + int(s[3:])
        
        A=[toi(x)  for x in t]
        A.sort()
        A.append(A[0] +24*60)
        return min(b-a  for (a,b) in zip(A,A[1:]))