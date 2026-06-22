class Trie:
    def __init__(self):
        self.nxt = {}
        self.endval = '_END_'
        self.cntval = '_CNT_'

    def getbin(self, x):
        b = ""
        if x > 2**60:
            raise ValueError("Wrong")
        for i in range(45):
            if (1<<i)&x > 0:
                b+="1"
            else:
                b+="0"
        return b[::-1]

    def insert(self, word):
        word = self.getbin(word)
        cur = self.nxt
        for x in word:
            if x not in cur:
                cur[x] = {}
                cur[x][self.cntval] = 0
            cur = cur[x]
            cur[self.cntval]+=1

        if self.endval not in cur:
            cur[self.endval] = 0
        cur[self.endval]+=1

    def remove(self, word):

        word = self.getbin(word)
        cur = self.nxt
        for x in word:
            cur = cur[x]
            cur[self.cntval]-=1
        
        cur[self.endval]-=1

    def maxXor(self, word):

        word= self.getbin(word)
        cur = self.nxt
        out = ""
        for x in word:
            lookingFor = '1' if x == '0' else '0'
            if lookingFor in cur and cur[lookingFor][self.cntval] > 0:
                cur = cur[lookingFor]
                out+=lookingFor
            elif x in cur and cur[x][self.cntval] > 0:
                cur = cur[x]
                out+=x
            else:
                return -1
        return int(out, 2)
            

class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:

        neighbors = defaultdict(list)
        for u,v in edges:
            neighbors[v].append(u)
            neighbors[u].append(v)

        sums = [0]*n
        ans = 0
        trie = Trie()
        def get_sums(node, seen):
            seen.add(node)
            nxt = [x for x in neighbors[node] if x not in seen]
            ssum = values[node]
            for x in nxt:
                ssum+=get_sums(x, seen)
            sums[node] = ssum

            return ssum

        def dfs(node, seen):

            nonlocal ans
            seen.add(node)
            nxt = [x for x in neighbors[node] if x not in seen]

            #preorder check the trie to find our best answer
            ssum = sums[node]
            #print("Checking for an xor. my value is ", ssum)
            res = trie.maxXor(ssum)
            if res != -1:
                #print("I received", )
                ans = max(ans, res^ssum)

            for x in nxt:
                dfs(x, seen)

            #postorder add our value to the trie
            #print("Adding", ssum, "to the trie")
            trie.insert(ssum)


        get_sums(0, set())
        dfs(0, set())
        return ans
