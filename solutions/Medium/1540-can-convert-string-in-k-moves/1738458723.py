class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:

        if len(s) != len(t):
            return False

        C = Counter()
        for a,b in zip(s,t):
            o1 = ord(a) - ord('a')
            o2 = ord(b) - ord('a')

            if o2 < o1:
                o2+=26
            needed = o2-o1
            if needed == 0:
                continue
            C[needed]+=1


        for m,v in C.items():
            if 26*(v-1) + m > k:
                return False
        return True