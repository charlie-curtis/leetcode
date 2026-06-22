class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:

        m = len(arrays)
        C = Counter()
        ans = []
        for i in range(m):
            A = arrays[i]
            for x in A:
                C[x]+=1
                if C[x] == m:
                    ans.append(x)
        return ans

        