class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        j = 0
        n = len(arr)
        ans = 0
        ssum = 0
        for i in range(n):
            ssum+=arr[i]
            if i - j + 1 > k:
                ssum-=arr[j]
                j+=1

            if i - j + 1 == k:
                avg = ssum/k
                if avg >= threshold:
                    ans+=1
        return ans
            
        