class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        odds = Counter()
        evens = Counter()

        #handle the case where there aren't more than 1 unique value
        odds[-1] = 0
        evens[-2] = 0

        n = len(nums)
        for i,x in enumerate(nums):
            if i % 2 == 1:
                odds[x]+=1
            else:
                evens[x]+=1
        A = sorted([[v,k] for (k,v) in odds.items()])
        B = sorted([[v,k] for (k,v) in evens.items()])

        A = A[-2:]
        B = B[-2:]

        if A[-1][1] == B[-1][1]:
            #need to mix-and-match
            a = A[-1][0] + B[-2][0]
            b = A[-2][0] + B[-1][0]
            return n - max(a,b)
        else:
            return n - (A[-1][0] + B[-1][0])

        