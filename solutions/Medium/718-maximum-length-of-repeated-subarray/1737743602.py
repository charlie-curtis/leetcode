class FixedDoubleHash:
    def __init__(self, windowSize, content):
        self.h1 = 0
        self.h2 = 0
        self.m = windowSize
        self.s = content
        self.MOD1 = 10**9 + 7
        self.MOD2 = 10**9 + 9

    def drop(self,i):
        self.h1 -= pow(26*31, self.m-1, self.MOD1)*self.s[i]
        self.h2 -= pow(26*31, self.m-1, self.MOD2)*self.s[i]
        self.h1%=self.MOD1
        self.h2%=self.MOD2

    def add(self, i):
        self.h1 = self.h1 * 26*31 + self.s[i]
        self.h2 = self.h2 * 26*31 + self.s[i]
        self.h1%=self.MOD1
        self.h2%=self.MOD2
    
    def get(self):
        return (self.h1, self.h2)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:


        l = 0
        r = min(len(nums1), len(nums2))

        def check(mid):
            seen = set()
            dh1 = FixedDoubleHash(mid, nums1)
            dh2 = FixedDoubleHash(mid, nums2)
            for i in range(len(nums1)):
                if i - mid >= 0:
                    dh1.drop(i-mid)
                dh1.add(i)
                if i >= mid-1:
                    seen.add(dh1.get())
            for i in range(len(nums2)):
                if i - mid >= 0:
                    dh2.drop(i-mid)
                dh2.add(i)
                if i >= mid -1:
                    if dh2.get() in seen:
                        return True
            return False

        #TTTTFFFF
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid -1
        return r

        