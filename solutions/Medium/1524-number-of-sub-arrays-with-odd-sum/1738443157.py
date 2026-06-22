class Solution:
    def numOfSubarrays(self, nums: List[int]) -> int:

        MOD = 10**9 + 7
        ssum = 0

        ans=0
        #if i'm an odd number, i can increment to any previously seen even sum (plus one)
        C = Counter()
        C[0] = 1
        for x in nums:
            ssum+=x
            ssum%=2
            if ssum%2 == 1:
                ans+=C[0]
            else:
                ans+=C[1]
            ans%=MOD
            C[ssum]+=1
        return ans

        

        #odds = 1 evens = 0
        #odds = 2 evens = 0
        #odds = 3 evens = 0