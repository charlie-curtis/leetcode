class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:


        #l = 0
        #r = count[i]

        #say we want to upgrade 5. We sell count[i]  - 5 = X comps and we now have sell[i]*X + M[i] money.
        #now we just need to make sure that the money is >= (count[i]-5)*upgrade[i]
        #we have 2*sell + money


        def check(i, want):

            sellable = count[i] - want
            available_money = sell[i]*sellable + money[i]
            return available_money >= want*upgrade[i]

        n = len(upgrade)
        ans = [0]*n
        for i in range(n):

            l = 0
            r = count[i]

            #TTTTTFF
            while l <= r:
                mid = l + (r-l)//2
                if check(i, mid):
                    l = mid + 1
                else:
                    r = mid - 1
            ans[i] = r
        return ans