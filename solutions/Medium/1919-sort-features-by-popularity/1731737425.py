class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:

        C = Counter()
        for li in responses:
            sset = set(li.split())
            for x in sset:
                C[x]+=1

        li = []
        for i,x in enumerate(features):
            li.append([-C[x], i])

        return [features[x[1]] for x in sorted(li)]


        