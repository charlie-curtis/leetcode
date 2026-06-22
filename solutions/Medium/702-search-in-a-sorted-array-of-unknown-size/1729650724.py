# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:

        n = 1
        res = 0
        sentinel = 2**31-1

        while res != sentinel:
            n<<=1
            res = reader.get(n)


        l = 0
        r = n

        while l <= r:

            mid = l + (r-l)//2
            can = reader.get(mid)
            if can == target:
                return mid
            
            if can < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1



        