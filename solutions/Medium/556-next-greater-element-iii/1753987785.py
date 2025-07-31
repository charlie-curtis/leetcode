class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = [x for x in str(n)]
        
        n=len(s)
        j=-1
        for i in range(n-1,0,-1):
            if s[i-1] < s[i]:
                j=i-1
                break
        if j == -1:
            return -1
        nums=s
        for i in range(n-1,j,-1):
            if nums[i] > nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
                nums[j+1:] = nums[j+1:][::-1]
                v = int(''.join(nums))
                if v <= 2**31-1:
                    return v
                return -1