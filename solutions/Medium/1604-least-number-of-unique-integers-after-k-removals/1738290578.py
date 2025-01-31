class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        C = Counter(arr)
        A = [v for k,v in C.items()]
        A.sort()
        n = len(A)
        for i,x in enumerate(A):
            if x > k:
                return n-i
            k-=x
        return 0