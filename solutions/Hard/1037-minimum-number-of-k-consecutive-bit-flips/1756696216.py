class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:



        #sliding window of size k to keep track of whether the current number is actually inverted
        #or not. If any of the last k-1 numbers required flipping, return -1 because the move is invalid
        n = len(nums)
        flipped = [False]*n
        inverted = False
        ans = 0
        for i in range(n):
            if i >= k:
                #slide out any numbers that are no longer in the window
                if flipped[i-k]:
                    inverted = not inverted
            if (nums[i] == 0 and not inverted) or (nums[i] == 1 and inverted):
                #simulate flipping this number
                ans+=1
                flipped[i] = True
                inverted = not inverted
        
        for i in range(k-1):
            if flipped[-i-1]:
                return -1
        return ans

            



        