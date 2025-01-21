class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        C = Counter(arr)
        n = len(arr)
        ssum = 0
        ans = 0
        for v in sorted(C.values(), reverse=True):
            ssum+=v
            ans+=1
            if ssum >= n//2:
                return ans
        