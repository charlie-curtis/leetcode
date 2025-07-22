#sqrt(10**9)
cut = 33000
PRIMES = [True]*cut
PRIMES[0] = PRIMES[1] = False
i = 2
while i*i <= cut:
    if PRIMES[i]:
        j = 2
        while j*i < cut:
            PRIMES[j*i] = False
            j+=1
    i+= (1 if i % 2 == 0 else 2)

sl = SortedList()
for i,x in enumerate(PRIMES):
    if x:
        sl.add(i*i)


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:

        lower = sl.bisect_left(l) #lower bound of special nums in this range, inclusive
        upper = sl.bisect_right(r)-1 #upper bound of special numbers in this range, inclusive
        res = (r-l+1) - (upper-lower+1)
        return res