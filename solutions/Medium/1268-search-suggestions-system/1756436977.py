class Trie:
    def __init__(self):
        self.root = {}
    
    def add(self,word):

        cur = self.root

        for x in word:
            if x not in cur:
                cur[x] = {}
                cur[x]['_q_'] = []
            cur = cur[x]
            heapq.heappush(cur['_q_'], word)
    
    def get(self, word):
        cur = self.root
        for x in word:
            if x not in cur:
                return []
            cur = cur[x]
        out = []
        q = cur['_q_']
        for _ in range(min(len(q),3)):
            out.append(heapq.heappop(q))
        for x in out:
            heapq.heappush(q, x)
        return out



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        t = Trie()

        for x in products:
            t.add(x)
        
        out = []
        s = ""
        for x in searchWord:
            s+=x
            out.append(t.get(s))
        return out
        