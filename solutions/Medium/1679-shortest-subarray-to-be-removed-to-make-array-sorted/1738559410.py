class Solution:
    def findLengthOfShortestSubarray(self, nums: List[int]) -> int:


        n = len(nums)
        right = [1]*n
        left = [1]*n

        for i in range(n-2, -1,-1):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1] + 1

        for i in range(1,n):
            if nums[i-1] <= nums[i]:
                left[i] = left[i-1] +1


        #print(left)
        #print(right)
        def check(k):

            if k == n:
                return True

            j = 0
            for i in range(n):
                if i -j + 1 > k:
                    j+=1
                L = (j == 0) or left[j-1] == j
                R = (i == n-1) or right[i+1] == n-(i+1)
                E = (j == 0 or i == n-1) or nums[j-1] <= nums[i+1]
                if L and R and E:
                    #print("found at", i,j)
                    return True
            return False

        l = 0
        r = n

        #FFFFTTTTTT
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                #print('True for', mid)
                r = mid -1
            else:
                #print('false for', mid)
                l = mid + 1

        return l