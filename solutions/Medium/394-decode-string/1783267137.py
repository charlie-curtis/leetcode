class Solution:
    def decodeString(self, s: str) -> str:
        n, stack = len(s), []

        #3[a]2[bc]
        for x in s:
            if x == '[':
                #this isn't really needed because the digit itself indicates that there should be a following opening bracket (e.g. 3[abc])

                #however, the case 2[2a] would be parsed as 22a instead of 2*2a, so we just add an empty string to separate numbers for those edge cases
                stack.append('')
                continue

            if x == ']':
                s1 = stack.pop()
                cnt = stack.pop()
                stack.append(s1*int(cnt))
                while len(stack) >= 2 and not stack[-1].isdigit() and not stack[-2].isdigit():
                    #if we just multiplied strings, see if any previously computed strings can now be combined
                    x = stack.pop()
                    stack[-1]+=x
            elif not stack or stack[-1].isdigit() != x.isdigit():
                stack.append(x)
            else:
                stack[-1]+=x
        return stack[-1]