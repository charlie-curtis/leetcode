class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        
        t = Counter()
        for x in words2:
            t|= Counter([s for s in x])
            
        for x in words1:
            C = Counter([s for s in x])
            if C >= t: ans.append(x)
        return ans
        