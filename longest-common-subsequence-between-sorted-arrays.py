#https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/description/
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:

        C = Counter()
        for x in arrays:
            seen = set()
            for j in x:
                if j in seen:
                    continue
                seen.add(j)
                C[j]+=1
        
        t = len(arrays)
        ans = []
        for x in arrays[0]:
            if C[x] == t:
                ans.append(x)
        return ans
