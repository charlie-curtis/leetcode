class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        k%=n
        if k==0 or n == 1:
            return

        #if we hit i+k = rotated

        def swap(start):
            i = start 
            hold = nums[i]
            flag = False
            cnt = 0
            for _ in range(n):
                if i == start:
                    if flag: break
                    flag = True
                i = (i+k) % n
                #print(nums)
                #print("swapping", nums[i], hold)
                cnt+=1
                hold,nums[i] = nums[i], hold
                #print(nums)
            return cnt

        cnt = swap(0)
        t = n//cnt
        for i in range(1,t):
            swap(i)