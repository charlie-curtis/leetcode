class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def check(x,y):
            
            m,n=len(x),len(y)
            if m-n != 1: return False
            f=0
            for i in range(n):
                if y[i] != x[i+f]:
                    if f==1:return False
                    f+=1
                    if y[i] != x[i+f]: return False
            return True
        n=len(words)
        words.sort(key=lambda x: len(x))
        dp=[1]*n
        for i in range(n):
            for j in range(i-1,-1,-1):
                if check(words[i],words[j]):
                    dp[i] = max(dp[i], 1+ dp[j])
        print(dp)
        return max(dp)
                    
                
        