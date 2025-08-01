class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:


        #p * r = q * s
        #p < q < r < s

        #p/q = r/s

        n = len(nums)
        C = Counter()

        ans = 0
        holding = []
        for i in range(n):
            for j in range(i+2,n): #compute s/r where i is acting as the 'r' and j = 's'
                r = nums[i]
                s = nums[j]
                gval = gcd(r,s)
                ans+=C[(s//gval,r//gval)] #this won't count any of the previous loop's p/q
            for p,q in holding:
                gval = gcd(p,q)
                C[(p//gval, q//gval)]+=1
            holding = []
            for j in range(i-2, -1, -1): #compute p/q where i is acting as the 'q'
                p = nums[j]
                q = nums[i]
                holding.append([p,q]) #instead of directly adding p/q to the count, delay it by a loop
        return ans