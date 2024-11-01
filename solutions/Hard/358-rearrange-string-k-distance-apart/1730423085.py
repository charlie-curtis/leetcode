class Solution:
    def rearrangeString(self, s: str, k: int) -> str:

        C = Counter(s)
        ht = deque()
        pq = []
        for letter,count in C.items():
            pq.append([-count, letter])

        heapq.heapify(pq)

        i = 0
        ans = ""
        while pq:
            cnt, letter = heapq.heappop(pq)
            cnt = -cnt
            cnt-=1
            ans+=letter
            if cnt > 0:
                ht.append([i+k, -cnt, letter])
            i+=1

            while ht and ht[0][0] <= i:
                _, cnt, letter = ht.popleft()
                heapq.heappush(pq, [cnt, letter])


        #print(pq, ht, i)
        #print(ans)
        return "" if len(ans) != len(s) else ans
                


        