class Solution:
    def findPermutation(self, s: str) -> List[int]:

        high = 2
        ans = [1]
        
        for char, g in groupby(s):
            m = len(list(g))
            if char == 'I':
                #just increase the stack, so like append (4,5,6,..)
                ans+= [x for x in range(high, high+m)]
            else:
                #take the last value (add 'm' to it in order to make room for our new values, then fill the new values in dec order)
                #so like [1,2,3] would become [1,2,7,6,5,4,3]
                last = ans[-1]
                ans[-1] = last + m
                ans+=[x for x in range(last+m-1, last-1, -1)]
                high = last+m+1

        return ans