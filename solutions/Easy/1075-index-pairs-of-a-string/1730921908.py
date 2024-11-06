class Solution:
    def indexPairs(self, s: str, words: List[str]) -> List[List[int]]:

        words = set(words)

        n = len(s)
        ans = []
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] in words:
                    ans.append([i,j])
        return ans

        