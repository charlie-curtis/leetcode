class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:


        pref = list(accumulate(cards, initial=0))
        mmin = 1e15
        n = len(cards)
        k = n-k
        for i in range(k-1,n):
            mmin = min(mmin, pref[i+1]-pref[i-k+1])
        return sum(cards) - mmin
            