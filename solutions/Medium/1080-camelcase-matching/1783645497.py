class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:


        n = len(pattern)
        def check(s):
            j = 0
            for i in range(len(s)):
                if j < n and pattern[j] == s[i]:
                    j+=1
                elif j < n and s[i].isupper():
                    return False
                if j == n:
                    for k in range(i+1, len(s)):
                        if s[k].isupper():
                            return False
                    return True
            return False

        out = []
        for s in queries:
            out.append(check(s))
        return out

        