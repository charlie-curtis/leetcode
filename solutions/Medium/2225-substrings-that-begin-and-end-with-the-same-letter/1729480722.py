class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        return sum([x*(x+1)//2 for x in Counter(s).values()])
        