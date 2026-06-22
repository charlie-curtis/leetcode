class Solution:
    def onceTwice(self, nums: List[int]) -> List[int]:

        #editorial

        #if rem % 3 == 2, then set it for the double
        #if rem % 3 == 1, set it for single
        #if rem % 3 == 0, then its either set in both single/double or not at all. This is the tricky case

        single = double = 0
        for i in range(32):
            cnt = 0
            for x in nums:
                cnt+=(1<<i)&x > 0
                cnt%=3
            if cnt % 3 == 1:
                single|=(1<<i)
            elif cnt % 3 == 2:
                double|=(1<<i)
        
        #we know some bits used in single, some used in double, but the ones that are used in BOTH
        #single and double are still unknown. We can partition the numbers in the input array by any bit that differs between single and double. This just ensures that the two numbers we care about will be in separate groups
        
        x = single^double #compute the bit difference
        lsb = x&(-x) #find any bit that differs. in this case, the lsb

        #[1,2,2,3,3,3,,4,4,4]
        #partition the numbers. single/double are now in separate groups, so you can do the same approach as before, but there won't be any ambiguity.

        #in group 1, the ONLY results when modding will be remainder 1 or remainder 0. If 1, the bit is set in single. If 0, it's not set
        #in group 2, the ONLY results when modding will be remainder 2 or remainder 0. If 2, the bit is set in double. If 0, it's not set

        for i in range(32):
            c1 = c2 = 0
            for x in nums:
                if x&(1<<i) > 0:
                    if x&lsb:
                        c1+=1
                        c1%=3
                    else:
                        c2+=1
                        c2%=3
            if max(c1,c2) % 3 == 2:
                double|=(1<<i)
            if c1 == 1 or c2 == 1:
                single|=(1<<i)

        if single&(1<<31):
            #this is a negative number
            single-=2**32
        if double&(1<<31):
            double-=2**32
        return [single, double]