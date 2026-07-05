class Solution:
    def lastRemaining(self, n: int) -> int:

        if n == 1:
            return 1

        '''
        The idea here is we don't need to track every number. We just need to track the start of the sequence and how big it jumps each time

        CASES
        1. starting from front, n is odd
        2. starting from front, n is even
        3. starting from back, n is even
        4. starting from back, n is  odd
    
        odd example: [a,b,c,d,e] -> [b,d] -> output is the same regardless of front or back
        even case: [a,b,c,d] -> [b,d] if front, [a,c] if back. Output varies by front or back

        So for even cases or odd cases where we are starting from the back, we need to advance our pointer by 1 spot (e.g. instead of pointing to a, point to b)

        
        '''

        start = 1
        gap = 1
        rem = n
        for i in range(100):
            if i % 2 == 0 or (i%2 == 1 and rem % 2 == 1):
                #if we are starting from the front OR we are starting from the back and the array length is odd, then the sequence's start is shifted
                start+=gap
            gap*=2
            rem//=2

            if rem == 1:
                return start