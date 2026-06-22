class Solution:
    def isTransformable(self, s: str, t: str) -> bool:

        n = len(s)
        d = defaultdict(deque)

        for i,x in enumerate(s):
            d[x].append(i)

        #iterate through all numbers in t. you can slide a number to the front
        #if there are only larger numbers between t and beginning of array

        t = deque(t)

        while t:
            l = t.popleft()
            if len(d[l]) == 0:
                #no more occurences of l exist in s
                return False
            #find the closest idx
            idx = d[l].popleft()
            #check values < l. If any of them have a closer value, the answer is no
            for i in range(int(l)-1, -1, -1):
                c = str(i)
                if len(d[c]) and d[c][0] < idx:
                    return False
        return True