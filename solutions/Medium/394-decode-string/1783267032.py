class Solution:
    def decodeString(self, s: str) -> str:
        n, stack = len(s), []

        #3[a]2[bc]
        for x in s:
            if x == '[':
                stack.append('')
                #not needed
                continue

            print(stack)
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