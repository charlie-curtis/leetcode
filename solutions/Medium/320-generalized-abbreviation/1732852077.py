class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:


        ans = []
        def backtrack(i, cur):
            nonlocal ans

            n = len(word)
            if i == n:
                ans.append(''.join([str(x) for x in cur]))
                return

            #either shorten this ans
            if not cur or isinstance(cur[-1],str):
                cur.append(1)
                backtrack(i+1, cur)
                cur.pop()
            else:
                cur[-1]+=1
                backtrack(i+1, cur)
                cur[-1]-=1

            #or don't modify this ans
            cur.append(word[i])
            backtrack(i+1, cur)
            cur.pop()



        backtrack(0, [])
        return ans
        