class Solution:
    def numTeams(self, rating: List[int]) -> int:


        def score(rating):
            ans = 0 
            n = len(rating)
            for i in range(n):
                smaller = 0
                larger = 0
                for j in range(i-1, -1, -1):
                    if rating[i] > rating[j]:
                        smaller+=1
                for j in range(i+1, n):
                    if rating[i] < rating[j]:
                        larger+=1
    
                ans+=(smaller*larger)
            return ans

        return score(rating) + score(rating[::-1])
                
        