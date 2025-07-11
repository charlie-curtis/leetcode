class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        C=Counter(words)

        A=[[-v,k] for k,v in C.items()]
        A.sort()

        return [a[1] for a in A][:k]