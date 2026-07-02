class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        C = Counter()
        n = len(arr)
        before = [[x for x in range(0,101)] for _ in range(n)]
        after = [[x for x in range(0,101)] for _ in range(n)]

        for i,x in enumerate(arr):
            for j in range(101):
                before[i][j] = C[j]
            C[x]+=1
                
        C = Counter()
        for i in range(n-1, -1, -1):
            x = arr[i]
            for j in range(101):
                after[i][j] = C[j]
            C[x]+=1

        MOD = 10**9 + 7

        ans = 0
        for i in range(n):
            for j in range(101):
                k = target - arr[i] - j
                if k < 0 or k > 100:
                    continue
                b = before[i][j]
                a = after[i][k]
                ans+=b*a
                ans%=MOD
        return ans
                
        