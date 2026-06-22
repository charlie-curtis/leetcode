class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:


        C = Counter()
        ans=None
        for li in responses:
            C1 = Counter()
            for x in li:
                if C1[x]:continue
                C1[x] = 1
                C[x]+=1
                
                if ans==None or C[x]>ans[0] or (C[x]==ans[0] and x < ans[1]):
                    ans=[C[x],x]
        
        return ans[1]
        