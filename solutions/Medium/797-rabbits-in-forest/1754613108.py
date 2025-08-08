class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        C=Counter(answers)

        ans=0
        for k,v in C.items():
            mx=k+1
            ans+=((v+mx-1)//mx)*mx
        return ans