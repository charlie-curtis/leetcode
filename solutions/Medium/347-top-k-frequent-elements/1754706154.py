class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        A = [[-v,k] for (k,v) in Counter(nums).items()]
        A.sort()

        return [a[1] for a in A[:k]]
        