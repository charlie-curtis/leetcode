class Solution:
    def numberOfWeeks(self, miles: List[int]) -> int:

        n = len(miles)
        if n == 1:
            return 1
        
        T = sum(miles)
        zmax = max(miles)
        lower = T - zmax
        if lower + 1 >= zmax:
            return lower + zmax
        
        return lower*2 + 1 
        