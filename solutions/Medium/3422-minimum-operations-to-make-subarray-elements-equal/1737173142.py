from sortedcontainers import SortedList
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:


        best = 1e15

        j = 0
        n = len(nums)
        lows, highs = SortedList(), SortedList()
        lowsum = highsum = 0

        def balance(x = None):
            #print('adding', x)
            nonlocal lowsum, highsum
            nonlocal lows, highs

            A = []
            if x != None:
                A.append(x)
            if lows:
                lowsum-=lows[-1]
                A.append(lows.pop())

            if highs:
                v = highs.pop(0)
                A.append(v)
                highsum-=v
            
            while len(lows) > len(highs):
                v = lows.pop()
                lowsum-=v
                A.append(v)
            while len(highs) > len(lows):
                v = highs.pop(0)
                highsum-=v
                A.append(v)
            A.sort(reverse=True)

            expected = len(A)//2
            if len(A) % 2 == 1:
                expected+=1
            for _ in range(expected):
                v = A.pop()
                lows.add(v)
                lowsum+=v
            while A:
                v = A.pop()
                highs.add(v)
                highsum+=v
            
        def remove(x):
            #print("removing", x)
            nonlocal lowsum, highsum
            nonlocal lows, highs

            if x in highs:
                highs.remove(x)
                highsum-=x
            else:
                lows.remove(x)
                lowsum-=x
            balance()

            

        A = nums
        j = 0
        best = 1e15 
        for i,x in enumerate(nums):

            if i-j + 1 > k:
                remove(A[j])
                j+=1

            #print(lows, highs)
            balance(x)

            #print(lows, highs)
            
            if i - j + 1 == k:
                if k % 2 == 1:
                    if len(lows) == len(highs):
                        raise ValueError("Wrong for odd k")
                    mid = lows[-1]
                else:
                    if len(lows) != len(highs):
                        raise ValueError("Wrong for even k")
                    mid = (lows[-1] + highs[0])//2
                
                cost = 0
                lowexpected = len(lows)*mid
                cost+=(lowexpected-lowsum)
                highexpected = len(highs)*mid
                cost+=(highsum - highexpected)
                best = min(best, cost)
        return best
