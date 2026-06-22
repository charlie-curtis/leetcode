class Solution:
    def isPossible(self, target: List[int]) -> bool:

        #I didn't get this problem on the first try. Had to lookup the editorial and then code it a couple times
        ssum = sum(target)
        pq = [-x for x in target]
        heapify(pq)
        n = len(target)

        if n == 1:
            return target == [1]

        while pq:

            #9,3,5 -> [x,3,5]
            # x + 3 + 5 = 9 (e.g. the sum of array 2 should be equal to A[0] in this example)
            #x + (ssum-high) = high
            #x = 2high - ssum

            high = abs(heappop(pq))
            x = 2*high - ssum

            #but we also need to handle the case [100000000, 1]. It would take a long time for A[0] to decrease by 1 until it reached 1, so we
            #can "jump" to the number >= nexthigh
            if pq:
                nexthigh = abs(pq[0])
                diff = high - nexthigh
                if diff == 0:
                    return False
                y = max(1,diff//(ssum-high))
                if y != 0:
                    #x = high - (ssum-high)*y
                    x = high + (high-ssum)*y
            
            #print("old", high, "new", x)
            ssum-=high
            ssum+=x

            if x <= 0:
                return False
            if ssum == n:
                return True

            heappush(pq, -x)
