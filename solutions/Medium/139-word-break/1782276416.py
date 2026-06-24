class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        d = set(wordDict)
        n = len(s)

        @cache
        def f(i):
            if i >= n:
                return True

            for j in range(i,n):
                if s[i:j+1] in d and f(j+1):
                    return True
            return False


        return f(0)

            
        