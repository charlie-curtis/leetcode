class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:


        def check(k):
            d = defaultdict(int)
            
            for i in range(k):
                start, end,val = queries[i]
                d[start]+=val
                d[end+1]-=val
            cur = 0
            n = len(nums)
            for i in range(n):
                cur+=d[i]
                #print(i, cur, "CUR")
                if nums[i] > cur:
                    print('returning false')
                    return False
            #print('returning true')
            return True



        l = 0
        r = len(queries)

        #FFFFFFFFTTTTTTTT

        while l <= r:
            mid = l + (r-l)//2
            #print("checking", mid)
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

            #print(l,r)
        return l if l <= len(queries) else -1
        