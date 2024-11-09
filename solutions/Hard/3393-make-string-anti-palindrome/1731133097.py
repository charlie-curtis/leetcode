class Solution:
    def makeAntiPalindrome(self, s: str) -> str:

        C = Counter(s)
        if max(C.values()) > len(s)//2:
            return "-1"

        n = len(s)
        mid = n//2 #crossover index
        ans = [x for x in sorted(s)]

        if ans[mid-1] == ans[mid]:
            j = mid -1
            while ans[mid-1] == ans[j]:
                j-=1

            need_to_move = mid-j-1

            j = mid
            while ans[j] == ans[mid]:
                j+=1
            offset = j - mid

            
            #we need ot shift need_to_move characters by an offset of $offset
            for i in range(mid, mid+need_to_move):
                ans[i], ans[i+offset] = ans[i+offset], ans[i]

        return ''.join(ans)