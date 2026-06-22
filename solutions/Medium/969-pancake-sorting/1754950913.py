class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        #3,2,4,1
        #2,3,4,1
        #4,3,2,1
        #1,2,3,4

        #if the array isn't already sorted, we'll need to "push elements in order to the back"

        #so in the example, the array isn't sorted, so let's focus on getting 1 to the back

        #3,2,4,1 (check)
        #now we need to get 2 to the back (so if it's not already there, then we need to get it to the front and flip it)

        #2,3,4,1
        #4,3,2,1 (check)
        #3 and 4 are already there, so we're good

        good = all([y-x == 1 for (x,y) in zip(arr, arr[1:])])
        if good:
            return []
        n = len(arr)
        expected = n-1
        out = []
        for x in range(1,len(arr)+1):
            j = -1
            for i in range(n):
                if arr[i] == x:
                    j = i
                    break
            if j == expected:
                expected-=1
                continue
            else:
                #moves this to the front
                arr[0:j+1] = arr[0:j+1][::-1]
                out.append(j+1)

                #moves this to the correct idx
                arr[0:expected+1] = arr[0:expected+1][::-1]
                out.append(expected+1)
                expected-=1
        out.append(n)
        arr = arr[::-1]
        return out


