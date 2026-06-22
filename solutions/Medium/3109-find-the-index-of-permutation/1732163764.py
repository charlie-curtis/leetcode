from sortedcontainers import SortedList
class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:


        M = 10**9+7
        @cache
        def factorial(x):
            if x in [0,1]:
                return 1
            return (x%M)*(factorial(x-1)%M) %M


        n = len(perm)
        ans = 0
        sl = SortedList()
        for i in range(n-1):
            #for this loop, assume we've fixed all the numbers that come before i, and we're going to decrease i by 1. How many perms can we make?
            #that answer is based off the number of slots to the right of us and the available numbers that we haven't used yet

            #so if we had the number 4 1 2 3 5, and we're processing i = 2, we can fix [4,1], and create a perm that starts with all the unused numbers less than 2 combined with the remaining elements. There are no unused elements less than 2
            available_lower_numbers = perm[i]-1 - sl.bisect_left(perm[i])
            used = i+1
            rem = n-used
            a = int(factorial(n-used))
            a*=available_lower_numbers
            a%=M
            ans+=a
            ans%=M
            sl.add(perm[i])
        return ans


        