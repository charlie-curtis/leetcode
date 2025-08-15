class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)
        for x in strs:
            h = tuple(sorted([s for s in x]))
            ans[h].append(x)
        return list(ans.values())
        