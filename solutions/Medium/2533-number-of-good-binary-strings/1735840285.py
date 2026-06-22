class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:

        M = 10**9 + 7


        #this took a while and I tried a lot of different things. Ended up looking at the editorial
        #because i couldn't reduce the state to be less than O(N^2)

        #the key observation that I was missing is, if we assume dp(x) represents a valid previous transition
        #then we can choose to either use operation A or operation B. Both will result in a valid transition.
        #In one case, if we transitioned from A, and use A again, then the output would be 2A which is still a multiple of A
        #same scenario for B.
        @cache
        def dp(i):
            if i == 0:
                return 1
            if i < 0:
                return 0

            a = dp(i-oneGroup)
            b = dp(i-zeroGroup)

            return (a+b) % M

        
        ans = 0
        for x in range(minLength, maxLength+1):
            ans+=dp(x)
            ans%=M
        return ans