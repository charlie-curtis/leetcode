class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        #"We sort inc first, then DEC second. This is so that if the x coordinates match, we can ensure that they'll never be in the same inc subsequence"
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        li = []

        #[[5,4],[6,4],[6,7],[2,3]]
        #[2,3], [5,4], [6,4], [6,7], 7,2, 8,4, 9,6

        #2,3 5,4 6,7 
        #[7,2] 8,4 9,6


        #[[3, 4], [12, 2], [12, 15], [30, 50]]
        #[[3, 4], [12, 15], [12,7] [12, 2], [30, 50]]

        #3,4
        #12,15, 30,50



        li = []
        for _,y in envelopes:
            idx = bisect_left(li, y)
            if idx == len(li):
                li.append(y)
            else:
                li[idx] = y

        return len(li)