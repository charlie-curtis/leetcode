class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:

        ss = SortedSet(nums)
        ss.add(0)
        ss.add(10**15)

        n = len(ss)
        used = 0
        ans = 0
        for i in range(n-1):
            a = ss[i]
            b = ss[i+1]
            chosen = min(k-used, b-a-1)
            used+=chosen
            m = a+chosen
            ans+=(m*(m+1)//2) - (a*(a+1)//2)

        return ans