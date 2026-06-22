class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:



        l = 0
        r = 10**9
        n = len(nums)

        def get_moves_required(val,total_moves):
            '''
            xa + yb >= val
            a + b = total
            
            b = total - a
            xa + y(total-a) >= val
            xa + ytotal -ya >= val
            
            xa -ya >= val - ytotal
            (x-y)a >= val - ytotal
            a >= val - ytotal / (x-y)
            a = ceil((val -ytotal) / (x-y))
            '''

            a = max(0,ceil((val - y*total_moves)/ (x-y)))
            #print(a, total_moves - a, mid)
            return a



        def check(mid):
            moves = 0
            for val in nums:
                if val - x*mid > 0:
                    return False
                moves+=get_moves_required(val,mid)
                if moves > mid:
                    return False
            return moves <= mid

        #FFFTTTTTTTT
        while l <= r:

            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid +1

        return l

