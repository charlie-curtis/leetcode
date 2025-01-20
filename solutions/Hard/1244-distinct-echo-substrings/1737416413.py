class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        ans = set()
        n = len(text)
        for L in range(2,n+1,2):
            for i in range(n):
                if i + L > n:
                    break
                a = text[i:i+L//2]
                b = text[i+L//2:i+L]
                if a == b:
                    #ans.add(a)
                    ans.add(hash(a))
        print(ans)
        return len(ans)
                
            
        