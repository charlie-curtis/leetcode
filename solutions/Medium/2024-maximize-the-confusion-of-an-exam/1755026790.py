class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        #there is also a binary search solution
        j = ans = 0
        C = Counter()
        C['T'] = C['F'] = 0
        for i in range(n):
            C[answerKey[i]]+=1
            while min(C.values()) > k:
                C[answerKey[j]]-=1
                j+=1
            ans = max(ans, i-j+1)
        return ans