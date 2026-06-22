class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:


        #the math intuition behind this was hard.

        #say k = 3, we have arr[0] +arr[1] + arr[2] == arr[1] + arr[2] + arr[3], which implies arr[0] == arr[3]. We have created a group in which
        #every third element needs to be equal, so we can group them as such and then find the median of each group

        #but since this is a circular array, the grouping is a bit more complex
        #if n = 6 and k = 3, then we could use size 3 and be fine.
        #what if n = 4 and k = 3?
        #arr[0] + arr[1] + arr[2] = arr[1] + arr[2] + arr[3]
        #arr[1] + arr[2] + arr[3] = arr[2] + arr[3] + arr[0]
        #arr[2] + arr[3] + arr[0] = arr[3] + arr[0] + arr[1]
        #arr[3] + arr[0] + arr[1] = arr[0] + arr[1] + arr[2]

        #so that implies arr[0] = arr[3], arr[1] = arr[0], arr[2] = arr[1], arr[2] = arr[3], so all the elements are now in a group.

        #this is because the array wraps back around after n, and if n isn't divisible by k, then it'll wrap around at a different offset.
        #so to find how big the groups need to be, do gcd(n,k)
        n = len(arr)
        H = defaultdict(list)
        g = gcd(n,k)
        for i,x in enumerate(arr):
            H[i%g].append(x)
        
        ans = 0
        for li in H.values():
            med = int(median(li))
            a = sum([abs(x-med) for x in li])
            ans+=a
        return ans