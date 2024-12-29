class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word
        n = len(word)
        k = n- numFriends+1

        pq = []
        for i in range(n):
            end = min(n, i+k)
            w = word[i:end]
            heapq.heappush(pq, w)

        heapq.heapify(pq)
        ans ="" 
        while pq:
            ans = heapq.heappop(pq)

        return ans
            