class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        l = 0
        r = 2*10**9

        heaters.sort()
        houses.sort()
        n = len(heaters)

        def check(mid):
            A = [False]*len(houses)
            j = 0
            k = 0
            for i,x in enumerate(houses):
                #gte
                while j < n and heaters[j] < x:
                    j+=1
                if j < n and heaters[j] - x <= mid:
                    A[i] = True
                while k+1 <n and heaters[k+1] <= x:
                    k+=1
                if k < n and x >= heaters[k] and x-heaters[k] <= mid:
                    A[i] = True
            return all(A)



        #FFTTTTT

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1


        return l