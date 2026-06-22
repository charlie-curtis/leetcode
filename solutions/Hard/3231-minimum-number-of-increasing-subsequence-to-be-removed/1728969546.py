from sortedcontainers import SortedList
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # 5, 4, 4, 6

        #5
        #4
        #4,6

        #iterate through all the numbers. For a given number X, find the minimum number Y in your sorted list
        #where X > Y, then replace those. If such a number doesn't exist, add it to the sorted list

        #this is kinda like the LIS problem

        sl = SortedList()
        for x in nums:
            idx = sl.bisect_left(x)
            if idx == 0:
                sl.add(x)
                continue
            
            #replace
            del sl[idx-1]
            sl.add(x)
        return len(sl)


