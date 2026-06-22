class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        S = 'aeiou'
        A = [1 if x[0] in S and x[-1] in S else 0 for x in words]
        pref = list(accumulate(A, initial=0))

        ans = [] 
        for l,r in queries:
            ans.append(pref[r+1] - pref[l])
        return ans
        