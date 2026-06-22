class Solution:
    def coloredCells(self, n: int) -> int:

        #for this problem, I drew the first 4 sequences and saw
        #the pattern

        '''
        h = 2*n-1
        ans = 2*n - 1
        h-=2
        while h > 0:
            ans+=2*h
            h-=2
        return ans
        '''

        #There is a math way to do it too
        #the sequence is like 1,3,5,7,5,3,1
        #so you can sum from 1..7 twice, and subtract out the duplicate 7
        #equation is L/2(a1 + an)
        an = 2*n-1 #this is the top term, an
        a1 = 1 #first term
        L = n #number of terms in length

        #return L*(a1 + an) - an
        # ^ this works


        #... but can further be simplifed to 
        #n(1 + 2n - 1) - an = n(2n) - an = 2n^2 - (2n-1) = 2n^2 - 2n + 1 = 2n(n - 1) + 1

        return 2*n*(n-1) + 1


