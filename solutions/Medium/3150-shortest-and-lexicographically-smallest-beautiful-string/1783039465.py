class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:


        j = 0
        n = len(s)

        cnt = 0
        can = ''
        for i in range(n):
            cnt+=1 if s[i] == '1' else 0
            while cnt == k:
                if (can == '') or ((i-j+1) < len(can)) or ((i-j+1) == len(can) and can > s[j:i+1]):
                    can = s[j:i+1]
                cnt-=1 if s[j] == '1' else 0
                j+=1
        
        return can if can else ''
        


        