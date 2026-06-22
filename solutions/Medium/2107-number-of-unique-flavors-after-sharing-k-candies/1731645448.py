class Solution:
    def shareCandies(self, can: List[int], k: int) -> int:

        n = len(can)

        C = Counter(can)
        ans = 0
        j = 0
        for i in range(n):

            C[can[i]]-=1
            if C[can[i]] == 0:
                del C[can[i]]

            if i-j+1 > k:
                C[can[j]]+=1
                j+=1

            if i-j+1 == k:
                ans = max(ans, len(C.keys()))
        return ans
            


        