class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:

        C = Counter(nums)

        ans = 0
        for T in range(3,300):
            for i in range(1,101):
                if i >= T or T%i:
                    continue
                for j in range(1,101):
                    k = T - i - j
                    if k < 1 or j < 1:
                        continue
                    if k > j:
                        continue
                    if T %k == 0 or T%j==0:
                        continue
                    a = C[i]
                    b = C[j]
                    c = C[k]
                    if k == j:
                        ans+=a*(b)*(b-1)*3
                    else:
                        ans+=(a*b*c)*6
        return ans