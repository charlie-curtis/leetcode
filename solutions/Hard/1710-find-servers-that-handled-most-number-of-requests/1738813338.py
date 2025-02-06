class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        C = Counter()
        n = len(arrival)
        avail = SortedList([i for i in range(k)])

        pq = []
        for i,(a,l) in enumerate(list(zip(arrival, load))):

            #print('arrivial time of', a)

            while (pq and pq[0][0] <= a):
                t,idx = heappop(pq)
                avail.add(idx)

            #print("available is", avail)

            if not avail:
                #print("Im dropping a request")
                continue


            t = i%k
            #print("I want to use idx", t)
            idx = avail.bisect_left(t)
            if idx == len(avail):
                idx = 0
            v = avail.pop(idx)
            C[v]+=1
            #print("I chose", v)
            heappush(pq, (a+l,v))

            #print(pq)
        v = max(C.values())

        #print(C.values())

        return [k for k,v1 in C.items() if v == v1]
