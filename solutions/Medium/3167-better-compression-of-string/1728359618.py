class Solution:
    def betterCompression(self, compressed: str) -> str:

        letter_pos = [i for i,x in enumerate(compressed) if x.isalpha()]

        C = Counter()

        ranges = list(zip(letter_pos, letter_pos[1:] + [len(compressed)]))

        for start,end in ranges:
            letter = compressed[start]
            val = compressed[start+1:end]
            C[letter]+=int(val)
        
        ans = ""
        for i in range(26):
            letter = chr(ord('a')+i)
            if letter in C:
                ans+=letter+str(C[letter])
        return ans
                
        