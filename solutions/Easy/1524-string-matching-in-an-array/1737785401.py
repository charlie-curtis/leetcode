class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = set()
        for i,x in enumerate(words):
            for j,y in enumerate(words):
                if j == i:
                    continue
                if x in y:
                    ans.add(x)
        return list(ans)