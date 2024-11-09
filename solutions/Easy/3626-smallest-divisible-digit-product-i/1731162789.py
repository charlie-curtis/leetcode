class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        

        while True:
            multi = 1 
            original = n
            while original > 0:
                multi*= original % 10
                original//=10
            
            if multi % t == 0:
                return n
            n+=1
                
                
        