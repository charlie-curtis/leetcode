class Solution:
    def findLucky(self, arr: List[int]) -> int:

        C = Counter(arr)
        for k in sorted(C.keys(), reverse=True):
            if C[k] == k:
                return k
        return -1
        