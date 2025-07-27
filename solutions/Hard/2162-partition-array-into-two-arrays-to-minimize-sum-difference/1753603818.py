class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        #editorial #meetinthemiddle
        seen = defaultdict(set)
        n = len(nums)
        
        def bt(i,end,balance,nums_chosen_diff, seen):
            if i == end:
                seen[nums_chosen_diff].add(balance)
                return
            
            bt(i+1, end, balance-nums[i], nums_chosen_diff+1, seen)
            bt(i+1, end, balance+nums[i], nums_chosen_diff-1, seen)

        seen2 = defaultdict(set)
        bt(0,n//2, 0, 0, seen)
        bt(n//2,n, 0, 0, seen2)


        ans = float('inf')
        for i in range(0, n//2+1): #i is the # of items selected from the left side (well, the delta/balance)
            A = sorted(list(seen2[i]))
            for b in seen[i]:
                idx = bisect_left(A, b)
                if idx != len(A):
                    ans = min(ans, abs(A[idx] - b))
                if idx-1 != -1:
                    ans = min(ans, abs(b - A[idx-1]))
        return ans





        