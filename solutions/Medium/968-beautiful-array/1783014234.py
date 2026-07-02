class Solution:
    def beautifulArray(self, n: int) -> List[int]:

        '''
        This problem is tricky; used AI to explain it. The general intuition is that you can START with a beautiful array (something simple like [1,2] or [2,1])

        Now, you can iteratively expand it by multiplying every element by x and shifting k positions
        A_prime = 2x + k for every element in A

        There is a proof to validate why this works, but honestly this isn't a problem where you'd just naturally assume "let's start with a beautiful array and see if some property holds"
        ''' 

        out = [2,1,4,3] #or [1,2] or [2,1] or any other beautiful array can be used as a seed
        while len(out) < n:
            #print(out)
            out = [2*x for x in out] + [2*x -1 for x in out]
        #print(out)
        
        return [x for x in out if x <= n]


        

