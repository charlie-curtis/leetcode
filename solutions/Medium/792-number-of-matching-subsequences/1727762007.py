class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:


        @cache
        def is_good(w1, w2):
            j = 0
            for i in range(len(w1)):
                if j == len(w2):
                    break
                if w1[i] == w2[j]:
                    j+=1

            return j == len(w2)

        return len([x for x in words if is_good(s, x)])

            

        