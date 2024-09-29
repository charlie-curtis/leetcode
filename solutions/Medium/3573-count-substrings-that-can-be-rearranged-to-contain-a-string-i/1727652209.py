class Solution:
    def validSubstringCount(self, s: str, word2: str) -> int:


        C = Counter()
        answer_key = Counter(word2)


        n = len(s)

        ans = 0
        j = 0
        for i in range(n):

            C[s[i]]+=1

            if C < answer_key:
                continue

            while C >= answer_key:
                ans+=len(s)-i
                C[s[j]]-=1
                if C[s[j]] == 0:
                    del C[s[j]]
                j+=1
        return ans

        