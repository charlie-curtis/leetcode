class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:


        n = len(s)
        seen = set()
        for i in range(n):
            if i+k > n:
                break
            seen.add(s[i:i+k])

        def bt(cur):
            if len(cur) == k:
                if ''.join(cur) not in seen:
                    return False
                return True

            cur.append('0')
            if not bt(cur):
                return False
            cur.pop()
            cur.append('1')
            if not bt(cur):
                return False
            cur.pop()
            return True

        return bt([])
            