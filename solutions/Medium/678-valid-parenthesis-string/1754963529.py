class Solution:
    def checkValidString(self, s: str) -> bool:


        #there is an O(N) stack way of doing this
        n = len(s)
        @cache
        def dp(i,b):
            if b < 0:
                return False
            if i == n:
                return b == 0
            
            if s[i] == '(':
                return dp(i+1, b+1)
            elif s[i] == ')':
                return dp(i+1, b-1)
            else:
                return any([
                   dp(i+1, b-1),
                   dp(i+1, b+1),
                   dp(i+1, b) 
                ])
        

        return dp(0,0)
            
        