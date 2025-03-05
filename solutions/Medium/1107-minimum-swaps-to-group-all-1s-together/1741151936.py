class Solution:
    def minSwaps(self, data: List[int]) -> int:

        k = data.count(1)
        if not k:
            return 0

        j = 0
        cnt = 0
        ans = 1e10
        n = len(data)
        for i,x in enumerate(data):
            cnt+=x

            if i-j+1 > k:
                cnt-=data[j]
                j+=1
            
            if i-j+1 == k:
                ans = min(ans, k-cnt)
        return ans

        