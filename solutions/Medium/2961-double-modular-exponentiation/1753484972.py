class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        
        
        def powmod(x, y, mod):
            if y == 0:
                return 1
            if y % 2 == 1:
                return (x%mod)*powmod(x,y-1, mod) % mod
            
            return ((powmod(x, y//2, mod) % mod)**2) % mod
            
            
            
        def wrapper(li):
            ai, bi, ci, mi = li
            first = powmod(ai,bi, 10)
            ans = powmod(first,ci, mi)
            return ans
            
            
        return [i for i in range(len(variables)) if wrapper(variables[i]) == target]
            
        
        