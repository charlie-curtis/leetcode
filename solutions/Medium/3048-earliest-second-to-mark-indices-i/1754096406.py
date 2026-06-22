class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changes: List[int]) -> int:

        m,n = len(changes), len(nums)
        l = 0
        r = m-1

        #algo - binary search for a given endpoint. Using that endpoint, record the last possible time you can unset a given index. Then, iterate from left to right. If it's the last possible time you can unset a given index, but you haven't collected enough decrements in order to get the number to 0, then return False

        def check(mid):
            lasts = {}
            for i in range(mid+1):
                lasts[changes[i]-1] = i
            if len(lasts) < n:
                return False
            have = 0
            for i in range(mid+1):
                curIdx = changes[i]-1
                if lasts[curIdx] == i:
                    if nums[curIdx] > have:
                        return False
                    have-=nums[curIdx]
                else:
                    have+=1
            return True


        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l+1 if l <= m-1 else -1