class Solution:
    def stringSequence(self, target: str) -> List[str]:
        
        
        n = len(target)
        ans = []
        overall = ""
        for i in range(n):
            lookingFor = target[i]
            cur = ""
            while cur != lookingFor:
                if not cur:
                    cur = "a"
                else:
                    cur = chr(ord(cur) + 1)
                
                ans.append(overall+cur)
            overall+=lookingFor
            cur = ""
        return ans
            

        