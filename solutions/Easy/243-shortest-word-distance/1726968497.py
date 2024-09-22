class Solution:
    def shortestDistance(self, words: List[str], a: str, b: str) -> int:

        def compute(words):
            aSeen = None
            ans = 1e10
            for i,x in enumerate(words):
                if x == a:
                    aSeen = i
                elif (x == b) and aSeen != None:
                    ans = min(ans, i-aSeen)
            return ans

        options = [compute(words), compute(words[::-1])]
        return min(options)


        