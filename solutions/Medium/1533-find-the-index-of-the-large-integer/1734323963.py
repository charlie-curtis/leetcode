# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:

        n = reader.length()

        l = 0
        r = n-1

        while l <= r:
            if l == r:
                return l
            length = r-l+1
            mid = l + (r-l)//2
            a,b = l, mid
            c,d = mid+1, r
            if length % 2 == 1:
                b-=1

            res = reader.compareSub(a,b,c,d)
            if res == 0 and length%2 == 1:
                return mid
            if res == -1:
                l = c
            elif res == 1:
                r = b
            else:
                raise ValueError("Wrong")