class Solution:
    def frequencySort(self, s: str) -> str:

        C = Counter(s)
        A = [[-v,k] for (k,v) in C.items()]
        A.sort()
        return ''.join([x[1]*-x[0] for x in A])
        