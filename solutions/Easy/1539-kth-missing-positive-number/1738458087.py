class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        sset = set(arr)
        for i in range(1, 100000):
            if i not in sset:
                k-=1
            if k == 0:
                return i
        