# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        candidates = deque([x for x in range(n)])

        while len(candidates) > 1:

            a, b = candidates.popleft(), candidates.popleft()

            res = knows(a,b)
            if not res:
                #if a doesn't know b, then b isn't the celebrity
                candidates.append(a)
            else:
                #if a DOES know b, then a isn't the celebrity
                candidates.append(b)

        a = candidates.popleft()
        #do a final veritification to make sure whoever is left is actually a celebrity
        for i in range(n):
            if a == i:
                continue
            if knows(a,i) or not knows(i,a):
                return -1
        return a