class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        banned = sorted(set(banned))
        m = len(banned)
        pre = list(accumulate(banned, initial=0))


        #2,3,5
        def check_helper(wants):
            l = 1
            r = n

            #true if chose gte wants numbers
            #FFFFTTTTTTTTTTTTT
            while l <= r:
                mid = l + (r-l)//2
                idx = bisect_right(banned, mid) #banned words that are smaller than it
                chosen = mid - idx
                if chosen >= wants:
                    r = mid -1
                else:
                    l = mid + 1
            return l # or something

        def check(x):

            #so x is the number of values that we want to see if they fit, but due to how banned is,
            #we don't actually know what value to choose in order to have x numbers in our answer,
            #so we nested binary search using check_helper
            val = check_helper(x)
            idx = bisect_right(banned,val)
            return val <= n and (val*(val+1)//2 - pre[idx] <= maxSum)


        l = 0
        r = n

        #TTTTTTTFFFF

        while l <= r:
            mid = l + (r-l)//2

            if check(mid):
                l = mid + 1
            else:
                r = mid -1

        return r


        