class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        C = Counter()
        n = len(nums)
        costs = [0]*(2*limit+2)
        for i in range(n//2):
            a,b = nums[i], nums[n-1-i]
            v = a + b
            mn,mx = min(a,b), max(a,b)
            small = v - mx + 1
            high = v - mn + limit

            #print(small,high)

            #[1,small-1] = cost is 2
            costs[1]+= 2
            costs[small]-=2
            #[small,v-1] = cost is 1
            costs[small]+= 1
            costs[v]-=1
            #[v] = cost is 0
            #[v+1, high] = cost is 1
            costs[v+1]+=1
            costs[high+1]-=1
            #[high+1, 2*limit] = cost is 2
            costs[high+1]+=2
            costs[2*limit+1]-=2

        ans = 10**9
        ssum = 0
        for i in range(1, 2*limit+1):
            ssum+=costs[i]
            ans = min(ans, ssum)
        return ans
        

