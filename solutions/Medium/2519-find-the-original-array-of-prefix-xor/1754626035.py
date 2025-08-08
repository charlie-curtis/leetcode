class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        n = len(pref)

        out = []
        #3,6,3,2,9
        #3^6^3^2
        #3^6^3
        for i in range(n):
            before = pref[i-1] if i-1 >=0 else 0
            me = pref[i]
            out.append(me^before)
        return out
            
