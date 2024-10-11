class Solution:
    def isStrobogrammatic(self, s: str) -> bool:
        
        l, r = 0, len(s)-1
        a,b = ['9', '6', '0', '8', '1'],  ['6', '9', '0', '8', '1']
        ma = dict(zip(a,b))

        while l <= r:
            a, b = s[l], s[r]
            if a not in ma or ma[a] != b:
                return False
            l+=1
            r-=1
        return True