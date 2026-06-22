class Solution:
    def minTotalTime(self, forward: List[int], backward: List[int], queries: List[int]) -> int:

        F = list(accumulate(forward, initial=0))
        B = list(accumulate(backward, initial=0))



        #1 [2 3 4] 5 6 7 
        # 2  3 7  10 14 19 23
        #0  2 3 7 10 14 19 23 
        #start = 2 end = 4
        #start = 4 end = 2

        print("forward", F)
        print("backward", B)
        queries = [0] + queries
        n = len(F)
        ans = 0
        for s,e in zip(queries, queries[1:]):
            if s == e:
                continue
            if s < e:
                a = F[e] - F[s] #this should be right
                b = B[s+1] + (B[-1] - B[e+1]) #we DO want to count start (so use s+1). We DON'T want to count end, so subtract end (by using e+1)
                #or B[-1] - (B[e] - B[s]) is another way to think about it. E.g. everything except for the range e-s
            else:
                a = F[-1] - F[s] + F[e]
                b = B[s+1] - B[e+1]

                #0 1
                # x y
                #0 x y

            ans+=min(a,b)
        return ans


        #so if we're going from 2 to 4 (N=5), and we want to go backwards, we need to compute backward(4), backward(3),
        #so in prefix sums that would be B[4+1] - B[2+1]

        #forward
        #1 2 3 4 5
        # x y z a b
        #0 x y z a b 


        #backward
        # 1 2 3 4 5
        #y x c b a 