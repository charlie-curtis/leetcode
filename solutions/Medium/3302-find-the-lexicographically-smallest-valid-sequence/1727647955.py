class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:


        dp = [0]*len(word1)


        dp[-1] = 0 if word1[-1] != word2[-1] else 1
        for i in range(len(word1)-2, -1, -1):
            dp[i] = dp[i+1]
            if dp[i] == len(word2):
                continue
            idx = len(word2)-1 - dp[i+1]
            if word1[i] == word2[idx]:
                dp[i]+=1
        

        out = []
        j = 0
        has_life = True
        for i in range(len(word1)):
            if j == len(word2):
                break
            
            if word1[i] == word2[j]:
                j+=1
                out.append(i)
                continue

            rem = len(word2) - j
            available = 0 if i + 1 == len(word1) else dp[i+1]

            if rem - 1 <= available and has_life:
                j+=1
                has_life = False
                out.append(i)

        if len(out) == len(word2):
            return out
        return []



