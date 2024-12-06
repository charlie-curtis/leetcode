class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        banned = set(banned)
        score = 0
        ans = 0
        for i in range(1,n+1):
            if i not in banned and score+i <= maxSum:
                score+=i
                ans+=1

        return ans