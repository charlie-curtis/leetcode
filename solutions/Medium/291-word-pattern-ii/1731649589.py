class Solution:
    def wordPatternMatch(self, letters: str, s: str) -> bool:



        m,n = len(letters), len(s)
        def bt(i,j, letter_to_str, str_to_letter):

            if j == n:
                #if we reach the end of the string, we should also be at the end of our mapping
                return i == m

            if i == m:
                #if we reached the end of our mapping, but not the end of the string, return false
                return False

            cur_letter = letters[i]
            
            if cur_letter in letter_to_str:
                #there is a pre-existing pattern, see if we can use it to satisfy our current
                #position in s
                prev_str = letter_to_str[cur_letter]
                prev_letter = str_to_letter[prev_str]
                if prev_letter != cur_letter:
                    return False
                if len(prev_str) + j <= n and prev_str == s[j:j+len(prev_str)]:
                    return bt(i+1, j+len(prev_str), letter_to_str, str_to_letter)
                return False
            else:
                #there is not a pre-existing pattern in d, brute force try it
                for k in range(j, n):
                    nxt_str = s[j:k+1]
                    if nxt_str in str_to_letter:
                        continue
                    letter_to_str[cur_letter] = nxt_str
                    str_to_letter[nxt_str] = cur_letter
                    if bt(i+1, j+len(nxt_str), letter_to_str, str_to_letter):
                        return True
                    del letter_to_str[cur_letter]
                    del str_to_letter[nxt_str]

            return False

        return bt(0,0,{}, {})

        