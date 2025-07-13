class Solution:
    def matchPlayersAndTrainers(self, A: List[int], B: List[int]) -> int:


        A.sort()
        B.sort()

        j=0
        n=len(B)
        ans=0

        for x in A:
            while j<n and B[j] < x:
                j+=1
            if j < n:
                ans+=1
                j+=1
            else:
                break
        return ans