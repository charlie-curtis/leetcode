class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:



        n = len(nums)
        l = max(nums) 
        r = 10**9+1

        def check(threshold):
            t = 0
            ssum = 0
            for i in range(n):
                if nums[i] + ssum > threshold:
                    t+=1
                    if t == k:
                        #if can't partition anymore, we need to make sure the rest of the elements, when summed, stay below threshold
                        #print("H1")
                        return ssum + sum(nums[i:]) <= threshold
                    else:
                        #continue on
                        ssum = 0

                ssum+=nums[i]
                #print(ssum, nums[i], t, threshold)

            #print("H2", t+1, k, threshold)
            return True
            


        #FFFFFFTTTT

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l
        