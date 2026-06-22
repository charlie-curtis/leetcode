class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        st = set(nums)

        #playing around with groupby
        for _,g in groupby(enumerate(nums), key=lambda x: x[1] - x[0]):
            li = [x[1] for x in g]
            ssum = sum(li)
            while ssum in st:
                ssum+=1
            return ssum

        
        #the idea is that groupby will catch sequentially increasing nums like [3,4,5,..]
        #so the first group will be the array we care about. From there, sum the numbers & figure out which one doesn't appear in nums