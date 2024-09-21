class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        '''
        C = Counter(nums)
        high = max(C.values())
        for k,v in C.items():
            if high == v:
                return k
        '''
        balance = 0
        ans = None
        for x in nums:
            if balance == 0:
                ans = x
            
            if ans == x:
                balance+=1
            else:
                balance-=1
        return ans

        