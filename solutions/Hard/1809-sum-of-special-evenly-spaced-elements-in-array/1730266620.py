from sortedcontainers import SortedDict
class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        prefs = {}
        n = len(nums)
        MOD = 10**9 + 7


        def get_sum(k, b):
            #this will lazily compute the pref and then return the value
            a = b % k
            if (k,a) not in prefs:
                ssum = 0
                tmp = []
                for i in range(a,n, k):
                    ssum+=nums[i]
                    tmp.append(ssum)
                
                prefs[(k,a)] = tmp
            table = prefs[(k,a)]
            #print(table, "TABLE")

            idx = (b-a)//k
            #print(idx, "IDX is", idx, b,a,k)
            return (table[-1] - (table[idx-1] if idx-1 >= 0 else 0)) % MOD

        def realtime(k,b):
            ssum = 0
            for i in range(b,n,k):
                ssum+=nums[i]
            return ssum % MOD


        out = []
        for b,k in queries:
            if k*k > n:
                out.append(realtime(k,b))
            else:
                out.append(get_sum(k,b))
        return out




